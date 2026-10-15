#!/usr/bin/env node
/** Adapt owner-enabled Chrome discovery to REA 6.4.0; never launch a browser.
 * Metadata comes from real CDP. Only the initially selected Explee target is
 * advertised/attachable. This is transport scoping, not a read-only sandbox:
 * use the passive capture helper, not arbitrary CDP clients.
 */
import { readFile, writeFile } from 'node:fs/promises';
import { createServer } from 'node:http';
import { createRequire } from 'node:module';
import { resolve } from 'node:path';
import { pathToFileURL } from 'node:url';

export function parseAdvertisement(text) {
  const [rawPort, path] = text.trim().split(/\r?\n/);
  const port = Number(rawPort);
  if (!/^\d+$/.test(rawPort) || !Number.isInteger(port) || port < 1 || port > 65535 ||
      !/^\/devtools\/browser\/[A-Za-z0-9_-]+$/.test(path ?? '')) {
    throw new Error('Invalid Chrome DevToolsActivePort advertisement');
  }
  return `ws://127.0.0.1:${port}${path}`;
}

export async function startBridge({ WebSocket, WebSocketServer, advertisement, sourceUrl, targetId }) {
  const source = new URL(sourceUrl);
  if (source.origin !== 'https://explee.com' || source.username || source.password) {
    throw new Error('Select an HTTPS Explee source URL without credentials');
  }
  const upstream = new WebSocket(parseAdvertisement(advertisement), { handshakeTimeout: 60000, maxPayload: 32 * 1024 * 1024 });
  await new Promise((resolveOpen, reject) => {
    upstream.once('open', resolveOpen);
    upstream.once('error', reject);
    upstream.once('close', () => reject(new Error('Chrome closed before authorization')));
  });
  let sequence = 0;
  let closing = false;
  let server;
  let websocketServer;
  const pending = new Map();
  const sessions = new Map();
  const clients = new Set();
  function send(client, value) {
    if (client.readyState === WebSocket.OPEN) client.send(JSON.stringify(value));
  }
  function rpc(method, params = {}, sessionId) {
    const id = ++sequence;
    return new Promise((resolveReply, reject) => {
      const timer = setTimeout(() => { pending.delete(id); reject(new Error(`Chrome timed out: ${method}`)); }, 30000);
      pending.set(id, { resolve: value => { clearTimeout(timer); resolveReply(value); }, reject: error => { clearTimeout(timer); reject(error); } });
      upstream.send(JSON.stringify({ id, method, params, ...(sessionId ? { sessionId } : {}) }));
    });
  }
  upstream.on('message', bytes => {
    let message;
    try { message = JSON.parse(bytes.toString()); } catch { return; }
    if (message.id !== undefined) {
      const waiter = pending.get(message.id);
      if (waiter) {
        pending.delete(message.id);
        message.error ? waiter.reject(new Error(message.error.message)) : waiter.resolve(message.result);
      }
      return;
    }
    const sessionId = message.sessionId ?? (message.method === 'Target.detachedFromTarget' ? message.params?.sessionId : undefined);
    const owner = sessions.get(sessionId);
    if (owner) send(owner, message);
    if (message.method === 'Target.detachedFromTarget') sessions.delete(sessionId);
  });
  upstream.on('close', () => {
    for (const waiter of pending.values()) waiter.reject(new Error('Chrome disconnected'));
    pending.clear();
    for (const client of clients) client.close();
    if (!closing) void close();
  });
  // Keep error messages free of the browser's capability URL.
  upstream.on('error', () => {});
  let version;
  let target;
  try {
    version = await rpc('Browser.getVersion');
    const result = await rpc('Target.getTargets');
    const matches = result.targetInfos.filter(item => item.type === 'page' && item.url === source.href &&
      (targetId === undefined || item.targetId === targetId));
    if (matches.length !== 1) throw new Error('Expected exactly one selected Explee tab');
    target = matches[0];
  } catch (error) { upstream.close(); throw error; }
  async function selectedTargets() {
    const result = await rpc('Target.getTargets');
    return result.targetInfos.filter(item => item.targetId === target.targetId &&
      item.type === 'page' && URL.canParse(item.url) && new URL(item.url).origin === source.origin);
  }
  const socketPath = '/devtools/browser/explee-rea-adapter';
  let endpoint;
  function permitted(request) {
    return request.headers.host === new URL(endpoint).host && !request.headers.origin;
  }
  server = createServer(async (request, response) => {
    if (!permitted(request)) { response.writeHead(403).end(); return; }
    if (request.method !== 'GET') { response.writeHead(405).end(); return; }
    try {
      let data;
      if (request.url === '/json/version') {
        data = { Browser: version.product, 'Protocol-Version': version.protocolVersion,
          'User-Agent': version.userAgent, 'V8-Version': version.jsVersion,
          'WebKit-Version': version.revision, webSocketDebuggerUrl: endpoint.replace('http:', 'ws:') + socketPath };
      } else if (request.url === '/json/list') {
        data = (await selectedTargets()).map(item => ({ id: item.targetId, type: item.type,
          title: item.title, url: item.url, attached: item.attached }));
      } else { response.writeHead(404).end(); return; }
      response.writeHead(200, { 'Content-Type': 'application/json', 'Cache-Control': 'no-store' }).end(JSON.stringify(data));
    } catch { response.writeHead(502).end(); }
  });
  websocketServer = new WebSocketServer({ noServer: true, maxPayload: 32 * 1024 * 1024 });
  server.on('upgrade', (request, socket, head) => {
    if (!permitted(request) || request.url !== socketPath) { socket.destroy(); return; }
    websocketServer.handleUpgrade(request, socket, head, client => websocketServer.emit('connection', client));
  });
  websocketServer.on('connection', client => {
    clients.add(client);
    client.on('error', () => {});
    client.on('message', async bytes => {
      let message;
      try {
        message = JSON.parse(bytes.toString());
        if (!Number.isSafeInteger(message.id) || typeof message.method !== 'string') throw new Error('Invalid CDP request');
        const { id, method, params = {}, sessionId } = message;
        let result;
        if (sessionId) {
          if (sessions.get(sessionId) !== client || method.startsWith('Target.') || method.startsWith('Browser.')) throw new Error('Session is outside selected target');
          result = await rpc(method, params, sessionId);
        } else if (method === 'Target.attachToTarget') {
          if (params.targetId !== target.targetId || params.flatten !== true || !(await selectedTargets()).length) throw new Error('Target is outside selected Explee scope');
          result = await rpc(method, params);
          if (typeof result.sessionId !== 'string') throw new Error('Chrome returned no session identity');
          if (client.readyState !== WebSocket.OPEN) await rpc('Target.detachFromTarget', { sessionId: result.sessionId });
          else sessions.set(result.sessionId, client);
        } else if (method === 'Target.detachFromTarget' && sessions.get(params.sessionId) === client) {
          result = await rpc(method, params);
          sessions.delete(params.sessionId);
        } else if (method === 'Browser.getVersion') result = version;
        else if (method === 'Target.getTargets') result = { targetInfos: await selectedTargets() };
        else throw new Error('Browser command is outside selected Explee scope');
        send(client, { id, result, ...(sessionId ? { sessionId } : {}) });
      } catch (error) {
        if (Number.isSafeInteger(message?.id)) send(client, { id: message.id, error: { code: -32000, message: error.message } });
      }
    });
    client.on('close', () => {
      clients.delete(client);
      for (const [sessionId, owner] of sessions) if (owner === client) {
        sessions.delete(sessionId);
        if (upstream.readyState === WebSocket.OPEN) void rpc('Target.detachFromTarget', { sessionId }).catch(() => {});
      }
    });
  });
  try {
    await new Promise((resolveListen, reject) => { server.once('error', reject); server.listen(0, '127.0.0.1', resolveListen); });
  } catch (error) { await close(); throw error; }
  endpoint = `http://127.0.0.1:${server.address().port}`;
  async function close() {
    if (closing) return;
    closing = true;
    for (const client of clients) client.terminate();
    websocketServer?.close();
    if (server?.listening) {
      server.closeAllConnections();
      await new Promise(resolveClose => server.close(resolveClose));
    }
    upstream.close();
  }
  return { endpoint, close, provenance: { adapter: 'chrome-existing-session-discovery-v1',
    rea_version: '6.4.0', chrome_product: version.product, selected_target_id: target.targetId,
    source_url: source.href, binding: '127.0.0.1', metadata_source: 'real Browser.getVersion and Target.getTargets',
    websocket_transport: 'single owner-authorized Chrome socket; scoped CDP session routing' } };
}

async function main() {
  const options = {};
  for (let index = 2; index < process.argv.length; index += 2) {
    const name = process.argv[index];
    if (!['--rea-package-root', '--active-port-file', '--ready-file', '--source-url', '--target-id'].includes(name) || !process.argv[index + 1]) throw new Error('Use --rea-package-root, --active-port-file, --ready-file and optional --source-url / --target-id');
    options[name] = process.argv[index + 1];
  }
  if (!options['--rea-package-root'] || !options['--active-port-file'] || !options['--ready-file']) throw new Error('Missing required argument');
  const packageFile = resolve(options['--rea-package-root'], 'package.json');
  const packageData = JSON.parse(await readFile(packageFile, 'utf8'));
  if (packageData.name !== 'rea-agents' || packageData.version !== '6.4.0') throw new Error('Use the installed REA 6.4.0 package');
  const WebSocket = createRequire(packageFile)('ws');
  const { WebSocketServer } = WebSocket;
  const bridge = await startBridge({ WebSocket, WebSocketServer,
    advertisement: await readFile(options['--active-port-file'], 'utf8'),
    sourceUrl: options['--source-url'] ?? 'https://explee.com/app-auto-gtm/p/40610',
    targetId: options['--target-id'] });
  try {
    await writeFile(options['--ready-file'], JSON.stringify({ ...bridge.provenance, endpoint: bridge.endpoint,
      started_at: new Date().toISOString() }, null, 2) + '\n', { flag: 'wx' });
  } catch (error) { await bridge.close(); throw error; }
  console.log(JSON.stringify({ status: 'ready', endpoint: bridge.endpoint, chrome_product: bridge.provenance.chrome_product }));
  for (const signal of ['SIGINT', 'SIGTERM']) process.once(signal, () => void bridge.close());
}
if (process.argv[1] && import.meta.url === pathToFileURL(resolve(process.argv[1])).href) {
  main().catch(error => { console.error(error.message.replace(/ws:\/\/\S+/g, '[loopback endpoint]')); process.exitCode = 1; });
}
