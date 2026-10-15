# REA and source acceptance protocol

> **Current local status:** `EX-OV-D-001` is accepted for the initial desktop overview through real REA 6.4.0, complete private export and remote-byte verification. Existing signed-in Chrome is connected through the documented discovery adapter. [Current checkpoint](../docs/handover-checkpoint.md) and [sanitized state record](../evidence/source-state-overview-20261015.json). Earlier cloud-access observations below are historical.

## Current state

The [reverse-engineering completion plan](reverse-engineering-completion.md) separates remaining R0–R4 evidence/contract work from future cloud integration and implementation. As of 2026-10-15 09:16:18 UTC, one initial desktop overview is accepted; broader visual/workflow coverage remains pending.

The user selected `https://explee.com/app-auto-gtm/p/40610` in their signed-in browser on Windows. The in-app browser snapshot identifies the requested reference; it is not a capture. The earlier cloud execution environment had no callable desktop-browser control tool or desktop CDP endpoint; local access is now established as recorded above.

REA 6.4.0 was actually initialized over MCP using the official Python MCP client and `npx rea-agents@6.4.0 mcp`. The target-free session and actual selected schemas are retained in `evidence/rea/`. The installed release skill reports version 37/170 tools; repository-main instructions can be newer. Use the connected schemas, not guessed fields or tool names.

The existing [capture helper](../scripts/capture_explee.py) and [Windows instructions](../docs/local-capture.md) are the starting point. They have synthetic Linux verification, not completed Windows/authenticated source acceptance.

The user's GitHub-first requirement adds DEP-11: verify private evidence storage/write/retrieval before collecting authenticated captures. Follow [the local handover](../docs/local-handover.md). Captures are temporarily staged, reviewed, published privately and remotely verified; sanitized findings/checkpoints are pushed to the public planning repo. Never upload credentials or browser profiles.

## Investigation sequence

1. Run REA on the machine that can reach the selected browser's literal loopback CDP endpoint. Do not turn the debugging endpoint into a public remote service.
2. Use the actual `list_browser_targets` schema with that endpoint and exact `https://explee.com` origin. Select the exact URL/target ID; resolve duplicate matching tabs explicitly.
3. Record browser/tool versions, exact target, URL, named state, viewport/device scale, timestamp, scope, and evidence/checklist IDs.
4. Use `inspect_web_page` for DOM/accessibility/resource inventory and attach-window network/body shapes. Capture a screenshot with `capture_web_screenshot`; verify the canonical bytes and digest.
5. Inventory before broader analysis. Use `analyze_web_bundle` only when the shipped frontend answers a specific unresolved question; routes and strings found statically are candidates, not observed private transactions.
6. Use `observe_web_session` for post-attach transitions/network activity where its schema permits. Passive inspection never clicks, navigates, evaluates page JavaScript, sends, starts campaigns, or changes settings.
7. If actions are needed, explicitly record the separate browser-control/scenario surface, initial state, action, resulting state, and effects. Only one controller drives a source target at a time. Existing records can be opened for inspection; sending, launch, billable enrichment, deletion, or booking effects are not ordinary inspection actions.
8. Export complete session Evidence, including error-path evidence. Keep limitations, retention IDs, profile digests, raw receipts, and artifact SHA-256 values.
9. If transport output is constrained, inspect the retained Evidence reference with `inspect_analysis_view` or export the bundle. Do not rerun an identical analysis just to obtain the same oversized answer.
10. Revisit the checklist and unresolved questions after each accepted capture group.

Do not call `open_binary` for target-free browser analysis. Do not run readiness diagnostics repeatedly when session availability is already established. Do not use REA for ordinary Ceverio source-repository reading.

## Required capture groups

Use the [source checklist](../docs/source-capture-checklist.md) as the inventory:

- Project navigation/overview and current Ceverio project settings.
- Targeting, country/size/role criteria, exclusions, score/research panels.
- Existing leads, provenance, verification, selection, and enrichment progress.
- Campaign copy, follow-ups, sending schedule, previews, policy, and lifecycle.
- Inbox tabs/category labels, existing threads, lead details, notes, response controls, and stop behavior.
- Budget/pause/autopilot/analytics status.
- Current booking-link configuration and meeting outcome indicators.
- Import/mapping/row errors and integration capability/status surfaces.
- Matched desktop and 390 × 844 mobile states, plus important dialogs, loading/empty/error states.

Capture the owner's existing campaign and created leads to derive account-specific defaults. Do not replace that audit with invented typical Explee settings.

## Acceptance record per state

| Field | Required information |
| --- | --- |
| Identity | Exact origin/URL/target ID, capture timestamp, viewport, named tab/dialog/scroll state. |
| Behavior | Initial state, action if any, expected observed result, actual resulting state, action surface. |
| Visual | Screenshot and digest; inspected rather than assumed to be the intended authenticated screen. |
| Structure/style | DOM/accessibility, supported computed-style and layout measurements, fonts/icons/assets and state variants. |
| Runtime | Relevant observed request/response shapes, attach interval, errors, and attribution limitations. |
| Static | Bundle candidates with their own Evidence IDs and inference labels. |
| Provenance | REA Evidence IDs, complete export, tool/provider/profile versions and artifact hashes. |
| Coverage | Accepted scope, gaps, truncation/drop/unavailable sections, same-URL state-alignment limitations. |

The kit collects screenshots and structural/runtime evidence. It does not currently prove a complete computed-style inventory or synchronization of changing same-URL content. Obtain missing style/layout/asset measurements through the supported browser surface before design acceptance; never turn absent measurements into guessed exact styles.

A login/loading/error page, wrong target, mismatched state, corrupt artifact, or materially incomplete required evidence cannot be accepted as the intended source state. A matching URL alone does not establish matching state.

## Build gate and fidelity

The user selected faithful recreation. [Product Design's URL-to-code SKILL.md](skill://Plugin_fa77aec24fc08191bc6e57f377126d76/url-to-code/SKILL.md) states: “Capture source evidence first. Do not scaffold, write app code”. Its full rule requires desktop/mobile capture, key states and required assets before implementation. Finish the current spec work while the browser dependency is pending. Once available, derive the visual target and component/state map from accepted captures; do not switch to a new aesthetic or fabricated clone.

That workflow also limits cloning to sites the user owns or has permission to recreate and requires following the site's terms. Reference inspection and reuse must respect Explee's applicable terms/permissions; authenticated account access alone does not establish a right to redistribute its assets.

Faithful states have source screenshot/style evidence and a rendered local comparison at the same viewport and state. Unavailable source states stay explicitly unverified. Proposed recovery/operational views can be specified, but are not described as copied Explee behavior.

Use the 12ui design guidance for actual nontrivial UI implementation while preserving the selected source target. The shared Product Design critical-overrides resource was unavailable from the skill provider; resolve that resource if the provider exposes it during design execution rather than claiming it was read.

Maintain `design-qa.md` during implementation. It names each source state, local route/state, screenshots, behavioral result, discrepancies and severities, fixes, and verification. Final UI handoff requires the required design QA to pass; a successful build/API test is insufficient.

## Evidence and distribution

Label claims `observed`, `documented`, `derived`, `proposed`, or `unverified`, preserving REA's own confidence/authority separately. Published API paths are not captured private frontend requests. Synthetic verification is not authenticated Explee observation.

Keep authenticated records, raw scripts/bundles, screenshots containing contacts, cookies, session storage, and account-specific profiles out of the distributable repository. Retain authorized private evidence locally with its original hashes; distribute reviewed specifications and generic fixtures. Do not replace provenance with a redacted artifact's new hash.
