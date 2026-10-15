# Decisions and dependencies

Status: requirements baseline with named integration dependencies. User instructions take precedence over older project documents. Delegated choices below are implementation defaults, not evidence of Explee internals.

## Answered requirement groups

| ID | Answer / resulting decision | Basis |
| --- | --- | --- |
| DEC-01 | Ceverio automation business first; use its operating material; reusable profiles for other businesses. | Q01, user answer. Ceverio working branch inspected. |
| DEC-02 | South Africa, U.S., U.K.; HVAC; 1–50 employees. Residential/independent preference and scorecard inherited as editable Ceverio defaults. | Q02 plus Ceverio scorecard. New geography overrides older U.S.-only guidance. |
| DEC-03 | Independent discovery adapters and CSV; Explee only a reference. | Q03. |
| DEC-04 | Google mailbox/calendar capabilities requested. Ordinary Ceverio DNS routes to Zoho; permitted campaign transport remains unresolved. | Q04–05; connected Google identity is personal; current Cloudflare MX/SPF inventory observed. |
| DEC-05 | Prefer the existing Ceverio sender identity; do not provision extra inboxes solely to increase volume. Actual reuse is conditional on permitted transport and account capability; migration/new provisioning and cost may be necessary. | Q05 delegation; existing Zoho Mail cannot supply the automated campaign channel. |
| DEC-06 | Deliverability and service limits govern volume. Pilot/caps are in product.md; no guaranteed inbox placement. | Q06; operational defaults and provider guidance. |
| DEC-07 | Bounded autonomous discovery, outreach, and replies; no daily batch approval. Controlled pilot precedes unattended activation. | Q07; Ceverio's existing authorization. |
| DEC-08 | Use Ceverio cadence as baseline; audit the existing Explee campaign when accessible. | Q08; actual Explee account not yet inspected. |
| DEC-09 | Reproduce Explee categories/transitions from capture; proposed internal taxonomy meanwhile. | Q09; exact taxonomy is an evidence dependency. |
| DEC-10 | Booking links first; confirmed outcomes synced separately. | Q10. |
| DEC-11 | Meeting duration, hours, buffers, horizon, conferencing, and cancellation defaults delegated; use Ceverio-specific configuration. | Q11; product.md. |
| DEC-12 | Whole application in the cloud; Windows is the owner browser and optional local client. | Q12 updated by the user's cloud-placement answer, 14 October 2026. |
| DEC-13 | Windows 11; use the Supabase plugin and assess Supabase/Postgres. React/TypeScript and Node 24 API/worker selected as the proposed coherent runtime. | Q13 delegation; Supabase documentation consulted. |
| DEC-14 | Faithful Explee interface; source evidence precedes application scaffolding and UI implementation. | Q14; Product Design source workflow. |
| DEC-15 | User selected their signed-in desktop Explee browser; use REA's real MCP. Local capture route remains required. | Q15 plus earlier settled source choice. |
| DEC-16 | Feature priority delegated. Existing Zoho CRM integration seam retained; Notion mirror deferred. | Q16 and inspected Ceverio CRM architecture. |
| DEC-17 | Zero new spending; rules/templates remain functional, Laya is the self-hosted decision candidate, and open-weight drafting uses a verified free allowance. Jev Ultrafast has hosted model dependencies. | Q17 updated by the supplied repositories and inspected source; model-evaluation.md. |
| DEC-18 | Retention/export/encrypted backup delegated; cloud plan requires off-VM recovery and separate owner key custody. | Q18 updated for whole-cloud placement; product.md and remaining-layers.md. |
| DEC-19 | Deterministic simulations first; controlled sender/recipient and booking tests before prospect pilot. | Q19. Actual test addresses remain required. |
| DEC-20 | Continue Plan mode; application implementation has not started. | Reaffirmed by the user on 15 October 2026. S3 and later are future build slices. |
| DEC-21 | Use the existing Explee REA Supabase project, `ojfcxjdeijbxlxrzesig`, in REA Org. | User-selected dashboard link; new connector verifies active eu-west-1 project, PostgreSQL 17 and Free organization plan. No application tables observed; no schema changed. |
| DEC-22 | Evaluate Jev Ultrafast and Laya at pinned source revisions; prefer Laya for the decision layer and keep browser automation experimental. | Source inspection in model-evaluation.md; no inference benchmark executed. |
| DEC-23 | Oracle Always Free ARM is the proposed full-app host; Cloudflare supplies candidate drafting inference and private access. | Oracle account creation/Ashburn Free Tier are user-reported; native Cloudflare account/zone inspected. Actual host capacity and specific service entitlements remain pending. |
| DEC-24 | Offload inference from the 8 GB integrated-graphics laptop. | User screenshots and cloud preference; momentary resource usage is not a performance benchmark. |
| DEC-25 | Oracle account created; use the reported US East (Ashburn) Free Tier home region. | User answer, 14 October 2026; account billing/settings, allocations and VM capacity not independently inspected. |
| DEC-26 | Cloudflare full DNS setup for ceverio.com is now active; keep GoDaddy registration and Zoho ordinary mail; proposed private app host leads.ceverio.com. | 15 October GET-only MCP verifies active zone and nine comparable GoDaddy records matching. DNSSEC pending; user has not added DS at GoDaddy. WebsiteBuilder alias prevents literal A comparison; parent-chain/live service checks remain. |
| DEC-27 | GitHub is the durable source of truth; eligible completed work/checkpoints are committed and pushed. Local files are temporary working material. Private captures require a verified private GitHub destination; secrets/browser profiles are never uploaded. | User's local-handover instruction, 15 October 2026. Public planning repo verified public and empty before publication. AGENTS.md and local-handover.md define publication verification and recovery. |

## Local source-continuation decision

DEC-28 — On 15 October 2026, the owner explicitly retained real REA capture as the source acceptance gate after being offered native Codex Browser/CDP capture. Native source evidence stays provisional. DEP-11's private-storage preflight is now verified; the browser endpoint is the remaining R0 blocker. See [the local access record](../evidence/local-source-preflight-20261015.json).

## Builder defaults

| Decision | Selected default | Consequence |
| --- | --- | --- |
| Application stack | React + TypeScript frontend; Node 24 + TypeScript API/worker; shared validation/contracts; PostgreSQL; isolated Python Laya sidecar. | Cloud ARM target with a Windows owner browser; Python REA capture remains beside the source browser. Resolve and pin actual dependency versions during build setup. |
| Database workflow | Supabase-compatible SQL schema/migrations and fixture PostgreSQL; the existing selected Explee REA project is the live target. | Confirm correct project access/plan/schema before later migration. No new project is planned by default; no schema changes occur in planning. |
| Database access | Browser talks only to the private API. Server accesses a private application schema through a dedicated least-privilege DB role. | No public anonymous access to lead data or browser-held service keys; own app signup is unnecessary. |
| Discovery | CSV and configured public directory/website seeds; optional independent search/enrichment adapters. | Zero-cost mode has bounded source coverage; public contact discovery is not mailbox verification. |
| Model | Private Laya sidecar on eligible cloud CPU; evaluated free-hosted open-weight drafting; templates/review when unavailable or unqualified. | No hosted TypeSafe dependency or automatic paid fallback. Unknown/unsupported replies go to the owner. |
| Host and access | Proposed eligible Oracle ARM VM in reported Ashburn home region, private Cloudflare Access/Tunnel on the candidate app hostname, selected Supabase persistence. | Account created is user-reported; actual free capacity, AI/Zero Trust entitlement, private access and recovery remain release prerequisites. |
| Pause | Stop new discovery/enrichment starts, cold sends, and automatic replies for the selected campaign; continue permitted read-only inbox/booking sync and reconciliation. | Existing meetings remain recorded; in-flight requests may finish and must be reconciled. Manual correspondence is separately visible and policy checked. |
| Owner replies | Sync owner mail sent outside the application; stop that enrollment and suppress automatic conversation responses until explicitly resumed. | Avoid competing with the owner's conversation. |
| Booking confirmation | Authoritative correlated booking-service event, not a link click or model classification. | Track acceptance/completion independently. |
| Source preservation | Complete reviewed REA evidence, hashes and provenance in a verified private GitHub destination; sanitized reusable material in the public planning repo. | Private artifacts are excluded from public Git and credentials are never uploaded. Temporary staging is not the durable archive. Captured bundles and real contacts cannot become public sample data. |

## Read-only connection findings

Inspected on 14 October 2026, with DNS follow-up on 15 October:

- Codex lists a local Ceverio project on Windows. This cloud workspace cannot read that path directly.
- GitHub main contains a short migration README. The substantive operating material is on the pinned outbound branch; it is not a fresh live-account audit.
- Connected Gmail and Google Calendar identify the owner's personal Google account, not the intended Ceverio sender.
- Connected Calendly exposes an unrelated website-development consultation in America/New_York.
- The callable Zoho connector supplies CRM capabilities. Ceverio's repository describes a separate local CRM/Mail MCP server; it is not callable in this cloud session.
- REA Org is now connected. The selected Explee REA project is active in eu-west-1 with PostgreSQL 17.11 and a Free organization plan. The returned table inventory has no application tables. Initial access through the previous general connection was denied; that limitation is resolved. Grants/usage/host connectivity remain unverified. No project or schema was created or changed.
- A real REA MCP session is usable here. No callable desktop browser tool or selected desktop CDP endpoint is available.
- Both model repositories were inspected at pinned commits. Laya publishes self-hostable weights; Jev Ultrafast's inspected decision URL is hosted and hardcoded. No model inference was run.
- Cloudflare MCP identifies the expected account. On 15 October ceverio.com is active, full Free Website, with 11 DNS-only records and assigned amanda/titan nameservers. Three MX, four TXT and two CNAME values match the uploaded export; the export's WebsiteBuilder Site alias is not a comparable A address. DNSSEC is pending and the user confirms Cloudflare's DS has not been added at GoDaddy. Actual parent DS, validated chain and live services remain unverified. See dns-followup-source-index.json.
- Cloudflare Access is not enabled, and no tunnel named ceverio-gtm was returned. Subscription read failed with an authentication/permission error; zone Free does not prove Workers AI/Zero Trust entitlement.
- Oracle account creation, Ashburn home region and Free Tier status are user-reported. There is no Oracle API/CLI credential or capacity inspection in this workspace. Optional Hugging Face eligibility remains unverified.
- Hardware is established only by the supplied screenshots; cloud ARM runtime and model timings remain unmeasured.

## Required inputs and unresolved outcomes

| ID | Dependency | Work that can proceed | Dependent action |
| --- | --- | --- | --- |
| DEP-01 | Local REA capture from the selected signed-in Explee browser, including screenshots/styles/states. | Spec, evidence protocol, source catalog, account research. | Faithful app scaffolding/UI and claims about the existing campaign or inbox taxonomy. |
| DEP-02 | Establish a provider permitting intended automated prospect outreach at an acceptable cost. Imported Ceverio DNS identifies ordinary Zoho routing; live hosting/authentication tests remain required. | Provider contracts, simulated sending, drafts, research, qualification. | Live automated prospect email. Zoho Mail is excluded for this campaign use by its current policy. |
| DEP-03 | Verify pinned Laya weights/runtime and Ceverio model quality; establish a confirmed free drafting allowance. Repo identification is resolved. | Model/adapter specs, reviewed fixtures and benchmark design. | Model download, deployment and promotion to automatic proposals in the build phase. |
| DEP-04 | Correct Ceverio booking URL/configuration and account capabilities. | Meeting settings spec and fixture event ingestion. | Sending a real booking link or changing an external scheduler. |
| DEP-05 | Design isolated application schema/backend grants and verify current usage/quotas and future-host database connectivity. Project selection, access, Free plan, region and table inventory are resolved. | SQL/migration and cloud deployment design against the actual selected project. | Migrations, credential enrollment and live persistence only in the build phase. |
| DEP-06 | Controlled test sender/recipient addresses and test booking configuration. | Deterministic provider tests. | Live send/book/cancel verification. |
| DEP-07 | Actual cloud host/dependency compatibility and Windows browser acceptance. Hardware is supplied; local heavy inference is no longer required. | Cloud architecture and runtime/evaluation plans. | Verified cloud startup, inference and owner browser workflows. |
| DEP-08 | Region/contact-purpose eligibility evidence for U.K. and South African prospects as well as the U.S. | Discovery/qualification and region-specific policy configuration. | New-region prospect dispatch. A U.S. operating playbook is not automatically valid for another region. |
| DEP-09 | Verify the reported Oracle Ashburn account's free allocations/capacity, actual Workers AI/Zero Trust entitlements and independent backup/key recovery. Cloudflare identity/zone are confirmed. | Complete deployment design and fixture specifications. | Cloud resource creation, exposure and unattended release in the later build phase. |
| DEP-10 | DNSSEC registrar DS/validated chain, independent delegation, WebsiteBuilder destination and live service checks. Cloudflare activation and nine comparable export records are verified; candidate app hostname absent from supplied sets. | Current DNS status, exact owner DS instructions, recovery plan and read-only checks. | User adds DS at GoDaddy; dependent live routing/release requires verified results. This work performs no configuration writes. |
| DEP-11 | Verify a private GitHub evidence destination and authenticated write/retrieval before collecting signed-in captures. Proposed Gerrard-Lewu/explee-private-evidence has not been created/verified by this handover. | Public handover/spec/checkpoint publication and source-independent planning. | Authenticated capture collection and acceptance; no substitution of public branches or local-only archives. |

Jev identification, hardware, full-cloud placement, the Supabase target/REA Org access, reported Oracle home region and Cloudflare activation are resolved. The export answers the record-inventory question for its supplied scope; it does not expose WebsiteBuilder's literal target or parent DS. The user answered that the registrar DS is not yet added. Source access, live DNS/service checks, sender, booking and controlled tests retain dependencies. The booking question remains pending; no default is treated as an entitlement. See [source completion](reverse-engineering-completion.md), [remaining layers](remaining-layers.md) and [DNS status](dns-cutover.md).

## Sources for consequential constraints

- [Ceverio operating branch](https://github.com/Gerrard-Lewu/Ceverio/tree/e544cbaac0034f68221c01970d824d2dffeece94): offer, scorecard, cadence, existing connections, verification, and sender decisions.
- [Zoho Mail usage policy](https://www.zoho.com/mail/help/usage-policy.html): excludes automated/promotional campaign sending through ordinary Zoho Mail.
- [Google email sender guidelines](https://support.google.com/a/answer/81126): authentication, reputation, recipient preference, pacing, and no delivery guarantee.
- [Supabase local development](https://supabase.com/docs/guides/local-development) and [local workflow](https://supabase.com/docs/guides/local-development/cli-workflows): container prerequisites, reproducible migrations, and development-only local stack.
- [Supabase API protection](https://supabase.com/docs/guides/api/securing-your-api): exposed schemas, grants, and RLS.
- [Supabase changelog](https://supabase.com/changelog): current access/dependency changes were checked; verify again before implementation.
