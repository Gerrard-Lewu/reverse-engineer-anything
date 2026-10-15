# Requirements and verification trace

All requirements below are currently `specified`; none is an implemented application claim. Source acceptance, fixture verification, provider verification, and source comparison are separate evidence states.

Origin codes: U = user answer/instruction; C = inspected Ceverio operating material; D = documented Explee reference; P = proposed implementation behavior; R = actual REA protocol/schema; M = inspected model source/current cloud documentation. Explee-derived behavior remains documented until authenticated observation replaces or supplements it.

| ID | Required behavior | Origin / decision | Slice | Acceptance |
| --- | --- | --- | --- | --- |
| REQ-SCOPE-001 | One-owner lead-to-meeting app with independent reusable project profiles and no own signup/billing. | U, DEC-01/12 | S3–S9 | ACC-001, ACC-026 |
| REQ-REF-001 | Distinguish observed/documented/derived/proposed/unverified claims with provenance and limitations. | U/R/D, DEC-14/15 | S0–S2 | ACC-023 |
| REQ-REF-002 | Associate each capture/action with exact browser target, state, viewport, timestamp, Evidence IDs and verified artifacts. | R, DEP-01 | S1 | ACC-023, ACC-031 |
| REQ-REF-003 | Claim fidelity only for accepted source states compared against the rendered app. | U, DEC-14 | S1–S9 | ACC-024, ACC-031 |
| REQ-DATA-001 | Version offer/ICP/region/size/exclusions/source parameters per project and retain the version used by each run. | U/C, DEC-01/02 | S3 | ACC-025, ACC-026 |
| REQ-DATA-002 | Persist contact/company facts, provenance, verification dates, conflicts, corrections and unknowns. | C/P, DEC-02 | S3–S4 | ACC-002, ACC-025 |
| REQ-DATA-003 | Import/export with row-level outcomes, interruption recovery, cancellation and repeat-import deduplication. | U/D, DEC-03 | S3 | ACC-002, ACC-003, ACC-027 |
| REQ-DATA-004 | Deduplicate strong identities, preserve shared endpoints/history/suppression, surface conflicting matches. | C/D/P | S3 | ACC-002, ACC-005, ACC-012 |
| REQ-DATA-005 | Resume discovery/enrichment using existing provider operation IDs; expose usage and uncertain charges. | D/P, DEC-03/17 | S4 | ACC-004, ACC-010 |
| REQ-DATA-006 | Explain scores and personalization with supporting facts; deterministic exclusions precede AI. | C/U, DEC-02/17 | S4 | ACC-025, ACC-032 |
| REQ-OUT-001 | Preview complete recipient envelope/content; bind activation and automation to a stored policy/version. | U/C/D, DEC-07/08 | S5 | ACC-001, ACC-006 |
| REQ-OUT-002 | Prevent simultaneous outreach to duplicate contacts/endpoints across projects. | C/P | S5 | ACC-005, ACC-026 |
| REQ-OUT-003 | Stable external-action identity and frozen payload; repeated submissions reuse the logical action. | P | S5 | ACC-005, ACC-006, ACC-007 |
| REQ-OUT-004 | Enforce region/contact eligibility, suppression, freshness, windows, pacing, ceilings, sender policy/health and budget immediately before dispatch. | U/C/P, DEC-06/07 | S5 | ACC-009, ACC-010, ACC-016, ACC-032, ACC-036 |
| REQ-OUT-005 | Pause and policy/content changes invalidate incompatible queued work while preserving in-flight outcomes. | U/D/P | S5 | ACC-006, ACC-009 |
| REQ-OUT-006 | Distinguish accepted/failed/unknown email outcomes; reconcile unknowns before another effect. | P | S5 | ACC-007, ACC-008 |
| REQ-OUT-007 | Apply the Ceverio 30-distinct-company readiness snapshot, five-first-contact pilot, cadence, ten/day ceiling and ten-minute spacing; unknown sends and replies consume allowance. | C/P, DEC-06/07/08 | S5–S9 | ACC-033 |
| REQ-IN-001 | Durable deduplicated incoming/owner-sent mail, thread correlation, sync health and expired-cursor recovery. | D/P | S6 | ACC-011, ACC-014, ACC-021 |
| REQ-IN-002 | Reply, opt-out, bounce, owner reply and meeting stop rules survive import/merge/resume. | C/D/P | S6 | ACC-011, ACC-012, ACC-014, ACC-018 |
| REQ-IN-003 | Automatic replies only in matched conversations and permitted factual policies; ambiguity enters action queue. | U/P, DEC-07/09 | S6 | ACC-013, ACC-032 |
| REQ-IN-004 | Detect owner replies, self-mail and automatic responders; prevent loops. | P | S6 | ACC-014, ACC-015 |
| REQ-IN-005 | Manual replies preserve thread/envelope; advanced CC/attachments explicitly follow capabilities. | D/P, DEC-16 | S6; extras later | ACC-024, ACC-032 |
| REQ-CAL-001 | Validate project booking configuration and show meeting settings/time zones separately from external-service state. | U/P, DEC-10/11 | S7 | ACC-016, ACC-017 |
| REQ-CAL-002 | Deduplicate/correlate authoritative booking outcomes; link-sent, booked, accepted and completed remain distinct. | U/D/P | S7 | ACC-017, ACC-018 |
| REQ-CAL-003 | Ingest reschedules/cancellations with event revisions; replay and conflicts remain visible. | P | S7 | ACC-018, ACC-019 |
| REQ-CAL-004 | Booking stops outreach; cancellation never silently reenrolls a lead. | C/P | S7 | ACC-018, ACC-019 |
| REQ-OPS-001 | Durable jobs, fenced leases, effect-based retries, bounded recovery and no blind mutation/billing repeats. | P/R | S3–S8 | ACC-003, ACC-004, ACC-007, ACC-008, ACC-034 |
| REQ-OPS-002 | Human-readable activity/action queue with pause, reconnect, review and reconciliation controls. | U/D/P | S3–S8 | ACC-008, ACC-009, ACC-021, ACC-024 |
| REQ-OPS-003 | Track quoted/reserved/actual/unknown usage and enforce zero-spending and supported caps. | U/C/P, DEC-06/17 | S4–S8 | ACC-004, ACC-010, ACC-022 |
| REQ-OPS-004 | Restore with dispatch paused and reconcile the whole uncertainty window; pace overdue work after outages. | P | S8 | ACC-020, ACC-029 |
| REQ-OPS-005 | Retention/export/encrypted backup preserve required suppression/recovery information. | U/P, DEC-18 | S8 | ACC-027 |
| REQ-OPS-006 | Analytics use named populations/date windows and exclude unknown outcomes from successes. | D/P | S8 | ACC-022 |
| REQ-INT-001 | Account capability, permission, policy and reconnect status without exposed credentials or silent identity changes. | U/C/P | S3–S9 | ACC-021, ACC-028, ACC-032 |
| REQ-CRM-001 | Ingest existing CRM identities/facts/suppression from export or verified read adapter; preserve provenance/conflicts and avoid upstream writes in the first release. | C/P, DEC-16 | S3–S4 | ACC-035 |
| REQ-UI-001 | Rendered source-matched core journeys with useful loading/empty/validation/error/recovery states and keyboard access. | U, DEC-14 | S3–S9 | ACC-024, ACC-031 |
| REQ-NFR-001 | Measure the cloud workload, startup/recovery and Windows owner-browser behavior; publish actual limitations. | U/P, DEC-12/13/23/24 | S9 | ACC-029, ACC-030 |
| REQ-AI-001 | Separate pinned self-hosted decisions from free-hosted generation; validated fact-bound proposals have no operational tools or permission to bypass workflow gates. | U/M/P, DEC-17/22 | S4/M1/S6 | ACC-037, ACC-038 |
| REQ-AI-002 | Promote each model role only from held-out domain evaluation/calibration; track revision, language, precision, schema, probabilities and truncation; unsupported/incomplete/uncertain results abstain. | M/P, DEC-22 | M1/S6 | ACC-038 |
| REQ-AI-003 | Verify free model entitlement and shared-account quota, reserve bounded usage and hold on exhaustion/error without paid, public-demo or unevaluated-model fallback. | U/M/P, DEC-17/23 | M1/S4–S8 | ACC-039 |
| REQ-HOST-001 | Run the app and worker on a verified free cloud target independent of laptop sleep; enforce private owner access and recover after host loss without duplicate effects. | U/M/P, DEC-12/21/23 | S2/S9 | ACC-040 |
| REQ-DNS-001 | Reconcile the complete authoritative zone before activation, preserve existing service/mail targets and logical TXT/key values, use appropriate proxy status and validate controlled mail/service outcomes. | U/M/P, DEC-26, DEP-10 | D0/S9 | ACC-041 |
| REQ-DNS-002 | Replace nameservers only with the selected zone's assigned pair and a verified registrar/parent DNSSEC transition; retain old-zone recovery and coordinate DS/TTL on rollback. | M/P, DEC-26, DEP-10 | D0/S9 | ACC-042 |
| REQ-REPO-001 | Publish eligible completed project work/checkpoints to GitHub; keep authenticated evidence in a verified private destination and secrets out of all uploads; verify remote refs/artifact hashes before cleanup or completion claims. Preserve the only working copy after a failed push. | U, DEC-27, DEP-11 | S0/S1 and every checkpoint | ACC-043 |

Each implementation slice adds the concrete implementation path, test binding, verification command/result, and evidence link to its rows. Do not mark a requirement verified by pointing at its own specification.

## Coverage accounting

Source fidelity denominator: the accepted, named core screen/state catalog. Feature coverage denominator: the retrieved documented capability catalog plus the user-selected first-release scope. Neither denominator claims exhaustive coverage of Explee's private implementation.

Release acceptance requires all first-release requirements to reach their applicable verification level. Live-sending and booking integration rows need provider evidence; fixture evidence alone is insufficient. Source fidelity rows need captured/reference comparisons. Deferred capabilities are explicitly excluded from the release denominator.

Direct slot negotiation/calendar event creation, phone enrichment, advanced attachments/CC, multiple inboxes, Notion sync and upstream CRM write-back remain deferred capabilities. The user moved whole-cloud operation into the first-release target; its account/capacity/access/recovery checks are required. M1 is the model-evaluation slice specified in model-evaluation.md and occurs only in the later build phase.

D0 is the future DNS configuration slice in dns-cutover.md. Its specification/read-only review can precede app building; no DNS or registrar change is performed in the current planning phase.
