# Implementation roadmap

The authoritative plan is now [the spec-driven execution sequence](../specs/build-plan.md), supported by [requirements](../specs/requirements.md), [acceptance scenarios](../specs/acceptance.feature), [contracts](../specs/contracts.md), and [user decisions](../specs/decisions.md).

The specification incorporates the answered Ceverio requirements. It does not claim that the application, authenticated Explee inspection, or live sending/booking integrations have been implemented.

| Slice | Result | Current status |
| --- | --- | --- |
| S0 | Requirements, source preparation, real REA session/schema record and reviewable specification | Planning baseline complete |
| S1 | Authenticated Explee capture, visual/state catalog, existing campaign/category audit | Requires desktop browser access |
| S2 | Source-aligned behavior and provider/database contracts | Partly specified; source/account facts pending |
| D0 | Ceverio DNS/DS/nameserver activation and service preservation | User activated zone; read-only comparison matches seven mail records/two CNAMEs. DNSSEC pending, DS not added; website target and live services unverified. |
| S3 | Project profiles, durable leads, import, qualification detail, database/jobs/activity | Not implemented |
| S4 | Independent discovery/research/verification and zero-spending usage controls | Not implemented |
| S5 | Autonomous campaign policy, previews, paced dispatch/follow-ups and uncertain-send recovery | Not implemented; live sender unresolved |
| S6 | Inbox sync, stop rules, manual/automatic replies and action queue | Not implemented |
| S7 | Validated booking link and confirmed booking/reschedule/cancel outcomes | Not implemented; real Ceverio link pending |
| S8 | Analytics, account health, retention/export/backup and whole-interval restore | Not implemented |
| M1 | Domain model evaluation/calibration and verified free inference boundaries | Specified; future build phase only |
| S9 | Private cloud deployment, Windows owner-browser/controlled-provider acceptance and five-prospect pilot | Not started; free host/account facts pending |
| S10 | Later capabilities and reviewed capacity changes | Deferred |

Source/design acceptance precedes faithful application scaffolding. The capture helper and public documentation are not sufficient to claim an Explee interface has been reproduced.

The user selected whole-cloud operation. [Cloud deployment](../specs/cloud-deployment.md) proposes Oracle Always Free app/worker and Laya inference, Cloudflare drafting/private access subject to actual free-plan verification, and the selected existing Explee REA Supabase project. [Model evaluation](../specs/model-evaluation.md) records the pinned Jev/Laya comparison. Account entitlements and model quality are not established by their public documentation.

[Remaining layers](../specs/remaining-layers.md) records the reported Oracle Ashburn account and active Cloudflare zone. [DNS status/steps](../specs/dns-cutover.md) records export parity, the remaining registrar DS/validated-chain and service checks, and recovery. [Source completion](../specs/reverse-engineering-completion.md) defines the separate Explee evidence/contract gate. This work makes no DNS/host/Access changes in Plan mode.

Meaningful tests cover interruption, stale policies, duplicate commands/events, billable-operation uncertainty, unknown send outcomes, inbox cursors, owner replies, booking-state distinctions and old-backup reconciliation. Real PostgreSQL evidence supports database guarantees; rendered-browser checks support UI guarantees; controlled provider checks support live integration claims.

Use booking links in the first release. Direct slot negotiation, advanced CC/attachments, phone enrichment, multiple inboxes, Notion sync and upstream CRM write-back are later explicitly specified slices.
