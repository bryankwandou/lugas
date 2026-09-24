# Research basis

Why the rules in this skill are what they are, and where they came from.

**Honesty note, and it matters.** Every entry below was retrieved and checked before it
was written down. There is no padded bibliography here. `boundaries.md` §4 forbids
inventing citations, and that rule binds this file first — a skill that fakes its own
references has no standing to tell anyone else not to. Where a claim is the skill's own
judgement rather than a finding, it says so.

Entries are grouped by what they changed in the skill.

---

## A. The structural layer (`structure-tells.md`)

**Russell, J., Rajendhran, R., Pham, C. M., Iyyer, M., & Wieting, J. (2026).
StoryScope: Investigating idiosyncrasies in AI fiction.** arXiv:2604.03136.
University of Maryland & Google DeepMind. Code: github.com/jenna-russell/storyscope
PDF: <https://arxiv.org/pdf/2604.03136v6>

The paper this skill's biggest revision is built on.

- **Method.** Ten narrative dimensions adapted from NarraBench (Agent, Social Network,
  Event, Plot, Structure, Setting, Time, Revelation, Perspective, Style; Paratext and
  Motivation dropped for lack of external context). Stories → structured JSON per
  dimension. A 600-story discovery pool (100 prompts × 6 sources) analysed pairwise by
  GPT-5.1 at high reasoning effort; 10 per-dimension expert prompts proposed 408
  candidate features; embedding dedup at cosine 0.85 merged 65 clusters down to **304
  features**. Assignment across the full corpus by Gemini 3 Flash; importance by XGBoost
  with bootstrap SHAP (B=50), sorting features into *core*, *fingerprint*, or *excluded*.
- **Corpus.** 10,272 prompts, human version (Books3) + five models
  (Claude Sonnet 4.6, GPT 5.4, DeepSeek V3.2, Gemini 3 Flash, Kimi K2.5) =
  **61,608 stories**, ~5,000 words each.
- **Results.** 93.2% macro-F1 human-vs-AI on narrative features alone — ~97% of what a
  style-inclusive model reaches. 68.4% macro-F1 on 6-way attribution. Under adversarial
  style editing, detection held at **93.9%**.
- **Effect on this skill.** Added `references/structure-tells.md` and step 4.5 in
  `SKILL.md`. Before this, the skill only had word- and sentence-level kill lists. The
  paper's central result is that those are the *weaker* signal and that editing them
  away changes almost nothing — which is a direct explanation for the re-prompt loop
  this skill exists to end.
- **Limits the authors state.** English fiction only; hybrid human-AI drafts and
  non-fiction untested. `structure-tells.md` §4 carries that caveat forward instead of
  overclaiming.

---

## B. Why one more paraphrase pass does not help

**Liang, W., Yuksekgonul, M., Mao, Y., Wu, E., & Zou, J. (2023). GPT detectors are
biased against non-native English writers.** arXiv:2304.02819; *Patterns* 4(7).

Over half of TOEFL essays by non-native writers were misclassified as AI-generated,
against near-perfect accuracy on US 8th-grade essays. Cause: low perplexity from
narrower lexical range. Enriching non-native word choice reduced false positives;
simplifying native text induced them.

- **Effect on this skill.** This is the evidential spine of `boundaries.md`'s refusal to
  promise a detector score. It also matters directly for the primary user base — an
  Indonesian student writing in English is in exactly the misclassified population, and
  a false accusation is not fixed by rewriting. The skill says the number is unreliable
  in both directions and refuses to chase it.

**Stress-testing machine generated text detection: shifting language models' writing
style to fool detectors.** arXiv:2505.24523.
**Exploring the limitations of detecting machine-generated text.** arXiv:2406.11073.
**DetectRL: benchmarking LLM-generated text detection in real-world scenarios.**
arXiv:2410.23746.
**Towards possibilities & impossibilities of AI-generated text detection: a survey.**
arXiv:2310.15264.
**A survey on LLM-generated text detection: necessity, methods, and future directions.**
arXiv:2310.14724.

Converging finding across these: detectors lean on superficial stylistic cues, degrade
out-of-domain, and are sensitive to text complexity. Style-level manipulation moves
their scores.

- **Effect on this skill.** Two things at once. Detector scores are not a quality target
  (`boundaries.md`). *And* the fact that style edits move detectors while StoryScope's
  structural classifier barely moves is the cleanest available argument that structure
  is the deeper layer — which is why `structure-tells.md` runs before the wording gate,
  not after.

**StyleDecipher: robust and explainable detection of LLM-generated texts with stylistic
analysis.** arXiv:2510.12608.
**Diversity boosts AI-generated text detection.** arXiv:2509.18880.

Relevant mechanism: AI text is sampled from a narrower conditional distribution, giving
higher token confidence and lower lexical diversity. Classifiers do best on narrow-
vocabulary text and worst on rich-vocabulary text.

- **Effect on this skill.** Supports the rebuild rules in `patterns-*.md` §5 for a reason
  better than taste: range is a property of thought, not decoration. It does *not*
  license random synonym-swapping to raise diversity — that is explicitly banned in
  `boundaries.md` §1 and makes text worse.

---

## C. Homogenization — why "it reads fine" is not enough

**Padmakumar, V., & He, H. (2023). Does writing with language models reduce content
diversity?** arXiv:2309.05196.

Controlled experiment on argumentative essays: writing with an instruction-tuned model
significantly reduced content diversity versus unaided writing. Feedback-tuned models
reduced it more than base models.

**Homogenizing effect of large language models on creative diversity: an empirical
comparison of human and ChatGPT writing.** *Journal of Creativity* (Elsevier),
ScienceDirect S294988212500091X.

**Doshi, A. R., & Hauser, O. P. — collective vs. individual creativity.** Reported in
the above line of work: human writing expanded the collective semantic diversity of a
corpus roughly **two to eight times** more than GPT-4 writing, even where individual
GPT-4 pieces rated higher.

**Chakrabarty, T. et al. / Evaluating creative short story generation in humans and
large language models.** arXiv:2411.02316.

LLM stories are stylistically complex but fall short on novelty, surprise, and
diversity. Sharpest finding for this skill: **LLMs and non-experts rate LLM stories as
more creative than human ones; expert ratings track the automated metrics instead.**
Non-experts and LLMs are responding to linguistic complexity; experts respond to
semantic complexity.

- **Effect on this skill.** This is the most uncomfortable entry here, and the reason
  for step 5 being a written gate rather than a vibe check. A model judging its own
  output — this skill, checking its own work — sits squarely in the population that
  systematically overrates machine text. The checklist is not bureaucracy; it is the
  correction for a known bias in the grader.

**LLMs exhibit significantly lower uncertainty in creative writing than professional
writers.** arXiv:2602.16162.
**Narrative flattening: how post-training compresses thematic, affective, and stylistic
variation in LLM fiction.** arXiv:2605.27878.
**Epistemic diversity and knowledge collapse in large language models.** arXiv:2510.04226.
**Argument collapse: LLMs flatten long-form public debate.** arXiv:2606.01736.
**Does AI homogenize student thinking? A multi-dimensional analysis of structural
convergence in AI-augmented essays.** arXiv:2603.21228.
**The limits of automatic evaluation of creativity in large language models.**
arXiv:2608.23705.

Independent corroboration of StoryScope's core claim from a different angle: the
flattening is thematic and structural, it is introduced or worsened by post-training,
and it shows up in student essays as *structural* convergence.

- **Effect on this skill.** Confirms the flatness is a property of the model, not of a
  careless prompt — so it cannot be fixed by asking more nicely. `structure-tells.md` §3
  is a mechanical pass for that reason.

---

## D. What homogenization costs a non-native writer

**Can we still hear the accent? Investigating the resilience of native language signals
in the LLM era.** arXiv:2604.08568.

Scientific writing is converging toward standardized English; native-language signal
detection rates dropped over 10% post-LLM. The traces of a researcher's linguistic
background are being smoothed away.

**Divergent LLM adoption and heterogeneous convergence paths in research writing.**
arXiv:2504.13629.

GPT adoption improves textual quality while converging writing style across researcher
groups.

**Four types of LLM reliance and their predictors among undergraduate writers.**
arXiv:2606.28749.
**Human thinking under plural LLM assistance.** arXiv:2604.02677.

- **Effect on this skill.** Directly motivates rule 9 of §4 in `SKILL.md` ("keep the
  author's voice") and §4 of `patterns-universal.md` ("do less where fluency is weaker").
  The default failure mode of an editing assistant is to sand an Indonesian writer's
  prose into generic international English and call it an improvement. The measured cost
  of that is a real loss, and it is invisible to the writer at the time. When in doubt,
  the skill leaves the author's choice alone.

---

## E. Sources for the Indonesian and campus-format rules

These are normative documents, not research. They govern `patterns-id.md`, `genres.md`,
and the `pedoman` skill.

- **Pedoman Umum Ejaan Bahasa Indonesia (EYD Edisi V)**, Badan Pengembangan dan
  Pembinaan Bahasa, Kemendikbudristek. The spelling authority behind the non-baku list
  (analisa → analisis, praktek → praktik, resiko → risiko, merubah → mengubah, ijin → izin).
- **KBBI (Kamus Besar Bahasa Indonesia) daring.**
- **Pedoman Umum Pembentukan Istilah** — Lampiran II Kepmendikbud 27 Agustus 1975
  No. 0196/U/1975. Cited by name inside the UAJM guideline itself (§5.5.2) as the rule
  for Indonesianizing foreign terms.
- **Program Studi Teknik Informatika, FTI, Universitas Atma Jaya Makassar (2015).
  Buku Pedoman Penulisan Skripsi / Tugas Akhir.**
- **Program Studi Informatika, FTI, Universitas Atma Jaya Makassar. Pedoman Kuliah
  Kerja Profesi (KKP).**
  Both extracted and encoded in the `pedoman` skill (`references/uajm-fti.md`).
- Guidelines the UAJM pedoman itself cites as its lineage, useful when a rule is
  ambiguous: IPB (2001) *Pedoman Penulisan dan Penyajian Karya Ilmiah*; ITB (2004)
  *Format Penulisan Tesis Magister*; PPs UNHAS (2005) *Pedoman Penulisan Tesis dan
  Disertasi*; UM Press (2000) *Pedoman Penulisan Karya Ilmiah*.

## F. Post-editing, and why the skill edits rather than regenerates

Checked September 2026. These are the papers that decide *how* lugas works, not just
what it flags.

- **Post-editing an LLM draft does not restore a personal voice.** Studies of
  post-edited text find that editing injects real stylistic diversity back into a
  machine draft, but not enough to reach unassisted human writing — and that after
  post-editing, a writer resembles *other people's post-edited text* more than their
  own unassisted writing.
  → This is the strongest argument for the skill's core move: rewrite from the
  meaning, against a named reader, rather than smoothing the existing draft
  sentence by sentence. Smoothing converges; rebuilding does not.
  <https://arxiv.org/abs/2604.24444>

- **"Just fix the grammar" is not a neutral instruction.** Minimal-edit and
  grammar-only prompts still produce measurable semantic drift: the text moves toward
  more formal, impersonal language and first-person expression drops sharply.
  → Why `boundaries.md` treats "rapikan sedikit saja" as a request that must be
  honoured literally, with the edit kept visible, instead of quietly upgrading the
  register.
  <https://arxiv.org/abs/2604.22142>

- **Structural convergence in AI-augmented student essays.** The convergence shows up
  at the level of essay architecture, not word choice — the same finding as
  StoryScope, in an academic register rather than fiction.
  → Supports the structural gate in `checklist.md` applying to coursework and reports,
  not only to narrative.
  <https://arxiv.org/abs/2603.21228>

- **Group-level homogenization even when individuals feel more creative.** Users
  generate more ideas each, while the *set* of ideas across users narrows, because the
  model proposes similar things to different people.
  → Why the skill refuses to offer a "best" opening formula, and why the pattern lists
  are things to avoid rather than templates to reach for.
  <https://www.sciencedirect.com/science/article/pii/S294988212500091X>

- **Lexical homogenization measured in published news.** Detectable narrowing of
  vocabulary in English news articles attributed to widespread LLM use.
  → Evidence that the phenomenon is not confined to lab tasks.
  <https://aclanthology.org/2025.acl-srw.95/>

- **Stylometric distinguishability of AI creative writing.** Each model's output forms
  a tighter cluster than human writing does; individual human voice survives even
  under a fixed prompt.
  → Background for the per-model fingerprints in `structure-tells.md`: the fingerprint
  is a model property, so it persists across topics.
  <https://www.nature.com/articles/s41599-025-05986-3> ·
  <https://arxiv.org/abs/2603.23219>

- **Two-dimensional detection: content versus expression.** Detection improves when
  content and expression are separated, which is the same split the skill uses when it
  keeps the user's claims untouched and rebuilds only the expression.
  <https://arxiv.org/abs/2503.00258>

- **Character variety in generated stories** — a narrower cast, drawn from a smaller
  space of character types, in LLM fiction.
  → Relevant only to narrative genres in `genres.md`; noted so nobody generalises it to
  reports.
  <https://arxiv.org/abs/2606.22454>

Searched and read September 2026. Links are given so a later reader can check whether
a finding held up; several of these are preprints and should be treated as such. When
one is contradicted by later work, change the rule it supports, or delete the rule.

---

## G. The wider literature (added September 2026)

`references/literature.md` now holds 130 further sources, each retrieved and checked
(metadata and abstract) before it was written down. What they changed:

- **`patterns-en.md` §6 and `patterns-id.md` §7.** New targets with measured backing:
  noun pile-up [lit: Reinhart 2024; Herbold 2023], missing epistemic markers
  [lit: Herbold 2023; Desaire 2023], confidence without support [lit: Xiong 2023;
  Min 2023], generic terminology [lit: Liao 2023; Gao 2023], flattened emotion
  [lit: Muñoz-Ortiz 2023], length padding [lit: Singhal 2023], sycophancy
  [lit: Sharma 2023], reused syntactic templates [lit: Shaib 2024].
- **The word-list caution.** Famous tell words fade once people know them, while
  others keep rising [lit: Geng 2025]. This is why the kill lists are "not an absolute
  ban list" and why the structural pass follows them.
- **`patterns-universal.md` §5.** Non-English tells (Japanese function words and
  commas [lit: Zaitsu 2023]), translationese as a trained habit [lit: Li 2025], and
  the Western drift of AI suggestions [lit: Agarwal 2024].
- **`structure-tells.md` §5.** Independent support for the structural layer
  [lit: Kim 2024; Xu 2024; Chakrabarty 2023, 2024], plus counter-evidence
  [lit: Harel-Canada 2024; Porter 2024].
- **The no-score rule, reinforced.** Detectors are fooled by one extra space
  [lit: Cai 2023], by prompting [lit: Lu 2023] and by paraphrase [lit: Krishna 2023;
  Sadasivan 2023], and they flag lightly polished human text as AI [lit: Saha 2025;
  Almohaimeed 2025]. Expert human editing evades them [lit: Artemova 2024]. Watermarks
  can be spoofed [lit: Sadasivan 2023], and strong watermarking is provably impossible
  under stated assumptions [lit: Zhang 2023]. A detector score measures probability,
  not quality. Nothing in the new sources changes `boundaries.md` §1.
- **Why edit rather than regenerate, again.** An LLM asked to rewrite AI text changes
  it little [lit: Mao 2024], and each paraphrase round moves text further from the
  author's own style [lit: Tripto 2023].

**Indonesian gap, stated honestly.** Searches found no peer-reviewed study of the
*style* of AI-written Indonesian. The only Indonesian-specific items are M4's
Indonesian news subset and one national-journal detection study (Alif et al., 2026).
The Indonesian rules remain editorial judgement supported by cross-language findings.

**Tag format.** `[lit: Surname Year]` = first author and year of an entry in
`literature.md`. "Chakrabarty 2023" = *Art or Artifice?* (arXiv:2309.14556, CHI
2024); "Chakrabarty 2024" = *Can AI writing be salvaged?* (arXiv:2409.14509). "Wang 2023" in the
Indonesian notes = M4 (arXiv:2305.14902).

---

## How to use this file

Do not cite it at the user. It exists so that:

1. A rule can be traced to a reason, and changed when the reason changes.
2. A user who asks "kenapa harus begitu?" gets a real answer.
3. Nobody, including a future revision of this skill, adds a rule on vibes.

If you add a rule, add its reason here. If you cannot find a reason, mark it as
judgement and say whose.
