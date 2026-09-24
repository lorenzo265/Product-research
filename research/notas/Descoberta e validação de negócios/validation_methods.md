# Business-idea validation methods and the evidence behind their decision thresholds

Research date: 2026-09-24. **How this was verified:** full-text fetches were blocked by the egress proxy for every publisher and vendor domain tried: Unbounce, Strategyzer, SSRN, ScienceDirect, Springer, Wiley, SAGE, arXiv, CEPR, gwern, MeasuringU, Wikipedia and evanmiller.org. The session's web-search budget also ran out partway through. Verification therefore rests on search-engine result text.

- **[V]** means the content was confirmed this session in search-result text, either from the source itself or from a secondary source that summarises it.
- **[K]** means the claim comes from the cited work as I remember it and was **not re-verified this session**. The report writer should soften these or check them before quoting the numbers.
- **[Calc]** means I computed it (exact binomial, Wilson intervals, Wald SPRT, Beta-Binomial). The results can be reproduced.

Source-type codes:

- **PR-MA:** peer-reviewed meta-analysis or systematic review.
- **PR:** peer-reviewed study.
- **Book:** practitioner book or author's primary material.
- **VB:** vendor benchmark with a disclosed dataset.
- **VBlog:** vendor or consultant content marketing with an undisclosed method.
- **PH:** practitioner heuristic.

Every bullet ends with **→ Gate:**, a one-line implication for the harness's buyer-test gates.

## 1. Interview methods: Mom Test, customer development, JTBD switch interviews (protocols, sample sizes, evidence)

### Takeaway
Interviews produce "say" evidence, the weak kind. They are the right tool for discovering problems and jobs, not for validating demand. Empirical saturation research gives these planning numbers:

- **9–17 interviews** for a homogeneous segment with a narrow aim (systematic review).
- About **12 interviews** to capture about 90% of codes.
- **20–30 interviews** to capture 90–95% of needs in a consumer-product context.

No study validates The Mom Test or switch interviews themselves as predictors of venture success. The best causal evidence is indirect. RCTs in Italy show that teaching founders to state hypotheses and run tests against explicit criteria raises performance and makes founders more willing to kill bad ideas.

### Cited Findings
**Protocols (practitioner primary material)**
- **Mom Test (Fitzpatrick) [K].** The protocol:
  - Talk about the customer's life, not your idea.
  - Ask about specific past behaviour, not generic or future hypotheticals.
  - Talk less and listen more.
  - Compliments, "fluff" (generic, hypothetical or future claims) and feature ideas count as bad data.
  - A meeting counts only if it ends in a **commitment** (time, reputation or money) or an **advancement** to a concrete next step.

  Source: [The Mom Test](https://www.momtestbook.com/). *Type: Book/PH; not geography-specific; B2B and B2C.* **→ Gate:** Score interviews only on past-behaviour facts plus commitments. "Would you buy?" scores 0, which matches the ladder's opinion rung. The ladder has no **reputation** rung (an intro to the boss or a colleague, or a public endorsement), which is Fitzpatrick's third currency.
- **Customer Development (Blank) [K].** It has four steps: customer discovery, customer validation, customer creation and company building ("get out of the building"). Blank's "earlyvangelists" meet five tests:
  - They have the problem.
  - They know they have it.
  - They are actively searching for a solution.
  - They have cobbled together a workaround.
  - They have, or can get, a budget.

  Source: [Steve Blank](https://steveblank.com/) (*The Four Steps to the Epiphany*). *Type: Book/PH; US; mainly B2B.* **→ Gate:** Use the earlyvangelist traits as the operational definition of a "qualified" interviewee or visitor. In B2B, count commitments only from budget-holders.
- **JTBD switch interview (Moesta/Spiek) [V, secondary].** Interview recent buyers or switchers. Reconstruct the timeline: first thought → passive looking → active looking → deciding → consuming. Code four forces: push, pull, anxiety of the new and habit of the present. Sources: [Gavel summary of Moesta's switch interview](https://usegavel.com/bob-moesta/switch-interview); [jobstobedone.org (Moesta & Spiek)](https://jobstobedone.org/). *Type: PH; US-origin; B2B and B2C.* **→ Gate:** Switch interviews need people who *recently bought something in the category*. That makes them a natural screen for whether the category has real past purchase behaviour.
- **Switch-interview sample size [V, secondary].** Moesta interviews about **10 recent buyers**. He claims 10 interviews reveal 3–5 buying patterns covering "90% of the market". Secondary guides say patterns start to emerge after 5–6 interviews and 10–15 give confidence. Sources: [SaaS Club podcast with Moesta, "10 Customer Interviews…"](https://saasclub.io/podcast/jobs-to-be-done-bob-moesta-423/); [Koji JTBD guide](https://www.koji.so/blog/jobs-to-be-done-interview-guide-2026). *Type: PH; the "90%" claim has no published data behind it that I could find.* **→ Gate:** 10 switch interviews per segment is a reasonable plan, but label it as a heuristic.

**Sample size and saturation (empirical)**
- **Hennink & Kaiser 2022 [V].** A systematic review of **23 empirical tests** of saturation. Saturation came within **9–17 interviews** or **4–8 focus groups**, for relatively homogeneous populations with narrow aims. Broader aims, heterogeneous populations and "meaning"/theoretical saturation needed larger samples. The authors present these as planning priors, not rules. Source: [Social Science & Medicine 292:114523](https://www.sciencedirect.com/science/article/pii/S0277953621008558); [RePEc](https://ideas.repec.org/a/eee/socmed/v292y2022ics0277953621008558.html). *Type: PR-MA; mostly health and social research, mixed geography; not B2B.* **→ Gate:** Plan at least 10–12 interviews per *homogeneous* segment, and 15–20+ if the segment mixes roles or company sizes.
- **Guest, Bunce & Johnson 2006 [K].** 60 in-depth interviews (women in Ghana and Nigeria). About 92% of codes (roughly 100 of 109) had appeared by interview 12, about 73% by interview 6, and the high-level metathemes were present by 6. Source: [Field Methods 18(1):59–82](https://doi.org/10.1177/1525822X05279903). *Type: PR; West Africa; non-commercial topic.* **→ Gate:** "12 interviews" is the most-cited empirical anchor. About 6 interviews surface the main themes, which is enough to decide which hypotheses to test behaviourally.
- **Guest, Namey & Chen 2020 [K].** An operational stopping rule: take a base set of interviews (e.g., 4), then a run of 2–3 further interviews, and stop when the run adds ≤5% new information (codes) relative to the base. Source: [PLOS ONE 15(5)](https://doi.org/10.1371/journal.pone.0232076). *Type: PR (method paper).* **→ Gate:** The harness can encode this rule: stop interviewing a segment when the last 3 interviews add ≤5% new codes.
- **Griffin & Hauser 1993 [V].** **20–30 interviews** are needed to identify **90–95% of customer needs**. One-on-one interviews are more cost-effective than focus groups, and several analysts should read and interpret the transcripts. Source: [Marketing Science 12(1):1–27 (MIT copy)](https://mitsloan.mit.edu/shared/ods/documents?PublicationDocumentID=5259); [Semantic Scholar](https://www.semanticscholar.org/paper/The-Voice-of-the-Customer-Griffin-Hauser/f4df2cca4a54f7ff240afc80967f552464872823). *Type: PR; US; B2C consumer-product context [K on the product].* **→ Gate:** Use 20–30 when the goal is to map needs broadly, not just find the top pain. Code transcripts with ≥2 independent analysts, such as two independent LLM coding passes plus reconciliation.

**Evidence that structured customer learning works**
- **Camuffo, Cordova, Gambardella & Spina 2020 (RCT) [V].**
  - Design: **116 Italian startups**, about 1 year, 16 data points. Both arms received 10 training sessions on getting market feedback. Only the treatment arm was taught to build theories, state hypotheses and test them rigorously "as scientists do".
  - Result: the scientific approach produced better outcomes.
  - [K]: treated firms earned more revenue and were more likely to terminate or pivot.

  Source: [Management Science 66(2)](https://pubsonline.informs.org/doi/10.1287/mnsc.2018.3249); [SSRN](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3295625). *Type: PR (RCT); Italy; mixed B2B/B2C early-stage.* **→ Gate:** This is the strongest causal support for the gate *process*: pre-stated hypotheses plus tests with explicit pass criteria. It does not support any specific numeric threshold.
- **Camuffo et al. 2024 replication [V].** **759 firms across four RCTs.** The treatment had a positive effect on **idea termination** and a non-linear effect on radical pivots: treated firms made a few pivots rather than none or many. They also searched for viable ideas more efficiently. Source: [Strategic Management Journal](https://sms.onlinelibrary.wiley.com/doi/full/10.1002/smj.3580). *Type: PR (RCTs); geography not confirmed this session.* **→ Gate:** A KILL is a success outcome. Track the harness's kill rate and time-to-kill, not only its GO decisions.
- **Koning, Hasan & Chatterji 2022 [K].** Tech startups that adopted A/B testing grew page visits more, launched more products, and were more likely to end up in the tails (both failure and scale). Source: [Management Science](https://doi.org/10.1287/mnsc.2021.4209). *Type: PR (observational panel; global web startups).* **→ Gate:** Experimentation raises the variance of outcomes. Pair cheap tests with quick kills.

### Inferences
- Use interviews to generate and rank hypotheses, then send them to behavioural tests. Do not use interviews as GO evidence. Default plan: 10–15 interviews per homogeneous segment with the ≤5%-new-codes stopping rule, or 20–30 when mapping all needs.
- In B2B, and especially in Brazil where buyer roles vary with company size, a "segment" should be role × company-size band × vertical. Each cell is its own saturation pool, so pooling across cells will under-sample.
- The Mom Test's commitment currencies map onto the ladder: time → call or meeting; money → deposit or order. **Reputation** (an intro to the decision-maker, or a named reference) is missing and would be a natural B2B rung between "meeting" and "deposit".

### Gaps
- No peer-reviewed study compares the predictive validity of Mom-Test or switch interviews with other interview styles.
- Saturation evidence comes almost entirely from health and social science. I found no saturation study of B2B buyers.
- Fitzpatrick's own numeric guidance on how many conversations to hold (if he gives one) was not verified.
- I recall that NSF I-Corps requires about 100 customer-discovery interviews per team, and I did not verify it. I did not retrieve I-Corps outcome data or Leatherbee & Katila's lean-startup study.

## 2. Smoke tests, fake doors, landing pages: benchmarks, B2B vs B2C, sample sizes, ethics

### Takeaway
The only large benchmark with a disclosed dataset is Unbounce 2024: 41k pages, 464M views and 57M conversions. It puts the median landing-page conversion at **6.6% across industries** and **3.8% for SaaS**, the lowest industry. Waitlist-specific numbers come only from vendor blogs with no stated method:

- Signup from cold traffic: typically 2–5%, best pages 8–20%.
- Waitlist → paid: 5–25%, falling sharply as the wait gets longer.

**No source links a landing-page signup rate to later business success**, so all signup thresholds are heuristics set against these benchmarks. Statistically, 1,000 visitors is more than enough to separate 5% from 8%. It is too few to separate a 0.5% pre-order rate from a 1% one.

### Cited Findings
- **Unbounce Conversion Benchmark Report 2024 (all industries) [V].** Median conversion is **6.6%**. The data covers 41,000 landing pages, 464M pageviews and 57M conversions. Sources: [Unbounce benchmark hub](https://unbounce.com/conversion-benchmark-report/); [Unbounce "What's a good conversion rate?"](https://unbounce.com/landing-pages/whats-a-good-conversion-rate/). *Type: VB, with vendor bias: Unbounce sells a landing-page builder. The pages belong to paying customers, often existing brands running paid traffic, and "conversion" means any page goal (form fill or click-through). Geography is not stated in the retrieved text; I infer the customer base leans North American. B2B and B2C mixed.* **→ Gate:** This is a generic landing-page benchmark, not a benchmark for smoke tests of unknown products. Use it only as a prior.
- **Unbounce 2024, SaaS [V].** SaaS median is **3.8%**, 42% below the overall 6.6% and the lowest of any tracked industry. Hardware pages convert at 4.1% and data/infrastructure at 3.3%. 79% of SaaS visits were on mobile, and pages with 250–725 words convert best. Source: [Unbounce SaaS benchmark](https://unbounce.com/conversion-benchmark-report/saas-conversion-rate/). *Type: VB; SaaS, leaning B2B; geography unstated.* **→ Gate:** The harness's B2B "KILL <5%" would kill pages that beat the SaaS median. That is defensible only if the traffic really is *qualified*, meaning warmer than typical paid traffic, and the gate should say so explicitly.
- **Waitlist signup rates (vendor blogs) [V].**
  - Best waitlist pages convert cold traffic at **8–20%**; a typical page converts at about **2–5%**.
  - Reported medians: SaaS about 3.4%, AI tools about 4.6%, consumer apps about 4.1%.

  Sources: [Flowjam](https://www.flowjam.com/blog/waitlist-landing-page-examples-10-high-converting-pre-launch-designs-how-to-build-yours); [LaunchList waitlist benchmark tool](https://getlaunchlist.com/tools/waitlist-benchmark); [Getwaitlist benchmarks](https://getwaitlist.com/blog/waitlist-benchmarks-conversion-rates). *Type: VBlog; no dataset disclosed; geography unstated; mixed B2B/B2C.* **→ Gate:** The harness's "≥8% GO" sits at the bottom of the "best pages" band. That makes it a top-tier bar, which is the right place for a GO gate.
- **Waitlist → paid (vendor blogs) [V].**
  - Waitlists convert to paid at **5–25%**.
  - The rate is about 20% when people get access within a month and falls below 10% if they wait more than 3 months.
  - One source says paid pre-orders convert at 5–25%, and free signups at 25–85% if access comes within a month.
  - Physical goods rarely exceed 5% from waitlist to purchase.

  Sources: [Getwaitlist, "From waitlist to paying customer"](https://getwaitlist.com/blog/from-waitlist-to-paying-customer-conversion-optimization); [ScaleMath](https://scalemath.com/blog/what-is-a-good-waitlist-conversion-rate); [Waitlister](https://waitlister.me/growth-hub/blog/waitlist-and-product-launch-statistics). *Type: VBlog; undisclosed method; likely survivorship-biased because the sources are waitlist-tool vendors; geography unstated; mostly SaaS and consumer apps.* **→ Gate:** An email's value decays with time-to-offer, so discount email rungs older than about 30 days. At face value, 5–25% email→paid means an email is worth 0.05–0.25 of an order. The ladder's email 1 : order 250 ratio values an email at 0.4% of an order, which is far more conservative. Some extra conservatism is defensible given the vendor bias.
- **Free trial → paid, a proxy for email → paid on a working product (vendor blogs) [V].**
  - Opt-in trials (no card) convert at about **18.2%** (range 8–22%, median 14%).
  - Opt-out trials (card required) convert at about **48.8%** (range 35–55%, median 44%).
  - Card-required funnels yield about **10.5 paying customers per 1,000 visitors**, versus about 3.6 without a card.
  - B2B SaaS median is quoted at 18.5–25%.

  Sources: [Kirro](https://kirro.io/free-trial-conversion-rate); [Userpilot](https://userpilot.com/blog/saas-average-conversion-rate/); [Powered by Search](https://www.poweredbysearch.com/learn/b2b-saas-trial-conversion-rate-benchmarks/). *Type: VBlog; B2B SaaS; geography unstated; I could not identify the original dataset behind 18.2%/48.8%.* **→ Gate:** A *working* product with a card-required trial converts about **1.05%** of visitors to paid. A pre-order rate of ≥1% for an *unbuilt* product therefore matches a mature-funnel benchmark, so "strong GO" is well placed. The statistical noise at n=1,000 is large, though (see [Calc] below).
- **Fake-door ethics and disclosure [V].**
  - When it is ethical: teams disclose immediately after the click, avoid critical workflows and do not misrepresent what is live.
  - Risks: perceived dishonesty, user frustration, brand damage among early adopters, curiosity clicks inflating the data, and compliance problems in regulated industries.
  - The post-click message should say the feature is in development, give a timeline if known, offer a sign-up for updates or the beta, and make it easy to go back.

  Sources: [Amplitude](https://amplitude.com/explore/experiment/fake-door-testing); [ProdPad](https://www.prodpad.com/glossary/fake-door-testing/); [AB Tasty](https://www.abtasty.com/glossary/fake-door-testing/). *Type: VBlog/PH.* **→ Gate:** Require a disclosure screen straight after the click. Never take money for a product that does not exist without explicit pre-order terms and an automatic refund path.
- **Strategyzer on simulated sales [V].** A simulated sale in which the customer does not know they are in an experiment "can get you close to real-world purchasing and produces strong evidence". Source: [Strategyzer, Testing Business Ideas summary](https://www.strategyzer.com/library/testing-business-ideas-book-summary). *Type: Book/PH (Strategyzer sells training).* **→ Gate:** Evidence strength and ethics pull against each other here. The strongest smoke tests are the least transparent, so disclosure rules must be designed into the gate.
- **Brazil legal constraints [K].**
  - Consumer Defence Code, art. 49: a 7-day right of withdrawal for purchases made outside a commercial establishment, which includes online sales. Source: [Lei 8.078/1990, CDC](http://www.planalto.gov.br/ccivil_03/leis/l8078compilado.htm).
  - LGPD: collecting personal data such as email addresses needs a legal basis and transparency. Source: [Lei 13.709/2018](http://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/l13709.htm).

  *Type: statute; Brazil; the CDC applies to B2C, and the LGPD applies to both.* **→ Gate:** In Brazil, B2C pre-orders and deposits must be refundable, and every smoke-test form needs a privacy notice.

**Statistics for the harness's smoke-test gates [Calc]** (exact binomial and Wilson 95% intervals)
- **Precision at n=1,000.** An observed rate of 5% has a 95% CI of 3.8–6.5%. For 8% it is 6.5–9.9%, for 15% it is 12.9–17.4%, and for 1% it is 0.54–1.83%. At n=500, 5% gives 3.4–7.3% and 8% gives 5.9–10.7%. At n=300, 5% gives 3.1–8.1%. **→ Gate:** At 1,000 visitors the 5% and 8% intervals just touch. Signup bands work, but the "iterate" band is narrow relative to the noise.
- **Misclassification with hard cutoffs at n=1,000** (KILL if observed <5%, GO if observed ≥8%). A page whose true rate is 5% gets KILLed **48%** of the time, and a true 6% page 7.8% of the time. A true 7% page reaches GO only 12% of the time, a true 8% page only **52%**, and a true 10% page 99%. **→ Gate:** Fixed cutoffs applied to *observed* rates behave like coin flips near the boundaries. Define KILL and GO as hypotheses (p₀, p₁) with error rates instead (see §5).
- **Visitors needed** (one-sided α=0.05, power 0.80):

  | Rates to separate | Visitors needed |
  |---|---|
  | 5% vs 8% signup | ~383 |
  | 3% vs 5% | ~538 |
  | 5% vs 10% | ~149 |
  | Pre-order 0.3% vs 1% | ~616 |
  | Pre-order 0.5% vs 1% | ~1,596 |

  **→ Gate:** "1,000+ qualified visitors" is more than the signup gate needs, and not enough for a pre-order gate that must tell 0.5% from 1%.
- **Pre-order gate "≥1%" at n=1,000** (≥10 orders). A true 1% rate passes only **54%** of the time, a true 0.75% rate 22%, a true 0.5% rate 3% and a true 1.5% rate 93%. **→ Gate:** Half of truly-1% ideas would miss "strong GO". Use the sequential rule in §5 instead.
- **Zero conversions** (rule of three). 0 out of 1,000 bounds the true rate below about 0.3% at 95% confidence, and 0 out of 300 bounds it below about 1%.

### Inferences
- The email-signup bands (KILL <5%, iterate 5–8%, GO ≥8–15%) are consistent with vendor "typical vs best page" bands. The GO bar is about 2× the Unbounce SaaS median. Nothing validates the bands as predictors of later success, so the harness should label them "practitioner heuristic calibrated to vendor benchmarks".
- Conversion depends mostly on the traffic source: warm community traffic, cold paid traffic and outbound links differ a lot. Pre-register the traffic source and the definition of "qualified" on the Test Card, or the thresholds mean nothing.
- For niche B2B in Brazil, 1,000 qualified visitors in 7–14 days will often be infeasible. There the harness should prefer **direct-outreach funnels**: contacted → replied → meeting → reputation/intro → deposit or paid pilot. Use Bayesian small-n rules for those (§5), not landing-page rates.

### Gaps
- I found no Brazilian or Latin American landing-page, waitlist or pre-order benchmark.
- I could not retrieve Unbounce's full distribution (quartiles, top decile) or a B2B vs B2C split beyond industry; the fetch was blocked.
- I found no academic study linking smoke-test or fake-door conversion to later sales or venture survival.
- The dataset behind the widely repeated 18.2%/48.8% trial-conversion figures could not be identified.

## 3. Pre-sales, LOIs, deposits, paid pilots; concierge/Wizard-of-Oz MVPs; Strategyzer evidence scale

### Takeaway
Strategyzer ranks evidence along four contrasts: *say vs do*, *opinion vs fact*, *lab vs real world* and *small vs large investment*. Money-backed behaviour counts as "strong". I found **no published benchmark** for LOI → contract, deposit → full purchase, or paid pilot → production conversion in startups. Evidence for concierge and Wizard-of-Oz MVPs is anecdotal. The harness's evidence ladder copies Savoia's "skin-in-the-game" caliper. Those point values were assigned by the author and are **not empirically calibrated**.

### Cited Findings
- **Strategyzer evidence hierarchy [V].**
  - Strong evidence: actual behaviour (purchases, usage, retention).
  - Moderate evidence: stated intentions and preferences.
  - Weak evidence: opinions and hypothetical answers.
  - What people *do* beats what they *say*. Interviews and surveys are quick to set up but produce "valuable, but weak" evidence.
  - Start with cheap, weak-evidence tests and move to costlier, stronger ones as the signal improves.

  Sources: [Strategyzer, Testing Business Ideas summary](https://www.strategyzer.com/library/testing-business-ideas-book-summary); [Strategyzer, "How strong is your innovation evidence?"](https://www.strategyzer.com/library/how-strong-is-your-innovation-evidence); [Strategyzer, "Designing strong experiments"](https://www.strategyzer.com/library/designing-strong-experiments). *Type: Book/PH (Strategyzer sells training and tools); not geography-specific; B2B and B2C.* **→ Gate:** This supports the ladder's *ordering* and the rule "no build without money-backed evidence".
- **Testing Business Ideas (Bland & Osterwalder 2019) [K].** A library of 44 experiments, each rated for cost, setup time, run time and evidence strength. Four evidence-strength criteria: opinions/beliefs vs facts/events; what people say vs what they do; lab vs real-world setting; small vs large investment by the customer. Source: [Strategyzer "Test" page](https://www.strategyzer.com/test). *Type: Book.* **→ Gate:** Tag each harness experiment with Strategyzer's four criteria. A test that scores "strong" on all four (real setting, behaviour, fact, large investment) is a money-backed rung.
- **Test Card [V + K].** [V]: the Test Card forces you to make explicit "what needs to be true" and turns guesses into verifiable assumptions. [K]: its fields are "We believe that… / To verify that, we will… / And measure… / We are right if…", with ratings for criticality, test cost, data reliability and time required. Sources: [Strategyzer, "Validate your ideas with the Test Card"](https://www.strategyzer.com/library/validate-your-ideas-with-the-test-card); [Isaac Jeffries, "How to fill in a Strategyzer Test Card"](https://isaacjeffries.com/blog/2019/3/26/how-to-fill-in-a-strategyzer-test-card). *Type: PH/tool.* **→ Gate:** Every buyer-test gate should carry a Test Card whose "we are right if" threshold is written **before** data collection. That is exactly the practice the Camuffo RCTs support.
- **Savoia's Skin-in-the-Game caliper, *The Right It* [V, secondary].** Opinions score **0**, a validated email **1**, a validated phone number **10**, and a **$50 cash deposit 50**. Opinions and promises with no skin in the game are "worthless". Sources: [HowToes summary](https://howtoes.blog/2024/04/20/the-right-it-book-summary/); [SoBrief](https://sobrief.com/books/the-right-it); [Bookey](https://www.bookey.app/book/the-right-it). *Type: Book/PH; US (Google innovation context); mostly B2C examples.* **→ Gate:** The harness ladder is Savoia's scale. The weights are ordinal judgements by the author, **not likelihood ratios**. No study shows that a phone number is 10× as predictive as an email. I could not verify this session whether Savoia's book assigns "30-minute meeting = 30" and "paid order = 250".
- **Fitzpatrick's commitment currencies [K].** Time, reputation and money, plus "advancement" (moving to a concrete next step) as the test of a good meeting. Source: [The Mom Test](https://www.momtestbook.com/). *Type: Book/PH.* **→ Gate:** An LOI without a price, date and budget-holder signature counts only as an advancement, not money.
- **Blank's earlyvangelist budget criterion [K].** Earlyvangelists "have or can acquire a budget". Source: [Steve Blank](https://steveblank.com/). *Type: Book/PH; B2B.* **→ Gate:** In B2B, only deposits, pilots and orders from budget-holders count as money-backed rungs.

### Inferences
- **LOIs** are non-binding. Treat an LOI as a *reputation/advancement* rung that ranks above a meeting and below a deposit. Upgrade it to money-backed only if it names a price, a start date and a budget-holder signatory, or comes with a deposit.
- **Paid pilots** are the B2B equivalent of a pre-order. A pilot counts as the strongest rung only if (a) it is paid at a meaningful share of the list price and (b) it has written success criteria that trigger conversion to a contract.
- **Deposits in Brazil:** PIX makes small refundable deposits nearly frictionless, so asking for a deposit costs little. Refund terms must be explicit (CDC art. 49 for B2C).
- **Concierge and Wizard-of-Oz MVPs** produce strong evidence on willingness to pay and delivery cost, but from very small n. Use them to learn and to earn the second money-backed rung, not to estimate market conversion.
- The rule "≥2 money-backed rungs before building" fits Strategyzer's "strong evidence" guidance and works as a **replication safeguard** against a single lucky result (§5). The number two has no empirical derivation.

### Gaps
- I found no data on conversion rates from LOI → contract, deposit → full purchase, or paid pilot → production for startups, in any geography.
- I recall a widely reported MIT NANDA 2025 finding that most enterprise GenAI pilots do not reach production. I did not verify it, and it concerns enterprises' internal pilots, not vendor pilot → contract rates.
- For concierge and Wizard-of-Oz MVPs I found only anecdotes I recall from Ries, *The Lean Startup* (2011): Food on the Table (concierge) and Zappos (manual fulfilment). I did not verify them and found no benchmark data.
- I did not verify Savoia's full scale (time commitments, order values) or his "Law of Failure" percentage.

## 4. Stated intent vs actual behaviour: purchase-intent conversion, hypothetical bias, deflators

### Takeaway
Two separate literatures are easy to confuse:

1. **Hypothetical bias in willingness to pay (WTP).** This is how much people overstate the *amount* they would pay. The median hypothetical/real ratio is **1.35** (Murphy et al. 2005, mostly environmental and public goods), and the mean is about 2.6 [K]. The average for consumer goods is **21%** (Schmidt & Bijmolt 2020). A factor of about 3 comes from List & Gallet 2001 [K].
2. **Purchase-intention → purchase conversion.** This is how many "would buy" answers turn into purchases. Intentions predict **worst** for new products, category-level questions, long horizons and questions asked without comparison. That describes the startup case.

**The harness's ÷1.35–3 range comes from WTP-amount calibration (literature 1). It is likely too lenient when applied to "would you buy?" probability statements about a new product (literature 2).**

### Cited Findings
- **Murphy, Allen, Stevens & Weatherhead 2005 [V].** A meta-analysis of **28 stated-preference studies (83 observations)**. The median ratio of hypothetical to actual value is **1.35**, with severe positive skew. Choice-based elicitation reduces bias. Student subjects may add bias, but that variable is confounded with group settings. [K]: the mean ratio is about 2.6, and the studies are mostly environmental/public goods from North America and Europe. Sources: [Environmental & Resource Economics 30(3):313–325](https://link.springer.com/article/10.1007/s10640-004-3332-z); [SSRN](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=437620); [RePEc](https://ideas.repec.org/a/kap/enreec/v30y2005i3p313-325.html). *Type: PR-MA; not B2B or commercial products.* **→ Gate:** ÷1.35 is the *median WTP-amount* deflator for mostly public goods. It is not a purchase-probability deflator.
- **List & Gallet 2001 [K].** Hypothetical values average about **3×** actual values. Bias is lower for private goods than public goods, and lower for WTP than for willingness-to-accept. Source: [Environmental & Resource Economics 20(3):241–254](https://doi.org/10.1023/A:1012791822804). *Type: PR-MA; mostly lab/field valuation studies (NA/Europe).* **→ Gate:** This is the likely origin of the ÷3 upper bound. For *private* goods, which is what startups sell, the same meta-analysis suggests the bias is smaller than 3×.
- **Schmidt & Bijmolt 2020 [V].** A meta-analysis of **77 studies in 47 papers**, giving **115 effect sizes**, with 24,347 hypothetical and 20,656 real WTP observations. The average hypothetical bias is **21%**. The size of the bias depends mostly on whether WTP was measured directly or indirectly, and *indirect* methods such as conjoint overestimate real WTP significantly more than direct ones. Sources: [JAMS 48(3):499–518 (Groningen portal)](https://research.rug.nl/en/publications/accurately-measuring-willingness-to-pay-for-consumer-goods-a-meta/); [EconPapers](https://econpapers.repec.org/RePEc:spr:joamsc:v:48:y:2020:i:3:d:10.1007_s11747-019-00666-6); [Marketing Center Münster](https://www.marketingcenter.de/en/research/publications/151167). *Type: PR-MA; consumer goods (B2C); mixed geography, largely Europe/NA [K].* **→ Gate:** For *price* answers from consumers, **÷1.2** is the best-supported central deflator. Use larger deflators for conjoint-style (indirect) measures.
  - *Conflict to flag:* Murphy et al. find choice-based elicitation *reduces* bias for public goods, while Schmidt & Bijmolt find indirect (choice-based) methods *overstate* WTP more for consumer goods. The two cover different domains, so the harness should follow Schmidt & Bijmolt for commercial products.
- **Morwitz, Steckel & Gupta 2007 [V].** Intentions correlate more strongly with purchases in six conditions:
  1. Existing products rather than new ones.
  2. Durables rather than non-durables.
  3. Short rather than long time horizons.
  4. Specific brands or models rather than the product category.
  5. Trial rates rather than total market sales.
  6. Comparative rather than monadic (single-product) data collection.

  Sources: [International Journal of Forecasting 23(3):347–364](https://www.sciencedirect.com/science/article/abs/pii/S0169207007000799); [SSRN](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=946194). *Type: PR (cross-study analysis); mostly US consumer data [K].* **→ Gate:** A typical startup test (new product, often a subscription service, open horizon, asked monadically) sits at the *worst* end of every moderator. Stated intent should be deflated more than ÷1.35–3, or excluded from gates entirely. Ask intent for a *specific offer at a specific price within a specific short window (≤30 days)*, alongside the buyer's current alternative.
- **Jamieson & Bass 1989 [V].** This was billed as the largest database of intentions vs actual purchases for new products assembled up to then. It compares models that adjust stated intentions for affordability, liking, availability and **willingness to consult others before purchase**, and finds large gaps between intention and behaviour. Sources: [Journal of Marketing Research 26:336–345](https://journals.sagepub.com/doi/10.1177/002224378902600307); [Semantic Scholar](https://www.semanticscholar.org/paper/Adjusting-Stated-Intention-Measures-to-Predict-of-A-Jamieson-Bass/f2b567a81cf39c13188341310eed320175a78fd0). *Type: PR; US; B2C new products.* **→ Gate:** "Needs to consult others" is the B2B buying-committee problem. Deflate intent from people who are not budget-holders more heavily.
- **Morwitz 2001, principles for forecasting from intentions [V].**
  - Measure intentions with **probability scales**.
  - Tell respondents to focus on their own circumstances.
  - **Adjust intentions to remove biases.**
  - **Segment respondents before adjusting.**
  - Rely more on intentions for behaviours respondents have done before.
  - Remember that **measuring intentions can change behaviour**, and that inaccurate recall of the last purchase biases predictions.

  Sources: [Principles of Forecasting chapter (Springer)](https://link.springer.com/chapter/10.1007/978-0-306-47630-3_3); [Columbia Business School](https://business.columbia.edu/faculty/research/methods-forecasting-intentions-data). *Type: evidence-based handbook chapter.* **→ Gate:** Ask "what is the 0–100% chance you'll pay R$X for this in the next 30 days?". Segment by whether the respondent already pays for a workaround, and deflate first-time category buyers more.
- **Chandon, Morwitz & Reinartz 2005 [K].** Asking about intentions changes later behaviour ("self-generated validity"). The intent–behaviour link seen among surveyed people therefore overstates the underlying link in people who were never surveyed. Source: [Journal of Marketing 69(2)](https://journals.sagepub.com/doi/10.1509/jmkg.69.2.1.60755). *Type: PR; US/Europe consumer panels.* **→ Gate:** Prospects who were interviewed will convert better than the market. Do not extrapolate conversion from interviewees to cold traffic.
- **Armstrong, Morwitz & Kumar 2000 [K].** For *existing* consumer products and services, forecasts based on intentions were on average more accurate than extrapolation. Source: [International Journal of Forecasting](https://www.sciencedirect.com/science/article/pii/S0169207000000583). *Type: PR; US.* **→ Gate:** Stated intent is most useful where there is purchase history, such as when switching from an existing tool. Weight intent from current category buyers more than from non-buyers.
- **Webb & Sheeran 2006 [K].** A meta-analysis of experiments: a medium-to-large change in intention (d≈0.66) produced only a small-to-medium change in behaviour (d≈0.36). Source: [Psychological Bulletin 132(2)](https://doi.org/10.1037/0033-2909.132.2.249). *Type: PR-MA; health and social behaviours; not purchases.* **→ Gate:** About half of any shift in intention shows up in behaviour.
- **Sheeran 2002 [K].** About **47%** of people who state a positive intention fail to act on it ("inclined abstainers"). Source: [European Review of Social Psychology 12](https://doi.org/10.1080/14792772143000003). *Type: PR-MA; health behaviours.* **→ Gate:** Even strong, positive intenders follow through only about half the time. **÷2 is a floor** for top-box ("definitely") answers, and weaker answers ("probably", "maybe") deserve much steeper discounts.
- **Morwitz 2021, "Intentions" review [V exists; content not retrieved].** Source: [Consumer Psychology Review](https://myscp.onlinelibrary.wiley.com/doi/abs/10.1002/arcp.1061). *Type: PR review.*

### Inferences
- **Split the deflator into two:**
  - (a) **Price/WTP amounts:** ÷1.2 central (consumer goods, direct question, Schmidt & Bijmolt), ÷1.35 median (Murphy), and ÷2.6–3 only as a pessimistic scenario (Murphy's mean, List & Gallet).
  - (b) **Purchase probability for a new product:** count only top-box answers, at **≥÷2** (Sheeran). Treat "probably/maybe" answers, category-level questions, long-horizon questions and monadic questions as near-zero evidence (Morwitz moderators).
- Better still, **keep stated intent out of GO gates**. Use it only to decide which behavioural test to run next, which is also Strategyzer's and Fitzpatrick's advice.
- In B2B, deflate intent further when the respondent is not the budget-holder (Jamieson & Bass's "consult others" variable). Deflate less when the respondent already pays for a workaround (Morwitz: prior behaviour predicts better).

### Gaps
- I could not verify numeric top-box weights, such as crediting about 75–80% of "definitely would buy" and 25–30% of "probably" in BASES-style volumetric models. They are widespread industry practice, but the search budget ran out.
- I found no B2B-specific study of hypothetical bias or intent → purchase conversion.
- I found no Brazil-specific data on hypothetical bias or intent translation.
- I did not retrieve the actual stated-vs-realised purchase percentages from Jamieson & Bass or Morwitz et al.

## 5. Decision thresholds with empirical backing; Bayesian and sequential GO/KILL with small samples

### Takeaway
**No specific conversion threshold has been validated against later venture outcomes.** The best-supported "threshold" is a procedure: write hypotheses and pass criteria before testing, and act on them, including by killing ideas (Camuffo RCTs). The only widely used numeric bar, Sean Ellis's 40% "very disappointed", is a practitioner benchmark from about 100 startups and applies only after launch. With the small samples that validation produces, pre-registered **sequential (SPRT)** or **Beta-Binomial** rules classify ideas more reliably than fixed observed-rate cutoffs.

### Cited Findings
- **Sean Ellis PMF test [V, secondary].** After benchmarking nearly 100 startups, Ellis found that those with fewer than 40% of users "very disappointed" (if they could no longer use the product) usually struggled to grow, while those above 40% generally had strong traction. He introduced the test around 2009. Sources: [Koji](https://www.koji.so/docs/sean-ellis-test-product-market-fit); [LearningLoop](https://learningloop.io/glossary/sean-ellis-score); [MeasuringU, "What is the PMF item?"](https://measuringu.com/product-market-fit-item/) (exists; content not retrieved). *Type: PH; US tech startups; B2C and B2B; not peer-reviewed.* **→ Gate:** This applies only *after* a concierge MVP or pilot has active users (inference: ≥30–40 respondents for a usable estimate). It is not a gate before building.
- **Camuffo et al. 2020, 2024 [V].** Pre-stated hypotheses and rigorous tests improve outcomes and make termination more likely (see §1). Sources: [Management Science](https://pubsonline.informs.org/doi/10.1287/mnsc.2018.3249); [SMJ](https://sms.onlinelibrary.wiley.com/doi/full/10.1002/smj.3580). *Type: PR (RCTs).* **→ Gate:** Thresholds must be written on the Test Card before the test runs, and the harness must actually execute KILL decisions.
- **Savoia's XYZ / Market Engagement Hypothesis [K].** Frame a test as "At least X% of Y will do Z". Source: [HowToes summary of *The Right It*](https://howtoes.blog/2024/04/20/the-right-it-book-summary/). *Type: Book/PH.* **→ Gate:** This is the right format for pre-registering p₁, the GO level. Add p₀, the KILL level, and a maximum N.
- **Peeking inflates false positives [K].** Checking a fixed-sample significance test repeatedly and stopping at the first "significant" result sharply raises the false-positive rate. Sequential designs fix this. Sources: [Evan Miller, "How not to run an A/B test"](https://www.evanmiller.org/how-not-to-run-an-ab-test.html); [Evan Miller, "Simple sequential A/B testing"](https://www.evanmiller.org/sequential-ab-testing.html). *Type: PH (statistician's widely cited blog).* **→ Gate:** If the harness checks results daily during a 7–14-day test, it needs a sequential rule. "Stop when it looks good" is not acceptable.
- **SPRT for the signup gate [Calc].** Wald SPRT with H₀ p=5% (KILL level), H₁ p=8% (GO level), α=0.05 and β=0.20. The **expected N is about 190** if the true rate is 5% and **about 240** if it is 8%.

  | Visitors so far | GO if signups ≥ | KILL if signups ≤ |
  |---|---|---|
  | 200 | 19 (≥9.5%) | 9 (≤4.5%) |
  | 500 | 38 (≥7.6%) | 28 (≤5.6%) |
  | 1,000 | 70 (≥7.0%) | 60 (≤6.0%) |

  **→ Gate:** Most signup decisions resolve within about 200–400 qualified visitors. That frees traffic for a second rung.
- **SPRT for the pre-order gate [Calc].** H₀ p=0.3%, H₁ p=1%, α=0.05, β=0.20. The **expected N is about 380–390**.

  | Visitors so far | GO if orders ≥ | KILL if orders ≤ |
  |---|---|---|
  | 500 | 6 | 1 |
  | 1,000 | 9 (≥0.9%) | 4 (≤0.4%) |

  **→ Gate:** Replace "≥1% at 1,000" with this rule. Truly-1% ideas then usually reach GO, where the fixed cutoff lets only 54% through.
- **Beta-Binomial for small B2B samples [Calc]** (uniform Beta(1,1) prior; "k/n" is deposits or paid pilots out of qualified accounts asked):

  | k/n | Posterior mean | 90% credible interval | P(p>10%) | P(p>20%) |
  |---|---|---|---|---|
  | 3/20 | 18% | 7–33% | 0.85 | 0.37 |
  | 1/10 | 17% | 3–36% | 0.70 | — |
  | 2/10 | 25% | — | 0.91 | 0.62 |
  | 0/15 | 6% | 0.3–17% | 0.19 | — |
  | 5/20 | — | — | 0.99 | 0.77 |
  | 8/30 | — | — | 1.00 | 0.85 |

  **→ Gate:** Express B2B money gates as posteriors, for example "GO if P(deposit rate >10%) ≥ 0.8", which is about 3 deposits from ≤20 qualified budget-holders. Do not express them as raw counts.
- **Beta-Binomial for a landing page with a benchmark prior [Calc].** The prior is Beta(3.8, 96.2): mean 3.8%, the Unbounce SaaS median, weighted as 100 pseudo-visitors.
  - 50/1,000 signups → P(p>5%) = 0.42.
  - 65/1,000 → P(p>5%) = 0.96 and P(p>8%) = 0.01.
  - 80/1,000 → P(p>8%) = 0.31.

  **→ Gate:** A benchmark-informed prior makes a GO at 8% demanding. That is appropriate for a GO gate, but the prior has to be declared in advance.

### Inferences
- **Recommended rule format:**
  - Pre-register p₀ (KILL level), p₁ (GO level), the traffic source and definition of "qualified", the maximum N and the maximum number of days.
  - Decide by SPRT, or by Bayes: **GO if P(p>p₁) ≥ 0.8; KILL if P(p<p₀) ≥ 0.8; otherwise iterate**, until the N or time cap is reached. At the cap, the default is KILL or pivot.
- **Multiple testing:** a harness that screens many ideas and variants will pass some by chance. The "≥2 money-backed rungs" rule works as a replication requirement against that, which is the best statistical justification for keeping it.
- For B2B, run gates on account funnels (n≈10–30 budget-holders) with Beta-Binomial rules, not on web-traffic rates.

### Gaps
- I found no empirical calibration of any GO/KILL cut point against later revenue or survival, for B2B or B2C, in any geography.
- I found no published evaluation of Bayesian or sequential decision rules in startup validation specifically. The recommendation above rests on standard statistics, not domain evidence.
- MeasuringU's empirical analysis of the PMF item could not be read (fetch blocked).

## 6. Audit of the harness's current numbers against the evidence

### Takeaway
The harness's **structure** is well supported: a behaviour-over-opinion ladder, money-backed rungs before building, and pre-set thresholds. Its **numbers** are practitioner heuristics:

- The ladder weights are Savoia's arbitrary scale.
- The ÷1.35–3 deflator comes from WTP-amount meta-analyses and is misapplied to purchase probability.
- The signup bands sit plausibly against vendor benchmarks.
- The ≥1% pre-order bar is well placed but statistically noisy at n=1,000.

The better-supported alternatives are statistical, not empirical: sequential or Bayesian rules and split deflators. No threshold can be called empirically validated.

### Cited Findings
- **Ladder: opinion 0, email 1, phone 10, deposit 50.** This equals Savoia's caliper [V] ([HowToes](https://howtoes.blog/2024/04/20/the-right-it-book-summary/)). The *ordering* has support from Strategyzer's say-vs-do hierarchy [V] ([Strategyzer](https://www.strategyzer.com/library/testing-business-ideas-book-summary)) and Fitzpatrick's commitment currencies [K]. The *magnitudes* have no empirical calibration. **→ Gate:** Keep the ordering and stop treating points as additive likelihood. Add a **reputation/intro** rung (B2B). Let email points decay after about 30 days (vendor waitlist decay [V], [Getwaitlist](https://getwaitlist.com/blog/from-waitlist-to-paying-customer-conversion-optimization)).
- **Ladder: 30-minute meeting 30, paid order 250.** I could not verify that Savoia assigns these. **→ Gate:** Label them harness heuristics.
- **≥2 money-backed rungs before building.** The principle is supported by Strategyzer's "strong evidence" [V] and by the Camuffo RCTs' pre-registered testing [V] ([Management Science](https://pubsonline.informs.org/doi/10.1287/mnsc.2018.3249)). The number two is a heuristic, best justified as replication against chance passes [Calc/Inference]. **→ Gate:** Keep it. In B2B, require that both rungs come from budget-holders.
- **Deflators ÷1.35–3.** ÷1.35 is Murphy et al.'s median *WTP-amount* ratio [V] ([ERE](https://link.springer.com/article/10.1007/s10640-004-3332-z)). ÷3 is about List & Gallet's mean calibration factor [K]. For consumer goods the best estimate is 21% (÷1.2) [V] ([JAMS](https://research.rug.nl/en/publications/accurately-measuring-willingness-to-pay-for-consumer-goods-a-meta/)). For *purchase probability* of new products, the Morwitz moderators [V] and Sheeran's ~47% non-follow-through [K] imply ≥÷2 for top-box answers and much steeper discounts for everything else. **→ Gate:** Split the deflator. Apply ÷1.2–1.35 (central) to ÷2.6–3 (pessimistic) to *price*. For *purchase probability*, count top-box answers only, at ≥÷2, and never let stated intent open a GO gate.
- **Signup "KILL <5%" (B2B, qualified traffic).** The Unbounce SaaS median is 3.8% and the all-industry median 6.6% [V] ([Unbounce](https://unbounce.com/conversion-benchmark-report/saas-conversion-rate/)). A typical waitlist page converts at 2–5% [V, VBlog]. The bar is stricter than the median, which is acceptable only for truly qualified traffic. A page whose true rate is 5% gets KILLed 48% of the time at n=1,000 [Calc]. **→ Gate:** Keep 5% as p₀ only if the traffic source is pre-registered as warm or qualified. For cold paid traffic, lower p₀ to about 3–4%.
- **Signup "iterate 5–8%, GO ≥8–15%".** Best waitlist pages convert at 8–20% [V, VBlog] ([Flowjam](https://www.flowjam.com/blog/waitlist-landing-page-examples-10-high-converting-pre-launch-designs-how-to-build-yours)). The GO bar is therefore top-tier, which is appropriate. With fixed cutoffs, a true 8% page reaches GO only 52% of the time [Calc]. **→ Gate:** Use p₁=8% in an SPRT or Bayesian rule, not "observed ≥8%".
- **Sample: "1,000+ qualified visitors, 7–14 days".** About 383 visitors separate 5% from 8%, and the SPRT's expected N is about 190–240 [Calc]. Separating pre-order rates of 0.5% and 1% takes about 1,600 visitors [Calc]. **→ Gate:** The requirement is more than signup gates need and less than pre-order gates need. Set N per gate from p₀/p₁. For B2B niches where 1,000 qualified visitors is infeasible, use account-level Beta-Binomial gates.
- **Pre-order "≥1% strong GO".** A mature card-required trial funnel converts about 1.05% of visitors to paid [V, VBlog] ([Kirro](https://kirro.io/free-trial-conversion-rate)). So ≥1% for an *unbuilt* product really is strong. At n=1,000, a true 1% rate passes only 54% of the time [Calc]. **→ Gate:** Keep 1% as p₁ with p₀≈0.3% under an SPRT: at n=1,000, GO at ≥9 orders and KILL at ≤4.
- **Geography and segment labels.** None of the conversion benchmarks is Brazilian. Unbounce's geography is unstated and likely North-America-heavy. The vendor waitlist and trial blogs give no geography. The academic intent and hypothetical-bias work is US/European and B2C. The only RCT evidence is from Italy. **→ Gate:** Treat every numeric threshold as a prior to be recalibrated on the harness's own Brazilian B2B results. Log each test's p₀, p₁, traffic source, n and outcome so the harness can build its own base rates.

### Inferences
- The best-supported upgrade is procedural and statistical, not new benchmark numbers:
  1. Write a Test Card with p₀, p₁, traffic source, maximum N and maximum days.
  2. Decide by SPRT or Beta-Binomial.
  3. Split the deflators into price and purchase probability.
  4. Keep stated intent out of GO decisions.
  5. Count money-backed rungs only from budget-holders.
  6. Log outcomes to calibrate local base rates.
- Where the harness's numbers disagree with benchmarks, they err on the strict side (KILL <5% sits above the SaaS median, and the email:order weight of 1:250 is conservative). The one place they err lenient is the ÷1.35–3 deflator applied to "would buy" statements.

### Gaps
- Brazil-specific B2B conversion benchmarks, LOI, deposit and pilot conversion data, and any outcome-calibrated threshold remain unfound. The harness will have to generate these itself by logging its tests.
- Several [K] items (List & Gallet factor, Murphy's mean ratio, Guest 2006 percentages, Sheeran 47%, Webb & Sheeran effect sizes, Chandon et al., Koning et al., Strategyzer's 44-experiment details, Savoia's full scale) should be spot-checked before final publication. Fetching was blocked and the search budget ran out this session.
