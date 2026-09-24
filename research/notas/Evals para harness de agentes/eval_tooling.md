# Eval tooling for a Claude Code–based agent harness (skills, subagents, slash commands) on a solo-founder budget

Research date: 2026-09-24. Legend for source types: **[Official docs]**, **[Official repo]** (README or docs source in the vendor's GitHub), **[Registry]** (PyPI/npm metadata), **[Anthropic eng/research blog]**, **[Anthropic product blog]**, **[Local skill source]** (the installed Anthropic `skill-creator` skill in this environment), **[Competitor page]** (a rival vendor's comparison page, so possibly biased), **[Practitioner repo]**, **[Own computation]**. Each finding ends with "→" and a one-line implication for a solo-operated Python + Markdown + JSONL repo that runs inside Claude Code, including cloud sessions.

Method caveat: in this session the egress proxy blocked vendor websites (promptfoo.dev, braintrust.dev, langchain.com, confident-ai.com, inspect.aisi.org.uk), and the web-search budget was used up. For that reason:
- Features and prices were checked against docs sources in the vendors' own GitHub repos (the same Markdown that builds their doc sites), against PyPI/npm, and against code.claude.com, platform.claude.com, anthropic.com and claude.com.
- Braintrust prices, LangSmith per-seat and per-trace prices, and Confident AI prices come only from competitor comparison pages dated Aug–Sep 2026. They are flagged below.

---

## Q1. Tools: promptfoo, Inspect AI, Braintrust, LangSmith, DeepEval, OpenAI Evals, and 2025–2026 newcomers (runs locally? cost, Claude support, LLM-graded rubrics, multi-step agent eval, CI, dataset/version management)

### Takeaway
Only two tools actually drive the real Claude Code agent: **promptfoo**, through its `anthropic:claude-agent-sdk` provider, and **Inspect AI**, through Inspect SWE's `claude_code()` agent. Both are free, MIT-licensed and run locally.
- **promptfoo** has first-class `skill-used` / `not-skill-used` assertions, trajectory assertions, cost caps, caching, `--repeat` and a GitHub Action. For skill, subagent and slash-command evals in a Git repo it fits with the least effort.
- **Inspect AI** has the stronger statistics (epochs with pass@k/pass^k reducers, standard errors) and sandboxing. It runs Claude Code in a Docker/k8s sandbox, which is heavier to operate and likely unavailable inside a Claude Code cloud session (see Q2).
- **Braintrust and LangSmith** are hosted observability and experiment platforms. Their free tiers are usable for one person, but neither adds anything a solo harness needs at the start.
- **DeepEval** fits pytest-style LLM-judge metrics but does not drive Claude Code itself.
- **OpenAI Evals** (the open-source repo) is effectively dormant and OpenAI-centric, so skip it.

### Cited Findings

**promptfoo**
- [Official repo] promptfoo is a CLI and library for evals and red-teaming. The README says "LLM evals run 100% locally - your prompts never leave your machine", the tool is MIT licensed, and "Promptfoo is now part of OpenAI. Promptfoo remains open source and MIT licensed." — [promptfoo README](https://github.com/promptfoo/promptfoo) → The core tool is free and local. The OpenAI ownership is a vendor-direction risk to watch, not a licensing risk today.
- [Registry] The latest npm release is `promptfoo` 0.123.1, published 2026-09-18, license MIT. — [npm: promptfoo](https://www.npmjs.com/package/promptfoo) → Actively maintained (weekly-scale releases), so pin the version in the repo for reproducible evals.
- [Official repo] The pricing page source lists three plans:
  - **Community**: "Free Forever", with "All LLM evaluation features", "All model providers", "Red teaming (10k probes/month)", "Run locally or self-host", and "CI/CD integration: community: true".
  - **Enterprise**: price "Custom".
  - **On-Premise**: price "Custom".

  Source: [promptfoo pricing.tsx](https://github.com/promptfoo/promptfoo/blob/main/site/src/pages/pricing.tsx) → The only cost is the model tokens the eval itself spends.
- [Official repo] The Claude Agent SDK provider (`anthropic:claude-agent-sdk`, alias `anthropic:claude-code`) needs `@anthropic-ai/claude-agent-sdk` installed. Its options include `working_dir`, `setting_sources`, `skills`, `plugins`, `agents` (programmatic subagents), `max_turns`, `max_budget_usd`, `permission_mode`, `output_format` (JSON schema), `sandbox` and `forward_subagent_text`. — [promptfoo Claude Agent SDK provider docs](https://github.com/promptfoo/promptfoo/blob/main/site/docs/providers/claude-agent-sdk.md) → It runs the real Claude Code loop against a fixture directory, so skills, subagents and CLAUDE.md are exercised as they are in production.
- [Official repo] The same provider page says `apiKeyRequired: false` "is useful when you're using a local Claude Code binary with an active session, such as Claude Code monthly plans". — [promptfoo Claude Agent SDK provider docs](https://github.com/promptfoo/promptfoo/blob/main/site/docs/providers/claude-agent-sdk.md) → Evals can draw on a Pro/Max subscription instead of API spend. The trade-off is that these runs are never cached (see Q3).
- [Official repo] promptfoo "normalizes Claude `Skill` tool invocations into `response.metadata.skillCalls`", so tests can assert `type: skill-used` / `not-skill-used`. For CI it recommends `setting_sources: ['project']` so tests "don't depend on user-specific skills". — [promptfoo Claude Agent SDK provider docs](https://github.com/promptfoo/promptfoo/blob/main/site/docs/providers/claude-agent-sdk.md) → Checks for skill triggering and routing come ready-made, with no parser to write.
- [Official repo] Deterministic assertions include `trajectory:tool-used`, `trajectory:tool-sequence`, `trajectory:step-count`, `trajectory:tool-args-match`, `is-json`, `contains-json`, `cost`, `latency`, and custom `javascript`/`python` assertions. — [promptfoo deterministic assertions](https://github.com/promptfoo/promptfoo/blob/main/site/docs/configuration/expected-outputs/deterministic.md) → Multi-step behaviour (which tools, how many steps, what cost) can be graded without an LLM judge.
- [Official repo] `llm-rubric` defaults to `claude-sonnet-4-5-20250929` as grader when only an Anthropic key is present; the grader provider and its parameters can be overridden. `agent-rubric` exists for judges that need to inspect files with agent tools. — [promptfoo llm-rubric docs](https://github.com/promptfoo/promptfoo/blob/main/site/docs/configuration/expected-outputs/model-graded/llm-rubric.md) → The judge can be Claude-only. Pin a cheaper grader (e.g. Haiku 4.5) explicitly to control cost.
- [Official repo] CI and datasets:
  - The `promptfoo/promptfoo-action@v1` GitHub Action runs a before-vs-after eval on PRs that touch prompt files and comments with a link to the results viewer. — [promptfoo GitHub Actions guide](https://github.com/promptfoo/promptfoo/blob/main/site/docs/integrations/github-action.md)
  - The CLI supports `--repeat`, `--filter-failing`, `-j/--max-concurrency`, `--no-cache`, and `-o` to csv/json/jsonl/html/junit.xml. — [promptfoo CLI reference](https://github.com/promptfoo/promptfoo/blob/main/site/docs/usage/command-line.md)

  → Test cases live as YAML/CSV/JSON in Git, so Git itself is the dataset versioning. JUnit output plugs into any CI.

**Inspect AI**
- [Official repo] Inspect AI is a UK AI Security Institute framework with "tool usage, multi-turn dialog, and model graded evaluations" and "over 200 pre-built evaluations". — [inspect_ai README](https://github.com/UKGovernmentBEIS/inspect_ai) → A mature, research-grade harness.
- [Registry] `inspect-ai` 0.3.268 was published 2026-09-22 under the MIT License. — [PyPI inspect-ai](https://pypi.org/project/inspect-ai/) → Pure Python and pip-installable, which fits a Python repo.
- [Official repo] Built-in scorers: `includes()`, `match()`, `pattern()`, `answer()`, `model_graded_qa()` and `model_graded_fact()`. — [Inspect built-in scorers](https://github.com/UKGovernmentBEIS/inspect_ai/blob/main/docs/_builtin-scorers.md) → Covers deterministic checks and LLM rubrics.
- [Official repo] The Anthropic provider is used as `inspect eval ... --model anthropic/claude-sonnet-4-0` with `ANTHROPIC_API_KEY`. — [Inspect providers](https://github.com/UKGovernmentBEIS/inspect_ai/blob/main/docs/providers.qmd) → Claude is first-class, but the native path needs an API key, not a subscription.
- [Official repo] Repetition and statistics: `--epochs` repeats each sample, and `--epochs-reducer` offers `mean`, `median`, `mode`, `max`, `at_least_{n}`, `pass_at_{k}` and `pass_k_{k}`. — [Inspect options](https://github.com/UKGovernmentBEIS/inspect_ai/blob/main/docs/options.qmd) → The best built-in handling of nondeterminism among the tools reviewed.
- [Official repo] Caching and resumable runs: `--cache` caches model output for 7 days by default. Eval sets retry failed work and resume where they stopped when the command is re-run. — [Inspect caching](https://github.com/UKGovernmentBEIS/inspect_ai/blob/main/docs/caching.qmd); [Inspect eval sets](https://github.com/UKGovernmentBEIS/inspect_ai/blob/main/docs/eval-sets.qmd) → Good cost control for re-runs.
- [Official repo] Sandboxes: `docker` and `local` ("Local file system (no sandbox)") are built in; `k8s`, `daytona`, `modal` and `proxmox` are external packages. — [Inspect sandboxing](https://github.com/UKGovernmentBEIS/inspect_ai/blob/main/docs/sandboxing.qmd) → Clean per-trial isolation is available, at the cost of running Docker.
- [Official repo] `sandbox_agent_bridge()` can run agents written in any language inside a sandbox, redirecting their Anthropic/OpenAI API calls to Inspect's model provider. Claude Code and Codex CLI are the showcased examples. — [Inspect agent bridge](https://github.com/UKGovernmentBEIS/inspect_ai/blob/main/docs/agent-bridge.qmd) → Inspect can evaluate the real Claude Code binary, not only raw model calls.
- [Official repo] Inspect SWE's `claude_code()` agent:
  - Takes `system_prompt`, `replace_system_prompt`, `skills`, `mcp_servers`, `disallowed_tools`, `attempts`, `subagent_model`, `cwd` and `version` (stable, latest, sandbox, or pinned).
  - By default "download[s] the current stable version of Claude Code and copy it to the sandbox".
  - Its own tests "depend on a valid sandbox being available (either `docker` or `k8s`)".

  Sources: [Inspect SWE claude_code docs](https://github.com/meridianlabs-ai/inspect_swe/blob/main/docs/claude_code.qmd); [inspect_swe README](https://github.com/meridianlabs-ai/inspect_swe) → Powerful, but it needs a container runtime.
- [Registry] `inspect-swe` 0.2.71 was published 2026-09-17 under the MIT License. — [PyPI inspect-swe](https://pypi.org/project/inspect-swe/) → Actively maintained.
- [Official repo] Inspect ships a standard `skill()` tool that gives models Agent Skills (per agentskills.io). — [Inspect standard tools: Skill](https://github.com/UKGovernmentBEIS/inspect_ai/blob/main/docs/tools-standard.qmd) → SKILL.md content can be evaluated with Claude through the raw API, without Claude Code, as a cheaper proxy.

**Braintrust**
- [Anthropic eng blog] Anthropic's eval-framework appendix describes Braintrust as combining "offline evaluation with production observability and experiment tracking". Its `autoevals` library includes pre-built scorers. — [Anthropic: Demystifying evals for AI agents](https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents) → Positioned for teams that also monitor production traffic.
- [Official repo] The Braintrust Python SDK README lists integrations for Anthropic (`anthropic>=0.48.0`) and Claude Agent SDK (`claude_agent_sdk>=0.1.10`). — [braintrust-sdk-python README](https://github.com/braintrustdata/braintrust-sdk-python) → Can trace Claude Agent SDK runs.
- [Official repo] The JS SDK has a `claude-agent-sdk` wrapper and auto-instrumentation. — [braintrust-sdk-javascript: claude-agent-sdk wrapper](https://github.com/braintrustdata/braintrust-sdk-javascript/tree/main/js/src/wrappers/claude-agent-sdk) → Same for TypeScript.
- [Official repo] autoevals uses `OPENAI_API_KEY` by default for model-graded scorers. — [autoevals README](https://github.com/braintrustdata/autoevals) → Claude-only grading needs extra configuration.
- [Registry] `braintrust` (Python) 0.42.0 was published 2026-09-22. — [PyPI braintrust](https://pypi.org/project/braintrust/)
- [Competitor page] Braintrust pricing, per Langfuse:
  - **Starter (free)**: 1 GB processed data, then $4/GB; 10k scores, then $2.50/1k; 14-day retention.
  - **Pro**: $249/month, with 5 GB (then $3/GB) and 50k scores (then $1.50/1k); 30-day retention.
  - Self-hosting of the data plane is Enterprise-only; the control plane is always Braintrust-managed.

  Source: [Langfuse: Braintrust comparison (Sept 2026)](https://langfuse.com/compare/braintrust). PostHog independently reports "Free Starter (10k scores/mo, unlimited seats) … Pro $249/mo" and a first-party GitHub Action that posts eval results to the PR, noting hard score gates "need a Reporter() you write" ([PostHog: best AI evaluation tools, 2026-08-28](https://posthog.com/compare/best-ai-evaluation-tools-for-production)). → The free tier fits solo use. The jump to $249 is steep, and nothing here is local-only.

**LangSmith**
- [Official docs, in repo] Trace allowances and retention:
  - Personal ("Developer") organizations are "limited to 5,000 traces per month until a credit card is added".
  - Plus organizations are "given an initial 10,000 traces per month".
  - Base traces keep 14-day retention; extended traces keep 180 days, the maximum as of September 14, 2026.

  Source: [LangSmith billing docs](https://github.com/langchain-ai/docs/blob/main/src/langsmith/billing.mdx) → The free tier covers a solo eval cadence.
- [Competitor page] LangSmith charges "$39/seat/month on Plus", "$0.005/base trace + $0.0025 extended upgrade", and the free tier is "5,000 base traces/month, 1 seat". — [Langfuse: LangSmith comparison (Sept 2026)](https://langfuse.com/compare/langsmith) → Cheap for one person, but still a hosted dependency.
- [Official docs, in repo] The LangSmith pytest plugin (`@pytest.mark.langsmith`) syncs each test case to a dataset example and creates an experiment per run. — [LangSmith pytest docs](https://github.com/langchain-ai/docs/blob/main/src/langsmith/pytest.mdx) → The best "pytest plus hosted dataset versioning" option if a hosted UI is wanted.
- [Official repo] The LangSmith Python SDK contains `langsmith/integrations/claude_agent_sdk`. — [langsmith-sdk](https://github.com/langchain-ai/langsmith-sdk/tree/main/python/langsmith/integrations/claude_agent_sdk) → Can trace Agent SDK runs.
- [Registry] `langsmith` 0.14.0 was published 2026-09-21 (client: MIT). — [PyPI langsmith](https://pypi.org/project/langsmith/)

**DeepEval / Confident AI**
- [Official repo] DeepEval is "similar to Pytest but specialized for unit testing LLM apps" (`deepeval test run`). It offers G-Eval (LLM-as-judge), DAG, and agentic metrics such as Task Completion, Tool Correctness, Step Efficiency and Plan Adherence, plus multi-turn metrics. It defaults to `OPENAI_API_KEY` but accepts custom models. — [DeepEval README](https://github.com/confident-ai/deepeval) → Good pytest-native LLM-judge metrics, but you must feed it the transcripts yourself.
- [Official repo] An `AnthropicModel` judge class exists. — [deepeval/models/llms/anthropic_model.py](https://github.com/confident-ai/deepeval/blob/main/deepeval/models/llms/anthropic_model.py) → Claude can be the judge.
- [Registry] `deepeval` 4.2.5 was published 2026-09-22 under Apache-2.0. — [PyPI deepeval](https://pypi.org/project/deepeval/)
- [Competitor page] Pricing: "Open-source core free forever; Starter plan from $200/mo" for Confident AI, and results "save … locally as JSON". — [PostHog comparison](https://posthog.com/compare/best-ai-evaluation-tools-for-production) → The cloud is unnecessary for solo use (UNVERIFIED on the official page).

**OpenAI Evals**
- [Official repo] The README now opens with "You can now configure and run Evals directly in the OpenAI Dashboard". It requires `OPENAI_API_KEY`, and its registry lives in Git-LFS. — [openai/evals README](https://github.com/openai/evals) → The open-source repo is effectively superseded by OpenAI's hosted product.
- [Registry] The last PyPI release of `evals` is 3.0.1.post1, dated 2024-05-01. — [PyPI evals](https://pypi.org/project/evals/) → Dormant for more than two years. Skip it for a Claude harness.

**Newcomers and alternatives (2025–2026)**
- [Anthropic product blog] **skill-creator eval/benchmark mode** (Mar 3, 2026): "Skill-creator now helps you write evals, run benchmarks … It tracks eval pass rate, elapsed time, and token usage." It runs evals with "independent agents … in parallel … each in a clean context", uses "comparator agents for A/B comparisons", and tunes descriptions for triggering ("improved triggering on 5 out of 6 public skills"). — [Claude blog: Improving skill-creator](https://claude.com/blog/improving-skill-creator-test-measure-and-refine-agent-skills) → A zero-install, Anthropic-native eval loop for skills (details in Q2).
- [Official repo] **Harbor**, from the Terminal-Bench creators, "evaluate[s] arbitrary agents like Claude Code, OpenHands, Codex CLI". It runs locally in Docker, or on Daytona, Modal and others, e.g. `harbor run --dataset terminal-bench@2.0 --agent claude-code`. — [Harbor README](https://github.com/laude-institute/harbor) → Built for containerized benchmark-scale runs; too heavy for a solo harness.
- [Official repo] **Pydantic Evals** is code-first Python. It "grades an agent's final outputs and its trajectory", including span-based (OpenTelemetry) evaluators and LLM-as-judge. — [Pydantic Evals docs source](https://github.com/pydantic/pydantic-ai/blob/main/docs/evals.md) → A lightweight Python alternative if you don't want promptfoo's Node dependency.
- [Official repo] **agentevals** (LangChain) offers trajectory match evaluators (strict, unordered, subset/superset) and a trajectory LLM-as-judge. — [agentevals README](https://github.com/langchain-ai/agentevals) → Reusable trajectory graders.
- [Competitor page] **Langfuse** is MIT, self-hostable, with a cloud free tier of 50k units/month and Core at $29/month; PostHog says ClickHouse acquired Langfuse in January 2026. **Arize Phoenix** is free and uncapped when self-hosted. — [PostHog comparison](https://posthog.com/compare/best-ai-evaluation-tools-for-production); [Langfuse: Braintrust comparison](https://langfuse.com/compare/braintrust) → Open-source tracing if observability is ever needed.
- [Anthropic eng blog] Anthropic's own advice: "frameworks … are only as good as the eval tasks you run through them. It's often best to quickly pick a framework that fits your workflow, then invest your energy in the evals themselves." — [Anthropic: Demystifying evals](https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents) → Tool choice matters less than the quality of the tasks.

### Inferences

#### Comparison matrix
Built from the findings above. Prices come from the sources cited above; LangSmith, Braintrust and DeepEval cloud prices are competitor-sourced.

| Tool | Runs locally | Cost for 1 person | Claude models | LLM rubric | Drives real Claude Code (skills/subagents) | CI | Datasets/versioning | Fit here |
|---|---|---|---|---|---|---|---|---|
| promptfoo | Yes (Node CLI) | Free (MIT) + tokens | Yes (API or subscription via Agent SDK) | `llm-rubric`, `agent-rubric` | **Yes**: `anthropic:claude-agent-sdk`, `skill-used`, trajectory asserts | GH Action, JUnit | YAML/CSV in Git; local results DB | **Best overall** |
| Inspect AI + Inspect SWE | Yes (Python) | Free (MIT) + tokens | Yes (API key) | `model_graded_qa/fact` | **Yes**: `claude_code()` in Docker/k8s sandbox | CLI + logs | Python tasks in Git; eval logs | Best statistics; heavier |
| skill-creator (Anthropic) | Yes (inside Claude Code) | Free + tokens/subscription | Native | Grader subagent | **Yes** (subagents + `claude -p`) | Scripts; no built-in CI | `evals/evals.json` in Git | Best for skill iteration |
| DeepEval | Yes (pytest) | Free (Apache-2.0); cloud optional | Yes (`AnthropicModel`) | G-Eval, DAG | No; you pass transcripts | pytest | Local JSON / Confident AI | Judge metrics only |
| Braintrust | No (SaaS) | Free Starter; Pro $249/mo | Yes (Agent SDK wrapper) | autoevals (OpenAI default) | Tracing only | GH Action | Hosted versioned datasets | Overkill now |
| LangSmith | No (SaaS) | Free 5k traces/mo; $39/seat Plus | Yes (Agent SDK integration) | Yes | Tracing only | pytest plugin | Hosted datasets | Overkill now |
| OpenAI Evals (OSS) | Yes | Free | Not designed for it | Yes | No | — | Git-LFS registry | Skip (dormant) |
| Harbor | Yes (Docker) | Free + tokens | Yes (`--agent claude-code`) | Custom | Yes (container) | — | Harbor registry | Too heavy |

#### Recommendation-ready trade-offs
- **Default pick: promptfoo plus pytest.** promptfoo is the only tool that asserts skill triggering declaratively against the real Claude Code agent, supports subscription auth, and has a PR GitHub Action. Costs: a Node dependency in a Python repo, OpenAI ownership (a strategic question mark), and no caching when using subscription auth.
- **Use skill-creator for authoring loops** (with and without the skill, blind A/B comparison, description tuning), then freeze its `evals.json` cases into promptfoo or pytest for regression. skill-creator has no CI story of its own.
- **Inspect AI if statistical rigor matters more than convenience**: epochs, `pass_k` reducers and standard errors. It needs Docker for Claude Code runs and an API key.
- **Defer hosted platforms** (Braintrust, LangSmith, Confident AI) until there is production traffic to monitor. A Git repo plus local JSON/JSONL results is enough for solo regression.

### Gaps
- Official Braintrust, LangSmith and Confident AI pricing pages could not be fetched (egress blocked). Braintrust tier numbers and LangSmith $39/seat and $0.005/trace come only from Langfuse's and PostHog's comparison pages; confirm on braintrust.dev/pricing, langchain.com/pricing and confident-ai.com/pricing.
- The date promptfoo joined OpenAI was not verified from a primary source. A search-aggregator snippet said "as of March 2026", but only the README statement is confirmed.
- Could not verify whether LangSmith self-hosting is Enterprise-only in 2026 (not in the fetched billing doc).
- Did not verify whether OpenAI's hosted Evals product can grade non-OpenAI (Claude) models. The open-source repo has no Anthropic completion function under `evals/completion_fns` (GitHub code search returned 0 hits).

---

## Q2. How to evaluate Claude Code artifacts specifically (headless `claude -p`, Agent SDK, skill-creator eval/benchmark, testing skills, subagents, CLAUDE.md changes)

### Takeaway
There are three layers, cheapest first:
1. **Headless `claude -p`** with `--output-format json|stream-json`, `--json-schema`, `--max-budget-usd` and `--max-turns`. It gives cost and result JSON, plus a stream that shows every Skill/Agent tool call, including nested subagents.
2. **The Claude Agent SDK** (Python or TypeScript), for pytest-driven runs with options such as `setting_sources`, `skills`, `agents`, `plugins`, `output_format`, `max_budget_usd` and hooks.
3. **skill-creator's eval loop**: evals.json, runs with and without the skill, a grader agent, benchmark.json with mean ± stddev, and a trigger-eval optimizer that runs each query 3 times.

Published practice for skills is to test triggering separately from quality, using near-miss negatives and distractor skills. For CLAUDE.md, skill or subagent changes, it is to run two fixture arms that differ in one file.

### Cited Findings

**Headless `claude -p`**
- [Official docs] `-p` runs Claude Code non-interactively. `--output-format` accepts `text`, `json` or `stream-json`. With `--json-schema`, the conforming output lands in `structured_output`. The JSON output includes `total_cost_usd` and a per-model cost breakdown, both "client-side estimates". — [Claude Code: Run programmatically (headless)](https://code.claude.com/docs/en/headless) → Every eval run can log its own cost and a schema-validated result.
- [Official docs] "User-invoked skills and custom commands work. Include `/skill-name` in the prompt string." — [Claude Code headless](https://code.claude.com/docs/en/headless) → Slash commands and user-invoked skills can be tested directly from scripts.
- [Official docs] In `stream-json`:
  - Subagent messages carry `parent_tool_use_id`. By default the subagent's `tool_use` and `tool_result` blocks are emitted; `--forward-subagent-text` adds text and thinking (v2.1.211+).
  - Nested subagents and forked skills appear too (v2.1.275+ for all nesting cases).
  - The `system/init` event lists `plugins` and `plugin_errors`, and "Fail CI when a plugin or MCP server doesn't load" is a documented pattern.

  Source: [Claude Code headless](https://code.claude.com/docs/en/headless) → Subagent delegation can be asserted by parsing JSONL, with no extra framework.
- [Official docs] `--bare` skips auto-discovery of "hooks, skills, custom commands, subagents, plugins, MCP servers, auto memory, and CLAUDE.md". It "is the recommended mode for scripted and SDK calls, and will become the default for `-p` in a future release". Bare mode needs `ANTHROPIC_API_KEY` ("never reads OAuth credentials"). Context comes back in explicitly via `--agents <json>`, `--plugin-dir`, `--mcp-config` and `--add-dir` (which loads skills from `.claude/skills/`). — [Claude Code headless](https://code.claude.com/docs/en/headless) → **Trap:** evals of skills, subagents or CLAUDE.md must *not* use bare mode (or must re-inject the config), and must be pinned against the coming default change.
- [Official docs] "Without `--bare`, a `-p` session runs the hooks in a project's `.claude/settings.json` and connects the servers in its `.mcp.json`, even in a folder you've never trusted." — [Claude Code headless](https://code.claude.com/docs/en/headless) → Project hooks will fire during evals, which is good for testing them but a side-effect risk.
- [Official docs] Cost and isolation flags:
  - `--max-budget-usd` (print mode; subagent spend counts toward the cap) and `--max-turns`.
  - `--no-session-persistence`, `--setting-sources user,project,local`, `--disable-slash-commands`, `--append-system-prompt-file`.
  - `--exclude-dynamic-system-prompt-sections`, which "improves prompt-cache reuse across different users and machines running the same task".

  Source: [Claude Code CLI reference](https://code.claude.com/docs/en/cli-reference) → Hard cost caps and config isolation per eval run.

**Claude Agent SDK**
- [Official docs] The Agent SDK is "a library that runs the Claude Code binary, with Claude Code's capabilities, such as built-in tools, permissions, sessions, and hooks". It also says: "Unless previously approved, Anthropic does not allow third party developers to offer claude.ai login or rate limits for their products … Use the API key authentication methods." — [Agent SDK overview](https://code.claude.com/docs/en/agent-sdk/overview) → Fine for personal eval runs; products built on it need API keys.
- [Official docs] Python `ClaudeAgentOptions` includes `max_budget_usd`, `output_format`, `hooks`, `agents`, `setting_sources`, `skills` and `plugins`. `ResultMessage` has `num_turns` and `total_cost_usd`. When `setting_sources` is omitted, the SDK "loads the same filesystem settings as the Claude Code CLI: user, project, and local"; pass `[]` to disable (in Python SDK ≤0.1.59 an empty list didn't work). — [Agent SDK Python reference](https://code.claude.com/docs/en/agent-sdk/python) → pytest can parametrize over cases and assert on cost, turns and structured output. **Trap:** set `setting_sources=["project"]` explicitly so personal `~/.claude` skills don't contaminate results. Note that promptfoo's provider instead defaults to *no* setting sources.
- [Registry] `claude-agent-sdk` 0.2.159 was published 2026-09-23 under MIT. — [PyPI claude-agent-sdk](https://pypi.org/project/claude-agent-sdk/) → Changes very fast, so pin the version.

**Anthropic skill-creator (installed locally and published in anthropics/skills)**
- [Local skill source] The workflow:
  - Test prompts go in `evals/evals.json`.
  - For each case, spawn "two subagents in the same turn — one with the skill, one without". When improving a skill, the baseline is a snapshot of the old version (`old_skill/`).
  - A grader subagent writes `grading.json` with `text`/`passed`/`evidence`.
  - `python -m scripts.aggregate_benchmark` produces `benchmark.json` and `benchmark.md` with "pass_rate, time, and tokens for each configuration, with mean ± stddev and the delta".
  - An analyzer flags "assertions that always pass regardless of skill (non-discriminating), high-variance" cases, and there is an optional blind comparator.

  Source: [skill-creator SKILL.md](https://github.com/anthropics/skills/blob/main/skills/skill-creator/SKILL.md) → A complete with/without-skill A/B loop that runs inside Claude Code, including cloud sessions (it only needs subagents).
- [Local skill source] Description optimization:
  - Build 20 trigger queries: 8–10 should-trigger and 8–10 should-not, with the negatives being "near-misses".
  - `scripts.run_loop` splits them "60% train and 40% held-out test", runs "each query 3 times to get a reliable trigger rate", iterates up to 5 times, and picks `best_description` "by test score rather than train score to avoid overfitting".
  - It also warns: "simple, one-step queries like 'read this PDF' may not trigger a skill even if the description matches perfectly".

  Source: [skill-creator SKILL.md](https://github.com/anthropics/skills/blob/main/skills/skill-creator/SKILL.md) → A ready-made, statistically aware skill-triggering eval. Trigger cases must be substantive tasks.
- [Local skill source] How `run_eval.py` detects triggering:
  - It creates a temporary command file in `.claude/commands/` so the candidate description appears in the skill list.
  - It runs `claude -p <query> --output-format stream-json --include-partial-messages`, strips `CLAUDECODE` so it can nest inside a session, and marks triggered when a `Skill` (or `Read` of the skill) tool call names the skill.
  - Defaults: `--num-workers 10`, `--timeout 30`, `--runs-per-query 3`, `--trigger-threshold 0.5`.

  Source: [skill-creator scripts/run_eval.py](https://github.com/anthropics/skills/blob/main/skills/skill-creator/scripts/run_eval.py) → A reference implementation to copy for a custom pytest trigger test. It needs the `claude` CLI and exits early after detection, so it is cheap.
- [Local skill source] `quick_validate.py` only allows the frontmatter keys `name`, `description`, `license`, `allowed-tools`, `metadata` and `compatibility`, with a kebab-case name of at most 64 characters and a description of at most 1024. — [skill-creator scripts/quick_validate.py](https://github.com/anthropics/skills/blob/main/skills/skill-creator/scripts/quick_validate.py); Claude Code's docs note that this upload/packaging schema is narrower than Claude Code's own frontmatter ([Claude Code skills](https://code.claude.com/docs/en/skills)) → **Trap:** Claude Code-only keys (`disable-model-invocation`, `when_to_use`, `hooks`, `argument-hint`) fail quick_validate. Write your own lint for Claude Code skills.
- [Official docs] Claude Code "ignores a field it doesn't recognize without reporting an error". The combined `description` + `when_to_use` "is truncated at 1,536 characters in the skill listing". — [Claude Code skills](https://code.claude.com/docs/en/skills) → A frontmatter typo fails silently, so a deterministic pytest lint on SKILL.md has high value and costs nothing.
- [Official docs] Anthropic's skill best practices: "Build evaluations first". Establish a baseline "without the Skill", create "at least three evaluations", and "Test with Haiku, Sonnet, and Opus". The doc also says "There is not currently a built-in way to run these evaluations". — [Skill authoring best practices](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices) → Minimum bar: 3 or more evals per skill, compared against a no-skill baseline. That last sentence appears to predate skill-creator's eval mode.

**Practitioner setups**
- [Practitioner repo] citypaul/.dotfiles:
  - A **routing** suite of 48 one-step decisions asks "does Claude load the right skill, and do the neighbouring skills stay quiet?" It takes about 10 minutes at concurrency 4, runs through promptfoo `anthropic:claude-agent-sdk` with local Claude Code login, and uses `skill-used` / `not-skill-used` assertions.
  - "Each case costs roughly 100k prompt tokens: the system prompt, all 50 skill descriptions, the loaded skill body and a handful of file reads."
  - A throwaway workspace symlinks the live skills to avoid duplicate discovery.
  - The suite is "deliberately **not** part of `npm test` or the per-push CI". A cheap offline guard test checks that every skill named in the cases exists. A workflow runs "on demand, weekly, or on a pull" request.

  Source: [citypaul/.dotfiles evals/skills README](https://github.com/citypaul/.dotfiles/tree/main/evals/skills) → A concrete template for this repo: an offline guard per push and paid routing and quality suites on demand or weekly.
- [Practitioner repo] kwhinnery/resend-skill-example tests "TRIGGERING" (code-based `skill-used` / `not-skill-used` as "ground truth", with `llm-rubric` as a cross-check) separately from "CONTENT CORRECTNESS" (a JS lint of the hard rules plus `llm-rubric`). Fixtures include "distractor skills … so the resend skill wins a realistic routing decision". — [resend-skill-example promptfooconfig.yaml](https://github.com/kwhinnery/resend-skill-example) → Add distractor skills and grade triggering deterministically.
- [Practitioner repo] bendrucker/claude runs a PR-body skill eval as two providers ("current" and "revised") that "differ in one file inside the fixture plugin … so a score delta is attributable to the guidance". It sets `setting_sources: []`, `max_turns: 12`, `max_budget_usd: 0.75` and a JSON-schema `output_format`. — [bendrucker/claude pr-body eval](https://github.com/bendrucker/claude/tree/main/plugins/pull-request/evals/pr-body) → The pattern for evaluating CLAUDE.md, skill or subagent edits: two arms, one diff.
- [Official repo] promptfoo's own skill-comparison example runs `review-standards-v1` and `v2` fixtures with `skills: ['review-standards']`, `output_format` JSON schema, `skill-used`, and a JS threshold on expected issue IDs. — [promptfoo example: skill-comparison](https://github.com/promptfoo/promptfoo/tree/main/examples/claude-agent-sdk/skill-comparison) → A copy-ready template.
- [Official repo] promptfoo's "Test Agent Skills" guide recommends "Positive prompts that should trigger each skill" and "Near-miss prompts that should trigger a sibling instead", plus `--repeat 3`. "If two versions are close, rerun the eval with repeats … not the one that wins a single lucky run." — [promptfoo guide: Test Agent Skills](https://github.com/promptfoo/promptfoo/blob/main/site/docs/guides/test-agent-skills.md) → Same design as skill-creator's trigger evals.

**Anthropic general guidance**
- [Anthropic eng blog] "It's often better to grade what the agent produced, not the path it took." Checking exact tool-call sequences is "too rigid and results in overly brittle tests". Build in partial credit. — [Anthropic: Demystifying evals](https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents) → Use trajectory assertions sparingly: skill-used, yes; exact tool order, rarely.

**Instruction loading and cloud sessions**
- [Official docs] The `InstructionsLoaded` hook "fires when a `CLAUDE.md` or `.claude/rules/*.md` file is loaded into context", with a `load_reason` matcher. — [Claude Code hooks reference](https://code.claude.com/docs/en/hooks) → During an eval, a hook can log which CLAUDE.md or rules actually loaded. This is a deterministic check for instruction-loading changes.
- [Official docs] "Cloud sessions share rate limits with all other Claude and Claude Code usage within your account … There is no separate compute charge for the cloud VM." — [Claude Code on the web](https://code.claude.com/docs/en/claude-code-on-the-web) → Evals run from a cloud session consume the same subscription limits as normal work.

### Inferences
- The cheapest high-signal eval for this repo is a **trigger/routing suite**: `claude -p` or the Agent SDK with `stream-json`, asserting on `Skill` tool names and on subagent spawns via `parent_tool_use_id`. It can exit early, as skill-creator's `run_eval.py` does.
- **Quality suites** (does the skill or subagent produce the right JSONL or Markdown?) should grade the *output files* deterministically first, and use an LLM rubric only for the residual.
- To evaluate a CLAUDE.md, skill or subagent change, copy bendrucker's two-arm pattern: two fixture directories (current vs candidate) under promptfoo, or a pytest parametrize over two `cwd`s. Keep `setting_sources=["project"]` and never use `--bare`.
- Inspect SWE's Docker requirement likely makes it impractical inside Claude Code cloud sessions. promptfoo or the Agent SDK run in-process with a local temp `working_dir`, so they are the cloud-session-friendly choice.

### Gaps
- Could not verify that nested `claude -p` or Agent SDK calls work inside Claude Code *cloud* sessions: auth inheritance, and whether a subscription token is available to child processes. skill-creator strips `CLAUDECODE` to allow nesting locally. Test this empirically.
- Could not verify that Docker is available in Claude Code cloud containers; no doc was fetched on this.
- No official Anthropic doc describes a dedicated "subagent eval" pattern beyond stream-json `parent_tool_use_id` and SubagentStop hooks. The practitioner patterns above are the best available.

---

## Q3. Regression practice: evals on each change, caching, cost control, nondeterminism with small N, pytest deterministic checks

### Takeaway
Use two tiers:
1. **Free, deterministic checks on every commit and PR.** pytest with JSON-Schema validation of JSONL, SKILL.md frontmatter lint, and "every referenced skill exists" guards.
2. **A paid, nondeterministic suite on demand, nightly or weekly, or when skills, agents or CLAUDE.md change.** 20–50 tasks drawn from real failures, 3+ repeats per case, hard `max_budget_usd` caps, and results reported as pass rate with a confidence interval (or pass^k), never as a single run.

With N=10, an 8/10 pass rate has a 95% CI of roughly 49–94%. Small suites therefore detect only large regressions: treat them as smoke alarms and compare runs paired on the same tasks.

### Cited Findings

**How big a suite, and what kind**
- [Anthropic eng blog] "20-50 simple tasks drawn from real failures is a great start … in early agent development … this large effect size means small sample sizes suffice." Also: "Capability" evals start at a low pass rate, "regression evals … should have a nearly 100% pass rate", and capability tasks "graduate" into the regression suite. — [Anthropic: Demystifying evals](https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents) → Right-size for one person: 20–50 tasks, split into a regression suite and a capability suite.

**Measuring nondeterminism**
- [Anthropic eng blog] Definitions: "pass@k measures the likelihood that an agent gets at least one correct solution in k attempts" and "pass^k measures the probability that all k trials succeed". For example, a 75% per-trial success rate over 3 trials gives (0.75)³ ≈ 42%. — [Anthropic: Demystifying evals](https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents) → For a harness you rely on daily, pass^k (consistency) is the right regression metric.
- [Anthropic eng blog] "Each trial should be 'isolated' by starting from a clean environment"; Claude once gained "an unfair advantage … by examining the git history from previous trials". — [Anthropic: Demystifying evals](https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents) → Run each trial in a fresh temp copy of the fixture, not in the live repo.
- [Anthropic research blog] Five recommendations:
  - Report the standard error of the mean (SEM).
  - Cluster standard errors when questions are related; clustered SEs "can be over three times as large as naive standard errors".
  - Resample answers per question ("Inspect … correctly computes standard errors … via its epochs parameter").
  - Use paired differences, since model question-score correlations are 0.3–0.7.
  - Use power analysis.

  Source: [Anthropic: A statistical approach to model evaluations (Nov 19, 2024)](https://www.anthropic.com/research/statistical-approach-to-model-evals) → Compare old and new config on the *same* tasks (paired), repeat each task, and cluster by skill if several tasks target one skill.
- [Anthropic eng blog] "Infrastructure configuration can swing agentic coding benchmarks by several percentage points". Infra error rates ranged from 5.8% (strict limits) to 0.5% (uncapped), and pass rates "fluctuate with time of day". — [Anthropic: Quantifying infrastructure noise (Feb 5, 2026)](https://www.anthropic.com/engineering/infrastructure-noise) → Retry infra or API errors separately from agent failures, and don't read small deltas as regressions.
- [Own computation] 95% Wilson intervals for small N: 3/3 → [0.44, 1.00]; 5/5 → [0.57, 1.00]; 8/10 → [0.49, 0.94]; 10/10 → [0.72, 1.00]; 18/20 → [0.70, 0.97]; 45/50 → [0.79, 0.96]. pass^k at a 90% per-trial rate: k=3 → 0.73, k=5 → 0.59. (Wilson score formula, z = 1.96.) → With N ≤ 20, only drops of about 20+ percentage points are distinguishable. Per-case repeats (3–5) plus paired comparison are the cheapest way to add power.
- [Official repo] promptfoo: "Run evals multiple times with `--repeat 3` to measure variance … If a prompt fails 50% of the time, the prompt is ambiguous. Fix the instructions rather than running more retries." — [promptfoo guide: Evaluate coding agents](https://github.com/promptfoo/promptfoo/blob/main/site/docs/guides/evaluate-coding-agents.md) → A flaky case is itself a signal of an ambiguous skill description or instruction.
- [Local skill source] skill-creator's `aggregate_benchmark.py` computes "mean, stddev, min, max for each metric" and the "delta between with_skill and without_skill". — [skill-creator scripts/aggregate_benchmark.py](https://github.com/anthropics/skills/blob/main/skills/skill-creator/scripts/aggregate_benchmark.py) → Reusable aggregation code.

**Caching**
- [Official repo] promptfoo caches on disk (`~/.promptfoo/cache`) with a default TTL of 14 days. With `--repeat` greater than 1, "each repeat index uses a separate cache namespace", and error responses are not cached. — [promptfoo caching](https://github.com/promptfoo/promptfoo/blob/main/site/docs/configuration/caching.md) → Unchanged cases re-run for free, and repeats stay distinct.
- [Official repo] The Agent SDK provider "caches responses … if the prompt, configuration, and files in the working directory … are the same". Caching is off by default when MCP is configured. "Local Claude login (`apiKeyRequired: false`) … remain[s] uncached." — [promptfoo Claude Agent SDK provider](https://github.com/promptfoo/promptfoo/blob/main/site/docs/providers/claude-agent-sdk.md) → **Trade-off:** subscription auth means no API bill but also no cache; API-key auth gives a cache but you pay per token. Changing a SKILL.md in the working dir correctly invalidates the cache.
- [Official repo] Inspect `--cache` defaults to 7 days, and eval sets resume incomplete work. — [Inspect caching](https://github.com/UKGovernmentBEIS/inspect_ai/blob/main/docs/caching.qmd); [Inspect eval sets](https://github.com/UKGovernmentBEIS/inspect_ai/blob/main/docs/eval-sets.qmd) → Same benefit in Python.
- [Official repo] promptfoo `--filter-failing <eval>` re-runs only the previously failed tests. — [promptfoo CLI](https://github.com/promptfoo/promptfoo/blob/main/site/docs/usage/command-line.md) → A cheap loop for fixing regressions.

**Cost control**
- [Official docs] Current API prices per MTok (input/output): Haiku 4.5 $1/$5; Sonnet 5 $2/$10 (the introductory price "is now the standard price"); Sonnet 4.6 $3/$15; Opus 5.5 $4/$20. Cache reads cost 0.1x the base input price (0.05x on Opus 5.5), and the Batch API gives "a 50% discount". — [Claude API pricing](https://platform.claude.com/docs/en/about-claude/pricing) → Use Haiku 4.5 for LLM-judge rubrics and pin the eval model explicitly.
- [Practitioner repo] "Each case costs roughly 100k prompt tokens" for real Claude Code skill-routing runs with about 50 skills. — [citypaul/.dotfiles evals](https://github.com/citypaul/.dotfiles/tree/main/evals/skills) → **[Inference]** At Sonnet 5 list price that is about $0.20 per case uncached, less with prompt caching. So 48 cases × 3 repeats is roughly $10–30 on an API key, or a slice of subscription limits.
- [Official repo] "A security audit might cost $0.10–0.30 and take 30–120 seconds." Cost and latency can be asserted (`type: cost`, `threshold: 0.25`). — [promptfoo guide: Evaluate coding agents](https://github.com/promptfoo/promptfoo/blob/main/site/docs/guides/evaluate-coding-agents.md) → Budget per case and fail on cost regressions too.
- [Official docs] Enterprise Claude Code averages "around $13 per developer per active day". Subscription users have usage included, and cloud sessions share rate limits with the account. — [Claude Code costs](https://code.claude.com/docs/en/costs); [Claude Code on the web](https://code.claude.com/docs/en/claude-code-on-the-web) → For a solo founder on Max, subscription-auth evals are close to free in dollars but compete with daily work for limits.
- [Official docs] GitHub Actions can authenticate Claude Code with `CLAUDE_CODE_OAUTH_TOKEN` (from `claude setup-token`) on Pro, Max, Team and Enterprise, or with an `ANTHROPIC_API_KEY`. — [Claude Code GitHub Actions](https://code.claude.com/docs/en/github-actions) → CI can run the paid suite on subscription auth. That token is tied to one person's subscription.

**Deterministic checks in pytest**
- [Official docs] "Prioritize volume over quality: More questions with slightly lower signal automated grading is better than fewer questions with high-quality human hand-graded evals." — [Anthropic: Define success criteria and build evaluations](https://platform.claude.com/docs/en/test-and-evaluate/develop-tests) → Lean on automated and deterministic grading.
- [Anthropic eng blog] "Choosing deterministic graders where possible, LLM graders where necessary". For LLM judges: "give the LLM a way out, like … return 'Unknown'", and grade "each dimension with an isolated LLM-as-judge". — [Anthropic: Demystifying evals](https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents) → One judge call per rubric dimension, on Haiku, with an explicit "Unknown" option.
- [Official repo] DeepEval (`deepeval test run`) and the LangSmith pytest plugin (`@pytest.mark.langsmith`) both put LLM evals inside pytest. — [DeepEval README](https://github.com/confident-ai/deepeval); [LangSmith pytest](https://github.com/langchain-ai/docs/blob/main/src/langsmith/pytest.mdx) → pytest can be the single runner for deterministic and LLM-graded checks.
- [Official docs] `claude -p --output-format json --json-schema '<schema>'` returns `structured_output` conforming to the schema; an invalid schema makes `claude` exit with an error. `format` keywords are annotations only and not enforced. — [Claude Code headless](https://code.claude.com/docs/en/headless) → Validate again client-side (e.g. Python `jsonschema`) if `format` constraints matter.

### Inferences
Proposed regression setup for this repo, synthesized from the findings above:
1. **Pre-commit and CI (free, every push)**, in pytest:
   - (a) Validate every JSONL line against a JSON Schema.
   - (b) Lint SKILL.md and agent frontmatter against Claude Code's accepted keys; include the 1,536-character description+`when_to_use` cap and kebab-case names.
   - (c) Check that cases reference existing skills and agents.
   - (d) Run the Python scripts' unit tests.
2. **Paid suite, triggered by path filters** (`.claude/skills/**`, `.claude/agents/**`, `CLAUDE.md`, `.claude/commands/**`), run on demand or nightly:
   - promptfoo with `anthropic:claude-agent-sdk`, `setting_sources: ['project']`, `max_budget_usd` of about $0.50–0.75 per case, and `--repeat 3`.
   - Report per-case pass^3 and overall pass rate with a Wilson CI.
   - Compare paired against the last baseline JSON committed to the repo.
3. **Model-upgrade runs**: re-run the full suite and use skill-creator's with/without-skill comparison to detect skills the model has outgrown.
4. **Separate infra failures** (API retry events, timeouts) from agent failures before scoring.

### Gaps
- No primary source found for a canonical "pytest + JSON Schema for JSONL" pattern specific to Claude Code repos. The pytest design above is inference from general practice plus the documented `--json-schema` behaviour.
- Could not verify exact subscription limits (Pro/Max session and weekly caps) as of Sept 2026, so the capacity for subscription-auth evals per week is unknown.
- No source quantified typical run-to-run variance for skill triggering specifically. skill-creator's choice of 3 runs per query at a 0.5 threshold is the only published default.

---

## Q4. Using Claude Code hooks to enforce deterministic checks (e.g., validating JSONL writes)

### Takeaway
Hooks turn deterministic checks into guarantees at runtime, both during normal use and during evals:
- **`PreToolUse`** on `Write|Edit` (narrowed with `if: "Write(**/*.jsonl)"`) can inspect the proposed content and **block** with exit 2; Claude receives the stderr reason.
- **`PostToolUse`** can re-validate the file on disk after `Edit`; exit 2 shows stderr to Claude, but the write already happened.
- **Writes made by Bash** (`>>` appends from Python scripts) bypass Edit/Write hooks. Cover them with a `Stop` hook, whose exit 2 prevents Claude from finishing, or a `FileChanged` watcher, which runs after the fact and cannot block.

Hooks live in `.claude/settings.json` (committed) or in skill/agent frontmatter, so they travel with the repo. Beware: `--bare` skips them.

### Cited Findings
- [Official docs] "Exit 2 means a blocking error." Per-event effects:
  - `PreToolUse`: "Blocks the tool call".
  - `PostToolUse`: "Shows stderr to Claude; the tool already ran".
  - `Stop`: "Prevents Claude from stopping, continues the conversation".
  - `SubagentStop`: "Prevents the subagent from stopping".
  - `PostToolBatch`: "Stops the agentic loop before the next model call".

  Source: [Claude Code hooks reference](https://code.claude.com/docs/en/hooks) → Choose the event by whether you need to prevent a write or only correct it.
- [Official docs] Exit code 0 plus stderr "goes to the debug log only … Claude never sees it. To surface a warning to Claude from a `PostToolUse` … hook, exit 2 instead". — [Claude Code hooks reference](https://code.claude.com/docs/en/hooks) → A validator must exit 2 (not 1) for Claude to see and fix the error.
- [Official docs] The `PostToolUse` input includes `tool_input` (for Write: `file_path` and `content`) and `tool_response`. File paths are absolute. — [Claude Code hooks reference](https://code.claude.com/docs/en/hooks) → A Python validator can read `tool_input.file_path` from stdin JSON and validate the JSONL on disk.
- [Official docs] The handler `if` field uses permission-rule syntax such as `"Edit(*.ts)"` or `"Bash(git *)"` to run only on matching calls. `"Edit(src/**)"` matches only the working-dir `src`; use `"Edit(**/src/**)"` for any depth. — [Claude Code hooks reference](https://code.claude.com/docs/en/hooks) → `"if": "Write(**/*.jsonl)"` avoids spawning the validator on every edit.
- [Official docs] "Claude Code doesn't run a `PostToolUse` hook matching `Edit|Write` when a `Bash` command or a process outside Claude Code rewrites the same file." `FileChanged` "runs the hook no matter what changed the file", but it takes literal filenames (no regex) and has no decision control. — [Claude Code hooks reference](https://code.claude.com/docs/en/hooks) → JSONL appended by Python scripts via Bash needs a Stop-hook sweep, or validation inside the script itself.
- [Official docs] `Stop` hooks receive `stop_hook_active` ("`true` when Claude Code is already continuing" because of a stop hook). — [Claude Code hooks reference](https://code.claude.com/docs/en/hooks) → Check it to avoid infinite loops in a "validate all JSONL before finishing" Stop hook.
- [Official docs] Skill hooks are "registered when you or Claude invoke the skill and keep running for the rest of the session", with `once: true` available. Subagent hooks "run only while that subagent is running", and a `Stop` hook there becomes `SubagentStop`. Project subagent frontmatter hooks require workspace trust, and "a `-p` session doesn't count as accepting it". — [Claude Code hooks reference](https://code.claude.com/docs/en/hooks) → Validators can be scoped to the skill or subagent that writes JSONL. **Trap:** subagent-frontmatter hooks won't fire in `-p` eval runs in an untrusted folder; settings-file hooks will.
- [Official docs] Two documented examples:
  - A `PostToolUse` hook with matcher `Edit|Write` running `jq -r '.tool_input.file_path' | xargs npx prettier --write`.
  - A `PreToolUse` script that exits 2 to "Prevent Claude from modifying sensitive files", after which "Claude receives feedback explaining why the edit was blocked".

  Source: [Claude Code hooks guide](https://code.claude.com/docs/en/hooks-guide) → Direct templates for a JSONL validator.
- [Official docs] "Prompt-based hooks" and "Agent-based hooks" exist, as do async background hooks, including a documented "Run tests after file changes" pattern. — [Claude Code hooks reference](https://code.claude.com/docs/en/hooks) → Hooks can also run pytest in the background after edits. Keep blocking validators synchronous and fast.
- [Official docs] `--bare` skips hooks, and without `--bare` a `-p` session runs project `.claude/settings.json` hooks even in untrusted folders. — [Claude Code headless](https://code.claude.com/docs/en/headless) → Evals of hook behaviour must run without `--bare`, and hook firing can itself be asserted in `stream-json` (`hook_started` / `hook_response` events are documented for SessionStart and Setup).

### Inferences
Suggested hook layout for a Python + JSONL repo:
- **`PreToolUse` on `Write`**, `if: "Write(**/*.jsonl)"`: parse `tool_input.content` line by line with `json.loads`, validate each line with `jsonschema`, and exit 2 with the line number and error on failure. This prevents the write.
- **`PostToolUse` on `Edit`**, `if: "Edit(**/*.jsonl)"`: re-validate the whole file from `tool_input.file_path`, because an `Edit` payload only carries `old_string`/`new_string`, not the full file. Exit 2 so Claude repairs it.
- **`Stop` hook**: validate all JSONL files changed in `git status --porcelain` (catches Bash and script appends), skip if `stop_hook_active`, and exit 2 on failure.
- **Reuse the same validator in pytest and CI**, so hooks and CI share one source of truth.
- Because hooks live in the committed `.claude/settings.json`, they should also apply in Claude Code cloud sessions that clone the repo (**not verified**).

### Gaps
- Did not verify from docs that the `tool_input` field names for `Edit` are exactly `old_string`/`new_string` in the current version. The field names come from general knowledge of the Edit tool, not from a fetched schema table.
- Did not find a first-party example specifically validating JSONL or JSON Schema in a hook. The recommended layout is assembled from documented primitives.
- Did not verify whether project hooks run identically in Claude Code cloud sessions (the web docs link to hooks config but the specifics weren't retrieved).
