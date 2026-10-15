# Explee reverse-engineering completion plan

> **Local continuation (2026-10-15 06:28:01 UTC):** the private evidence prerequisite is resolved and the local Codex Browser reaches the authenticated project. Real REA MCP initialization works on Windows; target discovery is blocked by an unavailable browser endpoint. Provisional native overview material is privately archived and remains unaccepted. The owner reaffirmed that REA is required. Earlier cloud-only access findings below remain historical; [the checkpoint](../docs/handover-checkpoint.md) records the current critical path.

Status: **planning only, 15 October 2026**. No application build has started. This is the remaining source-investigation plan, not a claim of access to the signed-in app or recovery of Explee's server implementation.

## Goal and critical path

Finish an evidence-backed product, interaction and technical blueprint for the selected Explee project, then specify the independent, reusable Ceverio application. The first profile targets HVAC companies with 1–50 employees in South Africa, the U.S. and U.K. Source observations inform the interface and behavior; the user's latest requirements govern the new product.

| Work | Actual status |
| --- | --- |
| Requirements/Ceverio context | Reviewed; 43 requirement IDs and 43 acceptance scenarios in the current planning baseline. |
| Public Explee research | Nine retained source views; 48 documented public method/path pairs. Selective documentation, not authenticated traffic. |
| REA MCP | Actual 6.4.0 session/schemas retained; synthetic capture checks passed. |
| Accepted signed-in Explee states | **Zero.** Screens, DOM/styles and account workflows remain uncaptured. |
| Model/database/cloud design | Pinned model comparison, verified Supabase metadata and named provider dependencies. No app/model deployment or inference benchmark. |
| Ceverio DNS | Cloudflare active; seven mail records and two CNAMEs match the export. DNSSEC pending; user has not added the registrar DS. Separate infrastructure milestone. |

The critical path is **GitHub/private-evidence preflight → browser connection → accepted source evidence → source-derived contracts → planning review**. Oracle provisioning and DNSSEC completion are not prerequisites for inspecting Explee. Follow [the local handover](../docs/local-handover.md) and DEP-11 before collecting authenticated captures.

## R0 — Connect REA to the signed-in source

The selected tab is on the user's Windows computer. This cloud shell cannot reach that machine's loopback browser port. The ambient in-app URL does not expose browser control or a REA transport; no callable desktop-browser surface is currently available here.

Fresh access check, 15 October: the user reconfirmed the existing Codex-browser sign-in. Available-tool and complete skill-catalog checks plus plugin discovery still exposed no desktop Browser/Node REPL connection. The native browser-panel command returned only a queued UI request, not page access. [The access record](../evidence/source-inspection-access-check.json) preserves the outcome. The missing prerequisite is a browser connection for this task, not another login. A question about enabling Browser or using local execution is pending; no Explee source was captured.

Use the existing [local capture instructions](../docs/local-capture.md): REA runs beside a supported Chromium-family browser with an actual literal-loopback CDP endpoint. If the Codex in-app browser later exposes supported tools/an endpoint, validate that exact connection. Otherwise use the documented dedicated Chrome profile, sign in there and run the existing lightweight capture kit. Heavy inference and the future app are not needed on the laptop.

The helper connects through the real REA MCP, discovers targets and validates the exact origin/URL/target. Use actual tool schemas; do not expose the debugging endpoint publicly or scan cloud-local ports as though they belonged to the user.

**First deliverable:** one accepted project-overview capture from `https://explee.com/app-auto-gtm/p/40610`, including receipt and complete export. Inspect its saved pixels/structure before accepting it or collecting further groups.

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

**Next source milestone: R0's accepted overview, then R1/R2 captures in small groups and R3 contracts.** Cloud setup cannot replace missing reference evidence.
