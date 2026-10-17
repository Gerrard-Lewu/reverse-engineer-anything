# Build specification

Revision: 0.6, 15 October 2026. This package specifies the requested build; it is not a claim that an application, authenticated Explee inspection, or live campaign has been completed.

**Current phase: planning only. The application build phase has not started.** The user explicitly reaffirmed this on 15 October 2026. Source investigation, requirement questions and specification review may continue; implementation slices remain future work.

The goal is a reusable, single-owner lead-to-meeting application, first configured for Ceverio and privately hosted in the cloud, used from the owner's Windows 11 browser. The user selected whole-cloud operation after supplying the laptop's hardware. Development follows requirements, behavioral examples, implementation slices, and recorded verification. Explee is the visual and workflow reference; independent data and communication adapters provide the actual services.

Read in this order:

For a local continuation, first read [START-HERE.md](../START-HERE.md), [the handover](../docs/local-handover.md), [checkpoint](../docs/handover-checkpoint.md) and [repository working agreement](../AGENTS.md). GitHub publication and private-evidence preflight are required by DEC-27/REQ-REPO-001.

1. [Product goal, scope, and defaults](product.md).
2. [User decisions and remaining dependencies](decisions.md).
   Current cost/capability findings are in [provider feasibility](provider-feasibility.md).
   The pinned [model comparison](model-evaluation.md) and [cloud deployment plan](cloud-deployment.md) refine the AI, host and selected Supabase layers.
   The current [remaining-layer plan](remaining-layers.md) and [Ceverio DNS status/remaining steps](dns-cutover.md) incorporate the reported Oracle account, activation and read-only export comparison.
3. [Explee reverse-engineering completion plan](reverse-engineering-completion.md) and [REA source acceptance](reference-protocol.md).
4. [Domain, provider, and recovery contracts](contracts.md).
5. [Requirements and traceability](requirements.md).
6. [Given/When/Then acceptance scenarios](acceptance.feature).
7. [Execution sequence and exit criteria](build-plan.md).

The current baseline incorporates all 19 answered requirement groups and the instruction to proceed. Additional integration questions remain pending; unanswered questions are recorded as dependencies rather than silently answered. Technical, retention, meeting, and testing choices delegated to the builder are specified as defaults that can be changed.

The future implementation loop is:

> Select the next unblocked slice → update its specification → implement its acceptance examples → implement the behavior → verify through its real interface → record evidence and remaining limitations.

Statuses distinguish `specified`, `implemented`, `fixture-verified`, `provider-verified`, and `source-compared`. A planning document or a passing capture-kit test cannot advance an application requirement to implemented.

## Evidence baseline

- Nine retained public Explee source views and 48 published method/path pairs are indexed in [the evidence index](../evidence/index.json). This is a retrieved reference catalog, not all of Explee.
- The actual REA 6.4.0 MCP session and tool schemas are retained under [evidence/rea](../evidence/rea/20261014T124304Z-session.json). It advertised 170 tools. Server readiness does not establish access to the desktop browser.
- Fifteen bounded authenticated REA states are accepted: overview, targeting, Companies, Project docs, Domains/mailboxes, integrations top and Needs reply empty inbox. The [current checkpoint](../docs/handover-checkpoint.md) records scope/limitations; R1–R4 remain open.
- Ceverio's operating material was read through GitHub at commit `e544cbaac0034f68221c01970d824d2dffeece94`, on `feat/outbound-launch-prep`; [source pointers and returned Git object IDs](../evidence/ceverio-context-index.json) are retained. It records past account checks; those are not fresh external-account verification.
- Private source captures, operating profiles, contact exports, and credentials belong outside the distributable repository.
- Jev Ultrafast and Laya were inspected at pinned repository commits; [source IDs and cloud documentation pointers](../evidence/model-cloud-source-index.json) are retained. No inference benchmark or cloud deployment was run. REA Org is connected; read-only metadata confirms the selected active Supabase project, Free plan and table inventory. No application schema was created.
- Cloudflare MCP confirms ceverio.com's active full Free zone on 15 October. All seven mail records and two CNAMEs match the supplied GoDaddy export; all 11 current records are DNS only. DNSSEC is pending and the user has not added Cloudflare's DS at GoDaddy. The symbolic website A value prevents exact source-IP parity; parent-chain/live service checks remain unverified. [Current DNS evidence](../evidence/dns-followup-source-index.json) supersedes the DNS portion of the [14 October findings](../evidence/remaining-layers-source-index.json). Access/billing observations remain dated 14 October, not fresh entitlement checks.

The specification now contains 43 requirement IDs and 43 acceptance scenarios. Structural links/trace references were checked. The earlier 36-scenario baseline received an independent review; model/cloud/DNS/GitHub additions received a local consistency review, not a new independent review. Application and DNS cutover scenarios are not implemented or executed.
