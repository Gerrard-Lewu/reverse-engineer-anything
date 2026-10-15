# Verification and evidence limits

## Responsive targeting checkpoint

Four REA states are accepted in total. The [responsive record](../evidence/source-state-targeting-responsive-20261015.json) gives private immutable references, screenshot/archive hashes and exact limits. All 17 remote files matched full local bytes; all 62 evidence member hashes passed. Seven `test_capture_explee.py` checks and two `test_chrome_discovery_bridge.mjs` checks passed on Windows. `observe_explee_transition.py` passed `py_compile`; its revised final-URL guard has not yet had a live execution. No application tests or build occurred.

Failed REA screenshot/initialization attempts and the unsuccessful navigation are retained, without converting native evidence into accepted REA states. Startup allowance/diagnostics are a tooling change whose revised live execution is still pending.

## Targeting/asset checkpoint — 2026-10-15 09:43:46 UTC

The second initial desktop viewport `EX-TG-D-001` passed real REA, saved-pixel/accessibility, credential and private remote-part/member checks. Four separately fetched loaded CSS/font assets and provenance matched remote bytes. Adapter tests passed again after exact-target selection was added: duplicate URL ambiguity is rejected and explicit selection remains scoped to one target. Native control recovered in a fresh same-profile tab. Full vertical/mobile/style/workflow/API acceptance remains pending. [Record and limitations](../evidence/source-state-targeting-20261015.json).

## Accepted local REA overview — 2026-10-15 09:16:18 UTC

- Existing helper: seven Windows unit tests passed; actual REA 6.4.0 capture with isolated MCP 1.29.0 succeeded.
- Discovery adapter: `node --test tests/test_chrome_discovery_bridge.mjs` with `REA_PACKAGE_ROOT` pointing to installed REA 6.4.0: **2/2 passed**. Tests cover 404-only discovery, real reply forwarding, selected-target and client-session isolation, origin/Host rejection and navigation outside scope.
- Saved screenshot and accessibility evidence agree on the authenticated project/dashboard. No truncation/unavailable sections or dropped events; expected policy/pre-attach limits remain. No requests occurred in the idle observation window.
- Private artifact/retrieval/acceptance records verified remotely; three complete binary parts match the archive, all 11 member hashes checked, and standalone records read back. Initial desktop viewport only; full vertical/mobile/style/assets/API coverage remains pending.
- Earlier startup timeout, freezing separate profile, legacy discovery HTTP 404 and binary-retrieval failures are retained in the [sanitized state record](../evidence/source-state-overview-20261015.json). The POSIX synthetic harness was not run on Windows.

## Earlier local Windows checks — 2026-10-15 06:28:01 UTC (historical)

- Python 3.12.14, Node 24.14.0, isolated MCP client 1.29.0 and REA 6.4.0 were exercised locally.
- `.venv\\Scripts\\python.exe -m unittest discover -s tests -p test_capture_explee.py -v`: **7/7 passed**.
- The actual helper initialized REA MCP, retained its session/schema records and exported diagnostics. `list_browser_targets` failed with `provider_unavailable / endpoint_unreachable`; no successful Windows source capture or real-browser integration pass is claimed.
- Private storage visibility, write/retrieval and all 14 archived artifact bytes were verified. Native source overview material remains provisional; later screenshot frames are clipped and no mobile state was collected.
- Automatic approval review rejected dedicated Chrome launch (“blocked by policy”). The owner retained the REA gate and agreed to open the browser.

[Current checkpoint](handover-checkpoint.md) and [sanitized machine-readable record](../evidence/local-source-preflight-20261015.json). Original Linux verification below remains historical evidence.

Updated 15 October 2026. The capture kit and document package are implemented. The internal lead-to-meeting app is a proposed future build. Authenticated Explee workflows are unverified. DNS follow-up below is read-only; original capture-kit test results remain dated to their prior execution.

Current phase: **planning**. The application build has not started. The [specification](../specs/README.md) now contains 43 unique requirements and 43 Given/When/Then scenarios. Their references and local links were checked. An independent read-only review covered the earlier 36-scenario baseline; model/cloud/DNS/GitHub additions received a local consistency review. These are specification checks, not executed app or DNS-cutover acceptance tests.

## Executed checks

| Check | Recorded result | What it establishes |
| --- | --- | --- |
| `python3 -m unittest discover -s tests -v` | 7/7 passed | Invalid remote/credentialed CDP endpoints and overwrite attempts are rejected; screenshot pixels/digests and material coverage gaps are handled. |
| `python3 tests/verify_capture_integration.py` | Passed against real Chromium 154 and REA 6.4.0 on Linux | Actual MCP discovery, exact target selection, page inspection, post-attach GET/JSON body-shape observations, verified PNG extraction, static bundle analysis, Evidence export, and artifact hashes. |
| Independent read-only review and isolated MCP boundary probes | Seven scenarios passed | Baseline success, URL/identity mismatch, retained-evidence errors, DOM truncation, expected policy filtering, and export failure preserve appropriate outcomes and diagnostics. |
| Public evidence index generation | Passed | Saved source and retrieval hashes, known source/response references, and documented path presence agree with the retrieved artifacts. |
| Markdown/link and package inspection | Passed | Local document targets and packaged capture-tool files exist. |
| Cloudflare/GoDaddy comparison, 15 October | Nine comparable service values match: seven mail and two CNAME; 11 current records DNS only | Active zone verified by GET-only MCP. Export's WebsiteBuilder Site alias prevents literal A parity. DNSSEC pending; user has not added current DS at GoDaddy. No validated parent chain or live mail test. |

The real-browser fixture is `tests/fixtures/index.html`; it explicitly identifies itself as synthetic. Its periodic JSON fetch supplies known post-attach traffic. Verification data is retained under `evidence/verification/` and excluded from Git. No Explee API mutation, outbound lead email, or meeting creation was performed.

## Requirement traceability

| Requirement | Result | Evidence |
| --- | --- | --- |
| Use REA MCP, not a CLI-only approximation | Confirmed for tooling | Real server identity 6.4.0, negotiated MCP session, and actual tool records in the synthetic capture. |
| Preserve records and exact screenshot bytes | Confirmed for selected fixture | Receipt hashes and PNG matched REA's declared digest and byte count. |
| Reject another same-origin route/target | Confirmed in unit/boundary probes | Saved failure rather than a successful attribution to the original URL. |
| Export retained evidence before failure teardown | Confirmed in isolated boundary probes | Export occurs in the session guard; export errors are recorded without replacing the original failure. |
| Report materially incomplete source capture | Confirmed in unit/boundary probes | Truncated/unavailable/dropped coverage yields `partial`; expected policy/attach limits remain disclosed. |
| Source-backed product/API baseline | Confirmed for retrieved public scope | Nine source entries and 48 indexed documented public method/path pairs. |
| Capture signed-in Explee screens and interactions | Partial | Initial desktop overview `EX-OV-D-001` accepted through real REA on Windows; other states remain pending. |
| Recover complete public OpenAPI schema | Partial | Only selectively retrieved schema fragments were available. |
| Verify faithful visual/UI recreation | Unverified | No Explee screenshots/style evidence or recreated app exists yet. |
| Validate live lead, email, and calendar integration | Unverified | Intended sender/booking configuration and app integrations remain unconfigured. Supabase access/metadata/Free plan are now verified; application grants and host connection are not. No application-level live test was performed. |
| Inspect Jev Ultrafast and Laya | Confirmed for source scope | Pinned code/manifests and published model/benchmark material reviewed; returned Git IDs in model-cloud-source-index.json. No model executed and no equal-condition benchmark performed. |
| Inspect the selected Explee REA Supabase project | Metadata and table inventory verified | New REA Org connector confirms active eu-west-1 project, PostgreSQL 17.11 and Free plan. Platform tables only in returned inventory; no application tables observed. No contact rows/keys retrieved or schema changes. |
| Establish a free cloud deployment | Proposed, unverified | Oracle Free Tier/Ashburn reported by user; actual capacity and VM not inspected. Cloudflare zone Free is observed; Workers AI/Zero Trust entitlement, private route and models remain untested. |
| Inspect ceverio.com Cloudflare setup | Active-zone status and comparable export parity verified, 15 October | Expected account, active full Free zone, exact assigned nameservers and 11 DNS-only records. All seven mail records and both CNAMEs match the supplied export. Symbolic A target, parent chain and live website/mail remain unverified. DNSSEC pending; DS not added at registrar according to user. No DNS/registrar changes by this inspection. |
| Inspect private access and billing | Partial | Access API reports not enabled; proposed named tunnel not returned. Account subscription read denied by authentication/permission error. No billing/Access configuration changed. |

## Remaining practical limits

The capture CLI was executed on Linux with Python 3.12 and Node 24.19. It requires Python 3.11+. Windows launch handling is included but Windows/macOS execution was not exercised. The synthetic integration harness uses POSIX process-group cleanup and is explicitly POSIX-only.

Source capture is sequential across REA calls. Matching target URL/identity does not prove that same-URL UI content remained unchanged between inspection and screenshot; the receipt states that limitation. Each saved screenshot must be inspected and matched to the intended state before becoming accepted source evidence.

The real-browser success path was exercised. Transport-budget and export-failure handling were exercised at the MCP boundary with isolated substitutes, not induced against the real REA process. No result from those substitutes is treated as Explee Evidence.

Public connector responses may be cached/selective; their saved bytes are complete as returned, not a claim that the full page/API schema was recovered. Firecrawl credit failures are access diagnostics. Exact backend internals, dataset possession, and managed inbox infrastructure remain outside what these sources can establish.
