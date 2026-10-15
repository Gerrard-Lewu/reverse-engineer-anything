import test from 'node:test';
import assert from 'node:assert/strict';
import { createServer, request } from 'node:http';
import { createRequire } from 'node:module';
import { resolve } from 'node:path';
import { parseAdvertisement, startBridge } from '../scripts/bridge_chrome_discovery.mjs';

const packageFile = resolve(process.env.REA_PACKAGE_ROOT, 'package.json');
const WebSocket = createRequire(packageFile)('ws');
const { WebSocketServer } = WebSocket;
const sourceUrl = 'https://explee.com/app-auto-gtm/p/40610';

test('Chrome advertisement cannot select a remote host or extra path', () => {
  for (const value of ['0\n/devtools/browser/abc', '9222\nws://remote/abc', '9222\n/devtools/browser/a?token=x', '9222\n/devtools/browser/a/b']) assert.throws(() => parseAdvertisement(value));
  assert.equal(parseAdvertisement('9222\r\n/devtools/browser/abc-123\r\n'), 'ws://127.0.0.1:9222/devtools/browser/abc-123');
});

test('real protocol replies, isolated clients and target scoping over 404-only discovery', async t => {
  const calls = [];
  const server = createServer((_, response) => response.writeHead(404).end());
  const wss = new WebSocketServer({ server });
  const version = { product: 'Chrome/155.test', protocolVersion: '1.3', userAgent: 'source-agent', jsVersion: 'real-js', revision: 'real-revision' };
  const targets = [{ targetId: 'selected', type: 'page', title: 'Source', url: sourceUrl, attached: false },
    { targetId: 'unrelated', type: 'page', title: 'Private unrelated', url: 'https://example.org/private', attached: false },
    { targetId: 'duplicate', type: 'page', title: 'Second source tab', url: sourceUrl, attached: false }];
  let sessionNumber = 0;
  wss.on('connection', socket => socket.on('message', bytes => {
    const message = JSON.parse(bytes.toString()); calls.push(message);
    let result;
    if (message.method === 'Browser.getVersion') result = version;
    else if (message.method === 'Target.getTargets') result = { targetInfos: targets };
    else if (message.method === 'Target.attachToTarget') result = { sessionId: `session-${++sessionNumber}` };
    else if (message.method === 'Page.captureScreenshot') result = { data: 'real-upstream-bytes' };
    else if (message.method === 'Page.getFrameTree') result = { frameTree: { frame: { id: 'selected', url: sourceUrl } } };
    else result = {};
    socket.send(JSON.stringify({ id: message.id, result, ...(message.sessionId ? { sessionId: message.sessionId } : {}) }));
  }));
  await new Promise(done => server.listen(0, '127.0.0.1', done));
  const port = server.address().port;
  assert.equal((await fetch(`http://127.0.0.1:${port}/json/version`)).status, 404);
  await assert.rejects(startBridge({ WebSocket, WebSocketServer, advertisement: `${port}\n/devtools/browser/real-owner-socket`, sourceUrl }), /exactly one/);
  const bridge = await startBridge({ WebSocket, WebSocketServer, advertisement: `${port}\n/devtools/browser/real-owner-socket`, sourceUrl, targetId: 'selected' });
  t.after(async () => { await bridge.close(); for (const socket of wss.clients) socket.terminate(); wss.close(); await new Promise(done => server.close(done)); });
  const discovered = await (await fetch(bridge.endpoint + '/json/version')).json();
  assert.equal(discovered.Browser, version.product);
  assert.equal(discovered['WebKit-Version'], version.revision);
  assert.equal(new URL(discovered.webSocketDebuggerUrl).port, new URL(bridge.endpoint).port);
  const list = await (await fetch(bridge.endpoint + '/json/list')).json();
  assert.deepEqual(list.map(item => item.id), ['selected']);
  assert.equal((await fetch(bridge.endpoint + '/json/list', { headers: { Origin: 'https://untrusted.example' } })).status, 403);
  assert.equal((await fetch(bridge.endpoint + '/json/list', { method: 'POST' })).status, 405);
  const hostStatus = await new Promise(done => {
    request(bridge.endpoint + '/json/list', { headers: { Host: 'untrusted.example' } }, response => { response.resume(); done(response.statusCode); }).end();
  });
  assert.equal(hostStatus, 403);
  async function client() {
    const socket = new WebSocket(discovered.webSocketDebuggerUrl);
    await new Promise((done, reject) => { socket.once('open', done); socket.once('error', reject); });
    function call(method, params = {}, sessionId) {
      return new Promise((done, reject) => {
        const timer = setTimeout(() => reject(new Error('Test CDP timeout')), 3000);
        socket.once('message', bytes => { clearTimeout(timer); done(JSON.parse(bytes.toString())); });
        socket.send(JSON.stringify({ id: 1, method, params, ...(sessionId ? { sessionId } : {}) }));
      });
    }
    return { socket, call };
  }
  const a = await client(); const b = await client();
  const blocked = await a.call('Target.attachToTarget', { targetId: 'unrelated', flatten: true });
  assert.match(blocked.error.message, /outside/);
  assert.equal(calls.some(item => item.method === 'Target.attachToTarget' && item.params.targetId === 'unrelated'), false);
  const [attachedA, attachedB] = await Promise.all([a.call('Target.attachToTarget', { targetId: 'selected', flatten: true }), b.call('Target.attachToTarget', { targetId: 'selected', flatten: true })]);
  assert.notEqual(attachedA.result.sessionId, attachedB.result.sessionId);
  const denied = await b.call('Page.captureScreenshot', {}, attachedA.result.sessionId);
  assert.match(denied.error.message, /outside/);
  const [screenshot, frame] = await Promise.all([a.call('Page.captureScreenshot', {}, attachedA.result.sessionId), b.call('Page.getFrameTree', {}, attachedB.result.sessionId)]);
  assert.equal(screenshot.id, 1); assert.equal(screenshot.result.data, 'real-upstream-bytes');
  assert.equal(frame.id, 1); assert.equal(frame.result.frameTree.frame.id, 'selected');
  const forbidden = await a.call('Browser.close'); assert.ok(forbidden.error);
  targets[0].url = 'https://other.example/';
  assert.deepEqual(await (await fetch(bridge.endpoint + '/json/list')).json(), []);
  const moved = await a.call('Target.attachToTarget', { targetId: 'selected', flatten: true }); assert.ok(moved.error);
  await a.call('Target.detachFromTarget', { sessionId: attachedA.result.sessionId });
  a.socket.close(); b.socket.close();
});
