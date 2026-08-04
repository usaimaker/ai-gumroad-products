# Inbox Insurance: The Free-Tier Email Deliverability Checklist for Solo Founders (August 2026)

A no-cost, one-afternoon setup that keeps your sales and newsletter email out of the spam folder, based on the rules Gmail, Yahoo and Microsoft actually enforce right now.

## Why this is urgent in 2026

- Google and Yahoo introduced synchronized bulk sender rules in October 2023, enforced from February 2024. Microsoft Outlook aligned with an equivalent rule set enforced from 5 May 2025, and all three still enforce in 2026.
- The penalty is no longer a quiet trip to the spam folder. Non compliant mail is deferred, throttled, or rejected at the SMTP layer with codes such as 550 5.7.26, 550 5.7.40 and 550 5.7.515.
- Free tiers have quietly shrunk. Mailchimp cut its free plan to 250 contacts and 500 sends per month on 17 February 2026, so many founders are migrating senders under deadline pressure and breaking authentication in the process.
- The bulk threshold is roughly 5,000 messages per provider per 24 hours. Google treats the bulk classification as permanent once you cross it, even if your volume drops later.

## The five rules that apply to everyone

- Publish SPF at the apex of your sending domain, and keep it under the 10 DNS lookup limit. Chained ESP includes are the usual cause of a breach.
- Enable DKIM signing with a 2048 bit key. Yahoo rejects 512 bit keys outright and treats 1024 bit as the floor.
- Publish a DMARC record at _dmarc.yourdomain.com. A policy of p=none satisfies the letter of the rules, but always include a RUA address so you can see what is happening.
- Align the From header domain with the SPF or DKIM domain. Gmail and Yahoo accept either one aligned. Microsoft prefers both SPF and DKIM to pass standalone before alignment, which is why mail that passes at Gmail can still bounce at Outlook.
- Add RFC 8058 one click unsubscribe to marketing mail: a List-Unsubscribe header with an HTTPS URL plus List-Unsubscribe-Post: List-Unsubscribe=One-Click. Process the request within two days. Transactional mail should not carry these headers.

Also required and often skipped: a valid PTR record with forward confirmed reverse DNS on the sending IP, TLS on SMTP, and clean RFC 5322 headers. Generic cloud hostnames as PTR records get penalized.

## Complaint rate: the number that decides your fate

- 0.30 percent is the hard ceiling at all three providers. That is three complaints per one thousand delivered messages.
- 0.10 percent is the working target. Anything above that leaves no headroom for one bad campaign.
- Yahoo calculates against inbox delivered mail rather than total sends, so the Yahoo number reads higher than the figure your sending platform shows. Set your alerts on the strictest reading.
- Microsoft gives you no complaint visibility by default. You must enroll in the Junk Mail Reporting Program and Smart Network Data Services, otherwise you are flying blind on the Outlook side.

## The free monitoring stack

- Google Postmaster Tools for spam rate, domain reputation and authentication pass rates. Free, and by far the best dashboard of the three.
- Yahoo Sender Hub for complaint feedback and placement insights.
- Microsoft SNDS plus JMRP for IP level data and individual complaint records.
- A free DMARC aggregate report reader, to turn the daily XML attachments into something a human can read.
- Free SPF, DKIM and DMARC record checkers. Run all three after every DNS edit, because propagation failures are silent.

## Free sending tools and their real ceilings

- HubSpot Marketing Free: around 2,000 marketing sends per month. The most generous permanent free marketing tier.
- Mailchimp Free: 250 contacts and 500 sends per month since February 2026. No longer viable for a real list.
- Apollo free: roughly 5,000 AI writing words per month, a small annual credit pool and two sequences. Enough to test outbound, not to run it.
- Hunter free: limited search and verification credits. Bulk verification and the campaign sender are paid.
- Snov free: about 50 credits per month with a single connected mailbox and no warmup. Fine for a handful of prospects, dangerous if you push volume through your primary inbox.
- Lemlist: no permanent free plan, only a 14 day full feature trial. Treat it as a two week experiment, not as infrastructure.
- Lavender free: five email reviews per month. Useful for scoring your one best template rather than daily writing.
- Calendly free: one event type with unlimited bookings, which removes the scheduling tax on every positive reply.

Treat any credit based free tier as a testing budget, not as a channel.

## Volume discipline for a one person operation

- Never send cold outbound from the domain that hosts your primary mailbox. Register a separate sending domain that points at the same brand.
- Ramp a new mailbox slowly. Single digits per day in week one, then increase gradually across four to six weeks. A new domain has no reputation to spend.
- Keep per mailbox daily volume conservative rather than maximal. Two calm mailboxes beat one burned one.
- Verify every address before sending. Bounces damage reputation faster than low reply rates do.
- Remove hard bounces immediately and non openers on a schedule. A shrinking clean list outperforms a large list sitting in spam.

## Red flags to check before every campaign

- Does the From domain match the DKIM d= tag.
- Is the DMARC record still present with a RUA, and has it survived your last DNS migration.
- Does the unsubscribe endpoint answer a POST request without showing a login screen.
- Do all links point to a single consistent domain, and does the message pass a free spam score test.
- Are you under the complaint threshold in Postmaster Tools for the last seven days.
- Is the reply address a real inbox that a human actually monitors.

## The weekly ten minute routine

1. Open Postmaster Tools and read spam rate, domain reputation and authentication pass rate.
2. Skim the DMARC aggregate summary for any unfamiliar sending source.
3. Check bounce reasons from the last campaign and fix the single largest cause.
4. Prune anyone who has not opened anything in ninety days.
5. Log the numbers in a sheet, so you are reading a trend instead of one noisy day.

## How to use

Block ninety minutes once, then ten minutes a week.

Session one, setup. Select or register your sending domain. Publish SPF, DKIM at 2048 bits, and DMARC with p=none plus a RUA address. Confirm each record with a free checker before you move on. Enroll in Postmaster Tools, Yahoo Sender Hub, SNDS and JMRP on the same day, because all of them need time to accumulate data before they become useful.

Session two, one week later. Add the one click unsubscribe headers to your marketing template. Send a small seed campaign to your own addresses across Gmail, Outlook and Yahoo, and confirm placement in each one. Only after all three land in the inbox should you start ramping real volume.

After thirty days of clean data, move DMARC from p=none to p=quarantine, and later to p=reject. Do not skip the monitoring window. Going straight to enforcement without reading the aggregate reports is the most common way a founder blocks their own mail.

Keep the red flag list open next to your sending platform and run it before every campaign. Deliverability is not a one time fix. It is a habit that costs nothing except attention.