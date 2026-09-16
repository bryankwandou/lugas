# Lugas
nLive guide: https://lugas.vercel.app

A writing skill for Claude (and other LLMs) that rewrites or drafts text so it reads
clearly and naturally, the first time. Indonesian first, English second.

Covers research papers, reports, proposals, website copy, READMEs and commit messages,
video scripts, ads, brochures, pamphlets, emails, CVs, and slides.

It does not promise AI-detector or Turnitin scores, and it will not disguise someone
else's work. See [references/boundaries.md](references/boundaries.md).

## Install

**Claude Code (personal):**
```bash
git clone https://github.com/bryankwandou/lugas ~/.claude/skills/lugas
```

**Claude Code (one project):** copy the folder to `.claude/skills/lugas` in the repo.

**Claude.ai:** zip the folder and upload it under Settings → Capabilities → Skills.

**Other models (GPT, Gemini, etc.):** paste `SKILL.md`, then the pattern file for your
language, `references/genres.md`, and `references/checklist.md` into the system prompt.
About 4,000 tokens total.

## Use

Just ask: "rapikan paragraf ini, terlalu AI", "tulis copy landing page untuk ...",
"make this README less robotic". Or call `/lugas` explicitly.

## Layout

```
SKILL.md                     workflow (loaded first)
references/boundaries.md     what it won't do
references/patterns-id.md    Indonesian patterns and rebuild rules
references/patterns-en.md    English patterns and rebuild rules
references/genres.md         12 genre sections
references/checklist.md      final quality gate
references/adding-a-language.md
examples/                    before/after pairs
```

## License

MIT
