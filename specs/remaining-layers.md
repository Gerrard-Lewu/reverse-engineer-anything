# Remaining-layer delivery plan

Status: planning only, 15 October 2026. The user created an Oracle Free Tier account in reported US East (Ashburn), activated Cloudflare and enabled DNSSEC signing. This work verified DNS read-only; the app build, host provisioning and deployment remain unstarted. DNSSEC is pending until registrar/chain completion.

## Goal and settled design

Deliver a private, reusable Ceverio lead-to-meeting app that keeps working while the laptop sleeps: independent discovery/CSV → evidence-based qualification → bounded permitted outreach → matched reply handling → a real booking outcome → auditable recovery.

Use React/TypeScript and a Node 24 API/worker, the selected Supabase PostgreSQL project, a private Laya decision sidecar and evaluated free-hosted open-weight drafting. Oracle Ashburn is the proposed host; use Cloudflare DNS plus owner-only Access/Tunnel for leads.ceverio.com, after hostname/source checks.

The 30-company readiness snapshot, five-prospect pilot, ten/day message ceiling, ten-minute spacing and recipient-zone rules remain unchanged. Model outputs and DNS authentication cannot bypass source, verification, consent/purpose, suppression or sender-policy checks.

## Current readiness

| Area | Status |
| --- | --- |
| Business/ICP/autonomy | Specified from user answers and Ceverio operating material. |
| Explee reference | Public catalog/REA protocol established; authenticated screens/styles/campaign settings still missing. |
| Supabase | Selected Explee REA project verified active, Free plan, eu-west-1, PostgreSQL 17; no application tables in returned inventory. |
| Oracle | Account created and Ashburn/Free Tier reported by user; tenancy settings, current allocations and A1 capacity not inspected. |
| Cloudflare | Correct account and active full Free ceverio.com zone verified through MCP; 11 DNS-only records. |
| Domain/DNSSEC | Seven mail records and two CNAMEs match the export. DNSSEC pending; user has not added DS at GoDaddy. WebsiteBuilder IP parity and live delegation/chain/services remain unverified. |
| Access/Tunnel | Access not enabled; the proposed named tunnel not observed. Nothing created. |
| Model | Jev/Laya code comparison completed; no weight installation, inference or domain benchmark. |
| Email | Ordinary Zoho routing observed; a permitted zero-budget automated prospect channel remains unresolved. |
| Booking | Correct Ceverio link/service/event mechanism remains to be confirmed. |
| Build | 43 requirements and 43 acceptance scenarios specified; no application implementation or acceptance execution. |

Current DNS facts are in [the 15 October comparison](../evidence/dns-followup-source-index.json); other account observations remain dated in [the 14 October evidence](../evidence/remaining-layers-source-index.json). [The source completion plan](reverse-engineering-completion.md) defines the Explee critical path. An account screenshot or user statement is not a cloud resource/entitlement test.

## Layers, deliverables and exits

| Layer | Planned deliverable | Exit evidence before live use |
| --- | --- | --- |
| L0 — Domain/DNS | Reviewed complete zone, preserved Zoho records, exact nameservers, DNSSEC cutover and recovery instructions. | GoDaddy/Cloudflare record parity, confirmed delegation, valid DNSSEC and controlled mail/service checks. See dns-cutover.md. |
| L1 — Oracle runtime | Eligible ARM Linux host in the user's Ashburn home region; Node app/worker, Python inference and restricted service identities. | Actual Always Free resource labels/current allowance, selected image/ARM compatibility, capacity and startup/restart checks. |
| L2 — Private access | One owner, one app hostname, Access policy and outbound remotely managed tunnel; loopback origin. | Correct owner succeeds; strangers/wrong identities/direct-origin attempts fail; origin validates Access tokens; tunnel reaches the intended app. |
| L3 — Data and secrets | Versioned isolated Supabase schema, least-privilege backend role, durable job/intents/usage, server-only credential references. | Real PostgreSQL constraints/lease tests, no anonymous/bundle secrets, verified encrypted database connection and account isolation. |
| L4 — Reference and interface | Accepted REA screenshot/structure/styles/assets/state catalog; faithful React views and recovery states. | Exact source association, desktop/mobile comparisons and required design QA. Capture precedes app scaffolding. |
| L5 — Lead pipeline | Independent source adapters/CSV/CRM read imports; provenance, deduplication, exclusions, employee/country evidence and verification. | Interrupted/replayed imports and source failures recover correctly; no invented employee count, consent or verified mailbox. |
| L6 — Decision/writing | Pinned Laya sidecar; bounded free Qwen candidate for wording; templates/review; policy-specific calibration and quota ledger. | M1 held-out quality/context/authority checks, actual memory/latency, confirmed free model path and no paid fallback. |
| L7 — Campaign/mail | Versioned previews/enrollment, single permitted sender, paced durable dispatch/follow-ups and recovery. | Account permits intended traffic; sender authentication, recipient readiness and controlled delivery/reply tests; no blind repeat of uncertain effects. |
| L8 — Inbox/replies | Source-derived categories, inbound/owner-sent sync, thread matching, notes, action queue and factual automatic replies. | Opt-out/bounce/owner reply precedence, replay safety, no loops, unsupported/ambiguous requests abstain. |
| L9 — Booking/calendar | Correct Ceverio link, delegated meeting settings and correlated authoritative outcomes. | Real booking/reschedule/cancel ingestion supported by that account/plan; link sent remains distinct from booked/accepted/completed. |
| L10 — Operations/recovery | Usage/health/activity, encrypted off-VM backups, retention/export and host replacement runbook. | Free storage/egress feasibility, separately recoverable keys, wiped-host/old-snapshot restoration and whole-interval reconciliation. |
| L11 — Launch and portability | Reproducible generic clone/configuration, measured cloud workload and Windows browser journey, controlled pilot. | All applicable source/fixture/provider checks; five-prospect outcomes reconciled before broader operation. |

L0 is partly complete through the user's activation and this read-only comparison. Its remaining checks and L1/L2 configuration are not executed in this planning turn. Account research and specs continue; S3 and model installation begin only after the user moves to building.

## Oracle plan with the new account

Keep the reported **US East (Ashburn)** home region. Always Free compute must be created in the tenancy's home region; do not move provisioning to Europe merely because Supabase is eu-west-1.

Candidate future allocation: one VM.Standard.A1.Flex with two OCPUs, 12 GB RAM and a 50 GB boot volume, using a current eligible ARM Linux image. Check the actual account's available allowance and existing allocations first. Current published limits are not proof that this exact allocation is available to the account.

Use the Free/Always Free labels and review resource/ancillary costs rather than relying on a $300 trial balance. No GPU, paid shape, automatic Pay As You Go upgrade, paid load balancer or paid database IPv4 add-on is a default dependency.

Ashburn A1 capacity may be unavailable. Check available availability domains and retry only within provider limits; do not rotate accounts, synthesize activity to defeat reclamation or silently switch to a paid region/shape. If capacity remains unavailable, report the deployment dependency and retain the reviewed plan/fixture work.

The database and host will be in different regions. Maintain a small connection pool, fetch paginated views in bounded queries, and measure actual latency/import timings before claims. Account/day and owner display use Africa/Johannesburg; recipient scheduling retains each resolved zone rather than using the host location.

Source: [Oracle Always Free resources](https://docs.oracle.com/en-us/iaas/Content/FreeTier/freetier_topic-Always_Free_Resources.htm). No Oracle API/CLI credentials were configured or requested here; account email is retained only in private enrollment notes.

## Access, credentials and background work

Use an existing owner identity for the app's external Access policy. Public hostname Access supports browser access without a device client. Application signup remains unnecessary; the Internet-facing access boundary is still authenticated.

Bind the app and Laya to loopback/private interfaces. Publish only the app through the actual tunnel, after its owner policy exists; do not expose database/model ports or a direct origin route. Check current [Tunnel prechecks](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/troubleshoot-tunnels/connectivity-prechecks/) from the future VM and retrieve current Access/JWT settings before configuration.

The cloud worker uses PostgreSQL jobs/intents, leases and fencing. VM replacement resumes from durable state, refreshes provider history and reconciles uncertain effects before dispatch. It does not rely on the laptop, Codex chat remaining open or a browser agent clicking Send.

Keep provider tokens/tunnel credentials in service-restricted server storage with recoverable owner custody. Ordinary logs, model prompts, Git and browser assets exclude them. Ceverio's Windows DPAPI integration is not automatically portable to Linux; first-release CRM uses exports/verified reads, while cloud provider authorization needs its own supported enrollment.

## Free-cost boundaries and backups

The observed **Free Website** zone is not proof of Workers AI or Zero Trust plan entitlements. Account subscription inspection returned an authentication/permission error; confirm the specific service plan through authorized access or its dashboard before enabling dependent use.

Candidate drafting uses Workers AI's supported free allowance, with explicit model/usage caps and paid paths disabled. Quota exhaustion holds dependent work or uses an already approved template; unknown questions remain in review. Do not route through paid AI Gateway credits as a fallback.

Candidate off-VM recovery storage is a private OCI Object Storage bucket in the selected account, using an eligible free allocation and restrictive permissions. Proposed initial storage cap: 5 GB including retained archives, subject to the account-wide usage check. This is separate from the VM's boot volume and from Supabase's missing Free automatic backups.

Retain seven daily and four weekly encrypted application snapshots, plus minimal recovery/suppression IDs, only after measuring the data size and monthly database egress. Keep the backup key separately with an owner recovery copy. A free allowance or a storage cap is not a restore test; verify loss of the VM, model cache and local key access before release.

## Remaining provider decisions

- **Sender:** Keep Zoho ordinary mail delivery during DNS activation. Its campaign-use constraint still applies. Establish an explicitly permitted sender identity/transport and acceptable cost before autonomous prospect email; self-hosting an SMTP server is not a deliverability solution. The first app release can be implemented/tested with fixtures while this remains unresolved, but cannot be called live outreach-ready.
- **Booking:** Prefer the user's correct existing Ceverio link. If none exists, prepare a separately branded free booking-page candidate with Google Calendar and the already specified meeting settings; do not overwrite the unrelated website-consultation event. Verify whether authoritative outcomes can be read from that plan or a validated selected-calendar adapter. Do not promise free scheduler APIs/webhooks without evidence.
- **Discovery/verification:** Begin with owner CSV/CRM export and bounded public-source adapters; establish provider terms/free allowance/catch-all result shape. Source coverage limits and missing employee evidence are visible.
- **Model:** Follow model-evaluation.md. A zero-cost classifier can still be wrong; do not replace hard readiness/stop rules with probabilities.
- **Optional extensions:** Notion mirror, upstream CRM writes, phone enrichment, CC/attachments, extra inboxes and direct calendar negotiation remain later independent slices.

## Execution sequence and stop conditions

1. Finish the remaining planning facts: registrar DS/validated chain, website alias and live services, selected Oracle settings/capacity, actual entitlements, source-capture route, sender and booking identity. DNS activation and nine comparable export values are resolved; do not repeat activation. Explee capture can proceed independently of these cloud checks.
2. Accept Explee source evidence through the actual REA MCP beside the selected signed-in browser (S1). Cloudflare/Oracle account access does not expose that desktop browser. Freeze category/component/state and provider contracts (S2).
3. Once the user explicitly moves to building, implement S3 leads/profiles/import/jobs, then S4 discovery/verification, then S5 campaign/dispatch and S6 inbox/replies, with meaningful acceptance examples and recorded evidence.
4. Evaluate M1 and promote only supported model roles. Implement S7 booking outcomes and S8 recovery/analytics/retention.
5. Prepare the actual cloud/DNS/Access/database deployment as a concrete reviewed change set. Recheck vendor APIs/limits and satisfy any required external-action confirmation at that action boundary; no premature permission loop during planning.
6. Run S9 cloud/Windows/source comparison, access/restart/restore/workload and controlled-provider checks. Release only the cleared capabilities.
7. Run the five-prospect pilot with the initial 30-company readiness snapshot and current gates. Broader automation follows the existing pilot exit conditions; it is not activated by passing mock tests.
8. Add S10 extensions/capacity changes under separate specs and budgets.

DNS uncertainty, failed private access, unavailable database/provider history, unknown effects or unverified paid exposure holds the dependent action. A complete plan names these conditions; it does not fabricate completed integrations.
