# Authenticated source capture checklist

Status: fifteen bounded REA states accepted: overview/targeting/Companies/Project docs plus Domains three desktop views, integrations top and Needs reply empty inbox. Broader screen/interaction coverage pending. Entries below are investigation targets from the user request and public documentation, not a claim that these exact routes/layouts were observed.

The [15 October completion plan](../specs/reverse-engineering-completion.md) gives the R0–R4 sequence and planning exit criteria. Cloudflare activation does not establish source access; the first initial desktop overview has passed private remote verification; full vertical/mobile coverage remains pending.

| Capture group | Required state/behavior | Current evidence |
| --- | --- | --- |
| Project start | `/app-auto-gtm/p/40610`, navigation, overview, existing records, full vertical extent | `EX-OV-D-001`: initial desktop viewport accepted; full vertical extent pending |
| Targeting | Offer/ICP, filters or criteria editor, preview, validation, save behavior | `EX-TG-D-001/002` and `EX-TG-M-001`: main form vertical/mobile presentation accepted; drawer, variants, validation and save behavior pending |
| Leads | Search/results, score/research details, selection, enrichment progress, empty/error results | Two bounded Companies desktop states accepted. Horizontal/bottom/detail/mobile and other states unresolved. |
| Project docs | Company profile, competitors, Reply facts and Files; vertical desktop/mobile layout | Four bounded states accepted; source-update cohorts recorded separately. No save/upload/delete behavior tested. |
| Import | Existing import controls, field mapping, validation/progress/row errors | Documented public contracts only |
| Campaign | Existing targeting/copy/schedule fields, lead/draft review, lifecycle indicators | Documented public contracts only |
| Inbox | Tabs, hot-lead view, an existing thread, reply preview, notes, attachments/CC controls | Needs reply empty desktop accepted (`EX-IB-D-001`). Selected-thread/status/Lead info and other variants/mobile remain pending; no workflow validation. |
| Controls | Budget/analytics views, pause/autopilot/reply-policy controls in their current states | Documented public contracts only |
| Meetings | Existing booking-link setting and meeting/outcome indicators | Advertised booking-link routing only |
| Integrations | Existing mailbox/HubSpot/booking connection surfaces and current status | Initial desktop accepted (`EX-IG-D-001`); lower/custom/API region, connection variants and mobile pending. |
| Domains/mailboxes | Existing counts/sender field, offer/setup timeline and FAQ disclosures | Top/middle/FAQ desktop accepted (`EX-DM-D-001/002/003`); timeline end clipped at initial horizontal position. Configuration, horizontal variants and mobile unverified. |
| Responsive | 390 × 844 layout and meaningful control states for the primary journey | Targeting accepted; Project docs top/lower accepted with source-cohort limits. Other groups and interaction variants unresolved. |
| Visual source | Fonts, icons/assets, colors, spacing, computed styles, component states | Targeting CSS/fonts and desktop/mobile measurements retained; leads/Docs supplements privately retained with explicit scope/cohort limits. Complete component/assets/variant coverage unresolved. |

For each accepted state record: exact URL, viewport, timestamp, starting state, user action if any, resulting state, screenshot, available DOM/style evidence, relevant request shapes, Evidence IDs, and limitations. Check the saved screenshot before accepting it. Do not treat a login/loading/error page as the intended app screen; record it as a blocker.

One path may contain multiple visual states, so a matching URL is not enough to establish state alignment. Keep the browser stable between inspection and screenshot, and describe the selected modal/tab/control state in notes.

Public API descriptions and static route/endpoint candidates remain separate from observed private requests. Record controls or states that could not be inspected as unresolved. Source capture precedes a faithful UI build under Product Design's URL-to-code guidance.
