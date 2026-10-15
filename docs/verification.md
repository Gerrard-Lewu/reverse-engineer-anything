# Verification and evidence limits

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
| Capture signed-in Explee screens and interactions | Blocked | No local browser connection exposed to this cloud chat. |
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
