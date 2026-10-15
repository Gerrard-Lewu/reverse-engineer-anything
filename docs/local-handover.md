# Local Codex handover

> **Current local status:** four authenticated REA states accepted: overview initial desktop and targeting top/lower desktop plus mobile. The owner-enabled existing Chrome connection and private remote verification are established. Continue R1–R4 from [the current checkpoint](handover-checkpoint.md); [existing-Chrome instructions](local-capture.md#existing-signed-in-chrome) document the working route. Earlier proposed-destination and cloud-access statements are historical.

Prepared 15 October 2026. **Planning/source investigation only.** This handover authorizes continuation of inspection and GitHub publication within the existing scope, not application implementation or live outreach.

## Outcome

Complete R0–R4 in [the source completion plan](../specs/reverse-engineering-completion.md): connect to the authenticated Explee reference, capture its relevant workflows and visual/technical evidence, derive the final blueprint/contracts, and review the planning gate. Keep GitHub current throughout; do not leave durable deliverables only on the computer.

## Execution and storage

| Item | Location / rule |
| --- | --- |
| Durable planning/code | Public `Gerrard-Lewu/reverse-engineer-anything`; use the verified published branch, then small pushed checkpoints. |
| Authenticated source evidence | Proposed private `Gerrard-Lewu/explee-private-evidence`; verify private visibility and access before any captures. It has not been created/verified by this handover. |
| Working checkout/capture staging | Disposable local directory, ideally under Windows temporary storage. A working copy is not the authoritative archive. |
| Browser login and credentials | Owner-managed browser/credential store; never GitHub, chat, an evidence bundle or a copied cookie file. |
| Model weights/dependencies/caches | Not project deliverables. No model installation in this phase. The laptop does not host the future app. |

A literal zero-file local run is not possible: Git, a browser and the capture tools use disk. The controlling rule is **no local-only durable project work**, plus remote verification before removing temporary copies. Do not delete the owner's existing checkout/profile or any artifact whose only copy is still local.

## 1. Open the GitHub-backed project locally

In Codex choose **Work in → This computer**, then open an existing checkout of the repository or clone it into a disposable directory. Do not overwrite an existing directory. For a fresh PowerShell checkout, after checking that the chosen destination does not exist:

```powershell
$expleeWorkRoot = Join-Path $env:TEMP ("explee-planning-" + [guid]::NewGuid().ToString("N"))
git clone https://github.com/Gerrard-Lewu/reverse-engineer-anything.git $expleeWorkRoot
Set-Location $expleeWorkRoot
git status --short
git log -1 --oneline
```

Use the published GitHub commit as the baseline. Read AGENTS.md and the checkpoint before acting. Do not recreate the project from this chat's memory or ask the user to repeat the answered business questionnaire.

Read-only clone access does not establish push permission. Verify the intended GitHub account is Gerrard-Lewu and that an available connector or normal Git credential can write this repo. Use supported sign-in if needed; never request pasted tokens or export credentials from another environment. The cloud shell's gh credential failed authentication; its connected GitHub app remained writable. Local credentials must be checked afresh.

## 2. Establish private evidence storage before capture

Inspect the exact proposed evidence repository and verify its owner and **private** visibility. If it does not exist, create it private through authorized GitHub access where available; do not change this public repository's visibility or substitute a public branch. If neither inspection nor creation is available, publish the blocker and continue source-independent planning, holding raw authenticated capture collection.

The proposed private repo stores reviewed screenshots, REA exports/receipts, source-style/asset records, acceptance notes and their manifests. Secrets, cookies and browser profiles are excluded even there. Use review/redaction procedures that preserve original versus derived hashes and disclose any removed fields; do not silently relabel redacted bytes as an original capture.

For each accepted group: stage a reviewed explicit list in the private repo, commit/push (or upload a uniquely named private release archive), retrieve/compare the remote copy and hashes, then publish only sanitized coverage/pointers in the planning repo. Avoid paid storage/LFS and expiring-only archives. A gitignored capture directory is temporary staging, not a completed storage solution.

## 3. Connect the existing browser and real REA MCP

Try the existing signed-in Codex browser first. In the local desktop task select `@Browser`, inspect the available tabs and choose the exact Explee project `https://explee.com/app-auto-gtm/p/40610`. The currently active desktop tab may be GitHub; do not assume it is Explee.

Under Settings → Browser → Agent permissions, allow the required website. Developer mode → Enable full CDP access supports DOM/style/network inspection when available; complete the app's explicit site-specific request. These settings do not themselves prove an MCP endpoint exists or that the browser connection is live.

Use the real REA MCP on this computer, with the actual connected schema and a supported literal-loopback browser endpoint. Pin the tested 6.4.0 release initially. The existing [capture instructions](local-capture.md) and helper start an ephemeral real MCP session; persistent global MCP configuration is not required for that route.

Check Python 3.11+, Git and supported Node/npm (22.x ≥22.19, 24.x ≥24.11, or 26+). Install only the capture dependencies needed for this authorized investigation, not application/model infrastructure. On Windows use the documented Python launcher paths; the helper's Windows path handling has not yet been exercised on a real Windows host.

If the Codex browser has no REA-compatible endpoint, record the missing capability. Then use the documented dedicated local Chromium profile route. Existing Codex cookies are not copied into Chrome; if a separate profile needs sign-in, the owner does it inside that browser. Keep the debugging endpoint loopback-only. Do not guess ports, expose debugging publicly or make cloud-local discovery stand in for desktop access.

## 4. First capture and acceptance

Collect one stable authenticated project overview first, using a fresh output directory and the actual validated endpoint. [local-capture.md](local-capture.md) contains the command. Retain target discovery, complete MCP records/export, exact screenshot, receipt, hashes and limits. Inspect the saved pixels to prove it is the intended authenticated account/project; URL equality alone is insufficient.

Publish the reviewed private evidence and verify it remotely before accepting the milestone or cleaning up staging. Record the public sanitized checkpoint. Do not announce an account audit from a login/loading/error page, public API docs, a queued browser panel or a synthetic fixture.

Then work in small groups:

1. Project offer, ICP, countries, size, exclusions and current Ceverio instructions.
2. Lead results, filters, details, provenance, scores, contact/employee evidence and existing import/export surfaces.
3. Campaign copy/personalization, cadence, schedules, review/lifecycle, sender and current autopilot/limits.
4. Exact inbox categories/semantics, existing threads, notes, stop rules, reply eligibility and owner/autoreply settings.
5. Existing booking-link/integration settings, outcome indicators, operations/analytics and advanced feature inventory.
6. Matched desktop/390 × 844 mobile states, DOM/computed styles/layout, fonts/icons/assets, dialogs and safely reachable empty/error/loading states.

Existing records/read-only previews are sufficient. Do not use Save/Start/Stop/Send, enrichment purchases, integration reconnection, deletion or booking creation to generate evidence. Browser navigation/control and passive REA observation are separate surfaces; one controller drives a target at a time.

## 5. Finalize contracts and publish each checkpoint

Update existing specs/blueprint with evidence-linked feature/state/component, workflow and data/API contracts. Preserve observed/documented/inferred/proposed/unverified labels. User requirements take precedence over old Ceverio or Explee settings. The current baseline has 43 requirement IDs and 43 acceptance scenarios; new source findings may require reviewed additions, not fabricated passes.

For every meaningful completed unit: update the sanitized checkpoint/coverage, run proportionate checks, inspect the explicit diff and excluded paths, commit/push to the correct repository and verify remote refs/artifacts. Do not force-push, silently include unrelated work, or report a failed upload as saved. Keep the only working copy until a durable remote copy is verified.

R4 planning acceptance is not application testing or rendered design QA. After it passes, remain in planning until the user explicitly starts the build phase.

## Settled context and dependencies

The [checkpoint](handover-checkpoint.md) records current facts. The final app remains privately cloud-hosted with reusable business profiles. Oracle Ashburn account details are user-reported; Supabase target metadata is verified; no application schema/host/model deployment exists. Model comparison recommends evaluating Laya for decisions plus a verified free writing path, not unmodified hosted Jev. A permitted prospect sender, Ceverio booking link, controlled test destinations, live model quality and deployment acceptance remain unresolved. These do not block reference inspection.

Cloudflare activation and nine comparable DNS values were verified read-only on 15 October. DNSSEC was pending and the user had not yet added the registrar DS. These are dated facts, not proof of the current chain or permission for a DNS change.

## Continuation prompt for local Codex

```text
Continue this repository's Explee reverse-engineering handover. Read AGENTS.md,
START-HERE.md, docs/local-handover.md, docs/handover-checkpoint.md and the specs.
We are still planning; do not build the application or perform live outreach,
DNS changes, provisioning or model installation.

Plan before executing. Verify GitHub write access, the public planning repo and
a private evidence destination first. Use the existing signed-in Codex Explee
tab through @Browser and the real REA MCP on this computer. Inspect actual tools,
schemas and endpoint access; do not assume that seeing a URL proves access.
Capture and accept one real project overview, then follow R1-R4 in small groups.

Preserve all settled Ceverio requirements. Keep source evidence and proposals
distinct. Push every eligible completed unit and checkpoint to GitHub; private
captures belong only in a verified private repo/asset destination. Local files
are temporary working material. Never upload credentials/browser profiles or
delete the only unverified copy. Report remote commits, evidence and remaining
blockers. Do not claim source capture or a push without verifying it.
```

Setup references: [Codex environments](https://learn.chatgpt.com/docs/environments/modes), [Browser and Developer mode](https://learn.chatgpt.com/docs/browser?surface=app), [MCP configuration](https://learn.chatgpt.com/docs/extend/mcp?surface=app), [REA upstream](https://github.com/morluto/rea).
