# Stiff Patterns — English

Each entry: **pattern → problem → replacement**. Not an absolute ban list. One apt use is
fine. Remove reflexive, repeated, or empty uses.

## §1 Throat-clearing openers (delete)

- "In today's fast-paced / digital / ever-evolving world, ..."
- "In the realm of ..." / "When it comes to ..."
- "It's important to note that ..." / "It's worth mentioning that ..."
- "Let's dive in." / "Let's explore ..." / "Buckle up."
- "Whether you're a beginner or an expert, ..."
- "Have you ever wondered ...?" (as a default opener)
- "Great question!" / "Certainly! Here is ..."

## §2 Filler words and stock vocabulary

| Pattern | Replace with |
|---|---|
| delve, dive deep, unpack | look at, examine, explain |
| leverage, utilize | use |
| harness the power of | use |
| navigate (challenges, the landscape) | handle, deal with |
| landscape, realm, tapestry, ecosystem (non-technical) | market, field, area — or cut |
| robust, seamless, cutting-edge, state-of-the-art, game-changer | say what it does |
| elevate, empower, unlock, supercharge | name the result |
| crucial, pivotal, vital, paramount (repeated) | important — or show why |
| meticulous, intricate, nuanced | cut or give the detail |
| a testament to | shows |
| plays a crucial role in | affects, decides, drives |
| in order to | to |
| due to the fact that | because |
| very, really, truly, incredibly | cut or quantify |
| moreover, furthermore, additionally (starting every paragraph) | also, and — or nothing |
| "not only X but also Y" (repeated) | use once, or split |
| "It's not just X — it's Y." | state Y |

## §3 Structural tells

1. **Rule-of-three reflex.** Triplets everywhere. Use the real count.
2. **Uniform paragraphs.** Same length, same shape. Vary.
3. **Mini-conclusion after each paragraph.** "Ultimately, this makes X essential." Cut.
4. **Headers and bullets in conversational text.** Emails and captions don't need them.
5. **Bold on random phrases.** Bold only what a skimmer must see.
6. **Em-dash overload.** Two per page is plenty. Use commas, periods, parentheses.
7. **"In conclusion" recap** outside formal papers. Cut.
8. **Colon reveals.** "The secret? Consistency." Once per piece at most.
9. **Hedging stacks.** "may potentially help to somewhat improve". One hedge, max.

## §4 Tone

- Fake enthusiasm: "Exciting news!", "You'll love this!"
- Sycophancy in replies: "What a great idea!"
- Condescension: "Simply do X" when X is not simple.
- Vague authority: "Experts say", "Studies show" with no source. Name it or cut it.

## §5 Rebuild rules

1. Active voice, actor first, unless the actor is unknown or unimportant.
2. Verbs over nouns: "make a decision" → "decide".
3. Sentences over ~25 words in web/marketing copy: split.
4. Specific over general: numbers, names, examples.
5. Contractions are fine in copy, emails, docs. Avoid in formal papers.
6. Match spelling variant to audience (US/UK) and keep it consistent.
7. Short sentences for emphasis. Not every time.

## §6 Research-backed additions (September 2026)

Each entry is tagged with its source in `literature.md`. These are editing targets
because they make text worse for a reader. None of them is a way to move a detector
score, and the skill does not use them that way (`boundaries.md`).

| Pattern | What the research found | Fix |
|---|---|---|
| **Noun pile-up.** "The implementation of the optimisation of the process" | Instruction-tuned models keep a noun-heavy, informationally dense style even when asked to sound informal [lit: Reinhart 2024]; ChatGPT essays use more nominalisations [lit: Herbold 2023] | Turn nouns back into verbs: "we optimised the process" |
| **No epistemic markers.** Every claim stated flat, no "probably", "in our sample", "we think" | ChatGPT essays have fewer discourse and epistemic markers than student essays [lit: Herbold 2023]; human scientists use "but", "however", "although" more [lit: Desaire 2023] | Put the hedge where the evidence is actually uncertain, once. §3.9 (no hedge stacks) still holds |
| **Confident tone without support** | Verbalised LLM confidence is overconfident [lit: Xiong 2023]; only 58% of atomic facts in ChatGPT biographies were supported [lit: Min 2023] | Every confident factual sentence needs a source, a number from the user, or `[figure?]` |
| **Generic terminology instead of the case at hand** | Human medical texts were more concrete and specific; ChatGPT used general terms [lit: Liao 2023]; reviewers found suspected AI abstracts "vaguer and more formulaic" [lit: Gao 2023] | Replace the category word with the instance: not "stakeholders" but "the three ward nurses" |
| **Politeness and no feeling** | Explained classifier: ChatGPT reviews are polite, lack specific details, impersonal, rarely express feeling [lit: Mitrović 2023] | In reviews, emails, personal statements: one real reaction, stated plainly |
| **Uniform sentence length** | Human news shows more scattered sentence lengths and more varied vocabulary [lit: Muñoz-Ortiz 2023] | Keep §5.7; let one sentence in a paragraph run long and one be very short |
| **Cheerful, emotion-flattened register** | LLM news shows less fear and disgust, more joy [lit: Muñoz-Ortiz 2023]; ChatGPT dialogue scores higher on positive tone [lit: Sandler 2024] | Keep bad news bad. Do not add an upbeat closing line to a negative message |
| **Padding for length** | RLHF reward gains are largely length [lit: Singhal 2023]; LLM judges prefer longer answers [lit: Saito 2023; Dubois 2024] | Longer is not better. Cut to what the reader needs |
| **Agreeing with the user's framing** | Assistants are consistently sycophantic [lit: Sharma 2023; Perez 2022] | In rewrite mode keep the user's claims, but do not add praise of the user's idea (§4) |
| **Canned templates across sections** | Models reuse syntactic templates from pre-training (76% of templates vs 35% for human text) [lit: Shaib 2024] | If three sections open with the same grammatical frame, rebuild two of them |
| **Famous tell words** (delve, intricate, underscore) | Rose sharply in scientific abstracts after ChatGPT [lit: Kobak 2024; Juzek 2024] | Keep §2, but see the caution below |

**Caution on word lists.** After "delve" became notorious its use fell, while other
LLM-favoured words kept rising [lit: Geng 2025]. Deleting famous words and keeping the
structure produces text that still reads as generated. Word lists age; the substance
rules (§5.4, `structure-tells.md`) do not.
