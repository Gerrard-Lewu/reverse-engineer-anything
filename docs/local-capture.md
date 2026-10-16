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

Windows equivalents use `python -m venv .venv` and `.venv\Scripts\python.exe`. The helper wraps the npm launcher for Windows. On 15 October 2026 its seven unit checks and a real authenticated Explee capture passed on Windows using the adapter below. On 16 October the expanded helper/series suite passed 21 Windows checks. Earlier synthetic integration evidence is Linux-only; that harness remains POSIX-only.

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

In the observed Chrome 155 mode, the advertised browser WebSocket worked but `/json/version` and `/json/list` returned HTTP 404. REA 6.4.0 requires those HTTP discovery endpoints and a matching WebSocket port. `scripts/bridge_chrome_discovery.mjs` provides loopback discovery from real `Browser.getVersion`/`Target.getTargets` replies, then routes CDP sessions over the owner-authorized socket. The REA package stays unchanged. The adapter advertises/attaches only the initial Explee target, rejects cross-client sessions and browser commands outside its narrow scope, and stops new attachment if that target leaves the source origin. It is transport scoping, not a sandbox for arbitrary CDP scripts: use the passive helper.

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

## Reuse the installed REA package and session

Both capture commands accept optional `--rea-package-root "C:/path/to/node_modules/rea-agents"`. This uses existing Node to run that package's `scripts/rea.mjs mcp`, bypassing npm startup only. Before creating an output directory, the helper checks package name/version (`rea-agents` 6.4.0), expected dispatcher and compiled runtime paths. Supply a trusted official installation; metadata checks are not publisher attestation. The real MCP `binary_session` version check remains required. Omitting the option preserves pinned npx launching. Cached launching alone did not resolve the observed startup timeout; a later warm run initialized successfully.

For a small group of stable states, initialize real REA once:

```powershell
.venv/Scripts/python.exe scripts/capture_explee_series.py `
  --rea-package-root "C:/path/to/node_modules/rea-agents" `
  --cdp-endpoint $taskChromeReady.endpoint `
  --target-id "ACTUAL_OBSERVED_TARGET_ID"
```

Wait for `READY`, which follows real initialization and tool discovery. Navigate with the existing Browser controls, let the page settle, then submit one JSON object per line:

```json
{"source_url":"https://explee.com/app-auto-gtm/p/40610/docs","label":"project-docs-desktop","output":"evidence/captures/project-docs-new","observation_seconds":1}
```

Commands run sequentially against the fixed selected target and exact supplied Explee URL. Every state needs a new directory; the same screenshot, identity, URL and completeness guards apply. The default observation is one second; 0.1–60 seconds is allowed. The process closes its own MCP session after at most six attempted states, EOF or `{"quit":true}`. A failed state remains reported individually and makes the final process exit code 1. Invalid commands are rejected without creating capture directories.

Each state retains a complete current session export. **Exports are cumulative**, so later folders can include earlier states' private evidence and grow larger; the receipt identifies `cumulative_shared_session`. No retained Evidence is cleared between states. Review and publish each complete private bundle with this scope explicit.

## Completed inspection exceeds the response budget

The helper recovers only REA's explicit completed, untruncated `inspect_web_page` result whose delivery failed at the `mcp-response` receive-buffer boundary. It preserves the original error, requests a real `export_evidence_bundle` into `retained-inspection-bundle.json`, checks the unique exact reported Evidence ID and operation, and saves `inspect_web_page-retained.json`. Both files are hashed. The actual retained normalized result then passes the existing URL/target/completeness guards before screenshot and final export continue. Missing, ambiguous or incompatible records and other tool errors remain failures. The receipt records recovery references, reported limits and the delivery limitation, including when a later operation fails. This recovers retained Evidence; it does not convert failed or incomplete analysis into successful evidence.

Verification command:

```powershell
.venv/Scripts/python.exe -m unittest discover -s tests -p test_capture_explee.py -v
```

All 21 Windows checks passed after the final exit-code/failure-provenance fixes. The already-running 16 October source series used its earlier loaded script versions; exact runtime snapshots/hashes were retained separately. Those live captures establish the earlier runtime behavior, while the 21-check result verifies the final minor fixes. Do not attribute later source edits to a process that had already loaded its code.

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

## Passive transition observation (experimental)

`scripts/observe_explee_transition.py` arms a real REA inspection while the operator navigates through the existing Browser controls. Supply `--cdp-endpoint`, `--target-id`, `--initial-url`, `--final-url`, `--label`, a new `--output`, and optionally `--observation-seconds` (1–60). Act immediately at the `OBSERVING` cue. It captures request shapes and a complete export, checks the selected target final URL, and takes no screenshots or source actions. Pair it with `capture_explee.py` for visual acceptance; `transition_not_confirmed` is not a successful workflow. The revised guard is syntax-checked, with live validation pending.

The capture helper permits up to 120 seconds for MCP initialization and separately reports the 45-second tool-discovery deadline. This changes startup tolerance/diagnostics, not source acceptance. The existing-Chrome adapter waits up to 180 seconds for the owner permission handshake. REA screenshot timeouts are a separate unresolved limitation; never substitute native pixels as accepted REA evidence under DEC-28.
