<div align="center">

# Documentation Templates

[![Docs](https://img.shields.io/badge/Docs-Templates-blue?style=flat-square)](../index.md)

</div>

Templates to keep documentation consistent across the project.
Copy a template, rename it, and fill in the placeholders (`{LIKE_THIS}`).

---

## Available Templates

| Template | Use for |
|----------|---------|
| [`doc_template.md`](doc_template.md) | New topic pages in `docs/` |
| [`module_template.md`](module_template.md) | Documenting a module in `src/` |
| [`notebook_template.md`](notebook_template.md) | Documenting Jupyter/Colab notebooks |
| [`adr_template.md`](adr_template.md) | Architecture Decision Records |

---

## Conventions

1. **Header block** — every page starts with a centered `# Title` + badge line
2. **Cross-links** — end every page with related links: `*Related: ...*`
3. **Badges** — use `shields.io` flat-square style, matching existing docs
4. **Tables** — use GitHub-flavored markdown tables for structured data
5. **Naming** — `snake_case.md` filenames in `docs/`
6. **No monoliths** — split large topics into separate files and cross-link

## Style Rules

- Emoji in headings: allowed, max one per heading, consistent with existing docs
- Code blocks: always specify language (` ```python `, ` ```bash `)
- Placeholder text: `{UPPER_SNAKE_CASE}` — remove before publishing
