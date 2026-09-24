# Literature — annotated bibliography

130 sources on machine-generated text: how it is detected, how it differs from human
writing, what it does to writing at scale, and how human editing changes it. Every entry
was retrieved (Semantic Scholar metadata and abstract, or the publisher page) in
September 2026. Titles, authors, years and venues are copied from those records, not
typed from memory. The finding after each entry comes from the paper's own abstract.

Rules for this file:

- It is background. `research-basis.md` says which rule each source changed; the
  pattern files cite sources by the tag `[lit: first-author year]`.
- Nothing here is a promise about detector scores. Sections A and B exist largely to
  show why the skill refuses to make one (`boundaries.md`).
- Preprints are marked "arXiv preprint". A later paper can overturn one. When that
  happens, fix the rule it supports.
- Sources already annotated in `research-basis.md` (StoryScope, Liang et al. 2023,
  DetectRL, the style-shift stress test, the detection surveys listed there) are not
  repeated here.

Part 2, with 385 further sources in eight more themes, is `literature-2.md`.

## A. Detection methods: what the machines actually measure

- **E. Mitchell, Yoonho Lee, Alexander Khazatsky et al. (2023). DetectGPT: Zero-Shot Machine-Generated Text Detection using Probability Curvature.** International Conference on Machine Learning. <https://arxiv.org/abs/2301.11305>
  LLM samples sit in negative-curvature regions of the model's log-probability; DetectGPT lifts fake-news AUROC from 0.81 to 0.95. The signal is word-choice probability, which a reader cannot see.
- **Guangsheng Bao, Yanbin Zhao, Zhiyang Teng et al. (2023). Fast-DetectGPT: Efficient Zero-Shot Detection of Machine-Generated Text via Conditional Probability Curvature.** International Conference on Learning Representations. <https://arxiv.org/abs/2310.05130>
  Conditional probability curvature: about 75% relative gain over DetectGPT and 340x faster. Again a probability signal, not a visible style.
- **Abhimanyu Hans, Avi Schwarzschild, Valeriia Cherepanova et al. (2024). Spotting LLMs With Binoculars: Zero-Shot Detection of Machine-Generated Text.** International Conference on Machine Learning. <https://arxiv.org/abs/2401.12070>
  Contrasting two related LMs detects over 90% of ChatGPT text at a 0.01% false-positive rate with no ChatGPT training data.
- **Xianjun Yang, Wei Cheng, Linda Petzold et al. (2023). DNA-GPT: Divergent N-Gram Analysis for Training-Free Detection of GPT-Generated Text.** International Conference on Learning Representations. <https://arxiv.org/abs/2305.17359>
  Divergent n-gram analysis: regenerate from a truncated text and compare n-gram overlap; training-free and explainable.
- **Jinyan Su, Terry Yue Zhuo, Di Wang et al. (2023). DetectLLM: Leveraging Log Rank Information for Zero-Shot Detection of Machine-Generated Text.** Conference on Empirical Methods in Natural Language Processing. <https://arxiv.org/abs/2306.05540>
  Log-rank features give zero-shot detection with fewer perturbations than DetectGPT.
- **V. Verma, Eve Fleisig, Nicholas Tomlin et al. (2023). Ghostbuster: Detecting Text Ghostwritten by Large Language Models.** North American Chapter of the Association for Computational Linguistics. <https://arxiv.org/abs/2305.15047>
  Ghostbuster: features from weaker LMs reach 99.0 F1 across essays, creative writing and news.
- **Fatemehsadat Mireshghallah, Justus Mattern, Sicun Gao et al. (2023). Smaller Language Models are Better Black-box Machine-Generated Text Detectors.** arXiv preprint. <https://arxiv.org/abs/2305.09859>
  Smaller, partially trained models are better universal detectors (OPT-125M AUC 0.81 on ChatGPT vs GPT-J-6B 0.45).
- **Xiaomeng Hu, Pin-Yu Chen, Tsung-Yi Ho (2023). RADAR: Robust AI-Text Detection via Adversarial Learning.** Neural Information Processing Systems. <https://arxiv.org/abs/2307.03838>
  RADAR trains a paraphraser and a detector adversarially and beats prior detectors when paraphrasing is present.
- **Xun Guo, Shan Zhang, Yongxin He et al. (2024). DeTeCtive: Detecting AI-generated Text via Multi-Level Contrastive Learning.** Neural Information Processing Systems. <https://arxiv.org/abs/2410.20964>
  Frames detection as telling apart the writing styles of different authors (multi-level contrastive learning); strong out-of-distribution results.
- **Chengzhi Mao, Carl Vondrick, Hao Wang et al. (2024). Raidar: geneRative AI Detection viA Rewriting.** International Conference on Learning Representations. <https://arxiv.org/abs/2401.12970>
  LLMs change human text more than AI text when asked to rewrite it; the edit distance is a detection signal. An LLM "rewrite" of AI text changes little.
- **John Kirchenbauer, Jonas Geiping, Yuxin Wen et al. (2023). A Watermark for Large Language Models.** International Conference on Machine Learning. <https://arxiv.org/abs/2301.10226>
  Watermarking: softly promote a secret "green" token list during sampling; detectable from short spans with a p-value.
- **John Kirchenbauer, Jonas Geiping, Yuxin Wen et al. (2023). On the Reliability of Watermarks for Large Language Models.** International Conference on Learning Representations. <https://arxiv.org/abs/2306.04634>
  Watermarks survive human and machine paraphrase: after strong human paraphrase about 800 tokens still detect at 1e-5 FPR, because paraphrases leak n-grams.
- **Hanlin Zhang, Benjamin L. Edelman, Danilo Francati et al. (2023). Watermarks in the Sand: Impossibility of Strong Watermarking for Generative Models.** IACR Cryptology ePrint Archive. <https://arxiv.org/abs/2311.04378>
  Proof that strong watermarking is impossible under natural assumptions; a generic attack removed three schemes' watermarks with minor quality loss.
- **Sebastian Gehrmann, Hendrik Strobelt, Alexander M. Rush (2019). GLTR: Statistical Detection and Visualization of Generated Text.** Annual Meeting of the Association for Computational Linguistics. <https://arxiv.org/abs/1906.04043>
  GLTR visualises token rank; it raised untrained humans' detection of generated text from 54% to 72%.
- **Rowan Zellers, Ari Holtzman, Hannah Rashkin et al. (2019). Defending Against Neural Fake News.** Neural Information Processing Systems. <https://arxiv.org/abs/1905.12616>
  Grover: humans rated generated propaganda more trustworthy than human-written disinformation; the best defence was Grover itself (92%).
- **Pengyu Wang, Linyang Li, Ke Ren et al. (2023). SeqXGPT: Sentence-Level AI-Generated Text Detection.** Conference on Empirical Methods in Natural Language Processing. <https://arxiv.org/abs/2310.08903>
  Sentence-level detection in LLM-polished documents (mixed human and LLM sentences); document-level methods struggle there.
- **Zae Myung Kim, K. H. Lee, P. Zhu et al. (2024). Threads of Subtlety: Detecting Machine-Generated Texts Through Discourse Motifs.** Annual Meeting of the Association for Computational Linguistics. <https://arxiv.org/abs/2402.10586>
  Hierarchical discourse motifs: human texts show more structural variability than LLM texts; discourse features help even on paraphrased samples.
- **Tharindu Kumarage, Joshua Garland, Amrita Bhattacharjee et al. (2023). Stylometric Detection of AI-Generated Text in Twitter Timelines.** arXiv preprint. <https://arxiv.org/abs/2303.03697>
  Stylometric signals help detect AI tweets and the point where a timeline switches from human to AI.
- **Kalpesh Krishna, Yixiao Song, Marzena Karpinska et al. (2023). Paraphrasing evades detectors of AI-generated text, but retrieval is an effective defense.** Neural Information Processing Systems. <https://arxiv.org/abs/2303.13408>
  DIPPER paraphrases defeat detectors; retrieval over stored generations recovers 80-97% of paraphrased text at 1% FPR.
- **Bradley Emi, Max Spero (2024). Technical Report on the Pangram AI-Generated Text Classifier.** preprint. <https://arxiv.org/abs/2402.14873>
  Vendor-authored technical report on a commercial classifier; claims low error across 10 domains and no bias against non-native English. Treat as a vendor claim.

## B. Detector unreliability, evasion and false accusation

- **Vinu Sankar Sadasivan, Aounon Kumar, S. Balasubramanian et al. (2023). Can AI-Generated Text be Reliably Detected?.** arXiv preprint. <https://arxiv.org/abs/2303.11156>
  Recursive paraphrasing cuts detection rates with small quality loss; watermarks can be spoofed so human text is flagged as AI.
- **Yafu Li, Qintong Li, Leyang Cui et al. (2023). MAGE: Machine-generated Text Detection in the Wild.** Annual Meeting of the Association for Computational Linguistics. <https://arxiv.org/abs/2305.13242>
  MAGE: detection is hardest out of distribution because linguistic distinctions between sources are shrinking.
- **Liam Dugan, Alyssa Hwang, Filip Trhlík et al. (2024). RAID: A Shared Benchmark for Robust Evaluation of Machine-Generated Text Detectors.** Annual Meeting of the Association for Computational Linguistics. <https://arxiv.org/abs/2405.07940>
  RAID: 6M+ generations; detectors that claim 99% are fooled by sampling changes, adversarial attacks and unseen models.
- **Yichen Wang, Shangbin Feng, A. Hou et al. (2024). Stumbling Blocks: Stress Testing the Robustness of Machine-Generated Text Detectors Under Attacks.** Annual Meeting of the Association for Computational Linguistics. <https://arxiv.org/abs/2402.11638>
  Editing, paraphrasing, prompting and co-generating attacks drop detector performance by 35% on average; none is robust to all.
- **Jiameng Pu, Zain Sarwar, Sifat Muhammad Abdullah et al. (2022). Deepfake Text Detection: Limitations and Opportunities.** IEEE Symposium on Security and Privacy. <https://arxiv.org/abs/2210.09421>
  Defences degrade sharply on in-the-wild deepfake text and cheap adaptive attacks; semantic features generalise better.
- **Shuyang Cai, Wanyun Cui (2023). Evade ChatGPT Detectors via A Single Space.** arXiv preprint. <https://arxiv.org/abs/2307.02599>
  One extra space evades detectors: they rely on "subtle differences", not semantic or stylistic gaps.
- **Ning Lu, Shengcai Liu, Ruidan He et al. (2023). Large Language Models can be Guided to Evade AI-Generated Text Detection.** Trans. Mach. Learn. Res.. <https://arxiv.org/abs/2305.10847>
  SICO prompts built from 40 human examples let GPT-3.5 evade six detectors, cutting AUC by 0.5 on average.
- **Ryuto Koike, Masahiro Kaneko, Naoaki Okazaki (2023). OUTFOX: LLM-generated Essay Detection through In-context Learning with Adversarially Generated Examples.** AAAI Conference on Artificial Intelligence. <https://arxiv.org/abs/2307.11729>
  OUTFOX: essay detectors lose accuracy under simple paraphrase; adversarial in-context examples help both attacker and detector.
- **Debora Weber-Wulff, Alla Anohina-Naumeca, Sonja Bjelobaba et al. (2023). Testing of detection tools for AI-generated text.** International Journal for Educational Integrity. <https://arxiv.org/abs/2306.15666>
  14 tools including Turnitin: "neither accurate nor reliable", biased toward calling text human; obfuscation and machine translation make them worse.
- **Michael Sheinman Orenstrakh, Oscar Karnalim, C. Suárez et al. (2023). Detecting LLM-Generated Text in Computing Education: Comparative Study for ChatGPT Cases.** Annual International Computer Software and Applications Conference. <https://arxiv.org/abs/2307.07411>
  Eight detectors on CS student work: all less accurate on code, on languages other than English, and after paraphrasing tools.
- **B. Tufts, Xuandong Zhao, Lei Li (2024). A Practical Examination of AI-Generated Text Detectors for Large Language Models.** North American Chapter of the Association for Computational Linguistics. <https://arxiv.org/abs/2412.05139>
  Under realistic prompting, detectors' true-positive rate at 1% FPR can fall to 0%.
- **Farid Adilazuarda, N. Arkoulis, O. Chumakov (2023). Beyond Turing: A Comparative Analysis of Approaches for Detecting Machine-Generated Text.** TRUSTNLP. <https://arxiv.org/abs/2311.12373>
  Statistical, fine-tuned and multilingual detectors differ widely in performance on the same data.
- **Xinlei He, Xinyue Shen, Zeyuan Chen et al. (2023). MGTBench: Benchmarking Machine-Generated Text Detection.** Conference on Computer and Communications Security. <https://arxiv.org/abs/2303.14822>
  MGTBench: paraphrasing, random spacing and adversarial perturbation significantly reduce detection; longer texts are detected better.
- **Canyu Chen, Kai Shu (2023). Can LLM-Generated Misinformation Be Detected?.** International Conference on Learning Representations. <https://arxiv.org/abs/2309.13788>
  LLM-written misinformation is harder for humans and detectors to catch than human misinformation with the same meaning.

## C. Human detection and human perception

- **Elizabeth Clark, Tal August, Sofia Serrano et al. (2021). All That’s ‘Human’ Is Not Gold: Evaluating Human Evaluation of Generated Text.** Annual Meeting of the Association for Computational Linguistics. <https://arxiv.org/abs/2107.00061>
  Untrained evaluators separated GPT-3 from human text at chance; training raised accuracy only to about 55%, with contradictory reasons.
- **Daphne Ippolito, Daniel Duckworth, Chris Callison-Burch et al. (2019). Automatic Detection of Generated Text is Easiest when Humans are Fooled.** Annual Meeting of the Association for Computational Linguistics. <https://arxiv.org/abs/1911.00650>
  Decoding tuned to fool humans leaves statistical artefacts machines catch; multi-sentence excerpts still fool expert raters over 30% of the time.
- **Liam Dugan, Daphne Ippolito, Arun Kirubarajan et al. (2022). Real or Fake Text?: Investigating Human Ability to Detect Boundaries Between Human-Written and Machine-Generated Text.** AAAI Conference on Artificial Intelligence. <https://arxiv.org/abs/2212.12672>
  RoFT: people can learn to spot where a text switches from human to machine; some sentence-level features correlate with their picks.
- **Maurice Jakesch, Jeffrey T. Hancock, Mor Naaman (2022). Human heuristics for AI-generated language are flawed.** Proceedings of the National Academy of Sciences of the United States of America. <https://arxiv.org/abs/2206.07271>
  People judge AI self-presentations with intuitive but flawed heuristics, which AI text can exploit to seem "more human than human".
- **Jenna Russell, Marzena Karpinska, Mohit Iyyer (2025). People who frequently use ChatGPT for writing tasks are accurate and robust detectors of AI-generated text.** Annual Meeting of the Association for Computational Linguistics. <https://arxiv.org/abs/2501.15654>
  Frequent LLM users detect AI non-fiction well: the majority vote of five such experts misclassifies 1 of 300 articles.
- **Adaku Uchendu, Jooyoung Lee, Hua Shen et al. (2023). Does Human Collaboration Enhance the Accuracy of Identifying LLM-Generated Deepfake Texts?.** Proceedings of the AAAI Conference on Human Computation and Crowdsourcing. <https://arxiv.org/abs/2304.01002>
  Collaboration raises human detection (by 6.36% for non-experts, 12.76% for experts); the strongest cue cited was lack of coherence and consistency.
- **G. Spitale, N. Biller-Andorno, F. Germani (2023). AI model GPT-3 (dis)informs us better than humans.** Science Advances. <https://arxiv.org/abs/2301.11924>
  697 participants could not tell GPT-3 tweets from real ones; GPT-3 wrote both clearer accurate information and more compelling disinformation.
- **Yikang Liu, Ziyin Zhang, Wanyang Zhang et al. (2023). ArguGPT: evaluating, understanding and identifying argumentative essays generated by GPT models.** arXiv preprint. <https://arxiv.org/abs/2304.07666>
  ArguGPT: English instructors spot machine essays at 61% (67% after self-training); machines use more complex syntax, humans more complex vocabulary.
- **C. Gao, Frederick M. Howard, N. Markov et al. (2023). Comparing scientific abstracts generated by ChatGPT to real abstracts with detectors and blinded human reviewers.** npj Digit. Medicine. <https://doi.org/10.1038/s41746-023-00819-6>
  Blinded reviewers flagged 14% of real abstracts as generated; the abstracts they suspected were "vaguer and more formulaic".
- **B. Porter, E. Machery (2024). AI-generated poetry is indistinguishable from human-written poetry and is rated more favorably.** Scientific Reports. <https://doi.org/10.1038/s41598-024-76900-1>
  Non-experts judged AI poems as human more often than real human poems and rated them higher; they read simplicity as human and complexity as AI incoherence.

## D. Lexical tells and measured language change

- **Dmitry Kobak, Rita González-Márquez, Emőke-ágnes Horvát et al. (2024). Delving into LLM-assisted writing in biomedical publications through excess vocabulary.** Science Advances. <https://arxiv.org/abs/2406.07016>
  15M+ PubMed abstracts: excess-vocabulary analysis puts at least 13.5% of 2024 abstracts as LLM-processed (up to 40% in some subcorpora); the excess words are style words.
- **Thomas Stephan Juzek, Zina B. Ward (2024). Why Does ChatGPT "Delve" So Much? Exploring the Sources of Lexical Overrepresentation in Large Language Models.** International Conference on Computational Linguistics. <https://arxiv.org/abs/2412.11385>
  21 focal words (e.g. delve, intricate, underscore) rose in scientific abstracts because of LLM use; model testing is consistent with RLHF playing a role.
- **Weixin Liang, Yaohui Zhang, Zhengxuan Wu et al. (2024). Mapping the Increasing Use of LLMs in Scientific Papers.** arXiv preprint. <https://arxiv.org/abs/2404.01268>
  950,965 papers: LLM-modified content up to 17.5% in computer science, least in mathematics and Nature journals (up to 6.3%); more in shorter papers and crowded fields.
- **Weixin Liang, Zachary Izzo, Yaohui Zhang et al. (2024). Monitoring AI-Modified Content at Scale: A Case Study on the Impact of ChatGPT on AI Conference Peer Reviews.** International Conference on Machine Learning. <https://arxiv.org/abs/2403.07183>
  6.5-16.9% of AI-conference peer reviews substantially LLM-modified; more likely near deadlines and in low-confidence reviews.
- **Mingmeng Geng, Roberto Trotta (2024). Is ChatGPT Transforming Academics' Writing Style?.** arXiv preprint. <https://arxiv.org/abs/2404.08627>
  Adaptive word-frequency estimate: about 35% of CS arXiv abstracts show LLM style (baseline: GPT-3.5 asked to "revise the following sentences").
- **Mingmeng Geng, Roberto Trotta (2025). Human-LLM Coevolution: Evidence from Academic Writing.** Annual Meeting of the Association for Computational Linguistics. <https://arxiv.org/abs/2502.09606>
  After "delve" became a known tell its use fell, while words like "significant" kept rising: authors filter famous tell words, so word lists age.
- **Weixin Liang, Yaohui Zhang, Mihai-Eugen Codreanu et al. (2025). The widespread adoption of large language model-assisted writing across society.** Patterns. <https://arxiv.org/abs/2502.09747>
  By late 2024, LLM-assisted writing in about 18% of financial complaints, 24% of corporate press releases, nearly 10% of small-firm job posts, 14% of UN press releases.
- **Creston Brooks, Samuel Eggert, Denis Peskoff (2024). The Rise of AI-Generated Content in Wikipedia.** Proceedings of the First Workshop on Advancing Natural Language Processing for Wikipedia. <https://arxiv.org/abs/2410.08044>
  Over 5% of new English Wikipedia articles flagged at 1% FPR; flagged pages are lower quality and often self-promotional or one-sided.
- **Hiromu Yakura, Ezequiel Lopez-Lopez, L. Brinkmann et al. (2024). Empirical evidence of Large Language Model's influence on human spoken communication.** arXiv preprint. <https://arxiv.org/abs/2409.01754>
  People adopt LLM vocabulary: a short chatbot exchange made participants reuse its words, persisting past a distractor task.
- **Pedro Reviriego, Javier Conde, Elena Merino-G'omez et al. (2023). Playing with words: Comparing the vocabulary and lexical diversity of ChatGPT and humans.** Machine Learning with Applications. <https://arxiv.org/abs/2308.07462>
  ChatGPT uses fewer distinct words and lower lexical richness than humans (authors call it preliminary).
- **Sandra Mitrovi'c, Davide Andreoletti, Omran Ayoub (2023). ChatGPT or Human? Detect and Explain. Explaining Decisions of Machine Learning Model for Detecting Short ChatGPT-generated Text.** arXiv preprint. <https://arxiv.org/abs/2301.13852>
  Explained classifier on short reviews: ChatGPT text is polite, lacks specific details, uses fancy atypical vocabulary, is impersonal and rarely expresses feeling.

## E. Stylistic and structural characterisation

- **Alex Reinhart, David West Brown, Ben Markey et al. (2024). Do LLMs write like humans? Variation in grammatical and rhetorical styles.** Proceedings of the National Academy of Sciences of the United States of America. <https://arxiv.org/abs/2410.16107>
  Instruction-tuned models write in a noun-heavy, informationally dense style even when asked for informal speech; they miss genre conventions.
- **Alberto Muñoz-Ortiz, Carlos Gómez-Rodríguez, David Vilares (2023). Contrasting Linguistic Patterns in Human and LLM-Generated News Text.** Artificial Intelligence Review. <https://arxiv.org/abs/2308.09067>
  Human news has more scattered sentence lengths, more varied vocabulary and stronger negative emotion; LLM text uses more numbers, symbols, auxiliaries and pronouns.
- **Steffen Herbold, Annette Hautli-Janisz, Ute Heuer et al. (2023). AI, write an essay for me: A large-scale comparison of human-written versus ChatGPT-generated essays.** arXiv preprint. <https://arxiv.org/abs/2304.14276>
  ChatGPT essays rated higher than students', but with fewer discourse and epistemic markers and more nominalisations.
- **Heather Desaire, Aleesa E. Chua, Madeline Isom et al. (2023). Distinguishing academic science writing from humans or ChatGPT with over 99% accuracy using off-the-shelf machine learning tools.** Cell Reports Physical Science. <https://doi.org/10.1016/j.xcrp.2023.101426>
  Human scientists write long paragraphs and use equivocal words ("but", "however", "although"); 20 such features separate them from ChatGPT at over 99%.
- **Chantal Shaib, Yanai Elazar, J. Li et al. (2024). Detection and Measurement of Syntactic Templates in Generated Text.** Conference on Empirical Methods in Natural Language Processing. <https://arxiv.org/abs/2407.00211>
  76% of syntactic templates in model text appear in pre-training data (35% for human text); templates survive RLHF and separate models.
- **Chantal Shaib, Joe Barrow, Jiuding Sun et al. (2024). Standardizing the Measurement of Text Diversity: A Tool and Comparative Analysis.** Proceedings of The 14th International Joint Conference on Natural Language Processing and The 4th Conference of the Asia-Pacific Chapter of the Association for Computational Linguistics: System Demonstrations. <https://arxiv.org/abs/2403.00553>
  Compression ratio and long-n-gram self-repetition capture "templated" canned structure across documents.
- **Mingjie Sun, Yida Yin, Zhiqiu Xu et al. (2025). Idiosyncrasies in Large Language Models.** International Conference on Machine Learning. <https://arxiv.org/abs/2502.12150>
  Five-way model attribution at 97.1%; idiosyncrasies sit in word distributions and survive rewriting, translation and summarising.
- **Dmitri Iourovitski, Sanat Sharma, Rakshak Talwar (2024). Hide and Seek: Fingerprinting Large Language Models with Evolutionary Learning.** arXiv preprint. <https://arxiv.org/abs/2408.02871>
  An auditor LLM and a detective LLM fingerprint model families from their answers to probing prompts.
- **Morgan Sandler, Hyesun Choung, Arun Ross et al. (2024). A Linguistic Comparison between Human and ChatGPT-Generated Conversations.** International Conferences on Pattern Recognition and Artificial Intelligence. <https://arxiv.org/abs/2401.16587>
  LIWC on 19.5K dialogues: humans more variable and "authentic"; ChatGPT higher on analytic style, social processes and positive tone.
- **Wenxiong Liao, Zheng Liu, Haixing Dai et al. (2023). Differentiating ChatGPT-Generated and Human-Written Medical Texts: Quantitative Study.** JMIR Medical Education. <https://arxiv.org/abs/2304.11567>
  Human medical texts are more concrete, diverse and informative; ChatGPT favours fluency and general terminology over context-specific information.
- **Yongqiang Ma, Jiawei Liu, Fan Yi et al. (2023). AI vs. Human -- Differentiation Analysis of Scientific Content Generation.** preprint. <https://arxiv.org/abs/2301.10416>
  AI scientific text shows a "writing style gap", less depth, and more factual errors.
- **Biyang Guo, Xin Zhang, Ziyuan Wang et al. (2023). How Close is ChatGPT to Human Experts? Comparison Corpus, Evaluation, and Detection.** arXiv preprint. <https://arxiv.org/abs/2301.07597>
  HC3 (English and Chinese): human-expert vs ChatGPT answers compared by human evaluation and linguistic analysis across open, finance, medical, legal and psychology questions.
- **Dongqi Liu, Vera Demberg (2023). ChatGPT vs Human-authored Text: Insights into Controllable Text Summarization and Sentence Style Transfer.** Annual Meeting of the Association for Computational Linguistics. <https://arxiv.org/abs/2306.07799>
  ChatGPT summaries and style-transfer outputs differ systematically from human ones.

## F. Homogenisation of writing and ideas

- **Vishakh Padmakumar, He He (2023). Does Writing with Language Models Reduce Content Diversity?.** International Conference on Learning Representations. <https://arxiv.org/abs/2309.05196>
  Writing with InstructGPT reduced essay diversity; the loss came from the model's contributed text, not the users' own text.
- **Barrett R Anderson, J. Shah, Max Kreminski (2024). Homogenization Effects of Large Language Models on Human Creative Ideation.** Creativity & Cognition. <https://arxiv.org/abs/2402.01536>
  ChatGPT users produced less semantically distinct ideas than users of another tool, and felt less responsible for them.
- **Anil R. Doshi, Oliver P. Hauser (2023). Generative AI enhances individual creativity but reduces the collective diversity of novel content.** Science Advances. <https://arxiv.org/abs/2312.00506>
  AI story ideas made individual stories rated more creative but made stories more similar to each other.
- **Dhruv Agarwal, Mor Naaman, Aditya Vashistha (2024). AI Suggestions Homogenize Writing Toward Western Styles and Diminish Cultural Nuances.** International Conference on Human Factors in Computing Systems. <https://arxiv.org/abs/2409.11360>
  AI suggestions pushed Indian writers toward Western styles; efficiency gains were larger for Americans.
- **Liwei Jiang, Yuanjun Chai, Margaret Li et al. (2025). Artificial Hivemind: The Open-Ended Homogeneity of Language Models (and Beyond).** arXiv preprint. <https://arxiv.org/abs/2510.22954>
  Artificial Hivemind: 26K open-ended queries show strong within-model repetition and striking similarity between different models.
- **Zhivar Sourati, Alireza S. Ziabari, Morteza Dehghani (2025). The Homogenizing Effect of Large Language Models on Human Expression and Thought.** Trends in Cognitive Sciences. <https://arxiv.org/abs/2508.01491>
  Review: LLMs reflect and reinforce dominant styles and marginalise alternative voices and reasoning strategies.
- **Maurice Jakesch, Advait Bhat, Daniel Buschek et al. (2023). Co-Writing with Opinionated Language Models Affects Users’ Views.** International Conference on Human Factors in Computing Systems. <https://arxiv.org/abs/2302.00560>
  An opinionated writing assistant shifted what 1,506 participants wrote and what they later believed.
- **Shibani Santurkar, Esin Durmus, Faisal Ladhak et al. (2023). Whose Opinions Do Language Models Reflect?.** International Conference on Machine Learning. <https://arxiv.org/abs/2303.17548>
  LM opinions misalign with US demographic groups about as much as the Democrat-Republican climate divide, even after steering.
- **Wei-Jia Xu, Nebojsa Jojic, Sudha Rao et al. (2024). Echoes in AI: Quantifying lack of plot diversity in LLM outputs.** Proceedings of the National Academy of Sciences of the United States of America. <https://arxiv.org/abs/2501.00273>
  Stories from the same prompt reuse combinations of plot elements; human stories stay more unique.
- **Sophie F. Jentzsch, K. Kersting (2023). ChatGPT is fun, but it is not funny! Humor is still challenging Large Language Models.** Workshop on Computational Approaches to Subjectivity, Sentiment and Social Media Analysis. <https://arxiv.org/abs/2306.04563>
  Over 90% of 1,008 ChatGPT jokes were the same 25 jokes.
- **H. Kumar, Jonathan Vincentius, Ewan Jordan et al. (2024). Human Creativity in the Age of LLMs: Randomized Experiments on Divergent and Convergent Thinking.** International Conference on Human Factors in Computing Systems. <https://arxiv.org/abs/2410.03703>
  LLM help boosted creativity during tasks but hurt later unassisted performance (1,100 participants).
- **Maria del Rio-Chanona, Nadzeya Laurentsyeva, Johannes Wachs (2023). Large language models reduce public knowledge sharing on online Q&A platforms.** PNAS Nexus. <https://arxiv.org/abs/2307.07367>
  Stack Overflow activity fell 25% within six months of ChatGPT relative to counterfactuals.
- **Ilia Shumailov, Zakhar Shumaylov, Yiren Zhao et al. (2023). The Curse of Recursion: Training on Generated Data Makes Models Forget.** arXiv preprint. <https://arxiv.org/abs/2305.17493>
  Training on model output makes the tails of the distribution disappear ("model collapse"); rare phrasing goes first.
- **Jooyoung Lee, Thai Le, Jinghui Chen et al. (2022). Do Language Models Plagiarize?.** The Web Conference. <https://arxiv.org/abs/2203.07618>
  LMs reproduce training data verbatim, as paraphrase, and at the level of ideas.

## G. Alignment side effects: length, sycophancy, mode collapse, confidence

- **Robert Kirk, Ishita Mediratta, Christoforos Nalmpantis et al. (2023). Understanding the Effects of RLHF on LLM Generalisation and Diversity.** International Conference on Learning Representations. <https://arxiv.org/abs/2310.06452>
  RLHF generalises better than supervised fine-tuning but significantly reduces output diversity.
- **Behnam Mohammadi (2024). Creativity Has Left the Chat: The Price of Debiasing Language Models.** arXiv preprint. <https://arxiv.org/abs/2406.05587>
  Aligned models have lower token entropy and fall into "attractor states"; the paper warns copywriters and ad makers directly.
- **Jiayi Zhang, Simon Yu, Derek Chong et al. (2025). Verbalized Sampling: How to Mitigate Mode Collapse and Unlock LLM Diversity.** arXiv preprint. <https://arxiv.org/abs/2510.01171>
  Mode collapse traced to typicality bias in preference data (annotators favour familiar text); asking for a distribution raises creative diversity 1.6-2.1x.
- **Prasann Singhal, Tanya Goyal, Jiacheng Xu et al. (2023). A Long Way to Go: Investigating Length Correlations in RLHF.** arXiv preprint. <https://arxiv.org/abs/2310.03716>
  Much of RLHF's reward gain comes from longer outputs; a length-only reward reproduces most of it.
- **Yann Dubois, Bal'azs Galambosi, Percy Liang et al. (2024). Length-Controlled AlpacaEval: A Simple Way to Debias Automatic Evaluators.** arXiv preprint. <https://arxiv.org/abs/2404.04475>
  Automatic evaluators favour longer answers; controlling length raises agreement with Chatbot Arena from 0.94 to 0.98.
- **Keita Saito, Akifumi Wachi, Koki Wataoka et al. (2023). Verbosity Bias in Preference Labeling by Large Language Models.** arXiv preprint. <https://arxiv.org/abs/2310.10076>
  GPT-4 as a judge prefers longer answers more than humans do.
- **Minghao Wu, Alham Fikri Aji (2023). Style Over Substance: Evaluation Biases for Large Language Models.** International Conference on Computational Linguistics. <https://arxiv.org/abs/2307.03025>
  Judges rate answers with factual errors above answers that are short or ungrammatical: style over substance.
- **Mrinank Sharma, Meg Tong, Tomasz Korbak et al. (2023). Towards Understanding Sycophancy in Language Models.** International Conference on Learning Representations. <https://arxiv.org/abs/2310.13548>
  Five assistants are consistently sycophantic; humans and preference models sometimes prefer convincing sycophancy to correct answers.
- **Ethan Perez, Sam Ringer, Kamilė Lukošiūtė et al. (2022). Discovering Language Model Behaviors with Model-Written Evaluations.** Annual Meeting of the Association for Computational Linguistics. <https://arxiv.org/abs/2212.09251>
  Larger LMs repeat back the user's preferred answer (sycophancy) more; more RLHF can make some behaviours worse.
- **Miao Xiong, Zhiyuan Hu, Xinyang Lu et al. (2023). Can LLMs Express Their Uncertainty? An Empirical Evaluation of Confidence Elicitation in LLMs.** International Conference on Learning Representations. <https://arxiv.org/abs/2306.13063>
  LLMs' verbalised confidence is overconfident; a confident tone is not evidence.
- **Sewon Min, Kalpesh Krishna, Xinxi Lyu et al. (2023). FActScore: Fine-grained Atomic Evaluation of Factual Precision in Long Form Text Generation.** Conference on Empirical Methods in Natural Language Processing. <https://arxiv.org/abs/2305.14251>
  ChatGPT biographies: only 58% of atomic facts supported. Fluent text carries unsupported claims.

## H. Fiction and creative-writing quality

- **Tuhin Chakrabarty, Philippe Laban, Divyansh Agarwal et al. (2023). Art or Artifice? Large Language Models and the False Promise of Creativity.** International Conference on Human Factors in Computing Systems. <https://arxiv.org/abs/2309.14556>
  LLM stories pass 3-10x fewer of 14 Torrance creative-writing tests than professional stories; LLM judges do not agree with experts.
- **Tuhin Chakrabarty, Philippe Laban, Chien-Sheng Wu (2024). Can AI writing be salvaged? Mitigating Idiosyncrasies and Improving Human-AI Alignment in the Writing Process through Edits.** International Conference on Human Factors in Computing Systems. <https://arxiv.org/abs/2409.14509>
  Professional writers agree on LLM idiosyncrasies in a seven-category taxonomy (e.g. clichés, unnecessary exposition); LAMP corpus of 1,057 expert-edited paragraphs.
- **Guillermo Marco, Julio Gonzalo, M.Teresa Mateo-Girona et al. (2024). Pron vs Prompt: Can Large Language Models already Challenge a World-Class Fiction Author at Creative Text Writing?.** Conference on Empirical Methods in Natural Language Processing. <https://arxiv.org/abs/2407.01119>
  GPT-4 lost to novelist Patricio Pron on an expert rubric; it wrote better from his titles than its own, and better in English than Spanish.
- **Mete Ismayilzada, Claire E. Stevenson, Lonneke van der Plas (2024). Evaluating Creative Short Story Generation in Humans and Large Language Models.** ICCC. <https://arxiv.org/abs/2411.02316>
  LLM stories are stylistically complex but lower in novelty, surprise and diversity; non-experts and LLMs still rate them as more creative.
- **Fabrice Y. Harel-Canada, Hanyu Zhou, Sreya Muppalla et al. (2024). Measuring Psychological Depth in Language Models.** Conference on Empirical Methods in Natural Language Processing. <https://arxiv.org/abs/2406.12680>
  On the Psychological Depth Scale, GPT-4 stories matched or beat highly rated Reddit stories. A counterweight: depth is not automatically missing.
- **Zhuohan Xie, Trevor Cohn, Jey Han Lau (2023). The Next Chapter: A Study of Large Language Models in Storytelling.** International Conference on Natural Language Generation. <https://arxiv.org/abs/2301.09790>
  LLM stories rival human quality but copy real stories when world knowledge is involved.
- **Piotr Wojciech Mirowski, K. Mathewson, Jaylen Pittman et al. (2022). Co-Writing Screenplays and Theatre Scripts with Language Models: Evaluation by Industry Professionals.** International Conference on Human Factors in Computing Systems. <https://arxiv.org/abs/2209.14958>
  Dramatron: LMs lack long-range coherence; hierarchical planning (title, characters, beats) was needed for scripts.
- **Mina Lee, Percy Liang, Qian Yang (2022). CoAuthor: Designing a Human-AI Collaborative Writing Dataset for Exploring Language Model Capabilities.** International Conference on Human Factors in Computing Systems. <https://arxiv.org/abs/2201.06796>
  CoAuthor: 1,445 sessions of 63 writers with GPT-3, a dataset of how suggestions are accepted or rewritten.
- **Andy Coenen, Luke Davis, Daphne Ippolito et al. (2021). Wordcraft: a Human-AI Collaborative Editor for Story Writing.** arXiv preprint. <https://arxiv.org/abs/2107.07430>
  Wordcraft: conversational AI editor for story writing (extended abstract).
- **Yuning Wu, Jiahao Mei, Ming Yan et al. (2025). WritingBench: A Comprehensive Benchmark for Generative Writing.** Neural Information Processing Systems. <https://arxiv.org/abs/2503.05244>
  WritingBench: 6 domains and 100 subdomains; query-specific criteria for style, format and length.

## I. Human editing, polishing and mixed authorship

- **Ekaterina Artemova, Jason Samuel Lucas, Saranya Venkatraman et al. (2024). Beemo: Benchmark of Expert-edited Machine-generated Outputs.** North American Chapter of the Association for Computational Linguistics. <https://arxiv.org/abs/2411.04032>
  Beemo: expert editing of LLM output evades detectors, while LLM-edited text is rarely taken for human.
- **Shoumik Saha, S. Feizi (2025). Almost AI, Almost Human: The Challenge of Detecting AI-Polished Writing.** Annual Meeting of the Association for Computational Linguistics. <https://arxiv.org/abs/2502.15666>
  APT-Eval (14.7K samples): detectors flag even minimally AI-polished human text as AI and cannot grade degrees of involvement.
- **Qihui Zhang, Chujie Gao, Dongping Chen et al. (2024). LLM-as-a-Coauthor: Can Mixed Human-Written and Machine-Generated Text Be Detected?.** NAACL-HLT. <https://arxiv.org/abs/2401.05952>
  MixSet: detectors struggle with mixed human/AI text, especially subtle revisions.
- **Yafu Li, Zhi-Lin Wang, Leyang Cui et al. (2024). Spotting AI's Touch: Identifying LLM-Paraphrased Spans in Text.** Annual Meeting of the Association for Computational Linguistics. <https://arxiv.org/abs/2405.12689>
  AI-paraphrased spans can be located sentence by sentence; the surrounding context matters.
- **Mervat T. Abassy, K. Elozeiri, Alexander Aziz et al. (2024). LLM-DetectAIve: a Tool for Fine-Grained Machine-Generated Text Detection.** Conference on Empirical Methods in Natural Language Processing. <https://arxiv.org/abs/2408.04284>
  Four labels: human, machine, machine-then-humanised, human-then-machine-polished; polishing framed as acceptable in academia but not in education.
- **Jiazhou Ji, Rui-Zhe Li, Shujun Li et al. (2024). Detecting Machine-Generated Texts: Not Just "AI vs Humans" and Explainability is Complicated.** arXiv preprint. <https://arxiv.org/abs/2406.18259>
  Human annotators needed an "undecided" label; binary AI-vs-human labelling is not enough.
- **N. Tripto, Saranya Venkatraman, D. Macko et al. (2023). A Ship of Theseus: Curious Cases of Paraphrasing in LLM-Generated Texts.** Annual Meeting of the Association for Computational Linguistics. <https://arxiv.org/abs/2311.08374>
  Each paraphrase round moves text away from the original author's style; classifier drops track that deviation.
- **Peipeng Yu, Jiahan Chen, Xuan Feng et al. (2023). CHEAT: A Large-Scale Dataset for Detecting CHatGPT-writtEn AbsTracts.** IEEE Transactions on Big Data. <https://arxiv.org/abs/2304.12008>
  CHEAT abstracts: detection gets harder the more human guidance goes into generation.
- **Baixiang Huang, Canyu Chen, Kai Shu (2024). Authorship Attribution in the Era of LLMs: Problems, Methodologies, and Challenges.** SIGKDD Explorations. <https://arxiv.org/abs/2408.08946>
  Survey of four problems: human attribution, LLM detection, LLM attribution, and human-LLM co-authored attribution.

## J. Languages other than English (Indonesian included)

- **Yuxia Wang, Jonibek Mansurov, Petar Ivanov et al. (2023). M4: Multi-generator, Multi-domain, and Multi-lingual Black-Box Machine-Generated Text Detection.** Conference of the European Chapter of the Association for Computational Linguistics. <https://arxiv.org/abs/2305.14902>
  M4 covers Arabic, Bulgarian, Chinese, English, Indonesian (news, about 6k parallel texts), Russian and Urdu; detectors tend to call unseen-domain machine text human.
- **Yuxia Wang, Jonibek Mansurov, Petar Ivanov et al. (2024). M4GT-Bench: Evaluation Benchmark for Black-Box Machine-Generated Text Detection.** Annual Meeting of the Association for Computational Linguistics. <https://arxiv.org/abs/2402.11175>
  M4GT-Bench: good detection usually needs training data from the same domain and generator.
- **Yuxia Wang, Jonibek Mansurov, Petar Ivanov et al. (2024). SemEval-2024 Task 8: Multidomain, Multimodel and Multilingual Machine-Generated Text Detection.** International Workshop on Semantic Evaluation. <https://arxiv.org/abs/2404.14183>
  SemEval-2024 Task 8: monolingual, multilingual (59 teams) and boundary-detection subtasks; the best systems all used LLMs.
- **Yuxia Wang, Artem Shelmanov, Jonibek Mansurov et al. (2025). GenAI Content Detection Task 1: English and Multilingual Machine-Generated Text Detection: AI vs. Human.** COLING Workshops. <https://arxiv.org/abs/2501.11012>
  COLING 2025 GenAI shared task, English and multilingual tracks (36 and 26 teams).
- **A. Sarvazyan, José Ángel González, Marc Franco-Salvador et al. (2023). Overview of AuTexTification at IberLEF 2023: Detection and Attribution of Machine-Generated Text in Multiple Domains.** Proces. del Leng. Natural. <https://arxiv.org/abs/2309.11285>
  AuTexTification (IberLEF 2023): 160K+ English and Spanish texts across five domains, detection and attribution.
- **Wissam Antoun, Virginie Mouilleron, Benoît Sagot et al. (2023). Towards a Robust Detection of Language Model-Generated Text: Is ChatGPT that easy to detect?.** JEPTALNRECITAL. <https://arxiv.org/abs/2306.05871>
  French: detectors trained on translated data work in-domain but are vulnerable out of domain.
- **Wataru Zaitsu, Ming-Zhe Jin (2023). Distinguishing ChatGPT(-3.5, -4)-generated and human-written papers through Japanese stylometric analysis.** PLoS ONE. <https://arxiv.org/abs/2304.05534>
  Japanese: the rate of function words alone separates GPT from human academic writing at 98.1%; comma placement and particle bigrams also differ.
- **T. Batura, E. Bruches, Milana Shvenk et al. (2025). AINL-Eval 2025 Shared Task: Detection of AI-Generated Scientific Abstracts in Russian.** arXiv preprint. <https://arxiv.org/abs/2508.09622>
  Russian scientific-abstract detection shared task (AINL-Eval 2025): 10 teams, 159 submissions.
- **Saleh Almohaimeed, Saad Almohaimeed, Mousa Jari et al. (2025). AI text detectors and the misclassification of slightly polished Arabic text.** Journal of Big Data. <https://arxiv.org/abs/2511.16690>
  Arabic: slight LLM polishing of human articles broke detectors (Originality.AI human-accuracy 92% to 12%).
- **M. Ammar, H. Hadi, Usman Butt (2025). AI-Generated Text Detection in Low-Resource Languages: A Case Study on Urdu.** arXiv preprint. <https://arxiv.org/abs/2510.16573>
  Urdu: new dataset with linguistic comparison; mDeBERTa reaches 91.3% F1.
- **Junchao Wu, Ye-Feng Liu, Chenyu Zhu et al. (2026). DetectRL-X: Towards Reliable Multilingual and Real-World LLM-Generated Text Detection.** Annual Meeting of the Association for Computational Linguistics. <https://arxiv.org/abs/2605.15518>
  DetectRL-X: multilingual real-world benchmark; performance depends on language, domain, attack and refinement operations.
- **Yafu Li, Ronghao Zhang, Zhi-Lin Wang et al. (2025). Lost in Literalism: How Supervised Training Shapes Translationese in LLMs.** Annual Meeting of the Association for Computational Linguistics. <https://arxiv.org/abs/2503.04369>
  LLM translations carry translationese from supervised training (literal, unnatural target language); polishing references and filtering reduces it.
- **Alif, R. M., Alam, S., & Lestari, C. D. (2026). Implementation of the BiLSTM Model for Detecting AI-Generated Indonesian Text.** Jurnal Teknologi Informatika dan Komputer 12(1). <https://doi.org/10.37012/jtik.v12i1.3551>
  Indonesian: 5,008 texts (news and SINTA-4 journals vs ChatGPT/Gemini paraphrases); 78.24% overall accuracy, but only 62.62% on AI text in academic structure. A small national-journal study; the one Indonesian-specific detection paper found.
- **T. Fagni, Fabrizio Falchi, Margherita Gambini et al. (2020). TweepFake: About detecting deepfake tweets.** PLoS ONE. <https://arxiv.org/abs/2008.00036>
  TweepFake: 25,572 tweets; short social text is hard for 13 detectors.

## K. Surveys

- **Mahdi Dhaini, Wessel Poelman, Ege Erdogan (2023). Detecting ChatGPT: A Survey of the State of Detecting ChatGPT-Generated Text.** Recent Advances in Natural Language Processing. <https://arxiv.org/abs/2309.07689>
  Survey of ChatGPT detection, including qualitative analyses of human vs ChatGPT characteristics.
- **Xianjun Yang, Liangming Pan, Xuandong Zhao et al. (2023). A Survey on Detection of LLMs-Generated Content.** Conference on Empirical Methods in Natural Language Processing. <https://arxiv.org/abs/2310.15654>
  Survey of detection strategies and benchmarks; calls for multi-faceted defence against attacks.
- **Tharindu Kumarage, Garima Agrawal, Paras Sheth et al. (2024). A Survey of AI-generated Text Forensic Systems: Detection, Attribution, and Characterization.** arXiv preprint. <https://arxiv.org/abs/2403.01152>
  Forensics survey organised as detection, attribution and characterisation.
- **Ruixiang Tang, Yu-Neng Chuang, Xia Hu (2023). The Science of Detecting LLM-Generated Text.** Communications of the ACM. <https://arxiv.org/abs/2303.07205>
  Communications of the ACM overview of why detection is hard.

---

## Checked and left out

- **Casal & Kessler (2023), "Can linguists distinguish between ChatGPT/AI and human
  writing?"** (Research Methods in Applied Linguistics, doi:10.1016/j.rmal.2023.100068).
  The record exists, but no abstract could be retrieved, so its numbers are not quoted.
- **MULTITuDE** (multilingual detection benchmark). The arXiv ID could not be confirmed
  during retrieval, so it is not listed.
- Indonesian-language detection: apart from M4's Indonesian subset and Alif et al.
  (2026), searches found only student projects and tool pages. No peer-reviewed study of
  Indonesian *AI writing style* (as opposed to detection) was found. `patterns-id.md`
  rules therefore still rest on editorial judgement plus cross-language findings.
