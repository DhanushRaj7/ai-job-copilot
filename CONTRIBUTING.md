# Contributing to AI Job Copilot

Thanks for your interest — contributions, bug reports, and ideas are all welcome. This is an actively developed project; the [Future improvements](./README.md#future-improvements) section of the README is a good place to find something to pick up.

## Ways to contribute
- **Report a bug** — use the [bug report template](./.github/ISSUE_TEMPLATE/bug_report.yml).
- **Suggest a feature** — use the [feature request template](./.github/ISSUE_TEMPLATE/feature_request.yml).
- **Improve docs** — typos to whole guides, all appreciated.
- **Write code** — pick an open issue or a roadmap item and open a PR.

## Development setup

```bash
git clone https://github.com/DhanushRaj7/ai-job-copilot.git
cd ai-job-copilot
python -m venv .venv
source .venv/bin/activate          # Windows: .venv\Scripts\Activate.ps1
pip install -r requirements.txt
pip install ruff pytest            # dev tools
cp .env.example .env               # add your API key
```

## Before you open a PR
1. **Branch** off `main`: `git checkout -b feat/short-description`.
2. **Format & lint:** `ruff format .` then `ruff check .`.
3. **Test:** `pytest -q`. Add tests for new behavior. Tests must not require live API keys — mock the LLM.
4. **Keep it focused.** One logical change per PR; small PRs get reviewed faster.
5. Fill out the **PR template** and link any related issue (`Closes #12`).

## Coding conventions
- **Style:** `ruff` (formatter + linter) is the source of truth. CI enforces it.
- **Types:** annotate public functions; the agent state is typed on purpose — keep it that way.
- **Structure:** one responsibility per node; branching logic lives in the router, not scattered across nodes.
- **Commits:** clear, imperative messages ("Add retry backoff to search node"). [Conventional Commits](https://www.conventionalcommits.org/) encouraged (`feat:`, `fix:`, `docs:`) but not required.

## Commit & PR etiquette
- Reference issues in commits/PRs where relevant.
- Don't commit secrets, `.env`, API keys, or large data files.
- Be kind in review — see the [Code of Conduct](./CODE_OF_CONDUCT.md).

By contributing, you agree your contributions are licensed under the project's [MIT License](./LICENSE).
