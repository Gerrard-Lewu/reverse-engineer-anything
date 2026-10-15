# Provider feasibility and contact eligibility

Planning research, 14 October 2026. These findings guide the specification; they do not establish connected application accounts or completed integrations.

## Zero-spending baseline

| Component | Finding | Planning consequence |
| --- | --- | --- |
| Database | Supabase currently lists a $0 tier, 500 MB database size, 5 GB egress, two active projects, inactivity pausing after one week, and no automatic backups. | REA Org access confirms the selected active project and Free plan. Verify actual usage/grants/host connectivity; implement own encrypted backups and measure backup traffic within egress. |
| Discovery | CSV and permitted directory/company-site seeds can support bounded research without a paid lead database. | Source coverage and publicly available facts limit results. No promise of Explee's proprietary database or exhaustive 1–50-employee coverage. |
| Verification | MailboxValidator documents up to 300 free API validations every 30 days. Its FAQ notes unsupported Yahoo and non-ASCII addresses and states that paid-plan auto recharge is separate. | Candidate for the initial adapter, subject to account/terms/result-shape checks. Unsupported, catch-all, blocked and unknown results remain unresolved; vendor validation is not an inbox-delivery guarantee. Reserve quota for initial checks and freshness checks. |
| Sender | Zoho Mail's current policy excludes automated/promotional campaigns. A permitted zero-cost prospect sender for the intended traffic has not been established. | Keep research, qualification and draft preparation available; live prospect automation is a named integration dependency. Low daily volume does not override provider policy. |
| Booking page | Cal.com advertises a free individual booking page with multiple event types/calendars. The selected existing Ceverio booking link has not been observed. | Prefer the user's verified existing configuration. A new page is a candidate, not an account creation performed in planning. |
| Booking outcomes | Cal.com's pricing/comparison material contains inconsistent general API statements and a specific restriction on hosted-free API access. API v2 documentation describes authentication, not this account's entitlement. | Do not promise free hosted API polling. Verify the selected account/plan. Read-only Calendly polling or validated selected-calendar events may be alternatives; webhook availability and trustworthy correlation require evidence. |
| AI | Inspected Jev Ultrafast requires hosted model calls; Laya publishes self-hostable decision weights and cannot generate emails. | Prefer cloud CPU Laya plus a verified free-hosted open-weight writer; see model-evaluation.md and cloud-deployment.md. Templates/review remain available without paid fallback. |
| Hosting | Whole-cloud operation is selected. The user reports an Oracle Free Tier account in Ashburn; Cloudflare MCP confirms its account and active ceverio.com Free Website zone. DNSSEC remains pending; registrar DS not yet added. | Verify Oracle free capacity and actual Workers AI/Zero Trust entitlements/private access before later deployment; zone Free is not proof of those service plans. |

Sources: [Supabase pricing](https://supabase.com/pricing), [MailboxValidator FAQ](https://www.mailboxvalidator.com/faqs) and [plans](https://www.mailboxvalidator.com/plans), [Zoho Mail usage policy](https://www.zoho.com/mail/help/usage-policy.html), [Cal.com pricing](https://cal.com/pricing), [Cal.com API comparison](https://cal.com/blog/calendly-api-vs-cal-com-api) and [API v2 introduction](https://cal.com/docs/api-reference/v2/introduction).

## Three-country eligibility specification

Discovery and market fit remain separate from permission to dispatch. Record recipient country, business/subscriber type where relevant, contact purpose, applicable policy version, consent/customer evidence, data-processing basis/notice where required, and objections. Unknown evidence enters research/review and cannot be filled from company size or an email-domain suffix.

| Country | Conservative proposed dispatch default |
| --- | --- |
| United States | Apply the configured truthful identity/content, postal address and opt-out policy to commercial B2B mail, plus provider permission and suppression. |
| United Kingdom | Establish whether the recipient is a corporate or individual subscriber. Require an appropriate recorded consent/customer route for individual subscribers and unknown types. Corporate B2B treatment does not remove personal-data, notice or objection obligations. |
| South Africa | Initially permit automated marketing only with recorded applicable consent; any existing-customer exception or consent-request workflow requires its own confirmed rules before activation. |
| Unknown/conflicting region | Hold dispatch while geography/policy applicability is unresolved. |

These are application eligibility defaults, not a finding that any actual prospect already satisfies them. Use the [FTC commercial-mail guidance](https://www.ftc.gov/business-guidance/resources/can-spam-act-compliance-guide-business), [ICO B2B guidance](https://ico.org.uk/for-organisations/direct-marketing-and-privacy-and-electronic-communications/business-to-business-marketing/), and the Information Regulator's [POPIA forms](https://inforegulator.org.za/popia-forms/) and [direct-marketing guidance index](https://inforegulator.org.za/guidance-notes/) to validate the selected policy before a pilot.

The ICO page flags ongoing guidance review. South African Form 4 references were retrieved, but the fuller guidance PDF and Chapter 8 page were not retrievable during this research. Preserve that coverage limit and complete the rule validation before live South African dispatch. The Gmail program-policy page also failed retrieval; do not describe its current full policy as freshly audited.

## Readiness levels

- **Market qualified:** the profile's country/industry/size/score evidence is sufficient.
- **Contact eligible:** contact purpose, verification, region policy, freshness and suppression are satisfied.
- **Dispatch ready:** sender policy/account health, configured campaign, time window, usage allowance and all contact gates are satisfied.

A lead can be valuable and market qualified while its address, entity type or consent still needs work. The 30-company Ceverio pilot snapshot counts dispatch-ready companies rather than preliminary scores.

## Planning dependencies

Resolve the desktop REA capture route, real sender transport, correct booking configuration, database usage/grants/host connectivity and other cloud account capabilities from inspection or the pending questions. Repository identification, hardware, full-cloud preference and selected Supabase access/Free plan are now settled. Specific test addresses and runtime/model quality remain dependencies; no application has been built.

The [model comparison](model-evaluation.md) and [cloud plan](cloud-deployment.md) separate downloadable weights, free hosted allowances and account entitlements. These updates do not establish a permitted free prospect sender.

The current [remaining-layer plan](remaining-layers.md) and [DNS status/steps](dns-cutover.md) preserve ordinary Zoho mail. Cloudflare activation and nine comparable export values are verified; the symbolic WebsiteBuilder A target prevents exact source-IP parity. Registrar DS/validated chain and live service checks remain outstanding. Private app access remains future work.
