# Application contracts

These are proposed implementation contracts, not recovered Explee backend designs. [Product defaults](product.md) supply the initial configuration; [decisions](decisions.md) identify unresolved external capabilities.

## Runtime and boundaries

Use React/TypeScript for the captured interface and Node 24/TypeScript for the API and worker. The current primary target is an eligible cloud ARM VM with private Cloudflare owner access; Windows is the owner browser. Serve the UI and API on one origin, binding the VM service to loopback behind its access-controlled tunnel. Validate Host/origin and require an application-issued request token on mutations; this is request protection, not app signup. Reject direct-origin bypass and unauthorized access. An optional local client retains loopback access.

Use PostgreSQL for relational records, unique constraints, transactionally claimed jobs, and usage reservations. The existing Supabase target is `ojfcxjdeijbxlxrzesig`: REA Org access, Free plan, eu-west-1 region and PostgreSQL 17 are verified; no application tables appeared in its inventory. Application grants and future-host connectivity remain to be configured/verified in the build phase. The frontend never connects directly to the database. Put application tables in an isolated private schema with a least-privilege backend role; revoke anonymous/public Data API access without changing unrelated schemas. If any schema is exposed, explicitly review grants and RLS. Keep service credentials and provider refresh tokens in secure server-side storage restricted to the service identity.

Application code remains independent of Supabase Auth, Notion, Make, and Codex runtime subscriptions. SQL migrations, generic seed fixtures, startup documentation, and environment-variable examples make the GitHub project reproducible. Actual Ceverio profiles and lead exports remain private.

Local Supabase containers are an optional development/fixture environment, not required on the 8 GB owner laptop. Hosted PostgreSQL requires connectivity; losing connectivity pauses external dispatch. The cloud worker can continue while that laptop sleeps. Actual cloud downtime/reclamation still requires paced reconciliation and recovery; free service availability is not guaranteed.

## Durable records

| Record | Contract |
| --- | --- |
| ProjectProfile / ProfileVersion | Business offer, approved answers/pricing, ICP, region rules, source configuration, template/schedule, meeting link, budgets, permitted automation actions. Immutable versions preserve what each run used. |
| Company / Contact / Endpoint | Stable local IDs; normalized domain; provider identities; person/company relationships; original email spelling; shared endpoints remain distinct from individual identity. |
| SourceObservation | Fact/value, source URL or provider record, retrieval time, evidence/verification status, original representation, expiry, conflicts, and manual override. |
| SearchRun / ImportRun | Frozen filters/source parameters or import fingerprint, row/page checkpoints, original provider operation ID, progress/results/errors, cancellation and usage. |
| Qualification | Rule/scorecard version, evidence per criterion, unknowns, exclusions, score, readiness gates and explanations; recipient region/type, purpose, consent/customer evidence, applicable data basis/notice and objections. Preliminary score is separate from contact eligibility. |
| CampaignVersion / Enrollment | Immutable sequence/policy; selected profile and sender; contact/endpoint; lifecycle/cycle; stop reason; next step; current version. |
| ExternalActionIntent | Stable logical operation key, operation kind, frozen envelope/payload hash, authorization/policy version, dispatch state, attempts, provider references, certainty, and reconciliation facts. |
| Job | Intent/reference, due time, effect/retry class, state, attempts, lease/fencing token, deadline, failure reason and next allowed action. |
| Thread / Message / Classification | Connection/provider IDs, reply headers, durable cursor batch, direction, parsed bounded content, classification version, proposed action and evidence. |
| ModelRun / ModelPolicy | Input hash, configured task/model, code/weight/config revision, schema, language/route, precision, calibration/threshold version, truncation/drop metadata, probabilities, usage/reservation, latency, proposal and acceptance/abstention disposition. |
| Meeting | Booking configuration/event identity, contact/campaign correlation, interval/zone, status/revision, attendee response and authoritative source. |
| UsageLedger | Quoted maximum, reserved, actual, unknown, allowance unit, period/time zone, provider quota and pricing evidence. |
| Suppression | Endpoint/company/person scope, reason, source, timestamp, global precedence and explicitly recorded changes. |
| Connection / Activity | Provider identity/capabilities/permissions, health/last sync, credential reference; human-readable operation/state history without secret material. |

## Identity and deduplication

Map every strong `provider + record-kind + external-ID` to one local entity. Normalize website domains and canonical profile URLs. Normalize email domains, preserving local parts unless a provider confirms equivalence. Do not generically strip dots or plus suffixes.

Use domain, independently normalized email/phone, and company-plus-address signals before new company creation. Conflicting strong signals enter review; a single concatenated business key cannot resolve contradictions. A shared role mailbox is not proof that two people are identical.

An import fingerprint and row ordinal provide replay identity; provider pages have retained cursors and source identities. Imports and merges preserve source observations, manual corrections, messages, action history, and suppression.

Initially allow one active outreach enrollment per contact/canonical endpoint across the installation. Project profiles remain independent; using a different business profile must not bypass an existing opt-out or active sequence.

## Provider interfaces

| Adapter | Required normalized contract |
| --- | --- |
| Discovery / Research | Validate filters; list/query configured sources; paginate or poll an existing run; bounded public-site retrieval; emit facts with provenance; report source and rate/cost capabilities. |
| Verification | Return valid/risky/invalid/unknown, catch-all flag, checked time, provider, expiry, and known/unknown usage. |
| Mailbox | Declare permitted use/verified sender, send/reply frozen intents, fetch sent-message evidence, sync inbox and owner-sent messages, preserve thread/reply IDs, report account limits and outcome certainty. |
| Booking | Validate a configured booking URL/account/event type; ingest/poll authoritative booked/rescheduled/cancelled events; report correlation, revision, interval, and capabilities. |
| Calendar | Read selected calendar capabilities and availability when needed. Direct event creation/update is deferred unless enabled by a later specification. |
| Model | Separate typed decisions from text generation. Use configured pinned self-hosted Laya or evaluated free-hosted drafting from a bounded fact set; validate schema, evidence, context completeness, model policy and usage. No direct operational tools or permission to change policy; no silent paid/model fallback. |
| CRM | First release: ingest an owner export or capability-confirmed read of identities/facts/suppression with provenance and conflicts preserved. Version field mappings for later write-back; upstream writes/deletion are outside first-release scope. |

Each adapter declares operation semantics: external effects, billability, price upper bound, provider idempotency key/window, authoritative reconciliation method, retryable failures, rate limits, and supported evidence. HTTP GET does not by itself prove that repeating a paid search is harmless.

Errors distinguish `retryable_read`, `rate_limited`, `authentication_required`, `invalid_request`, `policy_blocked`, `budget_blocked`, `capability_unavailable`, and `external_outcome_unknown`. An adapter cannot silently change accounts, providers, recipients, or paid modes to work around an error.

Public-site research is bounded by the source's supported usage, per-host limits, cache and redirect/size/time bounds. User/source URLs do not authorize requests to loopback/private-network/cloud-metadata addresses. A directory mention is a candidate; first-party confirmation determines usable facts.

## Workflow transitions

| Workflow | Main transitions |
| --- | --- |
| Lead | discovered → research → preliminary-qualified → ready; exclusions/suppression can prevent readiness at any time. |
| Campaign | draft → configured → active → paused/completed; activation stores policy/version and prerequisite results. |
| Enrollment | eligible → queued → awaiting-reply → conversation/closed; opt-out/bounce/manual response/booking invalidates old follow-ups. |
| Intent | prepared → dispatching → accepted/definitive-failure/reconciling; inconclusive reconciliation → needs-action. |
| Job | queued → running → succeeded/retry-wait/reconciling/needs-action/failed/cancelled. |
| Meeting | link-ready → link-sent → booked → rescheduled/cancelled/completed; attendee acceptance is separate. |

Owner-visible pause stops new research starts, cold messages, and automatic replies. It permits read-only listening, booking synchronization and reconciliation where account permissions remain valid. Already-dispatched provider requests can finish. An explicit manual compose action remains separate and subject to sender/recipient/cost policy.

Editing content, recipients, offer, or policy creates a new version and supersedes incompatible undispatched intents. It does not reuse an executed operation identity for a different payload.

## Dispatch contract

1. Check current profile/enrollment versions, campaign state, region/contact eligibility, suppression, recipient verification, evidence freshness, sender policy/capability, time window, global/account caps, account health, and budget.
2. Refresh relevant inbox/sent state before follow-ups. A stale/unavailable sync can block dispatch.
3. Create a frozen intent, unique logical key, payload hash, usage reservation, job and activity in one transaction. A repeat command with the same key returns the existing result; a different payload under that key is a conflict.
4. Claim a job atomically and record its lease/fencing token. Record dispatch start before the provider call; perform the network request outside the transaction.
5. Store provider acceptance, IDs and resulting state durably. Provider-accepted is not delivered. Unknown outcomes reserve message/cost allowance.
6. Reconcile a timeout, lost response, crash, or potentially accepted error. Use genuine provider idempotency only within its documented window with the same key/payload. Message-ID alone is not a general mailbox send-idempotency guarantee.
7. Do not repeat an uncertain effect merely because a sent-message search is empty or delayed. Without authoritative non-execution evidence or valid provider idempotency, retain `needs_action`.

Late provider responses must be retained against the original intent even if its worker lease expired. A stale worker cannot advance the workflow; reconciliation can consume its recorded response. Never discard evidence of an accepted effect and then assume non-execution.

Local locks cannot provide exactly-once execution across independent mailbox APIs. The guarantee is: stable action identity, no blind repeats of uncertain effects, explicit uncertainty, and outcome-aware recovery.

## Inbox and automation

Commit messages before advancing the associated cursor. Deduplicate provider message/event IDs. A bounded resync of an expired cursor preserves all existing message IDs and action identities.

Correlate by provider thread ID and RFC reply references; sender/subject similarity requires review when ambiguous. These fields correlate messages but do not authenticate a sender. Consider provider spam/authentication signals and conflicting identity before automatic action.

A first matched human reply cancels the cold sequence before classification. Owner mail sent outside the application also cancels incompatible pending work. Opt-out/bounce/suppression controls take precedence over interest or questions. Every automatic response key includes the originating inbound message, policy version, and action type; replaying ingestion cannot create another response.

Use strict structured categories and allowed next-action proposals. Rules/templates operate without a model; supported factual replies draw from approved profile facts. When a model is configured, email and research text remain content rather than instructions, and validated proposals pass normal dispatch checks. Unknown senders and ambiguous/conflicting requests remain owner-visible without autonomous sends.

Apply the [model evaluation contract](model-evaluation.md) before automatic model-dependent responses. Calibration is specific to checkpoint, dtype, language, task/schema and option shape. A high probability or low guard score cannot bypass a deterministic stop rule. Truncated decision-critical text, an unsupported route, invalid output, unverified quota or insufficient held-out quality causes abstention/review. Model service failure does not invent approved facts or automatically choose another model.

Recognize self-mail, delivery reports, bulk/list markers and automatic responders; prohibit autoresponder loops. Hold out-of-office sequences conservatively. Do not contact alternate addresses supplied in a reply without a separately validated recipient decision.

## Meetings

Validate and display the actual configured booking link before activating a campaign. A missing or unrelated link prevents automatic scheduling responses. Keep proposed application defaults distinct from external service settings.

Poll the selected provider/event type while the local worker runs; later verified webhooks can supplement this. Deduplicate provider events and retain revisions/cursors. Correlate using known attendee/booking identities and campaign context; ambiguous shared-address matches require review.

Confirmed booking stops outreach. A link click or `interested` label cannot mark a meeting booked. Changes ingested from the provider update one meeting; cancellation leaves outreach stopped. An external scheduler owns invitations and availability in the link-first release.

Store UTC intervals plus the relevant IANA time zones and original provider representation. Missing or ambiguous dates/zones cannot become a guessed direct booking.

## Cost, recovery, and retention invariants

- INV-001: Stable action keys and frozen payloads survive retries; edits create revisions, not altered replay.
- INV-002: An uncertain external action cannot automatically become “not executed.”
- INV-003: Billable starts and paid queries reconcile before another charge; polling an existing job is separately classified.
- INV-004: Import, merge, resume and profile switches cannot silently clear suppression.
- INV-005: Dispatch requires current policy/entity versions; in-flight outcomes remain recorded after Pause.
- INV-006: Documentation is not runtime observation; acceptance is not delivery; classification is not interest proof; booking is not attendee acceptance.
- INV-007: Sync checkpoints advance only after durable ingestion; replay does not create responses or inflate analytics.
- INV-008: Untrusted content cannot execute tools, expand recipients or modify policy.
- INV-009: UTC and original IANA zones survive scheduling and daylight-saving boundaries.
- INV-010: Restore pauses dispatch across the entire snapshot-to-present uncertainty interval, including effects that look queued or are absent in the old backup.
- INV-011: Local leases do not promise atomic read/send or free-busy/booking transactions with an external provider.
- INV-012: Outreach, read-only listening, meeting management, and manual correspondence have separate policies.

In zero-spending mode, disable billable calls and automatic paid fallback. Execute a free-quota call only where the adapter can establish applicable free allowance; uncertain pricing remains blocked. Budgets count quoted/reserved/actual/unknown usage. SDK-level automatic retries must not bypass these semantics.

Restore does not make the old database the authoritative state of the external world. Reconcile sent messages, provider operations, bookings and suppression changes since the snapshot before resuming. If provider history cannot cover the full uncertainty window, keep affected dispatch paused.

Purging content keeps minimal suppression/recovery identifiers under the configured retention policy. Backup and export mechanisms preserve this distinction. Analytics name their populations and date windows; duplicates and unknown actions cannot inflate successful outcomes.
