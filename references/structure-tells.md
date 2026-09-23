# Structure Tells — the layer under the words

Load this for any text longer than ~300 words, and always for narrative
(fiction, video script, case study, company story, personal statement, essay).

## Why this file exists

Until now this skill worked at the sentence layer: kill filler, cut stock phrases,
vary length. That layer is real but it is not where the strongest tells live.

Russell, Rajendhran, Pham, Iyyer & Wieting (2026), *StoryScope: Investigating
idiosyncrasies in AI fiction* (arXiv:2604.03136, University of Maryland + Google
DeepMind) built a classifier that reads **only** discourse-level narrative features —
no wording, no vocabulary, no sentence statistics — across 61,608 stories of ~5,000
words each from 10,272 prompts, one human version and five model versions each.

Two results matter for this skill:

1. **Structure alone separates human from machine at 93.2% macro-F1.** Narrative
   features carry ~97% of the signal that a full stylistic model gets.
2. **Editing the style away does not help.** When stories were deliberately rewritten
   to strip style tells, detection stayed at 93.9% — it did not drop a full point.

So: a text can pass every item in `patterns-id.md` and `patterns-en.md` and still read
as machine-written, because the *shape of the thinking* is unchanged. Paraphrasing
harder is not the fix. Restructuring is.

This is also why the user keeps re-prompting. They feel the residue and reach for
"bikin lebih natural" again, but the next pass only re-shuffles words.

**Read this file as craft advice, not as evasion advice.** These habits are named
because they make writing worse: over-explained, frictionless, closed. Fixing them
serves the reader. `boundaries.md` still holds — this is not a detector-defeat guide,
and no edit can promise a score.

---

## §1 The seven habits, with the measured gap

Numbers below are from StoryScope: AI rate vs. human rate on the same prompts.
They are evidence that a habit is systematic, not a target to hit.

### 1. Over-explanation of the theme — **77% vs. 52%**

The single largest gap. The narrator states the meaning instead of letting the material
carry it. In non-fiction this is the paragraph that tells the reader what they just
learned, the sentence after an anecdote that spells out the moral, the "Hal ini
menunjukkan bahwa ..." that restates the data one line below the data.

**Fix:** delete the sentence that explains. If the point does not survive the deletion,
the material before it is too thin — strengthen that instead of narrating it.

> Jarak tempuh turun dari 14 hari ke 3 hari. ~~Hal ini menunjukkan bahwa digitalisasi
> proses memberikan dampak signifikan terhadap efisiensi layanan.~~

### 2. Dialogue and quotes as philosophy — **59% vs. 34%**

Characters (or interviewees, or customers) speak in order to articulate the text's
thesis. Nobody talks past each other, changes the subject, or says something merely
practical. In a case study this is the quote that happens to summarize your value
proposition in your own vocabulary.

**Fix:** let a quote be specific and partial. People say small concrete things.
If every quote lands the thesis, keep one and cut the rest.

### 3. Single-track plot — **79% "no subplots" vs. 57%**, subplots integrated **21% vs. 42%**

One thread, one question, opened and closed. No side matter, no thread that is raised
and left, nothing that complicates the main line. In a report this is the section list
where every section advances the argument and nothing records an inconvenient finding.

**Fix:** keep the thing that does not fit. A limitation that has no resolution, a
finding that cuts against the conclusion, a detail that is there because it happened.
One unresolved thread is worth more than three resolved ones.

### 4. Everything resolves from inside the protagonist — **69% vs. 46%**, internal resolution **47% vs. 27%**

The problem is solved by the main subject deciding, realizing, or growing. No luck, no
external decision, no institution, no other person acting on their own reasons.

**Fix:** name what was outside your control. In a laporan magang: the supervisor who
reassigned you, the vendor who was late, the scope that changed. That is what a real
account looks like.

### 5. Moral flatness — ambivalent protagonist **38% vs. 59%**

Human writing frames choices as costly: the right decision damages something. AI
writing frames choices as correct. This is the "every trade-off was actually a win"
texture that makes a proposal or a reflection read as PR.

**Fix:** for the main decision in the text, write down what it cost. Put that in.

### 6. Emotion routed through the body — **81% vs. 38%**; smell imagery **82% vs. 57%**; named emotion **8% vs. 29%**

A strong counter-intuitive one. "Show don't tell" has been absorbed so completely that
pounding hearts, tight chests, and the smell of rain are now the machine default,
while human writers just say the person was angry roughly three times more often.

**Fix:** name the emotion plainly sometimes. Cut the somatic paragraph. The advice
"don't say sad, show sad" is now, statistically, advice to sound like a model.

### 7. A closed world — cites a specific work **24% vs. 47%**; breaks frame **39% vs. 67%**; addresses the reader **7% vs. 28%**

Human text leaks: it names the actual book, the actual town, the actual price, the
actual Tuesday. It steps outside itself. AI text is self-contained and generic —
"a local restaurant", "a popular framework", "recent studies".

**Fix:** replace every generic noun with the real one, or mark `[isi: nama ...]`.
Never invent the specific — `boundaries.md` §4 is absolute. An honest `[isi: ...]`
is better than a plausible invention, always.

---

## §2 Model fingerprints

StoryScope also attributes authorship 6 ways at 68.4% macro-F1. Each model has its own
habits. Know your own.

| Model | Fingerprint | What to watch for in your own output |
|---|---|---|
| **Claude** | Flattest event escalation; uniform narrative voice; reaches for epilogues; honors literary tradition (62% vs. 39–56%); avoids dream sequences | Stakes that never actually rise. A tidy closing section nobody asked for. Reverent, evenly-modulated tone throughout. |
| **GPT** | Gossip/rumor as plot engine (64% vs. 44–55%); retrospective framing across years; ensemble casts; subverts expectations (41% vs. 27–36%) | "Looking back, it all started when…" framing. A twist inserted for its own sake. |
| **Gemini** | Characterizes from outside; tidiest endings and long denouements; bleakest settings (88% tagged bleak/oppressive) | Description that never enters a head. An ending that keeps ending. Unearned gloom. |
| **DeepSeek** | Front-loads crucial context | Everything explained before anything happens. |
| **Kimi** | Generic center, fewest distinctive choices | Competent and shapeless. |

Claude's is the one that matters here, and it is the hardest to feel from the inside:
**flat escalation and an epilogue that closes what should stay open.** Before
delivering anything narrative, check those two specifically.

---

## §3 The structural pass

Run this after step 4 (Rebuild) in `SKILL.md`, before the checklist. It takes a minute
and it is the pass that stops the re-prompt loop.

1. **Find the explaining sentences.** Every place the text tells the reader what to
   conclude from what it just said. Delete them. Usually 3–8 in a 1,500-word piece.
2. **Find the unresolved thread.** If there is none, the text is lying by omission.
   Ask the user for one or mark `[isi: kendala/temuan yang tidak selesai]`.
3. **Find the cost.** The main decision or recommendation — what does it damage? Say so.
4. **Find the outside.** Who or what acted from beyond the subject's control? Name it.
5. **Count the generics.** Every "sebuah perusahaan", "berbagai pihak", "studi terkini"
   becomes a real name or an `[isi: ...]`.
6. **Check escalation.** Section 4 should carry more weight than section 2. If the
   sections are interchangeable in intensity, the piece is flat.
7. **Kill the epilogue.** If the last section only restates, and the genre does not
   require a summary (see `genres.md`), cut it.

If a rewrite passes all of §3 but the wording is still mediocre, fix the wording.
If it passes `patterns-*.md` but fails §3, the wording pass was wasted work.

---

## §4 Where this does and does not transfer

StoryScope measured ~5,000-word fiction. Be honest about the reach:

- **Direct transfer:** fiction, narrative video script, case study, company/founder
  story, personal statement, essay, reflective sections of a laporan magang.
- **Partial transfer:** research papers and reports. Habits 1, 3, 5, 6 apply
  (over-explanation, no loose ends, no cost, no specifics). Habits 2, 4, 7 mostly do
  not — a paper *should* close its argument.
- **Weak transfer:** captions, ads, commit messages. Too short for discourse structure.
- **Unmeasured by the paper:** hybrid human-AI drafts, non-fiction, non-English.
  The authors say so themselves. Treat §1 as craft guidance there, not as measurement.

The paper's own corpus is English. Nothing in §1 is lexical, so the habits carry across
languages — but the evidence does not. Do not quote these percentages at a user as if
they were measured on Indonesian text.

---

## §5 Wider evidence for the structural layer (September 2026)

StoryScope is not alone. Sources in `literature.md`, tagged `[lit: ...]`.

- **Structure is where human writing varies.** Human texts show more variability in
  hierarchical discourse structure than LLM texts, and discourse features kept working
  on paraphrased samples [lit: Kim 2024]. Same conclusion as StoryScope by a different
  method: rewording leaves the skeleton.
- **Plots repeat across generations.** Stories from the same prompt reuse combinations
  of plot elements [lit: Xu 2024]; LLM stories are lower in novelty and surprise
  [lit: Ismayilzada 2024] and pass 3-10x fewer expert creative-writing tests than
  professional stories [lit: Chakrabarty 2023]. Habit 3 (single-track plot) and
  habit 7 (closed world) are the local form of this.
- **Professional editors name the same faults.** Writers editing LLM paragraphs agreed
  on a taxonomy that includes clichés and unnecessary exposition [lit: Chakrabarty
  2024]. Unnecessary exposition is habit 1.
- **Coherence is what careful readers notice.** People detecting generated text in
  groups most often cited lack of coherence and consistency [lit: Uchendu 2023]. Before
  the seven habits, check that names, numbers and claims agree from start to end.
- **Counterweight.** On a reader-centred depth scale, GPT-4 stories matched highly
  rated Reddit stories [lit: Harel-Canada 2024], and non-experts preferred AI poems
  [lit: Porter 2024]. The structural pass is craft for a demanding reader, not a claim
  that machine text is always worse.
- **Transfer caution stays.** These studies are almost all English. §4 still applies.

## Source

Local copies: `research/storyscope-2604.03136v6.pdf`.
Notes and the wider literature: `references/research-basis.md`.
