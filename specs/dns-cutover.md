# Ceverio DNS status and remaining checks

Status: planning and read-only verification, **15 October 2026**. The user activated Cloudflare and enabled DNSSEC signing. This inspection made no DNS, registrar, Access or Tunnel changes and did not build an application.

## Verified current state

Cloudflare MCP GET responses were collected at **2026-10-15 05:13:31 UTC**. The uploaded GoDaddy export is dated 2026-10-14 18:21:20, with no timezone specified. Its archival comments are data, not instructions to import or edit DNS.

| Item | Finding |
| --- | --- |
| Zone | ceverio.com; **active**, full setup, Free Website plan. Activated at 2026-10-15 05:02:37 UTC. |
| Assigned nameservers | amanda.ns.cloudflare.com and titan.ns.cloudflare.com. Independent current parent/resolver views were not collected. |
| GoDaddy comparison | All nine comparable service records match logically: three MX, four TXT and two CNAME. |
| Zoho | MX priorities 10/20/50, SPF, verification, zmail._domainkey DKIM and monitoring DMARC all match. Presence is not a live signing/delivery test. |
| Proxy state | All 11 Cloudflare records are DNS only, including both apex A records, www and _domainconnect. |
| Website target | Cloudflare contains 13.248.243.5 and 76.223.105.230. The export's A value is `WebsiteBuilder Site`, not an IP address; source-IP parity is unverified. |
| TTL | GoDaddy export says 3600 seconds; Cloudflare API says 1, meaning Auto. This is not a one-second published TTL. |
| DNSSEC | **Pending**, algorithm 13, digest type 2, key tag 2371. The user confirms Cloudflare's generated DS has **not yet been added at GoDaddy**. The parent DS/validated chain is unverified. |
| Future app hostname | leads.ceverio.com is absent from both supplied record sets. It remains a proposed hostname; no app route exists from this work. |

The [current DNS evidence](../evidence/dns-followup-source-index.json) retains the export hash, logical comparisons and limitations. Raw responses/export are under ignored evidence/account/. The [14 October snapshot](../evidence/remaining-layers-source-index.json) remains historical and is superseded for current DNS status.

The old GoDaddy SOA and apex NS describe the former authority. They are expected to differ after migration and are not service records to re-import at Cloudflare. No additional SRV/CAA/subdomain entries appear in the supplied export; this does not establish that the provider exported every service.

## Immediate owner step: finish registrar DNSSEC

Enabling DNSSEC at Cloudflare generates signing data. The registrar must publish the matching DS to establish the parent chain. The user answered “Not yet” when asked whether this DS was added at GoDaddy.

In GoDaddy: **Domain Portfolio → ceverio.com → DNS → DS Records → Add**. Use the current Cloudflare DNSSEC card as the authority; at the observation above its values are:

| GoDaddy field | Current Cloudflare value |
| --- | --- |
| Key Tag | 2371 |
| Algorithm | 13 — ECDSA Curve P-256 with SHA-256 |
| Digest Type | 2 — SHA-256 |
| Digest | `288E6F374EC13A660DCF77F0EBA4B6EE353EB87015598CC52A0938C598D5778C` |

Save the DS at GoDaddy rather than adding an ordinary record in Cloudflare. Do not repeat the completed nameserver activation or substitute the former provider's signing data. If a DS is already present when opening that screen, compare it before changing it.

After propagation, re-read Cloudflare DNSSEC status, compare the actual parent DS with the current Cloudflare key and verify successful validating-resolver answers. Pending alone does not diagnose absence versus propagation or mismatch. The user's answer identifies a missing setup step, not an independent parent lookup.

Instructions: [Cloudflare DNSSEC](https://developers.cloudflare.com/dns/dnssec/) and [GoDaddy: add a DS record](https://www.godaddy.com/help/add-a-ds-record-23865). GoDaddy notes propagation can take up to 48 hours; observed answers/status establish completion, not elapsed time.

## Remaining service checks

1. **Delegation/DNSSEC:** compare current parent NS/DS and at least two independent validating resolver views, including a successful signed-domain answer. Retain actual results/timestamps. Current findings establish Cloudflare control-plane state, not this complete live check.
2. **Website:** confirm the actual GoDaddy Website Builder destination and ceverio.com/www HTTPS behavior. Preserve both A records while their required target is unresolved; the symbolic export does not authorize an IP correction.
3. **Ordinary Zoho mail:** later use owner-controlled addresses to verify inbound/outbound delivery and SPF/DKIM/DMARC alignment. No mail is sent during planning. Preserve MX, the single SPF, DKIM and current monitoring DMARC.
4. **Private app route:** only after the future app and owner-only Access policy exist, create the actual Tunnel route and app hostname using its real target. No guessed Oracle IP or public model/database endpoint.

The screenshot's yellow proxy notice concerns HTTP proxy/CDN/security features. DNS-only records can still use Cloudflare authoritative DNS and DNSSEC. Turning all records orange is not needed for DNSSEC. Mail and _domainconnect remain DNS only; proxying the existing website requires separate origin/HTTPS checks.

Keep registration at GoDaddy and ordinary mail at Zoho. Do not replace Zoho MX with Cloudflare Email Routing. DNS authentication does not resolve the permitted-campaign-sender dependency DEP-02. See [email DNS guidance](https://developers.cloudflare.com/dns/troubleshooting/email-issues/).

## Recovery and acceptance

Retain the export and pre/post-migration snapshots. If live checks fail, compare records, delegation and parent DS first. Prefer a targeted correction. Nameserver rollback requires a current old-provider zone and matching DS, with caches/TTLs accounted for; blindly restoring the old nameservers after publishing Cloudflare's DS can break validation.

REQ-DNS-001/002 and ACC-041/042 remain the acceptance references. This turn executed a read-only record comparison and verified Cloudflare activation status. It did not perform a DNS cutover, parent-chain validation, mail test or application acceptance test. DNS progress does not complete Explee source capture.
