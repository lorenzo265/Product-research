# Global opportunity-signal sources and web search/extraction APIs for AI agents (verified 2026-09-24)

**How these notes were verified, and how far to trust them.** The research date is 2026-09-24. The session ran behind an egress proxy that blocked most vendor domains (exa.ai, tavily.com, perplexity.ai, brave.com, firecrawl.dev, jina.ai, parallel.ai, serpapi.com, reddit, producthunt, trustmrr, developers.google.com, hn.algolia.com, artificialanalysis.ai, openbenchmarks.com). The shared session cap of 200 WebSearch calls was also used up partway through. Each claim therefore carries a tag for how it was checked:
- **[D] Direct.** I read the primary artifact myself: official docs page, the vendor's official GitHub README, a package registry, or cloud.google.com.
- **[S] Search snippet.** A search-engine summary of the official page (URL listed), not fetched directly.
- **[C] Competitor or third party.** Figures published by someone other than the vendor. Most competitor pricing below comes from Parallel's public content mirror on GitHub (Parallel is a competing search vendor). Treat it as "reported by Parallel, dated 2026", and check it against the vendor's own page before you commit money.
- **Benchmarks** are labelled **VENDOR-RUN** or **INDEPENDENT**. The two independent boards found (Artificial Analysis Search Index and Openbenchmarks) are known here only through Parallel's write-ups. Their original sites were blocked.

---

## Key Question 1 — Global opportunity-signal sources: access method, cost, limits, terms (plus a one-line implication for each)

### Takeaway
The cheap, legally clean, automatable signals are:
- **Hacker News**: the free Firebase API and the Algolia API.
- **The YC company directory**: an unofficial daily JSON snapshot of 6,248 launched companies.
- **Google Play reviews**: maintained scraper libraries that support `lang='pt'` and `country='br'`.
- **TrustMRR**: a verified-revenue API with low rate limits.

The high-value social sources are now gated:
- **Reddit** needs explicit approval for all access since the late-2025 Responsible Builder Policy, and commercial use costs $0.24 per 1,000 calls.
- **Product Hunt's API** is non-commercial unless they agree otherwise.
- **Google Trends** has no generally available official API. The alpha is allowlisted, and pytrends has been archived since April 2025.
- **Exploding Topics' API** costs $249/month for the base plan plus an add-on.

Acquire.com, Indie Hackers, G2, Capterra and Open Startups have no official public data API that I could verify.

### Cited Findings

**Hacker News (official Firebase API)**
- Endpoint prefix `https://hacker-news.firebaseio.com/v0/`. Stories, comments, jobs, Ask HNs and polls are all "items". The README says: "There is currently no rate limit." [D] — [HackerNews/API README](https://github.com/HackerNews/API)
- The v0 API is "essentially a dump of our in-memory data structures". To count comments or build Ask/Show lists you traverse item trees yourself. [D] — [HackerNews/API README](https://github.com/HackerNews/API)

**Hacker News (Algolia HN Search API)**
- Full-text search API at hn.algolia.com, limited to 10,000 requests per hour per IP. No key required (a direct fetch was blocked, so this comes from the page snippet). [S] — [HN Search API](https://hn.algolia.com/api)

**Reddit Data API**
- **Free tier.** Free for non-commercial use (personal projects, bots, moderator tools, academic research) at 100 queries per minute per OAuth client ID. [S/secondary] — [Octolens](https://octolens.com/blog/reddit-api-pricing); [Prowlo](https://prowlo.com/blog/reddit-data-api)
- **Commercial use.** Needs Reddit's approval and a paid agreement at $0.24 per 1,000 API calls. One secondary source cites a bundled commercial tier of $12,000/month for up to 50M calls and says there is no smaller paid plan between free and enterprise. [S/secondary, not verified on Reddit's own pages] — [Octolens](https://octolens.com/blog/reddit-api-pricing); [SocialCrawl](https://www.socialcrawl.dev/blog/reddit-data-api-2026)
- **Responsible Builder Policy.** Introduced on r/redditdev in November 2025 and updated June 5, 2026. It states: "You must request access and get explicit approval before accessing any Reddit data through our API." It applies to developers, moderators, researchers and bots alike. Self-service app registration was replaced by manual review. Reddit can deny without giving a reason, and developers report 2–4 week queues. [S; the policy page was listed in results but the direct fetch was blocked] — [Reddit Help: Responsible Builder Policy](https://support.reddithelp.com/hc/en-us/articles/42728983564564-Responsible-Builder-Policy); [Prowlo](https://prowlo.com/blog/reddit-data-api); [redditapis.com](https://www.redditapis.com/reddit-responsible-builder-policy); [ReplyDaddy](https://replydaddy.com/blog/reddit-api-pre-approval-2025-personal-projects-crackdown)
- **AI/model use.** Commercial use of any model trained on Reddit data is prohibited without explicit approval. [S/secondary] — [Reddit Help: Developer Platform & Accessing Reddit Data](https://support.reddithelp.com/hc/en-us/articles/14945211791892-Developer-Platform-Accessing-Reddit-Data)
- **Background.** Paid API access was announced in April 2023. [S] — [TechCrunch](https://techcrunch.com/2023/04/18/reddit-will-begin-charging-for-access-to-its-api/embed/)
- **Client library.** PRAW, the main Python client, is still maintained: v8.0.3 was published 2026-08-12. [D] — [PyPI praw](https://pypi.org/project/praw/)

**Product Hunt API v2 (GraphQL)**
- The docs say the API "must not be used for commercial purposes". Business use requires contacting hello@producthunt.com. [S] — [Product Hunt API docs](https://api.producthunt.com/v2/docs)
- Rate limits: 6,250 complexity points per 15 minutes on the GraphQL endpoint, and 450 requests per 15 minutes on other endpoints. Over the limit you get HTTP 429. Product Hunt can rate-limit apps it judges to be breaking fair use. [S] — [Product Hunt API: Rate Limits](https://api.producthunt.com/v2/docs/rate_limits/headers)

**Acquire.com (startup marketplace)**
- No official public listings API was found. Third-party Apify actors scrape public listing pages (title, asking price, annual revenue/profit, category) through the public sitemap and server-rendered pages without login. They also offer an "authenticated mode" that uses your own logged-in session. [S] — [Apify igolaizola/acquire-scraper](https://apify.com/igolaizola/acquire-scraper); [Apify lexis-solutions/acquire-scraper](https://apify.com/lexis-solutions/acquire-scraper/api)

**TrustMRR (verified-revenue database)**
- Revenue is verified through read-only connections to Stripe, LemonSqueezy and Paddle. The site shows MRR, total revenue, month-over-month growth, and a leaderboard. [S] — [Grokipedia: TrustMRR](https://grokipedia.com/page/TrustMRR); [Superframeworks](https://superframeworks.com/articles/trustmrr-api-ideas-indie-hackers)
- There is a public API. Standard keys get 10 requests/minute and premium keys 60 requests/minute. Fields include MRR, churn, growth, customer counts, and for listings for sale the asking price and multiples. [S] — [TrustMRR API docs](https://trustmrr.com/docs/api); [Superframeworks](https://superframeworks.com/articles/trustmrr-api-ideas-indie-hackers)
- **Coverage figures conflict:** "840+ startups across 82 countries" according to [Superframeworks](https://superframeworks.com/articles/trustmrr-api-ideas-indie-hackers), versus "470+ real startups" with asking prices and multiples according to [Netrows](https://www.netrows.com/blog/best-trustmrr-startup-revenue-apis-2026). The difference may come from different dates or subsets. [S]

**Y Combinator company directory**
- There is no official API. The unofficial `yc-oss/api` pulls from the YC website's Algolia search index (it does not scrape HTML) through a daily GitHub Action. It publishes static JSON endpoints: all companies, top companies, companies hiring, and more. It also publishes a daily change log at `changes/latest.json`. [D] — [yc-oss/api README](https://github.com/yc-oss/api)
- Snapshot as of 2026-09-24 02:19: 6,248 launched companies, 51 batches, 59 industries, 337 tags. [D] — [yc-oss/api README](https://github.com/yc-oss/api)
- My own parse of `companies/all.json` (downloaded 2026-09-24) [D, own computation]:
  - Fields: `one_liner`, `long_description`, `industry`, `subindustry`, `tags`, `batch`, `status`, `stage`, `team_size`, `regions`, `all_locations`, `website`, `isHiring`, `launched_at`, `top_company`.
  - Status counts: Active 4,322; Inactive 1,080; Acquired 823; Public 23.
  - 51 companies mention Brazil in `all_locations` or `regions`. — [yc-oss/api data](https://github.com/yc-oss/api)

**Google Play reviews and metadata (unofficial scrapers)**
- `google-play-scraper` (Python, JoMingyu): latest PyPI release 1.2.7 on 2024-06-07. [D] — [PyPI](https://pypi.org/project/google-play-scraper/)
  - `lang` and `country` take ISO 639-1 and ISO 3166 codes, so Brazil is `lang='pt', country='br'`.
  - Reviews come back 200 per page (Google Play's maximum) with a `continuation_token` for the next page. [D] — [JoMingyu/google-play-scraper README](https://github.com/JoMingyu/google-play-scraper)
- `google-play-scraper` (Node, facundoolano): npm 10.1.3 published 2026-05-31, so it is actively maintained. It takes `lang` and `country` parameters, and list endpoints go up to `num` 250. [D] — [npm registry](https://www.npmjs.com/package/google-play-scraper); [facundoolano/google-play-scraper](https://github.com/facundoolano/google-play-scraper)

**Apple App Store reviews (unofficial scrapers)**
- `app-store-scraper` (Node, facundoolano): npm 0.18.0, last published 2023-11-21.
  - Reviews take a `country` parameter that "also affects the language of the data".
  - `page` defaults to 1 and the "maximum allowed is 10".
  - Sort is RECENT or HELPFUL. [D] — [npm registry](https://www.npmjs.com/package/app-store-scraper); [facundoolano/app-store-scraper README](https://github.com/facundoolano/app-store-scraper)
- `app-store-scraper` (Python, cowboy-bebug): last PyPI release 0.3.5 on 2020-11-12, so effectively unmaintained. [D] — [PyPI](https://pypi.org/project/app-store-scraper/)

**Google Trends**
- **Official API (alpha).** Google announced it on July 24, 2025. Access is application-based and rolls out to a limited group; Google prioritises developers with a concrete use case who can give feedback.
  - Data: consistently scaled search interest going back 1,800 days (5 years), with daily, weekly, monthly and yearly aggregation, and region and sub-region filters.
  - A 2026 secondary source says the docs page still described it as alpha as of August 2026, with no published pricing and no GA timeline.
  - A Google community thread reports applications getting no response. [S] — [Google Search Central blog](https://developers.google.com/search/blog/2025/07/trends-api); [Trends API alpha page](https://developers.google.com/search/apis/trends); [DEV Community](https://dev.to/radevicb/google-trends-still-has-no-api-in-2026-heres-what-i-use-instead-1840); [Google community thread](https://support.google.com/webmasters/thread/430972036/google-trends-api-alpha-access-application-%E2%80%94-no-response-received?hl=en)
- **pytrends.**
  - The repository was archived (read-only) on April 17, 2025, after the maintainer stepped away. [S] — [GeneralMills/pytrends](https://github.com/GeneralMills/pytrends); [Issue #636 "Stepping out as a maintainer"](https://github.com/GeneralMills/pytrends/issues/636)
  - The last PyPI release is 4.9.2, uploaded 2023-04-13. [D] — [PyPI pytrends](https://pypi.org/project/pytrends/)
  - The README calls itself "Only good until Google changes their backend again". It says the rate limit "is not publicly known" and recommends proxies or sleeps when you get blocked. [D] — [pytrends README](https://github.com/GeneralMills/pytrends)
- **Alternative unofficial library.** `trendspy` 0.1.6 was released 2024-12-25; I did not verify how well it is maintained. [D] — [PyPI trendspy](https://pypi.org/project/trendspy/)

**Exploding Topics**
- The API is an add-on to the Pro Business plan, which starts at $249/month and includes 2,000 tracked trends. It comes in three add-on tiers; one third-party source says "from $1,000/mo". There is a 7-day trial of Business. The database holds more than 1.1M trends, with search volume, growth and forecasts. [S; the $1,000 figure is third-party] — [Exploding Topics API page](https://explodingtopics.com/feature/et-api); [Exploding Topics blog](https://explodingtopics.com/blog/exploding-topics-api); [The Rundown](https://www.therundown.ai/tools/exploding-topics)

### Inferences

One-line implication for each source, for a Brazil-first, solo-founder, geographic-arbitrage harness:
- **HN (Firebase + Algolia)**: free, unauthenticated and clean. Make it the default source for "problems people pay to solve abroad" (Show HN, Ask HN, "I'd pay for") at zero cost.
- **Reddit**: plan for approval delays and possible denial. For a commercial harness, budget $0.24 per 1,000 calls once approved, or read it through general web search results instead of the API. Do not build a core pipeline on unapproved scraping.
- **Product Hunt**: fine for personal or non-commercial discovery at low volume. If the harness becomes a commercial product, ask for permission (hello@producthunt.com) before collecting systematically.
- **Acquire.com**: no official API. Scraping through Apify runs into their ToS, which I could not verify. Use it manually or in small samples as a "proven revenue abroad" signal rather than as an automated feed.
- **TrustMRR**: the most direct "proven abroad" signal (Stripe-verified MRR plus country). At 10–60 requests/minute it supports daily pulls of the full catalogue. It is the best fit for arbitrage filters (non-BR, recurring revenue, small team).
- **YC directory (yc-oss)**: free, daily and structured. Only 51 of 6,248 companies are Brazil-located, which gives a ready "proven abroad, check for a BR equivalent" candidate list you can filter by industry, status and team size.
- **Google Play scraper**: the best cheap source of Brazilian demand pain. `country='br', lang='pt'` pulls PT-BR reviews of foreign apps (complaints) and local competitors. Unofficial, so throttle it and store it minimally.
- **App Store scraper**: capped at 10 review pages per app and country, with the Node library last published in 2023. Use it as a secondary check only.
- **Google Trends**: there is no dependable programmatic path at solo-founder cost. Apply for the alpha, meanwhile use the Trends UI manually or a paid SERP/Trends scraper, and do not rely on pytrends in automation.
- **Exploding Topics**: at least $249/month, and the API adds far more. That is out of budget for a solo founder, so use the free web UI manually for spot checks.

### Gaps
- **Indie Hackers**: I found no official API or data-access terms. Searches ran out before I could check its ToS or current ownership.
- **G2 and Capterra**: I could not verify API availability, pricing or anti-scraping terms (domains blocked, search budget exhausted). This remains a gap for the report writer.
- **Open Startups** (open-revenue lists such as openstartuplist.com): not verified, because the domain was blocked.
- **Official terms for app-store scraping**: Google Play and Apple ToS clauses on automated collection were not checked. The libraries above are unofficial, and their legal status under store terms is unverified.
- **Acquire.com ToS and robots.txt**: the actual clauses on automated collection were not verified.
- **Reddit**: I could not fetch Reddit's own pricing page. The $0.24 per 1,000 calls rate and the $12,000/month tier come from secondary sources only.
- **Google Trends alpha**: no primary confirmation of its status after August 2026. Google's pages were blocked by the proxy.

---

## Key Question 2 — Search and extraction APIs for agents: pricing, benchmarks (independent vs vendor-run), MCP availability, Portuguese/Brazil coverage

### Takeaway
The per-1,000-call list prices cluster at $1–$7:
- Parallel: $1 (Turbo/Fast) and $5 (Basic/Advanced)
- Brave: $5
- Perplexity Search API: $5
- Tavily basic: $5–$8
- Exa: $7 with contents
- Google grounding: $14 per 1,000 on Gemini 3, and Google Custom Search is closing on January 1, 2027
- Claude's native web search: $10 per 1,000, plus tokens for the results

Every vendor listed now has an official MCP server, and Parallel, Exa, Firecrawl and Jina offer keyless or anonymous free tiers. The only independent benchmarks found (Artificial Analysis Search Index, and Openbenchmarks' company search, both August 2026) put Parallel, Exa, Brave (LLM Context) and You.com within about 1–2 points of each other at the top on general agentic search. On multi-constraint company discovery the spread is much wider (F1 of about 46 versus about 30). No published benchmark measures Portuguese queries or Brazilian sites for any of these vendors.

### Cited Findings

#### Pricing and free tiers (verified 2026-09-24; tag shows source type)

| API | List price | Free tier | Source |
|---|---|---|---|
| **Claude API web search** | $10 per 1,000 searches plus standard tokens for the returned content. Errors are not billed. | none | [D] [Claude docs: web search tool](https://platform.claude.com/docs/en/agents-and-tools/tool-use/web-search-tool) |
| **Claude API web fetch** | No extra charge, tokens only. An average 10 kB page is about 2,500 tokens; a 500 kB PDF about 125,000. | n/a | [D] [Claude docs: web fetch tool](https://platform.claude.com/docs/en/agents-and-tools/tool-use/web-fetch-tool) |
| **Parallel Search** | Turbo about 200 ms, $1/1k. Fast under 1 s, $1/1k. Basic about 1 s, $5/1k. Advanced about 3 s, $5/1k (default). 10 results included; extra results $1/1k. Extract $1/1k URLs. Task API $5–$2,400/1k runs. Responses $10–$250/1k. Monitor $3/1k. Default rate limit 600 req/min for Search and Extract. | $5/month in credits with a card on file (about 5,000 Turbo searches), plus a free keyless hosted MCP | [D, first-party content] [Parallel: Claude web search vs Parallel](https://github.com/parallel-web/parallel-llms-txt/blob/main/public/articles/claude-web-search-vs-parallel.md); [Parallel: free web search APIs](https://github.com/parallel-web/parallel-llms-txt/blob/main/public/articles/best-free-web-search-api.md) |
| **Exa** | Search $7/1k (10 results, contents included). Deep search $12/1k. Deep-reasoning $15/1k. Contents $1/1k pages. Answer $5/1k. Monitoring $15/1k. | $20 at signup plus $10/month, no card | [C, reported by Parallel] [Exa→Parallel migration](https://github.com/parallel-web/parallel-llms-txt/blob/main/public/articles/exa-to-parallel-search-api.md); [free tiers](https://github.com/parallel-web/parallel-llms-txt/blob/main/public/articles/best-free-web-search-api.md) |
| **Tavily** | Credits: basic search 1 credit, advanced 2. $0.008/credit pay-as-you-go. Project plan $30/month for 4,000 credits. Growth $500/month for 100,000 credits ($0.005/credit). That works out to $5–$8/1k basic and $10–$16/1k advanced. Extract about $4/1k. Research 4–250 credits. | 1,000 credits/month, no card | [C] [Tavily→Parallel migration](https://github.com/parallel-web/parallel-llms-txt/blob/main/public/articles/tavily-to-parallel-search-api.md) |
| **Perplexity** | Search API: flat $5/1k requests. Sonar: $1/M tokens plus $5–12/1k requests depending on search context. Sonar Pro: $3/$15 per M plus $6–14/1k. Sonar Reasoning Pro: $2/$8. Deep Research: $2/$8 plus citation tokens, reasoning tokens and $5/1k searches. Agentic Research API: web search $0.005/call and URL fetch $0.0005/call, with the model billed at its provider's rates. | not stated | [C] [Perplexity Search vs Parallel](https://github.com/parallel-web/parallel-llms-txt/blob/main/public/articles/perplexity-search-api-vs-parallel-search-api.md); [Sonar vs Parallel](https://github.com/parallel-web/parallel-llms-txt/blob/main/public/articles/perplexity-sonar-vs-parallel.md) |
| **Brave Search API** | Search $5/1k (web, LLM Context, news, video, image, place) at 50 requests/second. Answers $4/1k plus $5/M input and $5/M output tokens at 2 requests/second. The Summarizer is deprecated. | Free tier eliminated February 2026. Now $5/month credits (about 1,000 searches); card required; attribution required to claim the credit. | [C] [Brave vs Parallel](https://github.com/parallel-web/parallel-llms-txt/blob/main/public/articles/brave-search-api-vs-parallel.md); [free tiers](https://github.com/parallel-web/parallel-llms-txt/blob/main/public/articles/best-free-web-search-api.md) |
| **Firecrawl** | Yearly billing: Hobby $16 for 5k credits (5 concurrent), Standard $83 for 100k (50), Growth $333 for 500k (100), Scale $599 for 1M (150). No pay-as-you-go; credits do not roll over. Search is 2 credits per 10 results; scrape is 1 credit per page. | 1,000 credits/month, 2 concurrent requests, no card | [C] [Firecrawl vs Parallel](https://github.com/parallel-web/parallel-llms-txt/blob/main/public/articles/firecrawl-vs-parallel.md); [free tiers](https://github.com/parallel-web/parallel-llms-txt/blob/main/public/articles/best-free-web-search-api.md) |
| **Jina Reader / Search** | Token-metered, about $0.045–0.05 per M tokens on paid top-ups. `s.jina.ai` charges from 10,000 tokens per request. Failed requests are not charged. | 10M free tokens per new key. `r.jina.ai` also works with no key at a rate limit. | [C] [Jina vs Parallel](https://github.com/parallel-web/parallel-llms-txt/blob/main/public/articles/jina-ai-reader-vs-parallel.md); [D] [jina-ai/reader README](https://github.com/jina-ai/reader) |
| **SerpApi** | Starter $25 for 1,000/month. Developer $75 for 5,000. Production $150 for 15,000. Big Data $275 for 30,000. Searcher $725 for 100,000. | 250/month (50/hour throughput) | [C] [SerpApi vs Parallel](https://github.com/parallel-web/parallel-llms-txt/blob/main/public/articles/serpapi-vs-parallel.md) |
| **Vertex AI: Grounding with Google Search** | Gemini 3: 5,000 grounding queries/month free across models, then **$14 per 1,000 grounding queries**. Gemini 2.5 Pro: 10,000 grounding prompts/day free, then **$35 per 1,000 grounding prompts**. Billed only when the response includes at least one grounding URL; standard Gemini token fees also apply. | as stated | [D] [Google Cloud Vertex AI pricing](https://cloud.google.com/vertex-ai/generative-ai/pricing) |
| **Google Programmable Search (Custom Search JSON API)** | $5/1k beyond 100 free queries/day, hard cap 10,000/day. Closed to new customers; retires January 1, 2027. Google points users to Vertex AI Search (site search, up to 50 domains). | 100/day, existing customers only | [C] [Parallel: Google CSE alternative](https://github.com/parallel-web/parallel-llms-txt/blob/main/public/articles/the-best-google-custom-search-api-alternative-for-ai-agents.md), which cites [Google CSE overview](https://developers.google.com/custom-search/v1/overview) |

Other pricing notes:
- On Gemini 3, grounding is billed per search query the model runs, not per prompt. One prompt that searches three times is three billable uses, so "the multiplier is now unbounded and controlled by the model". [C] — [Gemini grounding vs Parallel](https://github.com/parallel-web/parallel-llms-txt/blob/main/public/articles/gemini-google-search-grounding-vs-parallel.md)
- Microsoft deprecated the Bing Search API on August 11, 2025. [C] — [Parallel: free web search APIs](https://github.com/parallel-web/parallel-llms-txt/blob/main/public/articles/best-free-web-search-api.md)
- Other options, from the same source [C]:
  - Serper: 2,500 free queries one-time, then from $0.30/1k (scraped Google SERP).
  - Linkup: 4,000 free queries at signup, then $5/month in credits; its benchmark harness is open-source.
  - SearXNG: self-hosted, no per-query cost.
- **Brave storage clause.** Storing results "in part or in whole, including for training or tuning a model" requires a plan that explicitly grants storage rights. That covers caching, vector stores, and audit logs. [C] — [Brave vs Parallel](https://github.com/parallel-web/parallel-llms-txt/blob/main/public/articles/brave-search-api-vs-parallel.md)

#### Official MCP servers (all [D] from each vendor's official GitHub README, read 2026-09-24)
- **Exa.** Hosted at `https://mcp.exa.ai/mcp`, and works anonymously at rate limits; OAuth or an API key raises limits and unlocks Exa Agent. The default tool is `web_search_exa`. Optional tools: `web_search_advanced_exa` (domain and date filters, subpage crawl), `web_fetch_exa`, and `agent_run` (multi-step research). — [exa-labs/exa-mcp-server](https://github.com/exa-labs/exa-mcp-server)
- **Tavily.** Remote server at `https://mcp.tavily.com/mcp/` with an API key or OAuth. Tools: search, extract, map, crawl. `DEFAULT_PARAMETERS` can set, for example, `search_depth` and `max_results`. — [tavily-ai/tavily-mcp](https://github.com/tavily-ai/tavily-mcp)
- **Perplexity.** Hosted at `https://api.perplexity.ai/mcp` with a Bearer key. Tools:
  - `perplexity_search`: Search API, with `search_recency_filter` and `search_domain_filter`.
  - `perplexity_ask`: Agent API "fast" preset.
  - `perplexity_research`: "high" preset, which can run for minutes.
  - The legacy `sonar-pro`, `sonar-reasoning-pro` and `sonar-deep-research` models have been replaced by Agent API presets in this server. — [perplexityai/modelcontextprotocol](https://github.com/perplexityai/modelcontextprotocol)
- **Brave.** An official server that runs locally by default over STDIO, with HTTP optional. Tools: `brave_web_search`, `brave_local_search` (full use needs Pro), video, image, news, `brave_summarizer`, `brave_place_search`. Parameters include `country` (default US), `search_lang` (default en) and `ui_lang` (default en-US). `extra_snippets` requires a Pro plan. I saw no hosted URL in the README. — [brave/brave-search-mcp-server](https://github.com/brave/brave-search-mcp-server)
- **Firecrawl.** Hosted keyless free tier at `https://mcp.firecrawl.dev/v2/mcp`: scrape, search and parse work without a key but are rate-limited. Crawl, map and agent need a key or OAuth (`/v2/mcp-oauth`). The full profile has 26 tools, including credit-usage and monitor tools, and the server can be self-hosted. — [firecrawl/firecrawl-mcp-server](https://github.com/firecrawl/firecrawl-mcp-server)
- **Jina.** Hosted at `https://mcp.jina.ai/v1`. `read_url` (web page or PDF to markdown) works without a key at rate limits; `search_web` requires a key. Tools can be filtered with `include_tags=search,read`, and `max_tokens` caps `read_url` output. — [jina-ai/MCP](https://github.com/jina-ai/MCP)
- **Parallel.** Free keyless hosted Search MCP at `https://search.parallel.ai/mcp` with tools `web_search` and `web_fetch`. No account or key is needed; it is meant for personal and hobby use. The README includes `claude mcp add --transport http --scope project parallel-search https://search.parallel.ai/mcp`. [D] — [parallel-web/search-mcp](https://github.com/parallel-web/search-mcp). Per Parallel, `web_search` runs Basic mode, `web_fetch` handles JavaScript-heavy pages and PDFs, and output is capped at about 25,000 characters per call. [first-party] — [Parallel: free web search APIs](https://github.com/parallel-web/parallel-llms-txt/blob/main/public/articles/best-free-web-search-api.md)
- **SerpApi.** Hosted at `https://mcp.serpapi.com/mcp` with a Bearer key. One `search` tool covers every engine (Google, Bing, Yahoo, DuckDuckGo, YouTube, eBay and more), and engine parameter schemas are exposed as MCP resources. — [serpapi/serpapi-mcp](https://github.com/serpapi/serpapi-mcp)
- **Jina Reader (not MCP).**
  - `r.jina.ai/<url>` converts a URL to LLM-friendly markdown, PDFs included.
  - `s.jina.ai/<query>` searches, then fetches and converts the top 5 results.
  - `x-max-tokens` and `x-token-budget` headers control cost.
  - The code is open source. — [jina-ai/reader README](https://github.com/jina-ai/reader)
- **Google (Vertex grounding).** No MCP server was checked in this session.

#### Benchmarks: INDEPENDENT (both reported through Parallel's write-ups; the original sites were blocked)
- **Artificial Analysis Search Index** (August 2026, with a September 8 2026 snapshot checked September 22).
  - Method: a fixed agent harness (GPT-5.6 Luna) in which only the search API varies. The composite score is the equal-weighted mean of DeepSearchQA F1, BrowseComp accuracy and AA-Omniscience accuracy.
  - Scores: Parallel Advanced 75, Brave LLM Context 75, You.com (highlights) 74, Exa (auto) 74, Parallel Fast 73, Parallel Turbo 67.
  - Combined model-plus-search cost per 1,000 tasks: Parallel Advanced $83.51, Brave LLM Context $129.53, Parallel Fast $68.08. Parallel Fast had the lowest search-only cost, $8.41 per 1,000 tasks.
  - Latency: Brave about 19 s per task, Parallel Advanced 38 s, Parallel Fast about 16 s.
  - Sources: [Brave vs Parallel](https://github.com/parallel-web/parallel-llms-txt/blob/main/public/articles/brave-search-api-vs-parallel.md); [free tiers](https://github.com/parallel-web/parallel-llms-txt/blob/main/public/articles/best-free-web-search-api.md); [Parallel blog on AA](https://github.com/parallel-web/parallel-llms-txt/blob/main/public/blog/artificial-analysis-best-search-api.md); original: [artificialanalysis.ai/agents/search-api](https://artificialanalysis.ai/agents/search-api)
  - **Conflict:** one Parallel post says "15 search API products from 7 providers", another says "across 12 providers". Tavily, Perplexity and Firecrawl scores were not given in the posts I read.
- **Openbenchmarks multi-turn company search** (first published August 22 2026, last run August 28 2026).
  - Method: a fixed agent (gpt-5.6-sol, medium effort) answers 45 hand-labelled questions that combine 3–4 constraints (investors, accelerator, **headquarters geography**, founding era, funding). It gets up to 8 turns, 14 searches and 10 results per search. Harness, scoring and raw responses are published under CC-BY.
  - **Search-only F1:** Parallel basic 46.5 (precision 88.7), Exa deep 45.4, Parallel advanced 44.2, Exa instant 43.3, Linkup and Tavily about 41, Firecrawl and Brave about 30, Seltz 14.5, a Google SERP feed through RapidAPI 0.4.
  - **Search-plus-fetch F1:** Exa deep 48.2, Exa instant 44.9, Parallel basic 42.3, Parallel advanced 42.2, Linkup 42.0 (precision 90.7).
  - Sources: [Parallel: best API for company research](https://github.com/parallel-web/parallel-llms-txt/blob/main/public/articles/best-api-for-company-research.md); original: [openbenchmarks.com](https://openbenchmarks.com/multi-turn-company-search)

#### Benchmarks: VENDOR-RUN (labelled by who ran them)
- **Parallel** (evals run September 9, 2026, with the same GPT-5.6 Sol agent at the frontier tier and Luna at the low-cost tier for every provider; LLM-judge grading) — [Parallel benchmarks page](https://github.com/parallel-web/parallel-llms-txt/blob/main/public/benchmarks.md):
  - **SimpleQA Verified, n=100.** Parallel Fast 94% at $2 per 1,000 questions, Basic and Advanced 97%. Perplexity 94% (low-cost) and 95% (frontier). Tavily 94% and 92%. Exa Auto 91% at both tiers.
  - **BrowseComp, n=50.** Parallel Advanced 74% at $399/1k. Perplexity frontier 74% at $275/1k. Exa Auto frontier 70% at $971/1k. Tavily frontier 66% at $935/1k. Low-cost tier: Perplexity 46%, Parallel Fast 44%, Exa 36%, Tavily 32%.
  - **WideSearch, n=100, partial credit.** Parallel Advanced 57.6. Exa and Tavily frontier 55.9. Perplexity frontier 53.5.
- **Parallel single-step SimpleQA** (July 10–12, 2026): Parallel Turbo 91, Exa Instant 89.3, Brave 87, SerpAPI 76.7, Tavily Ultra Fast 72. [C/vendor-run] — [Parallel: best fast search APIs](https://github.com/parallel-web/parallel-llms-txt/blob/main/public/articles/best-fast-search-apis.md)
- **Firecrawl self-reported:** SimpleQA 94.7% with a GPT-5.4 agent making up to 20 tool calls (/search plus scrape), July 2026. Parallel notes this setup is not comparable with its own single-step setup. [C/vendor-run] — [Firecrawl vs Parallel](https://github.com/parallel-web/parallel-llms-txt/blob/main/public/articles/firecrawl-vs-parallel.md)
- **Perplexity `search_evals`** (open-source MIT harness, published by Perplexity Research). It compares end-to-end agent or deep-research systems, not raw search endpoints. [D] — [perplexityai/search_evals](https://github.com/perplexityai/search_evals)

| Benchmark | Perplexity | OpenAI | Anthropic (Managed Agents) | Exa | Parallel |
|---|---|---|---|---|---|
| DeepSearchQA (dsqa) | 0.871 | 0.733 | 0.815 | 0.53 | 0.81 |
| BrowseComp | 0.805 | 0.720 | 0.598 | 0.38 | 0.56 |
| HLE | 0.612 | 0.614 | 0.566 | 0.387 | 0.515 |
| WideSearch | 0.651 | 0.522 | 0.590 | 0.471 | 0.584 |

- **Parallel Task API** (deep research; tested August 26 2026 on the same 100-question subset for everyone): BrowseComp 88–94% for Parallel Lite through Ultra4x, Perplexity high 86%, GPT-5.6 Sol PTC max 85%, Exa Agent Max 78%, Gemini 3.1 Pro high 72%. [vendor-run] — [Parallel benchmarks page](https://github.com/parallel-web/parallel-llms-txt/blob/main/public/benchmarks.md)
- The vendor-run tables disagree with each other. Perplexity's own harness puts Parallel's agent at 0.56 on BrowseComp, while Parallel's harness puts Parallel's Task API at 88–94%. Configurations and question subsets differ between the two. — [search_evals](https://github.com/perplexityai/search_evals); [Parallel benchmarks](https://github.com/parallel-web/parallel-llms-txt/blob/main/public/benchmarks.md)

#### Portuguese and Brazil coverage (evidence found)
- **Brave.** The MCP exposes `country`, `search_lang` and `ui_lang` on web, news, video and image search (defaults US, en, en-US), so `country=BR, search_lang=pt-br` style targeting is possible. [D] — [brave/brave-search-mcp-server](https://github.com/brave/brave-search-mcp-server)
- **SerpApi.** Supports every SerpApi engine with engine-specific parameters, including Google's (for example, country and language). The parameter schemas are exposed as MCP resources. [D] — [serpapi/serpapi-mcp](https://github.com/serpapi/serpapi-mcp)
- **Claude API web search.** Accepts `user_location` with a two-letter ISO country code, and rejects unsupported codes with a 400. Which countries are supported is not listed. [D] — [Claude docs: web search tool](https://platform.claude.com/docs/en/agents-and-tools/tool-use/web-search-tool)
- **Perplexity.** The Search API has language and recency filters. [C] — [Perplexity Search vs Parallel](https://github.com/parallel-web/parallel-llms-txt/blob/main/public/articles/perplexity-search-api-vs-parallel-search-api.md)
- **Jina Reader.** Lets you set locale and referer per request. [C] — [Jina vs Parallel](https://github.com/parallel-web/parallel-llms-txt/blob/main/public/articles/jina-ai-reader-vs-parallel.md)
- **Openbenchmarks.** Its company-search questions include "headquarters geography" constraints, but no results broken down by geography or language were reported. [C] — [Parallel: company research](https://github.com/parallel-web/parallel-llms-txt/blob/main/public/articles/best-api-for-company-research.md)

### Inferences
- **Parallel**: the free keyless MCP plus $5/month in credits, and $1 per 1,000 on Turbo/Fast, make it the lowest-cost AI-native option. It also leads or ties on both independent boards, although most of the supporting evidence comes from Parallel itself.
- **Exa**: the anonymous hosted MCP, $10/month in free credits (competitor-reported) and the top search+fetch score on Openbenchmarks company discovery make it the strongest fit for the arbitrage task "find companies abroad with constraints X/Y/Z".
- **Tavily**: 1,000 free credits a month with no card is safe for prototyping. It is mid-pack on the independent company board, so there is no quality reason to prefer it over Exa or Parallel.
- **Perplexity**: Search API at $5 per 1,000 is fine for search. Its Agent API or MCP (`perplexity_research`) is a strong, pricier deep-research option; the best BrowseComp and DSQA scores come from its own harness only.
- **Brave**: its own independent index, explicit country and language parameters, and a tie for first on the AA index. However, the free tier is gone, a card is required, and there is a storage-rights clause, which matters if the harness caches results.
- **Firecrawl**: its keyless MCP (scrape, search, parse) is a good free fallback for JS-heavy or blocked pages. As a search provider it is weak on company discovery (about 30 F1).
- **Jina Reader**: `r.jina.ai` with no key is the cheapest way to get raw full-page markdown when Claude Code's WebFetch summarisation is too lossy.
- **SerpApi**: best when you need Google-exact SERP structure (Google Brazil rankings, Shopping, local pack). Its 250 free searches a month and $25+ plans are costly per useful answer, and it scored 76.7% on single-step SimpleQA, a Parallel-run test.
- **Google Programmable Search**: do not build on it, because it retires January 1, 2027 and is closed to new customers. **Vertex grounding** at $14 per 1,000 Gemini 3 queries only makes sense if the harness runs on Gemini.
- **On the benchmarks themselves**: the BrowseComp samples are small (n=50 in Parallel's table), which gives roughly ±14 percentage points of 95% uncertainty at p≈0.5 (my calculation). Differences of a few points between the top providers are within noise. The independent AA index shows the top four within 2 points, so for a solo founder, cost and locale control should decide the choice more than leaderboard rank.
- **On Portuguese coverage**: none of the vendors publishes Portuguese-query or Brazilian-site results. The only way to learn this is to measure it: run the harness's own 30–50 PT-BR queries through two or three free-tier MCPs.

### Gaps
- **Direct confirmation of vendor pricing pages** (exa.ai/pricing, tavily.com/pricing, docs.perplexity.ai pricing, brave.com/search/api, firecrawl.dev/pricing, jina.ai, serpapi.com/pricing, parallel.ai/pricing): blocked by the egress proxy. Competitor-reported figures above need checking before any purchase.
- **Independent benchmark originals** (Artificial Analysis, Openbenchmarks): not accessible, so I could not check the full tables, the Tavily, Perplexity and Firecrawl scores, or the exact provider count.
- **Portuguese or Brazilian-site quality for any vendor**: no published benchmark or independent evaluation found. Whether Exa's embedding index, Tavily and Parallel expose country or language parameters was not verified.
- **Tavily's and Exa's own vendor benchmarks**, and their exact numbers: not retrieved.
- **Google Vertex AI Search** (the replacement for Programmable Search): open-web pricing and availability not verified. Parallel says open-web use goes through a contact form.
- **An empirical PT-BR probe**: not possible here. The keyless MCP endpoints (search.parallel.ai, mcp.exa.ai, mcp.firecrawl.dev, mcp.jina.ai) were unreachable from this sandbox.

---

## Key Question 3 — What Claude Code's native WebSearch and WebFetch can and cannot do, and when a paid API measurably improves agentic research

### Takeaway
Claude Code's WebSearch returns only titles and URLs, from Anthropic's search backend, which is not configurable. It runs up to 8 backend searches per call, supports allow and block domain lists, has no locale or country parameter in Claude Code, and is capped at 200 calls per session across all subagents.

WebFetch is "lossy by design". A small, fast model answers your prompt against a truncated markdown conversion of the page, so Claude never sees the raw page. It has a 15-minute cache and does not follow cross-host redirects.

I found no independent benchmark that isolates Claude's native search against Exa, Tavily or Parallel with the agent held constant. The only head-to-head is Perplexity's vendor-run end-to-end comparison, where Anthropic Managed Agents score 0.598 on BrowseComp against Perplexity's 0.805. Anthropic's own analysis attributes 80% of BrowseComp variance to token usage, not to the search provider.

A paid or specialized API should measurably help in five situations:
1. Raw results you can store and deduplicate.
2. Locale control for PT-BR/BR.
3. Large parallel fan-outs beyond the 200-search cap.
4. Full-page or JavaScript extraction.
5. Multi-constraint company discovery, where independent boards show large gaps between providers.

### Cited Findings

**Claude Code WebSearch (CLI tool)** [D] — [Claude Code tools reference](https://code.claude.com/docs/en/tools-reference)
- It "runs a query against Anthropic's web search backend and returns result titles and URLs. It doesn't fetch the result pages". Reading a result needs a follow-up WebFetch.
- It "may issue up to eight backend searches per call". `allowed_domains` or `blocked_domains` can be set, but not both.
- "The search backend is not configurable. To search with a different provider, add an MCP server that exposes a search tool."
- **Session cap.** At most 200 WebSearch calls per session, counted across the main conversation and every subagent (v2.1.212+). You can raise it with `CLAUDE_CODE_MAX_WEB_SEARCHES_PER_SESSION` but not turn it off; `/clear` resets it. Capped calls look like searches that did nothing.
- Available on the Claude API and Claude Platform on AWS. On Microsoft Foundry it needs an Anthropic-hosted deployment. It works on Google Cloud's Agent Platform with Claude 4+. It is not available on Amazon Bedrock.
- **Observed in this session** [own observation]:
  - The WebSearch tool schema offers only `query`, `allowed_domains` and `blocked_domains`, and describes itself as "US-only". There is no `user_location` or country parameter, unlike the API tool.
  - The shared 200-search cap was hit partway through this research (parallel researchers share the budget), and later searches returned a "budget used" notice.

**Claude Code WebFetch (CLI tool)** [D] — [Claude Code tools reference](https://code.claude.com/docs/en/tools-reference)
- It "fetches the page, converts the response to Markdown ... and runs the prompt against the content using a small, fast model. For most fetches, Claude receives that model's answer, not the raw page." The docs call it "lossy by design". A result saying a page doesn't mention X "may only mean the prompt didn't ask about it". For the raw page, the docs point to `curl` via Bash.
- Other behaviour:
  - Large pages are truncated to a fixed character limit before processing.
  - Responses are cached for 15 minutes by default (`CLAUDE_CODE_WEBFETCH_CACHE_TTL_MS` changes this on v2.1.233+).
  - A page gets a 5-minute deadline (`CLAUDE_CODE_WEBFETCH_DEADLINE_MS` on v2.1.268+).
  - Redirects to a different host come back as a notice instead of being followed.
  - HTTP is upgraded to HTTPS, and localhost and hosts without a dot are refused.
  - The User-Agent starts with `Claude-User`, and the Accept header prefers Markdown.
  - Every fetch passes a domain safety check. Permission prompts apply in Manual and acceptEdits modes; a built-in set of documentation domains is preapproved.
- **Observed in this session** [own observation]: in this cloud sandbox, both WebFetch and curl were blocked by the environment's egress proxy for most vendor domains. That is an environment network policy, not a WebFetch limit, but it matters for cloud-run harnesses.

**Claude API server tools (what the same backend offers when called directly)** [D]
- **Web search** — [Claude docs: web search](https://platform.claude.com/docs/en/agents-and-tools/tool-use/web-search-tool):
  - Versions: `web_search_20250305` (basic), `web_search_20260209` (adds dynamic filtering, where Claude writes code to filter results before they enter context; Claude 4.6+), and `web_search_20260318` (adds `response_inclusion`).
  - `max_uses`, allow and block domain lists, and `user_location` (city, region, ISO country, timezone).
  - Each result has `url`, `title`, `page_age` and `encrypted_content`, which must be passed back unchanged. Citations are always on, with `cited_text` up to 150 characters.
  - $10 per 1,000 searches. The Batches API throttles searches per organisation. Not available on Bedrock.
- **Web fetch** — [Claude docs: web fetch](https://platform.claude.com/docs/en/agents-and-tools/tool-use/web-fetch-tool):
  - It can only fetch URLs that already appeared in the conversation (user messages, client tool results, or earlier search/fetch results).
  - "Does not support websites dynamically rendered with JavaScript". PDFs are supported.
  - `max_content_tokens` caps what enters context. `use_cache: false` (v20260309+) bypasses the cache.
  - URLs are limited to 250 characters. Blocks for `robots.txt`, private addresses and similar return `url_not_allowed`.
  - Only text, HTML and PDF are supported, and there is no charge beyond tokens.

**Evidence comparing native and specialized search**
- **VENDOR-RUN (Perplexity).** Anthropic Managed Agents score BrowseComp 0.598, DSQA 0.815, HLE 0.566 and WideSearch 0.590. Perplexity's Agent API scores 0.805, 0.871, 0.612 and 0.651; OpenAI 0.720, 0.733, 0.614 and 0.522; Parallel 0.56, 0.81, 0.515 and 0.584; Exa 0.38, 0.53, 0.387 and 0.471. These are whole systems (model, search and orchestration), not search tools compared alone. [D] — [perplexityai/search_evals](https://github.com/perplexityai/search_evals)
- **Anthropic (first-party engineering post, June 13, 2025)** [D] — [Anthropic: How we built our multi-agent research system](https://www.anthropic.com/engineering/multi-agent-research-system):
  - A multi-agent setup (Opus 4 lead, Sonnet 4 subagents) scored "90.2% improvement over single-agent Claude Opus 4" on an internal research eval.
  - On BrowseComp, three factors explained 95% of variance, and "token usage by itself explains 80%". The others are the number of tool calls and model choice.
  - Agents use about 4× the tokens of chat; multi-agent systems about 15×.
  - Early agents "consistently chose SEO-optimized content farms over authoritative but less highly-ranked sources", which was fixed with source-quality heuristics in the prompt.
- **Parallel (vendor-authored comparison)** [first-party/C] — [Parallel: Claude web search vs Parallel](https://github.com/parallel-web/parallel-llms-txt/blob/main/public/articles/claude-web-search-vs-parallel.md):
  - With a server-side tool, results "land inside Claude's context". "You cannot route the results to a different model, cache them in your own store, or index them".
  - Search is tied to inference, so a pure retrieval job still pays for a model turn.
  - Claude's search costs $10 per 1,000, against Parallel's $1–5.
- **Parallel's benchmarks page** describes itself as comparing against "Exa, Tavily, Brave, OpenAI, and Claude search", but the current (September 9, 2026) tables do not include a Claude-search row. [D] — [Parallel benchmarks](https://github.com/parallel-web/parallel-llms-txt/blob/main/public/benchmarks.md)
- **Independent company-discovery board.** Provider choice changes F1 from about 46 (Parallel basic, Exa deep) to about 30 (Brave, Firecrawl) to 0.4 (a Google SERP feed through RapidAPI), with the agent held constant. Claude native search was not on the board. [C] — [Parallel: company research](https://github.com/parallel-web/parallel-llms-txt/blob/main/public/articles/best-api-for-company-research.md)

### Inferences
- **Native WebSearch**: good for discovery (finding URLs) at no extra setup cost. It cannot return page content, cannot target Brazil or Portuguese locale except through the query wording, and shares a 200-call budget with every subagent. Wide fan-out research will hit the cap, as this session did.
- **Native WebFetch**: fine for "extract fact X from page Y". It is unreliable for quoting or completeness checks, because the summariser sees a truncated page and answers only your prompt, and it does not render JavaScript (inferred from the API tool's docs and plain HTTP fetching). Use `curl`, `r.jina.ai` or the Firecrawl or Parallel fetch tools for raw or JS-heavy pages such as app stores, marketplaces and SPA pricing pages.
- **When a paid or specialized API measurably helps**, in rough order of evidence strength:
  1. **Company or entity discovery with constraints** (the core arbitrage query). The independent board shows a spread of 15+ F1 points between providers, so adding Exa or Parallel MCP is justified.
  2. **Scale.** More than 200 searches per session, or deduplicated monitoring, needs results as data.
  3. **Locale.** Brave or SerpApi `country=BR` and `lang=pt` give Brazilian-market SERPs that Claude Code cannot request.
  4. **Extraction.** JS-heavy pages and full-text quoting.
  5. **Deep research tasks.** Perplexity- and Parallel-run tables suggest gains, but only vendor-run data exists.
- **Cost for a solo founder**: layering the keyless or free-tier MCPs (Parallel, Exa, Firecrawl, Jina) on top of native search adds almost no cost. Paying only starts to matter at thousands of searches a month, where Parallel Turbo/Fast at $1 per 1,000 or the Perplexity Search API at $5 per 1,000 beats Claude's $10 per 1,000 (API billing).
- **What moves quality most**: Anthropic's own analysis says token budget and the number of tool calls explain most BrowseComp variance. Harness design (fan-out, source-quality heuristics, fetch depth) probably matters more than swapping providers for general research. A provider swap matters most on narrow entity-discovery and locale-bound tasks.

### Gaps
- **Head-to-head evidence**: no independent evaluation found that compares Claude Code's native WebSearch or WebFetch (or the API `web_search` tool) with Exa, Tavily, Parallel or Brave with the agent held constant.
- **The search index behind Claude's native search**: not documented in the pages I read ("Anthropic's web search backend"). Its quality on Portuguese and Brazilian sites is unknown.
- **The meaning of "US-only"** in the Claude Code WebSearch tool description (availability, or result locale): not clarified in the docs I read.
- **WebFetch's exact truncation limit** (character count) and which model it uses: the docs say only "fixed character limit" and "small, fast model".
- **Cost of WebSearch in Claude Code on subscription plans**, as opposed to API billing at $10 per 1,000: not verified.
- **Dates for the Perplexity `search_evals` results table**: the README does not give run dates or configurations. The repo was last updated September 21, 2026.
