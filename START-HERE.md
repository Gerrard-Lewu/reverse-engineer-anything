# Continue the Explee investigation locally

**Current phase: planning and source inspection only. No application build.**

This repository is the durable project record. Start with [the handover](docs/local-handover.md) and [current checkpoint](docs/handover-checkpoint.md). The project has 43 requirements and 43 acceptance scenarios, a public research baseline and a tested REA capture kit. **No signed-in Explee state has been accepted yet.**

## On your Windows computer

1. In Codex, start an inspection task with **Work in → This computer**.
2. Open this repository in a temporary working checkout. Its GitHub URL is [Gerrard-Lewu/reverse-engineer-anything](https://github.com/Gerrard-Lewu/reverse-engineer-anything).
3. Keep the existing signed-in Explee tab available. Select `@Browser` in the local task. Under Settings → Browser, allow the site; enable Developer mode/full CDP only for the required DOM/style/network inspection and complete the app's site-specific prompt.
4. Paste [the continuation prompt](docs/local-handover.md#continuation-prompt-for-local-codex). Let the agent verify browser, REA and GitHub connections before collecting evidence.

The laptop runs the browser/capture tools; it does not need to host Laya, a database or the future application. The proposed final application remains cloud-hosted.

All durable eligible work must be committed/pushed to GitHub. Temporary checkouts, screenshot staging and tool caches are necessary during execution. Authenticated captures need a **verified private GitHub destination**; this public repository must not receive real inboxes, contact exports or browser credentials. Full rules are in [AGENTS.md](AGENTS.md).
