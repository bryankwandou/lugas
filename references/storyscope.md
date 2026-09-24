# StoryScope in full: the 30 core features, the fingerprints, and how to use them

Source: Russell, Rajendhran, Pham, Iyyer & Wieting, *StoryScope: Investigating
idiosyncrasies in AI fiction*, arXiv:2604.03136v6 (10 Aug 2026), **COLM 2026**.
University of Maryland + Google DeepMind. Local copy:
`research/storyscope-2604.03136v6.pdf`. Every number below was read from that PDF
(section or table given). `structure-tells.md` is the short version; this is the
long one. Load this file when the text is narrative, when the user asks *why* a
structural rule exists, or when the short version does not settle a case.

---

## 1. What the paper did, in six lines

1. **Corpus.** 10,272 human short stories from Books3. For each, Gemini 2.5 Flash
   reverse-engineered a writing prompt; five models wrote to that prompt (Claude
   Sonnet 4.6, GPT-5.4, DeepSeek V3.2, Gemini 3 Flash, Kimi K2.5). 61,608 stories,
   mean 4,753 words. Models refused 24 stories. (§2, fn. 8)
2. **Template.** GPT-5.1 converted each story to a JSON outline over ten NarraBench
   dimensions: Agent, Social Network, Event, Plot, Structure, Setting, Time,
   Revelation, Perspective, Style. (§2.1, Fig. 8)
3. **Discovery.** On a held-out pool of 600 stories (100 prompts × 6 sources), GPT-5.1
   compared the six outlines per prompt and proposed closed-form features; three runs,
   408 candidates, embedding dedup at cosine 0.85 → **304 features** (124 categorical,
   59 ordinal, 45 scale, 44 binary, 32 multi-select). (§2.1)
4. **Assignment.** Gemini 3 Flash scored every story on all 304 features.
   Repeatability over 5 runs: Krippendorff's α = 0.90; agreement with humans on 240
   items: Cohen's κ = 0.84. (fn. 14)
5. **Classifier.** XGBoost + bootstrap SHAP (B = 50). Features sorted into **core**
   (30: stable, gap ≥ 0.20, holds across all five models), **fingerprint** (75:
   concentrated in one source), or excluded. (§2.2, App. D)
6. **Test.** 8,262 held-out stories, grouped by prompt so no prompt leaks.

## 2. The results that matter for a writer

| Result | Number | Where |
|---|---|---|
| Human vs AI, narrative features only (no style) | **93.2 %** macro-F1 | Table 2 |
| Same, narrative + style | 96.0 % | Table 2 |
| Style features alone | 85.8 % | Table 2 |
| 30 core features alone | 84.8 % | Table 2 |
| After style edit (LAMP rewrite of 278 Gemini stories) | **93.9 %**, from 95.5 % unedited: −1.6 points | §4.2 |
| Six-way attribution, narrative only | 68.4 % (chance 16.7 %) | Table 3 |
| Human rarity percentile vs AI | 0.71 vs 0.49; Cohen's d = 0.83 | §5 |
| Human story is the rarest of its six versions | 57.8 % of prompts (chance 16.7 %) | §5 |
| In the rarest 10 % corpus-wide | 24.7 % of human stories vs 7.1 % of AI | §5 |
| Human–AI centroid distance vs AI–AI | 6.6 vs 4.3 | §5 |
| Length-matched test | narrative model unchanged at 93.2 % | App. G, Table 11 |
| By topic (six topics) | no significant difference, H = 4.69, p = 0.46 | App. G |
| Memorised stories dropped | results unchanged (93.18 → 93.23) | App. F |
| Text baselines (ModernBERT, TF-IDF) | ≥ 99.5 %; Binoculars zero-shot only 55.9 % | Table 2 |

Four readings for this skill:

- **Structure is its own signal, and it survives wording edits.** Rewriting the
  sentences leaves the shape. The re-prompt loop ("bikin lebih natural" again and
  again) is the user feeling a residue that another wording pass cannot reach.
- **No single habit carries it.** Trained on one dimension, the best reaches 80.2 %
  (Agents); removing any one dimension costs at most 1.2 points. The signal is
  *redundant across dimensions* (App. E, Table 8). Fixing one habit does not change
  the shape; the pass in `structure-tells.md` §3 works because it touches several.
- **The five models share one region.** Machine stories cluster together; human
  stories are spread wider (radius 33.2 vs 27.4) and sit in rarer places. The fault is
  not any single choice. It is that the model makes the *most likely* choice on every
  axis at once.
- **Detectors still read wording better.** Supervised raw-text classifiers hit
  ≥ 99.5 %. That is why `boundaries.md` refuses score promises: no craft pass removes
  that layer, and it is not this skill's job to try.

## 3. The 30 core features, with human and AI values

From Table 16 (grouped by theme) and Tables 14–15 (definitions). *s* = 1–5 scale
(mean), *o* = ordinal (mean code), % = share of stories with that option. Gap =
human − AI. Prose readings of the same numbers come from §4.1.

### 3a. AI-elevated: thematic over-determination

| Feature | Question it asks | Human | AI |
|---|---|---|---|
| Thematic explicitness & moralizing (s) | how explicitly are theme/moral stated? | 3.28 | 3.94 |
| Moral/philosophical weighting (s) | how much are moral questions foregrounded? | 3.26 | 3.68 |
| Thematic unity (s) | do subplots and flourishes all serve one theme? | 4.41 | 4.74 |
| Narratorial thematic commentary = yes | does the narrator comment on theme directly? | 52 % | 77 % |
| Dialogue function = philosophical debate | is dialogue used to argue ideas? | 34 % | 59 % |
| Reference explicitness = implicit echoes | are references vague allusions? | 50 % | 72 % |

**Writer's reading.** The text tells the reader what it means, keeps everything on
one theme, and uses speech to argue that theme. Non-fiction form: the "Hal ini
menunjukkan bahwa …" sentence after every data point; the quote that restates the
thesis.

### 3b. AI-elevated: sensory and embodied performance

| Feature | Human | AI |
|---|---|---|
| Emotional expression = embodied metaphor | 38 % | 81 % |
| Setting as psychological mirror (s) | 3.58 | 4.07 |
| Environmental/ecological emphasis (s) | 2.83 | 3.21 |
| Sensory modalities include olfactory | 57 % | 82 % |
| Sensory density (s) | 3.66 | 3.93 |
| Depth of interior access (s) | 3.67 | 3.93 |

**Writer's reading.** Feelings are routed through chests, throats and breath; weather
and rooms mirror moods; there is always a smell. "Show, don't tell" is now the
machine default. Humans *name* the emotion 29 % of the time vs 8 % for AI
(§4.1, Table 16).

### 3c. AI-elevated: structural streamlining

| Feature | Human | AI |
|---|---|---|
| Continuity of main causal chain (s) | 3.92 | 4.20 |
| Spatial granularity (o) | 2.27 | 2.53 |
| Resolution driven by protagonist's choice | 46 % | 69 % |
| Character introduced by external description | 30 % | 52 % |
| No subplots | 57 % | 79 % |
| Resolution by internal understanding/acceptance | 27 % | 47 % |
| Opening spatial grounding (o) | 2.12 | 2.33 |
| Investment built before major threat (s) | 2.76 | 2.99 |

**Writer's reading.** One unbroken cause-and-effect line; the opening sets the scene
carefully; the hero is introduced by a description of how they look; stakes arrive
only after a long warm-up; and the problem is solved by the hero deciding or
accepting something. Nothing happens *to* the story from outside.

### 3d. Human-elevated: intertextual richness

| Feature | Human | AI |
|---|---|---|
| Intertextual strategy includes an explicitly named reference | 47 % | 24 % |
| Reference explicitness = balanced mix of explicit and implicit | 37 % | 16 % |

### 3e. Human-elevated: reader engagement

| Feature | Human | AI |
|---|---|---|
| Fourth-wall permeability (o) | 0.67 | 0.39 |
| Direct reader address (o) | 0.28 | 0.07 |

§4.1 reports the binary forms: breaks the fourth wall 67 % vs 39 %, addresses the
reader 28 % vs 7 %.

### 3f. Human-elevated: temporal complexity

| Feature | Human | AI |
|---|---|---|
| Depth of recontextualization after a surprise (s) | 3.28 | 2.95 |
| Chronological discontinuity (s) | 2.40 | 2.12 |
| Nonlinear framing to delay disclosure (s) | 1.96 | 1.68 |
| Anachrony intensity — flashback/flash-forward (s) | 2.58 | 2.31 |

**Writer's reading.** Humans reveal things that change how earlier scenes read, and
use time jumps to hold information back. "A human mystery might open at the funeral
and spiral backward through decades, while AI tells the same story from first clue
to the grand reveal" (§4.1).

### 3g. Human-elevated: narrative diversity

| Feature | Human | AI |
|---|---|---|
| Location variety (o) | 1.34 | 1.08 |
| Dialogue-to-narration proportion (s) | 2.95 | 2.70 |
| Subplots thematically parallel to the main line | 42 % | 21 % |
| Protagonist framed as morally ambivalent/mixed | 59 % | 38 % |
| Emotion named with an explicit label | 29 % | 8 % |

## 4. Fingerprints (Table 17, §5)

Count of fingerprint features: Human 32, Claude 26, GPT 11, Gemini 11, DeepSeek 7,
Kimi 3. Per-class F1, narrative only: Human 0.89, Claude 0.77, GPT 0.73, Gemini 0.60,
DeepSeek 0.57, Kimi 0.55 (Table 12).

| Source | Top fingerprints (Table 17 + §5 prose) | Check in your own draft |
|---|---|---|
| **Human** | characters introduced *in dialogue*; single focal character; no direct narrator address in that mode; **back-loaded revelation**; crossover-genre ambition; plus withholding, atmosphere, subplot density, naming, twist placement | — this is the target direction, not a template |
| **Claude** | **weakest event escalation** of any source; low event-type diversity; ending that jumps forward (epilogue/flash-forward); no dreams or visions; uncanny/haunted setting mood; plus event density, conflict modality, relationship trajectory, heteroglossia (uniform voice), closure. Reverent/continuist toward tradition 62 % vs 39–56 %; "quiet endings over avalanche endings" | Do the stakes actually rise? Are all events of the same kind? Is there an epilogue nobody asked for? Does every character sound like the narrator? |
| **GPT** | gossip/rumour as plot engine 64 % vs 44–55 %; narrator looking back from years or decades; no habitual/iterative narration; subverts expectations 41 % vs 27–36 %; partial/ambiguous reconciliation; ensemble casts | "Looking back, it all started…" frames; twists for their own sake |
| **Gemini** | protagonist's social circle expands; speech mostly direct; siege/ordeal schema; everyone named; frequent flashbacks; tidiest endings and long denouements; bleakest settings (88 % bleak/oppressive); external character description | an ending that keeps ending; unearned gloom |
| **DeepSeek** | visible narrator presence; emotion via behavioural cues; plot vs atmosphere balance; backstory **evenly interleaved**; embedded storytelling scenes; front-loads context | explanation before anything happens |
| **Kimi** | introduces characters in action; opens in medias res; avoids explicit trait labels; otherwise the generic centre | competent and shapeless |

Most confused pairs are all AI–AI (Gemini↔DeepSeek 222 and 207 stories); the most
common human error (Human→Kimi) is 46 (§5, Fig. 3).

## 5. The self-audit: an outline pass adapted from the paper's template

The paper's first stage is useful on its own. Before revising a narrative over ~1,000
words, fill this outline from the *draft* (not from the plan). Where a field comes
out empty, flat, or single-valued, that is where the draft sits in the machine
cluster. Adapted from Fig. 8; the questions in the right column are this skill's,
not the paper's.

| Field (Fig. 8) | Fill in | Red flag |
|---|---|---|
| agents: emotion trajectory per major character | start → change → end | every trajectory ends in acceptance or understanding |
| agents: how each is introduced | description / action / dialogue / others' report | all introduced by physical description |
| social network: relationships | A–B: type and quality | nothing changes between anyone |
| events: causality | event1 → event2: why | a single unbroken chain; nothing from outside |
| events: sequence, by kind | list the kinds of event | all events of one kind, at one intensity |
| plot: moral | one sentence if signalled | the narrator states it outright |
| plot: subplots | list | none, or none that echo the main line |
| setting: locations | list | one or two, each mirroring a mood |
| revelation: surprises and when | what, where | no surprise changes an earlier scene |
| time: structure | linear / nonlinear / mixed | linear from first clue to reveal |
| perspective: focalization, dialogue speakers | per scene | every voice sounds like the narrator |
| style: allusions | list | only vague allusions, nothing named |

Fix at most three red flags per pass, starting with the ones in `structure-tells.md`
§3. Never fill a red flag with an invented fact (`boundaries.md` §4): a named book,
town, or event must come from the user or be marked `[isi: ...]`.

## 6. How far the evidence reaches

- **Measured:** English literary short fiction, ~5,000 words, five specific model
  versions from early 2026. Topic did not change detectability; length did not either.
- **Not measured:** non-fiction, non-English text, short texts, hybrid human–AI
  drafts. The authors do not claim these. Use sections 3–5 as craft guidance there.
- **Not a target list.** Hitting the human column on every feature does not make a
  text human, and nothing here predicts a detector score. The features name habits
  that make stories predictable; removing them is a quality fix.
- **Model versions age.** GPT-5.4 cut its em-dash rate (§1). Fingerprints will move
  faster than core features; core features are the part the authors expect to last.

## 7. What changed in this skill because of this file

- `structure-tells.md` §1 now lists habits 8–11 (character introduced by
  description, setting as mood mirror, linear time with no recontextualization,
  long warm-up before stakes) with the Table 16 numbers.
- `structure-tells.md` §2 fingerprint table extended from Table 17.
- `checklist.md` structural gate gained the matching soft-fail items.
- The sentence "detection did not drop a full point" was corrected: the drop was 1.6
  points (95.5 → 93.9) on 278 LAMP-edited Gemini stories.
