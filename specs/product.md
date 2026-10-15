# Product specification

## Goal

Build a reusable single-owner tool that discovers and qualifies a prospect, prepares and dispatches permitted outreach, handles matched replies within a stored policy, shares a booking link, and records a confirmed meeting. The first deployment now targets a private cloud host so the worker can operate while the owner's Windows 11 laptop sleeps. Oracle Always Free is the proposed host, conditional on actual capacity and verified free settings.

The first business profile is Ceverio: managed missed-call recovery and lead-response automation for HVAC businesses. Its current offer, signature, pricing, supporting facts, and exclusions are loaded from a private profile derived from the Ceverio operating repository. The generic GitHub template contains fictional examples and no actual lead pool, private phone number, account tokens, or captured inbox content.

The first release succeeds when:

- A fresh clone can be configured for another business without changing application code.
- Ceverio can prepare a pool of 30 distinct qualified companies using recorded fit, contact, verification, personalization, and suppression evidence.
- The complete journey works with controlled providers, including an interested reply and a confirmed booking.
- All specified critical failure/recovery scenarios pass, and the owner can inspect and resolve uncertain actions through the UI.
- A five-prospect pilot can run after a permitted sender, current recipient eligibility, authentication, controlled-test destinations, and the zero-spending constraints are satisfied.
- Captured core Explee states have been compared with the rendered implementation and recorded in design QA.

These are product acceptance targets. Prospect responses, meetings, revenue, and inbox placement cannot be guaranteed.

## User-selected scope

| Area | Requirement |
| --- | --- |
| Ownership | One owner per installation; multiple configurable business/project profiles; independently reusable from GitHub. |
| Application accounts | No app signup, tenant management or app billing. Cloud owner access uses an external private-access boundary; provider authorization remains necessary. |
| Ceverio audience | HVAC businesses with 1–50 employees in South Africa, the United States, and the United Kingdom. |
| Discovery | Independent sources and CSV import; no operational dependency on Explee. |
| Communication | Automated discovery, outreach, and replies within limits; Gmail/Google Workspace and Google Calendar integration requested, with actual Ceverio sender hosting to resolve. |
| Meetings | Existing booking-link workflow; meeting configuration delegated to the builder. |
| Reference | Faithful Explee screens and interactions, established from the owner's authenticated source evidence. |
| Runtime | Whole application in the cloud; Windows 11 owner browser and optional lightweight local client. |
| Cost | No new paid subscriptions or billable API use by default. |

The [cloud deployment plan](cloud-deployment.md) supersedes the older Windows-local-first topology. The [model plan](model-evaluation.md) selects self-hosted Laya decisions and bounded open-weight drafting under a verified free allowance; no model can send mail, invent qualification evidence or confirm bookings.

The latest country and discovery instructions supersede Ceverio's older U.S.-only, batch-only sourcing plan for this build. Existing source-verification, suppression, private-business, and provider-policy requirements remain relevant.

## Ceverio qualification defaults

Use Ceverio's existing residential-HVAC positioning, preference for independent local operators, owner/operational decision-maker research, and exclusions for franchises, rollups, suppliers, associations, commercial-only operators, equivalent advanced automation, invalid data, and suppressed contacts.

Preserve its 100-point scorecard: residential HVAC fit 25, independent-owner fit 15, missed-call/response pain evidence 20, lead demand 15, decision-maker reachability 15, and data confidence 10. A score of at least 80 is preliminary qualification; it does not independently authorize a send.

Country and employee range are hard filters. Unknown or contradictory employee counts remain research/review items; absence of evidence is not proof of a 1–50-person company. Missing pain evidence remains unknown. A first-party website observation may support a question, but does not establish that the business actually misses calls.

Readiness requires fit evidence, a justified relevant contact, current independent mailbox-verification evidence, a real personalization point, permitted contact purpose, current suppression clearance, and a sender permitted for the campaign. Public email display, an MX record, or a catch-all result alone does not satisfy mailbox verification.

Apply the [region-specific eligibility defaults](provider-feasibility.md) separately from market qualification. Unknown U.K. subscriber type and missing South African consent remain contact-eligibility gaps; finding a company in a target country does not make it dispatch ready.

## Outreach defaults

Use Ceverio's short founder-led plain-text approach: one verifiable observation, one problem, one low-friction question, no invented familiarity, no first-contact attachment, minimal links, clear identity, and a text opt-out. Private profile configuration supplies the required sender and address details.

Cadence: initial message, follow-up on day 4, final follow-up on day 9; at most three sequence messages. Delays are calendar dates relative to the accepted initial message in the recipient's time zone, deferred to the next eligible window where needed. Eligible sending days are Monday–Friday, 09:00–16:00 in a resolved recipient business time zone. The account day and daily counter use Africa/Johannesburg. Recipient zones are established from sufficiently specific location evidence rather than guessed from a country.

Before the first prospect pilot, capture a readiness snapshot of 30 distinct currently eligible companies; preliminary scores or two people at the same company cannot fill that pool. The pool is an initial milestone, not a requirement to maintain 30 unsent companies after every reply. Recheck each recipient's gates immediately before every dispatch.

The pilot permits five distinct first-contact prospects. A proposed initial ceiling is ten application-originated messages per calendar day, including follow-ups and automated conversation replies. Count uncertain sends against the ceiling until reconciled. Separate first-contact and conversation-response reservations prevent follow-ups consuming all capacity. The older 30/day Ceverio target is a future maximum to evaluate, not an automatic ramp or a requirement to fill a quota.

Broader unattended outreach becomes eligible only after the application/control tests pass, the five first-contact outcomes are reconciled, inbox/booking sync is healthy, and no observed provider or delivery-health blocker appears over at least two business days. Prospect interest is not a required test outcome. The stored policy can allow continuation at ten messages/day; an unresolved effect or adverse health signal holds it. This small pilot cannot establish a guarantee of future deliverability.

Use one sender initially. Respect the stricter of application pacing, provider limits, and observed account health. Default minimum dispatch spacing is ten minutes; provider deferrals may make it longer. Pause when material authentication, abuse, or delivery-health problems appear; a complaint requires review. Multiple inboxes or aliases do not increase the global project allowance automatically.

These are conservative operating defaults, not proof of provider permission or a promise against spam classification. The sender integration remains blocked for prospect automation if its current policy excludes that use.

## Reply defaults

Capture Explee's actual category names and transitions before claiming classification parity. Until that evidence is available, specify proposed internal categories: interested, question, objection, pricing, out-of-office, not-interested, opt-out, bounce, automatic-response, and ambiguous.

Automation may share the configured booking link after explicit interest and answer a factual question from approved profile content. It may quote only approved pricing and scope, with no invented discounts, guarantees, or contractual commitments. A message can have more than one signal; opt-out and bounce controls take precedence.

Ambiguous intent, unknown senders, recipient/identity changes, sensitive requests, unsupported facts, and conflicting signals enter the action queue. The first correlated human reply stops the cold sequence. Owner replies sent outside the application also stop it. Out-of-office messages hold outreach until an explicit policy permits resumption. Self-messages, bounces, and automatic responders do not trigger response loops.

## Meeting defaults

Proposed consultation: 30 minutes, ten-minute buffers, Monday–Thursday 15:00–19:00 Africa/Johannesburg, at least 24 hours' notice, a 14-day booking horizon, and at most two new consultations per day. These hours provide some UK/U.S. overlap and remain editable. Prefer Google Meet if the selected booking service and connected account support it.

Use a Ceverio-specific configuration. The connected Calendly account currently exposes an unrelated website consultation in America/New_York; do not repurpose it silently. Configuration in the application is distinct from changing an external scheduling account.

Sending a link creates `link_sent`, not `booked`. A correlated authoritative booking event establishes a booking; attendee acceptance and meeting completion are separate facts. Rescheduling or cancellation does not silently restart cold outreach. Direct slot negotiation/event creation is an optional later capability.

## First-release feature order

1. Projects, source-backed leads, CSV import/export, deduplication, qualification, and lead notes.
2. Campaign policy, draft preview, activation/pause, durable dispatch, usage ceilings, and activity/recovery.
3. Synced inbox, explainable categories, manual replies, bounded automation, and suppression.
4. Booking-link configuration and confirmed booking synchronization.
5. Basic campaign outcomes, operational health, backup/export/restore, and a Windows startup workflow.

Support importing existing Zoho CRM identities, qualification facts and suppression from an owner export or a capability-confirmed read adapter. Retain an integration seam and field mapping for later write-back. The new database owns application jobs and external-action history; the first release does not require upstream CRM writes and never deletes or blindly overwrites existing records. Notion is a later optional mirror of selected outcomes, not a dependency or a second workflow engine.

Phone enrichment, advanced CC/attachments, multiple inboxes, direct calendar negotiation, large-scale sending, and broad CRM sync follow only after the core is verified and the source behavior/cost justifies them.

## Workload and retention defaults

Initial measured workload: 5,000 lead rows, one active campaign/sender, multiple stored profiles, and a paginated lead table. Record actual cloud CPU/RAM/runtime and Windows browser timings before publishing performance claims. Target a 5,000-row fixture import within 60 seconds and an already-loaded lead-page/filter response within one second on the measured host, excluding external research calls.

Retain active contact facts and action history until deliberate deletion or archival. Retain fetched research snapshots for 90 days and cached message bodies for 180 days by default; the mailbox remains the source for older mail. Download attachments only when requested; expire temporary attachments after 30 days. Keep minimal action identity/provider references needed for reconciliation separately from expiring content.

Create encrypted backups while the cloud app runs, keeping seven daily and four weekly snapshots within verified database-egress/storage allowance. Keep a recoverable off-VM copy and a separate owner-held recovery key; Windows secure storage is an optional local custody mechanism. Losing the key makes a backup unreadable. Provide an explicit archive/export and restore drill. Purging a contact preserves a minimal suppression fingerprint and opt-out reason; deleting expired backups must not reintroduce suppressed contacts.

The primary cloud worker is independent of laptop sleep. Host reclamation, provider quota and database/network outages can still interrupt it; recovery reconciles uncertain actions and paces due work. No free-service availability guarantee is assumed.
