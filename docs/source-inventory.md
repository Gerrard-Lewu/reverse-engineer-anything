# Official Explee source inventory

Collected on 14 October 2026. This inventory supports the product and technical blueprint with public source material. The signed-in application at `/app-auto-gtm/p/40610` was not observed by this collection.

## Evidence classification

- **Official copy:** Explee's published claims about its product, infrastructure, datasets, outcomes, and pricing. These establish stated scope; they do not verify operation.
- **Official documentation:** Published interface and integration descriptions. These are documented public contracts, not captured private application traffic.
- **Retrieval diagnostic:** Tool failures and empty views. These provide access information and establish no product capability.
- **Design decision:** A proposed behavior for the internal tool must be labeled as a decision unless it has separate app observation evidence.

Every raw tool response is preserved in `evidence/public/pub-NNN.json` with its request, tool, retrieval time, and stable record ID. `evidence/public/sources.json` maps canonical source IDs to those records and includes hashes. `source-NNN.txt` files preserve the connector-returned page/search views by source. `documented-operations.json` indexes the public operation headings found in those excerpts with source lines and response IDs. A stored response is complete as returned by the connector; it is not necessarily the entire webpage or JSON document.

## Source register

| Source ID | Primary URL | Classification | Retrieval records | Coverage |
| --- | --- | --- | --- | --- |
| EX-PUB-001 | [Explee](https://explee.com/) | Official copy | PUB-004 | Homepage, pipeline example, FAQ, and indexed homepage variants. |
| EX-PUB-002 | [Pricing](https://explee.com/pricing) | Official copy | PUB-004, PUB-005 | Indexed excerpt and current page view. Prefer PUB-005. |
| EX-PUB-003 | [HubSpot integration](https://explee.com/integrations/hubspot) | Official integration documentation | PUB-004, PUB-005 | Setup, data access, matching rules, and FAQ. |
| EX-PUB-004 | [Public API documentation](https://api.explee.com/public/api/docs) | Official public API documentation | PUB-004, PUB-005, PUB-007, PUB-008, PUB-009 | Multiple line-numbered excerpts of a 1,055-line document; selective coverage. |
| EX-PUB-005 | [OpenAPI schema](https://api.explee.com/public/api/openapi.json) | Official public API schema | PUB-007, PUB-008, PUB-009 | Header, early schema fragment, and references; complete valid JSON was not recovered. |
| EX-PUB-006 | [B2B database](https://explee.com/b2b-database) | Official dataset copy | PUB-006 | Dataset scope, categories, enrichment fields, and use cases. |
| EX-PUB-007 | [Maps dataset](https://explee.com/gm-dataset) | Official dataset copy | PUB-006 | Dataset scope and selected field descriptions; partial page view. |
| EX-PUB-008 | [Segments Explorer](https://explee.com/tools/explorer) | Retrieval diagnostic | PUB-006, PUB-007 | Page identity returned, but no usable interactive workflow content. |
| EX-PUB-009 | [API root](https://api.explee.com/) | Indexed excerpt of official documentation | PUB-004 | Search excerpt only. Not opened. |

The retrieval connector was `mcp__codex_apps__search_service_web_run`. It labeled the opened sources as crawled today. Retrieval time records the tool call, not deployment time; indexed search snippets can be older.

## Supported product scope from the homepage

The following short fragments are quoted from [Explee's homepage](https://explee.com/) (EX-PUB-001). The quotes below total 24 words; the descriptions are paraphrases of the cited page views.

| Capability described by Explee | Exact source fragment | Evidence location |
| --- | --- | --- |
| Website-based business analysis and ICP refinement | “research the market, sharpen your ICP” | PUB-004, homepage lines 5, 150–177, 276–278 |
| Prospect discovery | “find high-intent prospects” | PUB-004, homepage lines 5, 178–214 |
| Personalized email generation | “personalized emails” | PUB-004, homepage lines 5, 215–221 |
| Meeting-oriented outreach | “book demos” | PUB-004, homepage lines 5, 222–228 |
| Agent replies and scheduler links | “agent answers questions” | PUB-004, homepage lines 291–293 |
| Lead review, template preview, natural-language steering, and pause/budget controls | “one click pauses everything” | PUB-004, homepage lines 279–290 |
| Own-lead CSV import | “30,000 contacts” | PUB-004, homepage lines 294–296 |
| Sending through Explee-managed warmed mailboxes | “pre-warmed inboxes” | PUB-004, homepage lines 282–287 |

The scheduler FAQ names Calendly, Cal.com, and HubSpot Meetings. This supports booking-link routing; it does not establish a free/busy calendar API or direct event creation. Dataset size, inbox-rate, lead-cost, and conversion figures remain vendor claims.

## Published public API scope

[API documentation](https://api.explee.com/public/api/docs) (EX-PUB-004) documents the following families; no endpoint was executed:

| Family | Documented scope | Exact locator fragment |
| --- | --- | --- |
| Search and enrichment | Company/people search, domain lookup, criteria scoring, natural-language filters, email/phone enrichment, async jobs, and deduplication. | `/public/api/v1/search/companies` |
| Projects and campaigns | Targeting/copy/schedule definitions; creation, review, approval, start/stop; own-lead async import. | `/public/api/v1/autogtm/campaigns` |
| Inbox | Hot-lead feed; conversation tabs, threads, replies, CC, attachments, and notes. | `need_reply`, `replied`, `sent`, `can_reply` |
| Controls | Project/campaign budgets, analytics, autopilot, delayed auto-reply, and project reply CC. | `autopilot_enabled`, `auto_reply_delay_minutes` |
| Suppression | Shared person/domain lists checked before sending, including ongoing sequences. | “Suppress list” |

Evidence: PUB-005 API lines 10–234; PUB-007 lines 286–319, 397–590, 873–902, 929–1054; PUB-008 lines 319–340, 601–643, 698–846; PUB-009 lines 662–670, 873–877.

Documented campaign states include `discovery`, `review`, `outreach`, and stopped `listening`. The docs describe automatic approval after a default 12-hour review window when automatic management is enabled. Imported campaigns differ from discovery campaigns.

These contracts use `X-API-Key`. They do not establish the signed-in frontend's private API, implementation framework, storage, queue, prompts, or model providers.

## Other primary sources

[Current pricing](https://explee.com/pricing) (EX-PUB-002, PUB-005 lines 8–30) lists outreach as “Pay as you go with no subscription” and displays $30 for 750 emails. The homepage agrees at $0.04 per sent email. PUB-004's older indexed pricing snippet reports 1,000 emails for $30 and historical AI Search plans; do not treat that snippet as current. Current pricing also describes country/global bulk datasets, semantic search, enrichment, and additional paid research/contact data. All displayed outcome estimates are marketing estimates.

[HubSpot documentation](https://explee.com/integrations/hubspot) (EX-PUB-003, PUB-005 lines 4–71) describes syncing “Hot leads only”, selecting a pipeline/stage, optional historic sync, and recording conversations. Contact matching uses email; company matching uses domain. Setup is described at project Settings → Integrations. The integration uses HubSpot OAuth and can be disconnected. Its stated plan eligibility is documentation, not tested entitlement.

[The B2B database page](https://explee.com/b2b-database) (EX-PUB-006, PUB-006) describes “105M+ Companies Worldwide” and fields spanning descriptions, geography, size/funding, contacts, traffic, employees, website content, Maps, and technologies. Field coverage varies; these figures and refresh claims were not independently verified. This establishes desired research-data categories, not possession of a reproducible dataset.

[The Maps dataset page](https://explee.com/gm-dataset) (EX-PUB-007, PUB-006 lines 2–26) advertises “218M+ local business profiles”, 55 fields, and a four-week refresh cycle. Retrieved categories include identity, geography, contact details, ratings/reviews, and other venue attributes. Explee's pricing page instead lists 210M+ places and 51 fields. Preserve that public-copy discrepancy rather than selecting one as verified.

## Access diagnostics

PUB-001 (map), PUB-002 (scrape), and PUB-003 (search) record the initial Firecrawl attempts at 12:00:12 SAST. All failed because the connected Firecrawl account lacked credits; search reported HTTP 402. No Firecrawl page data was collected and no retry was attempted. These records are diagnostic evidence only. Public material was subsequently retrieved through the web connector. This collection did not use executor HTTP access to Explee.

## Gaps to close with REA/browser evidence

- No signed-in screens, sidebar/navigation, real campaign/project fields, inbox records, lead list, settings, permission states, or error/loading states were captured.
- No desktop/mobile layout, visual tokens, component measurements, DOM, CSS, assets, browser storage, JavaScript bundle, or request/response trace was captured here.
- The API document and OpenAPI schema were only selectively retrieved. Private application API equivalence, exact schema completeness, rate-limit behavior, and successful requests remain unverified.
- Booking links are documented; calendar availability, rescheduling/cancellation, conferencing, invitation ownership, and meeting-confirmation detection require observation or an explicit design decision.
- Marketplace integrations, channel support beyond email, database exports, and segment exploration were not comprehensively inventoried.
- Public lifecycle descriptions contain mode-dependent start/resume behavior; capture the reference app before requiring exact parity.
- Import copy describes validation differently from API docs, which specify verification at send time. Resolve timing through app evidence.
- Lead databases and warmed sending infrastructure need their own providers or implementation choices for an independent internal tool; page inspection cannot recover those assets.

