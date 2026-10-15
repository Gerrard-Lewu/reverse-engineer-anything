# Authenticated source capture checklist

Status: first initial desktop overview `EX-OV-D-001` accepted; other screen and interaction captures pending. Entries below are investigation targets from the user request and public documentation, not a claim that these exact routes/layouts were observed.

The [15 October completion plan](../specs/reverse-engineering-completion.md) gives the R0–R4 sequence and planning exit criteria. Cloudflare activation does not establish source access; the first initial desktop overview has passed private remote verification; full vertical/mobile coverage remains pending.

| Capture group | Required state/behavior | Current evidence |
| --- | --- | --- |
| Project start | `/app-auto-gtm/p/40610`, navigation, overview, existing records, full vertical extent | `EX-OV-D-001`: initial desktop viewport accepted; full vertical extent pending |
| Targeting | Offer/ICP, filters or criteria editor, preview, validation, save behavior | Uncaptured |
| Leads | Search/results, score/research details, selection, enrichment progress, empty/error results | Documented public contracts only |
| Import | Existing import controls, field mapping, validation/progress/row errors | Documented public contracts only |
| Campaign | Existing targeting/copy/schedule fields, lead/draft review, lifecycle indicators | Documented public contracts only |
| Inbox | Tabs, hot-lead view, an existing thread, reply preview, notes, attachments/CC controls | Documented public contracts only |
| Controls | Budget/analytics views, pause/autopilot/reply-policy controls in their current states | Documented public contracts only |
| Meetings | Existing booking-link setting and meeting/outcome indicators | Advertised booking-link routing only |
| Integrations | Existing mailbox/HubSpot/booking connection surfaces and current status | Public HubSpot setup documentation only |
| Responsive | 390 × 844 layout and meaningful control states for the primary journey | Uncaptured |
| Visual source | Fonts, icons/assets, colors, spacing, computed styles, component states | Uncaptured |

For each accepted state record: exact URL, viewport, timestamp, starting state, user action if any, resulting state, screenshot, available DOM/style evidence, relevant request shapes, Evidence IDs, and limitations. Check the saved screenshot before accepting it. Do not treat a login/loading/error page as the intended app screen; record it as a blocker.

One path may contain multiple visual states, so a matching URL is not enough to establish state alignment. Keep the browser stable between inspection and screenshot, and describe the selected modal/tab/control state in notes.

Public API descriptions and static route/endpoint candidates remain separate from observed private requests. Record controls or states that could not be inspected as unresolved. Source capture precedes a faithful UI build under Product Design's URL-to-code guidance.
