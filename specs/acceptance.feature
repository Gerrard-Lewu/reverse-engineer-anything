Feature: A reusable single-owner lead-to-meeting tool
  These scenarios are specifications, not tests already executed.
  Bind them to domain, database, adapter, and rendered-browser tests in their slices.
  All contacts and providers are synthetic unless a scenario explicitly names controlled accounts.

  @ACC-001
  Scenario: Complete the controlled lead-to-meeting journey
    Given a configured project, an eligible fixture contact, a permitted sender and a validated booking link
    When discovery qualifies the contact and the stored policy activates outreach
    And a matched interested reply arrives followed by an authoritative booking event
    Then one initial outreach message and one permitted booking-link reply are recorded
    And the confirmed booking appears in the UI with its source
    And cold follow-ups remain stopped

  @ACC-002
  Scenario: Import duplicates, invalid rows, shared addresses and suppressed contacts
    Given a CSV containing those cases and prior source observations
    When the same CSV is imported twice
    Then accepted entity counts remain stable and each row outcome is visible
    And shared endpoints do not silently merge distinct people
    And source observations and suppression remain effective

  @ACC-003
  Scenario: Resume an interrupted import
    Given an import with a durable checkpoint and a partially committed next batch
    When the worker is interrupted and restarted
    Then every accepted row exists once and rejected rows retain their reasons
    And resumed progress does not skip unfinished rows

  @ACC-004
  Scenario: Recover a billable provider start after its response is lost
    Given a provider accepted an enrichment start before local completion was lost
    When recovery can identify the original operation
    Then the existing operation is reconciled or polled
    And no second paid start is issued
    And the ledger retains one actual or uncertain charge

  @ACC-005
  Scenario: Prevent duplicate enrollment and repeated command effects
    Given two source records point to the same canonical recipient
    When competing campaigns activate and the same send command is submitted twice
    Then only one permitted active enrollment and logical initial send exist
    And the duplicate or conflicting command has an understandable result

  @ACC-006
  Scenario: Change content after an intent was prepared
    Given a prepared message bound to a policy version
    When its recipient, content or policy changes before dispatch
    Then the old incompatible intent is superseded
    And a different payload cannot reuse the old operation key
    And only currently permitted content can dispatch

  @ACC-007
  Scenario: Recover a send accepted before a crash
    Given a provider accepted an email and local completion was lost
    When the worker restarts and authoritative sent-message evidence is available
    Then the original intent records that message without another email
    And a late original response is retained rather than discarded

  @ACC-008
  Scenario: Retain an inconclusive send
    Given a timeout and inconclusive sent-message evidence
    When reconciliation remains inconclusive
    Then the UI shows the original envelope as unknown or needs action
    And time passing alone does not cause a resend
    And its allowance remains reserved and follow-ups do not assume success

  @ACC-009
  Scenario: Apply pause and current dispatch prerequisites
    Given queued cold messages and automatic replies
    When the campaign pauses or its window, cap, policy or health blocks sending
    Then no new incompatible dispatch begins
    And permitted read-only sync and reconciliation can continue
    And already-dispatched results remain recorded

  @ACC-010
  Scenario: Enforce zero spending and transactional allowance
    Given a zero paid budget and a provider with uncertain or positive per-call cost
    When new work is requested
    Then it is blocked without paid fallback
    Given a known free allowance sufficient for one operation
    When two workers compete for that allowance
    Then only one operation receives a valid reservation

  @ACC-011
  Scenario: Replay inbox sync and recover a cursor
    Given a matched human reply before follow-up preflight
    When sync replays the message and rebuilds an expired cursor
    Then one message and one resulting action exist
    And stale follow-ups are cancelled and the stop reason remains visible
    And the checkpoint advances only after durable ingestion

  @ACC-012
  Scenario: Preserve an opt-out across data changes
    Given a suppressed endpoint
    When it is reimported, merged, assigned to another profile or its campaign resumes
    Then automated outreach remains blocked
    And a changed suppression decision requires an explicit recorded workflow

  @ACC-013
  Scenario: Treat untrusted content and ambiguous conversations as review items
    Given an unknown sender, ambiguous forwarding, or instructions in a message to export records or change policy
    When classification runs
    Then content remains readable and the unresolved item appears in the action queue
    And no unrelated recipient, operational tool call or policy change is created

  @ACC-014
  Scenario: Respect owner correspondence outside the application
    Given the owner replies directly in the connected mailbox
    When sent-mail sync ingests the reply
    Then it appears in the conversation history
    And incompatible follow-ups and automatic responses stop

  @ACC-015
  Scenario: Avoid self-mail and automatic responder loops
    Given a self-message, bounce or automatic responder
    When it is repeatedly ingested
    Then no automatic response loop develops
    And any out-of-office resumption follows the stored policy

  @ACC-016
  Scenario: Preserve recipient and owner time zones
    Given Johannesburg and daylight-saving-zone fixture recipients
    When sending windows and meeting intervals cross a daylight-saving boundary
    Then UTC and displayed local dates agree
    And an unresolved recipient time zone cannot become a guessed sending window

  @ACC-017
  Scenario: Validate a project booking link without inventing a booking
    Given a missing link or an event type belonging to another business
    When a scheduling response is proposed
    Then it is held with a visible configuration reason
    Given a valid configured link
    When the link is sent
    Then the outcome is link sent and no booked-meeting count is added

  @ACC-018
  Scenario: Reconcile one authoritative booking
    Given a correlated booking-service event
    When polling or event delivery repeats it
    Then one meeting is recorded with its provider identity and revision
    And outreach stops for the correct enrollment
    And booked, attendee accepted and completed remain separate facts

  @ACC-019
  Scenario: Respect external rescheduling and cancellation
    Given a booked meeting changed by its scheduler
    When updated or cancelled provider events replay
    Then one meeting reflects the latest authoritative revision
    And conflicts or ambiguous correlation are visible
    And cancellation does not reenroll the lead

  @ACC-020
  Scenario: Restore across the full external uncertainty interval
    Given a backup shows an email queued and lacks a later booking
    And the email was sent and the booking created after the snapshot
    When the backup is restored
    Then dispatch remains paused while the snapshot-to-present interval is reconciled
    And neither apparently queued nor absent actions are blindly recreated
    And insufficient provider history leaves affected work unresolved

  @ACC-021
  Scenario: Reconnect without changing sender or reviving stale work
    Given revoked provider authorization and durable pending work
    When jobs or sync run
    Then reconnect status is visible and records survive
    When the intended account reconnects
    Then only currently valid work resumes and stopped contacts remain stopped

  @ACC-022
  Scenario: Report evidence-based outcomes and usage
    Given accepted sends, an unknown send, duplicate events, classified replies, links and bookings
    When analytics and usage are displayed
    Then named counts match their populations and time windows
    And duplicates and unknown outcomes do not inflate successes
    And unsupported open or delivery metrics are absent

  @ACC-023
  Scenario: Keep source classes and targets distinct
    Given public documents, synthetic REA verification and authenticated source captures
    When a reference claim is reviewed
    Then its class, target, timestamp, artifact and limitations are identifiable
    And public or synthetic evidence is not reported as private Explee behavior

  @ACC-024
  Scenario: Exercise the rendered core journey and recovery
    Given accepted reference targets and configured fixture failures
    When the owner uses project, lead, preview, inbox, meeting and activity views
    Then loading, empty, validation, error, pause and recovery states are usable
    And keyboard focus and thread-aware manual reply behavior work
    And browser results are recorded separately from API tests

  @ACC-025
  Scenario: Qualify from evidence within the Ceverio audience
    Given HVAC candidates in the three target countries and employee evidence inside, outside or unknown for the 1 to 50 range
    When the versioned scorecard runs
    Then out-of-range and excluded candidates cannot become ready
    And unknown or contradictory facts require research rather than fabricated matches
    And each score and personalization point links to supporting facts

  @ACC-026
  Scenario: Reuse the application for another business
    Given a fresh clone with fictional fixtures and a second project profile
    When the owner configures its offer, countries, sources and policies
    Then its drafts and qualification use that profile without code changes
    And no Ceverio pricing, actual contact data, credentials or private phone number leak into it
    And global suppression and active-endpoint guards still apply

  @ACC-027
  Scenario: Export, expire content and restore encrypted backups
    Given expired research/mail cache, an opted-out contact and a readable encrypted snapshot
    When retention, contact deletion and export run
    Then selected data exports correctly and expired content is removed
    And minimal suppression and recovery identity survive
    When the snapshot is restored with its separately stored key
    Then records are readable and dispatch remains paused for reconciliation

  @ACC-028
  Scenario: Keep the login-free app and database private
    Given the cloud UI behind owner-only access and its isolated backend database role
    When a foreign origin attempts a mutation or an anonymous Data API client reads application data
    Then the attempted access is rejected
    And provider/database secrets are absent from browser bundles and logs
    And the backend cannot access unrelated project data outside its allowed schema

  @ACC-029
  Scenario: Resume cloud work after an outage without a burst
    Given due jobs and saved cursors while the worker stops or loses database connectivity
    When the verified cloud startup workflow resumes
    Then current state is recovered and prerequisites are rechecked
    And overdue messages follow present pacing instead of dispatching as a burst
    And database unavailability pauses external effects

  @ACC-030
  Scenario: Measure the initial workload
    Given 5000 synthetic lead rows and recorded cloud hardware/runtime and Windows browser configurations
    When import and paginated filter workflows are measured
    Then observed timings are compared with the specified targets
    And any unmet target or unmeasured machine limitation remains explicit

  @ACC-031
  Scenario: Verify faithful source states
    Given accepted source screenshots, style/assets evidence and named viewport states
    When the rendered implementation is compared at matching states
    Then design QA records the comparison and behavioral result
    And required blocking discrepancies are fixed before handoff
    And uncaptured states are not called faithful reproductions

  @ACC-032
  Scenario: Enforce provider, recipient and automation capability
    Given a provider excluding the campaign use or a lead lacking current verification or region eligibility
    When activation or dispatch is requested
    Then the blocked prerequisite is visible and no prospect message is sent
    Given a matched reply asking for unsupported facts, discounts or another recipient
    When an automatic response is proposed
    Then it enters review instead of inventing an answer or expanding the envelope
    And advanced CC or attachments remain disabled until their capability is configured and verified

  @ACC-033
  Scenario: Enforce the configured Ceverio pilot, cadence and allowance
    Given only 29 distinct fully ready companies plus preliminary records and duplicate company contacts
    When first prospect dispatch is requested
    Then it waits for the initial 30-company readiness snapshot
    Given that snapshot and an activated five-prospect pilot
    When five distinct first contacts dispatch and a sixth becomes due
    Then the sixth waits until the specified pilot exit conditions pass
    And every recipient is checked again even after the snapshot
    When messages include cold emails, follow-ups, automatic replies and an unknown outcome
    Then all ten consume the same calendar-day application allowance and an eleventh waits
    And no dispatch ignores the ten-minute spacing or recipient window
    And follow-ups are not due before the configured day 4 and day 9
    And a reply does not require rebuilding a pool of 30 unsent companies

  @ACC-034
  Scenario: Fence competing workers without losing late evidence
    Given two workers contend for one queued intent
    When one claim succeeds and the other attempts completion
    Then only the current lease holder can advance its workflow
    Given dispatch began before that lease expired
    When a replacement worker recovers the intent and a late original response arrives
    Then the replacement reconciles instead of repeating the uncertain external effect
    And the late response is retained against the original intent
    And stale completion cannot schedule another follow-up

  @ACC-035
  Scenario: Preserve existing CRM records and suppression
    Given an owner CRM export or capability-confirmed read contains a manual correction, an opted-out endpoint and conflicting identity signals
    When it is ingested twice
    Then entities deduplicate while CRM provenance and the manual facts remain visible
    And suppression remains effective before outreach
    And conflicting matches enter review
    And no upstream CRM create, update or delete is issued

  @ACC-036
  Scenario: Separate market fit from region-specific contact eligibility
    Given market-qualified U.K. records with corporate, individual and unknown subscriber evidence
    And market-qualified South African records with present or absent applicable consent
    When contact eligibility is evaluated under the stored region policy
    Then missing required evidence prevents dispatch readiness without erasing market qualification
    And public contact display or a 1 to 50 employee estimate cannot supply consent or legal entity type
    And objections override any otherwise permitted contact route
    And a provider excluding the campaign still blocks even a region-eligible recipient

  @ACC-037
  Scenario: Separate decision and writing models from operational authority
    Given a pinned self-hosted Laya endpoint and a configured free-hosted drafting model
    When reply decisions and fact-bound draft proposals are requested
    Then each result records its model and question or prompt version
    And Laya is not expected to generate an email body
    And no unconfigured TypeSafe call or on-request model download occurs
    Given a proposal changes approved pricing, recipients or workflow rules
    When it is validated
    Then the change is rejected or reviewed and cannot directly send, book or execute tools

  @ACC-038
  Scenario: Abstain on unevaluated or incomplete model evidence
    Given a candidate with no passing held-out calibration and quality record for this role and language
    When an automatic response is proposed
    Then model-dependent automation remains in shadow or review
    Given a supported model drops decision-critical text or returns invalid or conflicting output
    When the response is evaluated
    Then it abstains rather than treating missing context as permission
    And the owner can inspect the model revision, precision, schema, threshold and truncation evidence
    And model confidence never overrides an opt-out, bounce, owner reply or other deterministic stop rule

  @ACC-039
  Scenario: Enforce the free cloud model boundary
    Given unknown account entitlement or an account that may incur paid overage
    When hosted inference is requested under the zero-spending policy
    Then it is blocked until an applicable free path is established
    Given a verified free allowance becomes exhausted or the inference endpoint is unavailable
    When model-dependent work becomes due
    Then it waits or uses an explicitly approved template for a supported case
    And unsupported questions remain visible for review
    And no paid model, purchased credits, public demo or unevaluated fallback is enabled
    And reserved, actual and unknown usage remain visible without duplicate response dispatch

  @ACC-040
  Scenario: Operate privately in the cloud while the laptop sleeps
    Given a verified free cloud host, selected database, private owner-access policy and configured fixture providers
    When the owner's Windows laptop sleeps
    Then the cloud worker continues eligible scheduled work independently of that laptop
    When an unauthenticated caller, wrong identity or direct-origin request accesses the app
    Then access is denied while the valid owner can use the core journey
    Given the cloud host is lost after an external action began
    When a replacement starts from the durable database and recoverable configuration
    Then uncertain effects reconcile before another dispatch and suppression remains effective
    And no paid resource upgrade, quota evasion or unpaced burst occurs

  @ACC-041
  Scenario: Preserve existing services during DNS activation
    Given a pending Cloudflare quick-scan import and a complete authoritative GoDaddy zone
    When required service records and proxy settings are reviewed
    Then missing or conflicting required records block activation until reconciled
    And Zoho MX targets and priorities, the single SPF value, verification, DKIM key and DMARC survive
    And mail and domain-control records use compatible DNS-only behavior
    When the later nameserver cutover is validated
    Then required service answers and owner-controlled ordinary mail work as recorded
    And DNS authentication is not treated as permission for automated prospect campaigns
    And Cloudflare Email Routing cannot silently replace the existing Zoho MX route

  @ACC-042
  Scenario: Coordinate DNSSEC, nameservers and recovery
    Given old parent DS evidence is missing or its removal has not passed the applicable TTL validation
    When nameserver replacement is proposed
    Then it remains held even if Cloudflare reports DNSSEC disabled
    Given the complete source zone and a validated DNSSEC transition
    When the assigned Cloudflare nameserver pair is configured in a later authorized phase
    Then parent delegation and independent resolver checks establish the expected state
    And the new DS chain is enabled only after the new zone is stable
    Given a required service validation fails
    When recovery is selected
    Then dependent dispatch remains paused and records are compared with the saved baseline
    And any rollback coordinates provider DS and cached TTL state instead of blindly restoring old nameservers

  @ACC-043
  Scenario: Persist the local investigation through GitHub checkpoints
    Given a public planning repository, reviewed project changes and an authenticated evidence group
    When the investigator publishes a completed checkpoint
    Then eligible plans and sanitized findings are committed and pushed to the planning repository
    And authenticated evidence is stored only in a verified private destination with retrievable references and hashes
    And credentials and browser profiles are excluded from every upload
    When a push or evidence upload fails
    Then the checkpoint is reported as unpublished and its only working copy is retained
    And temporary staging is removed only after remote copies and their hashes are verified
