# TOFIX

Findings from a code scan on 2026-10-04.

## High

- `src/pypptkit/utils.py:54` - `download()` is an empty stub (`pass`), so the advertised `download-links` command (`src/pypptkit/main.py:60`, "Download links from ppt files") collects the links and then silently does nothing and exits 0. Implement the download (e.g. `urllib.request`/`requests` into the current directory) or remove the endpoint until it exists.

## Medium

- `src/pypptkit/utils.py:45` - external links are told apart from internal parts by `target_ref.startswith("..")`, duplicated in `src/pypptkit/main.py:28`. python-pptx exposes this directly as `rel.is_external`; use that, and share one helper between `extract_text` and `get_sorted_refs` instead of two copies.
- `src/pypptkit/configs.py:9` - `ConfigObject` is never imported or used anywhere, and `no_err_run()` (`src/pypptkit/utils.py:33`) has no caller either; both are dead code. Remove them.

## Low

- `src/pypptkit/main.py:32` - `# pylint: disable=no-member` (and `# pylint: disable=unused-argument` / `# noinspection PyUnusedLocal` at `src/pypptkit/utils.py:52`-`53`) are leftovers: pylint is not run by this repo (the build uses ruff and mypy). Delete the stale suppressions.
- `pyproject.toml:88` - `mypy_path = "src:python:scripts"` names `python/` and `scripts/` directories that do not exist in this repo; reduce it to `src`.
- `doc/TODO.txt:1` - the file is empty (0 bytes); delete it or put the planned work in it.
