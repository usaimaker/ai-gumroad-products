# The 90-Minute Measurement Setup: A Free-Tier Analytics Stack That Answers Five Questions

A zero-cost analytics setup for solo founders, built around decisions instead of dashboards, with the 2026 free-tier limits that actually bite.

## Why most free analytics stacks fail

The failure is rarely the tool. It is that one product gets asked to answer every question. Traffic acquisition, behaviour insight, product funnels, privacy posture and reporting are five different jobs, and no single free tier does all five well. So the founder installs a script, looks at a session count, feels vaguely informed, and changes nothing.

The fix is to pick the questions first and let each question select its tool. Three tools is usually the ceiling. Anything more and the stack becomes a chore instead of a signal.

The five questions:

- Where did visitors come from, and which campaigns actually worked?
- Which page or step is leaking, and why did people get stuck there?
- Do people come back, and what did the ones who stayed do differently?
- Are we collecting data we can defend if a customer asks about it?
- Can the answer fit on one screen that someone will actually open?

## The stack, all at zero cost

- Traffic and acquisition: Google Analytics 4. Still the most capable free baseline, with Search Console, Ads and BigQuery hooks built in.
- Behaviour: Microsoft Clarity. Heatmaps, session recordings, rage clicks, dead clicks and scroll depth, positioned as free forever with no site cap, and running on more than two million sites and apps.
- Product analytics, only if you ship software: PostHog free tier, currently covering one million analytics events, five thousand session recordings, one million feature flag requests and 250 survey responses per month. Mixpanel is the alternative with a 20 million event free plan. Self-hosting PostHog removes the event ceiling entirely.
- Reporting: Looker Studio. Free, and it visualises data rather than collecting it, so it never becomes another source of truth to reconcile.
- Optional privacy-light traffic layer: Cloudflare Web Analytics if the site already sits behind Cloudflare. One click, no snippet, no cookies, no consent banner, at the cost of sampling. Umami has a free cloud hobby tier and is free to self-host.

## Hour one: set up GA4 so it is still useful next year

Install the tag, then fix the setting that silently destroys the data you will want in month nine.

- GA4 user-level and event-level data retention defaults to 2 months. The maximum on a free standard property is 14 months. Analytics 360 extends to 26, 38 or 50 months.
- The change is not retroactive. Data already outside the previous window is gone and cannot be recovered. Set 14 months on day one, before there is anything to lose.
- Path: Admin, then Data settings, then Data retention, set the dropdown to 14 months, save. While you are there, keep the option that resets user data on new activity enabled.
- Retention applies to Explorations: free-form, funnel, path and cohort analysis. Standard aggregated reports keep their totals, which is exactly why the gap is so easy to miss. You will still see that January had 10,000 sessions, but you will not be able to break those sessions down by segment once the window closes.
- Define at least one key event before collecting anything. Signup for software, purchase for commerce, subscribe for content. Traffic without a defined conversion is a vanity feed.
- Link Search Console. It is free, it holds 16 months of organic query history, and it is the only place that tells you what people typed before they arrived.
- If you expect to need multi-year raw data, switch on the daily BigQuery export now. Daily export is free, streaming is paid. BigQuery includes 10 GB of free storage and 1 TB of free query volume per month, then charges roughly 0.02 USD per GB stored and 5 USD per TB scanned. For a small site this rounds to nothing and buys permanent history.

## Hour two: install Clarity and watch ten sessions

Quantitative tools tell you the conversion rate fell. They cannot tell you that the mobile call to action sits underneath a sticky banner. Clarity does that, and it costs nothing.

- Install the script alongside GA4. The two do not conflict.
- Watch ten recordings of visitors who reached your pricing or signup page and did not convert. Ten is enough. The same obstacle usually shows up three times.
- Check rage clicks and dead clicks first. A dead click is an element that looks interactive and is not, which is the cheapest conversion bug in existence to fix.
- Read the scroll map on your longest page. If seventy percent of visitors never reach the offer, the copy is not the problem, the position is.
- Turn on field masking before you share recordings with a contractor, so customer input never leaves your account.

## Free tiers that are not what founders assume

Free tier pages are marketing, and they move. Checked in 2026:

- Hotjar free is now heavily rationed, commonly reported at 35 sessions on the free plan with heatmaps capped around 2,000 monthly unique visitors. Clarity covers the same job without the meter.
- Plausible has no forever-free hosted plan. There is a 30-day trial, then paid tiers starting around 9 USD per month. The Community Edition is genuinely free, but you host it.
- Fathom is trial-then-paid as a hosted product. Treat any claim of a free 100,000 pageview plan as out of date until you see it on the vendor pricing page.
- Matomo self-hosted is free in licence terms only. You still pay in hosting and maintenance time.
- Cloudflare Web Analytics is free and sampled. Fine for directional traffic, wrong for revenue attribution.
- GA4 is generous but its real cost is configuration error. A misconfigured property produces no warnings, only quietly degraded data.

## The weekly review that keeps the stack alive

Fifteen minutes, same slot every week:

- GA4: top five acquisition sources ranked by key events, not by sessions.
- Search Console: queries gaining impressions while sitting below position ten.
- Clarity: three recordings from the worst-performing page of the week.
- One written sentence: what changed, and what you will change because of it.

If a tool has not influenced a decision in four weeks, remove it. Unused tracking is liability, not insight.

## How to use

1. Block 90 minutes. Do not read more comparison posts first.
2. Write your five questions on one line each before installing anything.
3. Install GA4. Immediately set data retention to 14 months, define one key event, link Search Console, and enable the free daily BigQuery export if you want history beyond 14 months.
4. Install Clarity. Watch ten sessions the same day and write down the top three obstacles you observed.
5. Add PostHog or Mixpanel only if you ship software with returning users. Skip it entirely for a landing page or a newsletter.
6. Build one Looker Studio page with four numbers: visitors, key events, conversion rate, top source. Bookmark it, and resist building a second page.
7. Put the 15-minute weekly review in your calendar, plus a quarterly reminder to re-verify every free-tier limit above against the vendor pricing page. The tiers that were generous last year are exactly the ones being cut this year.