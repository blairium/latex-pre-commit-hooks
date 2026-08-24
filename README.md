# latex-pre-commit-hooks

Pre-commit hooks for cleaning up LaTeX source files.

## Hooks

- **replace-latex-math** — replaces inline `$...$` math delimiters with `\( ... \)` in `.tex`/`.md` files, skipping TikZ coordinates.
- **fix-nbsp** — replaces non-breaking spaces (U+00A0) with regular spaces in `.tex` files.
- **latex-syntax-cleaner** — normalizes whitespace inside `\cite{}` and `\citep{}`, and spacing around `\cref`.

## Usage

Add this to your `.pre-commit-config.yaml`:

```yaml
repos:
- repo: https://github.com/blairium/latex-pre-commit-hooks
  rev: v0.2.0
  hooks:
  - id: replace-latex-math
  - id: fix-nbsp
  - id: latex-syntax-cleaner
```

Then install and run:

```bash
pre-commit install
pre-commit run --all-files
```
