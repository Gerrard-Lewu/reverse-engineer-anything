# Explee reverse-engineering completion plan

> **Current source status (2026-10-17 05:09:41 UTC):** R0 first authenticated REA overview `EX-OV-D-001` accepted for the initial desktop viewport, with complete private export and remote byte verification. Existing signed-in Chrome is connected through a documented loopback discovery adapter. R1–R4 remain open; [the checkpoint](../docs/handover-checkpoint.md) identifies exact artifact/acceptance commits and remaining coverage. Earlier cloud-only findings below are historical.

Status: **planning only, 16 October 2026**. No application build has started. Selected authenticated states are accepted; this is the remaining source-investigation plan, not recovery of Explee's server implementation.

## Goal and critical path

Finish an evidence-backed product, interaction and technical blueprint for the selected Explee project, then specify the independent, reusable Ceverio application. The first profile targets HVAC companies with 1–50 employees in South Africa, the U.S. and U.K. Source observations inform the interface and behavior; the user's latest requirements govern the new product.

| Work | Actual status |
| --- | --- |
| Requirements/Ceverio context | Reviewed; 43 requirement IDs and 43 acceptance scenarios in the current planning baseline. |
| Public Explee research | Nine retained source views; 48 documented public method/path pairs. Selective documentation, not authenticated traffic. |
| REA MCP | Actual 6.4.0 session/schemas retained; synthetic capture checks passed. |
| Accepted signed-in Explee states | **Twenty-one accepted bounded states:** overview/targeting/Companies/Docs/Domains/integrations plus empty inbox, selected thread/status/Lead info, suppression and schedule presentations. Remaining groups, variants and contracts await evidence. |
| Model/database/cloud design | Pinned model comparison, verified Supabase metadata and named provider dependencies. No app/model deployment or inference benchmark. |
| Ceverio DNS | Cloudflare active; seven mail records and two CNAMEs match the export. DNSSEC pending; user has not added the registrar DS. Separate infrastructure milestone. |

The critical path is **GitHub/private-evidence preflight → browser connection → accepted source evidence → source-derived contracts → planning review**. Oracle provisioning and DNSSEC completion are not prerequisites for inspecting Explee. Follow [the local handover](../docs/local-handover.md) and DEP-11 before collecting authenticated captures.

## R0 — Connect REA to the signed-in source

Historical cloud context, before local continuation: the selected tab is on the user's Windows computer. That cloud shell could not reach the machine's loopback browser port. The ambient in-app URL does not expose browser control or a REA transport; no callable desktop-browser surface is currently available here.

Historical cloud access check, 15 October, before successful local captures: the user reconfirmed the existing Codex-browser sign-in. Available-tool and complete skill-catalog checks plus plugin discovery exposed no desktop Browser/Node REPL connection in that environment. The native browser-panel command returned only a queued UI request. [The access record](../evidence/source-inspection-access-check.json) preserves that historical outcome; later local browser/REA captures supersede its access blocker.

Use the existing [local capture instructions](../docs/local-capture.md): REA runs beside a supported Chromium-family browser with an actual literal-loopback CDP endpoint. If the Codex in-app browser later exposes supported tools/an endpoint, validate that exact connection. Otherwise use the documented dedicated Chrome profile, sign in there and run the existing lightweight capture kit. Heavy inference and the future app are not needed on the laptop.

The helper connects through the real REA MCP, discovers targets and validates the exact origin/URL/target. Use actual tool schemas; do not expose the debugging endpoint publicly or scan cloud-local ports as though they belonged to the user.

**R0 first deliverable achieved for the initial desktop viewport:** one accepted project-overview capture from `https://explee.com/app-auto-gtm/p/40610`, including receipt and complete export. Inspect its saved pixels/structure before accepting it or collecting further groups.

## R1 — Inventory the account and state coverage

These groups are investigation targets, not claims that particular screens were observed. Record actual navigation, routes, controls, permissions and integration statuses. Expand them into named state IDs for tabs/dialogs/selections/scroll positions, disabled controls and responsive variants. Include exposed features deferred from first-release implementation.

| Group | What remains to inspect | Derived contract |
| --- | --- | --- |
| Project/offer | Existing Ceverio offer, ICP, countries/size, roles, exclusions and natural-language steering. | Account facts and profile defaults; preserve differences from the user's newer rules. |
| Discovery/leads | Existing filters/results, research/provenance, scoring, contact/employee evidence, enrichment/status, detail, selection and deduplication. | Fields, filter/scoring meanings, uncertainty, lifecycle and lead interactions. |
| Import/export | Controls, formats/columns, mapping, progress and existing validation/error views. Do not upload contacts to test the source. | Mapping, identity/conflicts, row results and export scope. |
| Campaigns | Existing copy/preview, personalization, cadence/follow-ups, sender, schedule, review/lifecycle and current pause/autopilot controls. | Observed policy and transitions mapped to the independent bounded policy. |
| Inbox | Exact category labels/filters/counts, existing thread, reply eligibility, notes, stop indicators, owner/autoreply settings and compose controls. | Exact taxonomy/semantics and observed transitions; public labels are not account evidence. |
| Booking/integrations | Existing booking URL/settings, outcome indicators and mailbox/CRM/scheduler status/permissions. | Supported link/outcome flow and integration boundaries. |
| Operations/advanced | Analytics definitions, usage/budget, suppression, activity/health/recovery and exposed phone/CC/attachments/multiple-inbox features. | Metric/limit semantics, errors and full feature matrix with first-release/later disposition. |

Inspect existing records and read-only previews. Passive REA and browser navigation/control are separate surfaces; only one controller drives the source. Do not launch/pause/edit a campaign, save/send a reply, purchase enrichment, reconnect integrations, delete data or create bookings to produce evidence. Safely unreachable states remain blocked/unobserved.

## R2 — Capture visuals, behavior and runtime evidence

Follow [the source protocol](reference-protocol.md) and [capture checklist](../docs/source-capture-checklist.md) for each named state:

- Preserve exact URL/target, timestamp, viewport, initial/action/result, REA Evidence IDs, complete export, screenshot bytes and artifact hashes.
- Inspect pixels and align them with available DOM/accessibility evidence. Same-URL content can change; matching URLs alone are insufficient.
- Capture full vertical extent, sticky/lazy-loaded elements and relevant interactions at the recorded desktop viewport and **390 × 844** mobile viewport.
- Collect supported computed styles/layout, typography, fonts, icons/assets and component variants. The helper's structural/resource capture alone does not establish a full style catalog. Resolve required assets before faithful scaffolding.
- Record observed read request/response shapes and error semantics in the attach interval. Keep sensitive payload values out of derived contracts. Use shipped bundle analysis only for specific gaps; static names remain candidates.
- Inventory loading/empty/error/validation states separately. Capture safely reachable examples; do not trigger external effects for them.

Retain pre-attach gaps, excluded origins, truncation and unavailable sections. A helper success cannot accept a wrong/login/loading page as the requested app state. Keep raw captures, real contacts and message history outside distributable Git.

## R3 — Complete the blueprint and spec

Update the existing documents rather than creating a conflicting architecture:

1. **Feature/state matrix:** observed source state → evidence → first-release/later scope → requirement/acceptance IDs → unresolved gap. Include every exposed relevant control.
2. **Component/style catalog:** responsive layouts, tokens, resolved assets/fonts, variants and interactions. Each selected faithful state requires its screenshot and available DOM/style/layout evidence; replacements need provenance/reasons.
3. **Workflow contracts:** discovery → qualification/review → campaign → inbox → booking, including source-derived categories/counts, stop conditions, permissions and failures. Distinguish observed transitions from documented/proposed ones.
4. **Data/API contracts:** fields, validation, pagination, filters, timestamps, IDs and async status. Compare public docs with observed private read shapes and retain discrepancies. Complete the public schema if accessible; current fragments do not prove a complete private API.
5. **Independent-service boundary:** preserve independent providers, durable jobs, no-duplicate effects, model roles, zero-spend limits and recovery. Screens do not recover Explee's private datasets, warmed inbox fleet, server architecture, prompts or model weights.

Classify consequential statements as **observed**, **documented**, **inferred**, **proposed** or **unverified**, with evidence or decision IDs. Do not label proposed Ceverio behavior exact Explee parity. Account-unavailable features retain an explicit limitation and independent design decision.

## R4 — Review and close planning

The source investigation is complete for an explicitly inventoried scope only when:

- The correct account/project and actual feature/navigation inventory are confirmed.
- Every interaction/state selected for faithful recreation has accepted desktop/mobile visual and available structure/style evidence, with required assets/fonts resolved. Missing required source evidence keeps the fidelity gate blocked.
- Requested existing project/lead/campaign/inbox/booking facts are evidence-linked, with exact-parity claims withheld for inaccessible facts. Exact inbox taxonomy is not asserted before observation.
- Feature/state/component/workflow/data contracts agree; consequential behavior maps to requirements and meaningful acceptance examples. New findings do not silently override the user's later business rules.
- Evidence attribution, gaps, scope and provider boundaries receive a recorded planning review. This is not application testing or rendered design QA.

The output is a reviewable blueprint and dependency register. **The user's no-build instruction remains in force after planning completion.** S3 implementation, model installation, provisioning, live sends and booking tests do not start during this work.

## Separate final-product prerequisites

These remain in [remaining layers](remaining-layers.md), [decisions](decisions.md) and [the build sequence](build-plan.md); they do not block read-only source capture.

| Dependency | Remaining work |
| --- | --- |
| DNS/services | Add current DS at GoDaddy; validate chain/delegation, website destination and later controlled Zoho delivery. [Exact steps](dns-cutover.md). |
| Private cloud | Verify Ashburn Always Free allowance/capacity; later prepare owner-only Access/Tunnel, host services and independent recovery. |
| Database/model | Supabase metadata is resolved; schema/grants/host access and model runtime/quality remain future checks. |
| Prospect sender | Establish permitted transport and exact sender account; DNS parity is not campaign permission or deliverability. |
| Booking/testing | Confirm Ceverio booking link/account and controlled test addresses/events. |

**Next source milestone: R1/R2 captures in small groups, including full vertical/mobile overview coverage, followed by R3 contracts.** Cloud setup cannot replace missing reference evidence.
