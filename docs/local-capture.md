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

Windows equivalents use `python -m venv .venv` and `.venv\Scripts\python.exe`. The helper wraps the npm launcher for Windows; end-to-end verification so far was on Linux. The synthetic browser test harness is POSIX-only.

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
