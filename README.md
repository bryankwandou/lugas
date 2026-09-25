# Lugas

Live guide: https://lugaskit.vercel.app (source: github.com/bryankwandou/lugaskit)

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
references/storyscope.md     StoryScope (arXiv:2604.03136) encoded in full
references/literature*.md    515 sources; literature-read.md = checked in full
rangka/                      outlines for any document, 22 Indonesian campuses + foreign
kampus/atmajaya/             UAJM: KKP, proposal, skripsi, sidang (Informatika 2015)
kampus/pedoman/              format checks: 37 Indonesian + 5 foreign institutions
evals/                       real-use test runs
```

Coverage is stated per file. Universities not listed are **not** encoded; the skill
asks for their guideline instead of guessing.

## License

MIT
