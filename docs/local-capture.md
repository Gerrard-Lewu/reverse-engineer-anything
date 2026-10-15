# Capture the signed-in Explee reference locally

This kit bridges the missing evidence connection: run it on the same computer as the signed-in source browser, then publish the reviewed capture bundle to a verified private GitHub destination. A cloud process cannot attach to your computer's loopback debugging port. Follow [the local handover](local-handover.md) for GitHub preflight/checkpoints; capture folders are temporary staging, not local-only deliverables.

The helper uses REA 6.4.0 through the official Python MCP client. It opens an ephemeral server connection and leaves persistent Codex configuration untouched. It never navigates, clicks, sends email, or changes a campaign. Existing source-browser tools can be used instead if they expose a REA-supported CDP endpoint.

## Prepare the runtime

Use Python 3.11+ and an existing Node.js/npm installation supported by REA 6.4.0: Node 22.x >=22.19, 24.x >=24.11, or 26+. Installing the kit's Python dependency does not install a lead-to-meeting app.

```bash
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements.txt
npx -y rea-agents@6.4.0 --version
```

Windows equivalents use `python -m venv .venv` and `.venv\Scripts\python.exe`. The helper wraps the npm launcher for Windows. On 15 October 2026 its seven unit checks and a real authenticated Explee capture passed on Windows using the adapter below. Earlier synthetic integration evidence is Linux-only; that harness remains POSIX-only.

## Expose the source browser

If your existing source browser already exposes `http://127.0.0.1:PORT`, use that endpoint. The in-app browser's visible URL alone does not establish a CDP connection.

Otherwise start a dedicated Chromium-family profile on your computer and sign into Explee there. The following commands use an existing browser; select the one installed on your machine.

macOS:

```bash
"/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" --remote-debugging-port=9222 --user-data-dir="$PWD/.rea-browser" "https://explee.com/app-auto-gtm/p/40610"
```

Linux:

```bash
chromium --remote-debugging-port=9222 --user-data-dir="$PWD/.rea-browser" "https://explee.com/app-auto-gtm/p/40610"
```

Windows PowerShell, when Chrome is installed at this location:

```powershell
& "$env:ProgramFiles\Google\Chrome\Application\chrome.exe" --remote-debugging-port=9222 --user-data-dir="$PWD\.rea-browser" "https://explee.com/app-auto-gtm/p/40610"
```

A separate profile is required for debugging-port launches on recent Chrome versions. REA attaches to a literal loopback endpoint with an explicit port. The profile and browser remain yours to close after collection.

## Existing signed-in Chrome

This route was verified on Windows with Chrome 155, REA 6.4.0, Python 3.12.14, Node 24.14.0 and isolated `mcp==1.29.0`. Chrome 144+ can let an owner enable debugging for an already running session ([official Chrome guidance](https://developer.chrome.com/docs/devtools/agents/use-cases/auto-connect)). The owner completes `chrome://inspect/#remote-debugging` and any Chrome Allow prompt manually. This grants profile debugging access; inspect only the selected Explee tab. Never copy cookies or profiles.

In the observed Chrome 155 mode, the advertised browser WebSocket worked but `/json/version` and `/json/list` returned HTTP 404. REA 6.4.0 requires those HTTP discovery endpoints and a matching WebSocket port. `scripts/bridge_chrome_discovery.mjs` provides loopback discovery from real `Browser.getVersion`/`Target.getTargets` replies, then routes CDP sessions over the owner-authorized socket. The REA package and capture helper stay unchanged. The adapter advertises/attaches only the initial Explee target, rejects cross-client sessions and browser commands outside its narrow scope, and stops new attachment if that target leaves the source origin. It is transport scoping, not a sandbox for arbitrary CDP scripts: use the passive helper.

Use the already installed REA **6.4.0** package directory; the adapter loads its existing `ws` dependency and does not install anything. Start it in one PowerShell terminal:

```powershell
node scripts/bridge_chrome_discovery.mjs `
  --rea-package-root "C:/path/to/node_modules/rea-agents" `
  --active-port-file "$env:LOCALAPPDATA/Google/Chrome/User Data/DevToolsActivePort" `
  --ready-file ".capture-staging/chrome-ready.json"
```

Use a new ready-file path each run. For duplicate matching tabs, add `--target-id` with an actual observed CDP target ID; ambiguity is rejected instead of choosing arbitrarily. The owner approves Chrome if prompted. Once the adapter prints `ready`, use the emitted endpoint in a second terminal:

```powershell
$taskChromeReady = Get-Content -Raw .capture-staging/chrome-ready.json | ConvertFrom-Json
.venv/Scripts/python.exe scripts/capture_explee.py `
  --cdp-endpoint $taskChromeReady.endpoint `
  --output evidence/captures/overview-new `
  --label project-overview-desktop
```

If npm startup is slow and this exact package is already cached, a process-scoped `NPM_CONFIG_OFFLINE=true` was used successfully. The first initialization attempt exceeded 45 seconds; a later warm/offline launch succeeded. These observations do not prove a network-only cause. Leave Chrome stable during each capture. Stop the adapter with Ctrl+C after collection; it releases its own sessions/socket and leaves Chrome open. If an older native tab attachment remains detached, a fresh tab in the same signed-in profile restored native control in this investigation. Use its actual target identity for subsequent REA captures. Preserve only its safe ready/provenance metadata, never `DevToolsActivePort` or the upstream WebSocket capability URL.

Verify the adapter with `REA_PACKAGE_ROOT` pointing to the installed REA directory:

```powershell
$env:REA_PACKAGE_ROOT = "C:/path/to/node_modules/rea-agents"
node --test tests/test_chrome_discovery_bridge.mjs
```

The first accepted state and exact private commits are in the [sanitized overview record](../evidence/source-state-overview-20261015.json). GitHub Contents API omits binary content above 1 MB; the complete archive is also retained as ordered sub-1-MB parts with `archive-reconstruction.json`. Retrieve every part at the recorded immutable commit, compare full bytes/hashes, concatenate in order and check the archive/member hashes. Keep readback failures explicit.

## Capture one stable state

Open the intended page manually, wait for it to settle, and run:

```bash
.venv/bin/python scripts/capture_explee.py --cdp-endpoint http://127.0.0.1:9222 --output evidence/captures/01-project-desktop --label project-overview-desktop --analyze-bundle
```

If the visible URL differs, pass that exact URL with `--source-url`. For duplicate tabs use the target ID in the saved discovery record with `--target-id`. Every capture needs a new output directory so earlier evidence is preserved.

The 10-second observation window collects newly arriving requests. Keep the intended state in view; after the window ends, leave it stable until the command finishes. A route or target change makes the capture fail rather than attributing another page to the selected URL. Same-URL content can still change; the receipt records that cross-call visual/DOM alignment is not proven.

For subsequent UI states, open the relevant control manually and run another capture with its own label/folder. REA saves viewport screenshots, so scroll and capture numbered sections for content below the fold. Capture mobile at 390 × 844 using the browser's supported device emulation; the screenshot receipt preserves the observed viewport.

## What comes back

- Complete returned REA records for discovery, page inspection, screenshot, and optional static bundle analysis.
- Exact PNG screenshot bytes checked against REA's declared byte count and SHA-256.
- An exported session Evidence bundle, including retained results when a tool response encounters a transport budget limit.
- Actual selected tool schemas and server identity.
- A receipt with hashes, Evidence IDs, viewports, completeness markers, and an honest result status.

`captured` is bounded to the chosen capture. `partial` flags material missing/truncated evidence. `failed` preserves diagnostics and attempts an Evidence export before teardown. All states can carry policy and attachment limits: request history before attach is unavailable, excluded-origin resources stay excluded, and body-shape evidence contains types rather than payload values.

REA's passive DOM capture is structural; it does not supply a full computed-style catalog. Screenshots and loaded-resource metadata are useful evidence, but faithful styling still needs supported DOM/CSS/asset collection. Do not substitute guessed tokens.

Source maps are not fetched by this helper. The optional bundle pass derives static candidates, which remain separate from runtime behavior.

## Return the source evidence

Keep complete capture groups, including receipt.json, screenshot and bundle, until reviewed private GitHub publication and remote hash verification succeed. Integrate sanitized references/coverage into the public evidence index, blueprint and checkpoint, then push those updates too. Never upload credentials/browser profiles or place authenticated data on public branches. Start with the project overview and existing lead/review/inbox states in [the checklist](source-capture-checklist.md). Existing records and previews are sufficient; live outreach and meeting creation belong to the later integration phase.
