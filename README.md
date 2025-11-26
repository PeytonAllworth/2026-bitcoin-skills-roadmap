# 2026 Skills Roadmap – Bitcoin Policy, Lightning Research, and Economic Modeling

**Context:**  
Starting January 2026, I begin a Bitcoin Policy Institute fellowship in Washington, D.C.,  
serving in an office on the hill focused on Bitcoin, digital assets, financial services, or technology policy.

My goal for 2026 is simple:

> **Build the hard skills that turn me into a credible, data-capable, policy-focused Bitcoin researcher.**

This roadmap is structured into **phases**, with each phase defining:
- Core skills
- Flexible example projects
- Checkpoints for "good enough"
- Folder/sub-repo where work for that phase lives

**Projects can change. Skills are the priority.**

Some sections will be worked on immediately (Phase 1),  
others won't be touched until many months from now.

This README is a **living document** that grows with me.

---

# 🚀 **[→ START HERE: Day 1 Guide](./GETTING_STARTED.md)**

New to this roadmap? Read the Getting Started guide first!

---

# 🧭 Overview of Phases (Skills-First Roadmap)

| Phase | Timeline | Skills Focus | Folder |
|-------|----------|---------------|--------|
| **1. Policy Skills & Communication** | Nov 2025 – Jan 2026 | Memos, structure, clarity, Clarity Act research | `/phase1_policy_memos` |
| **2. Data Visualization & Python Cleanliness** | Jan – Apr 2026 (parallel) | Clean charts, smoothing, Python style | `/phase2_viz` |
| **3. Lightning Network Mechanics** | Mar – Jul 2026 | LN channels, routing, liquidity | `/phase3_lightning` |
| **4. Economic Analysis (Lite)** | Jun – Oct 2026 | Understanding models, scenario analysis, BTC econ | `/phase4_econ_models` |
| **5. Data Analysis (Lite)** | Sep – Dec 2026 | Running regressions, interpreting results, basic stats | `/phase5_stats_pipelines` |
| **6. Basic Cryptography** | All year | Hashes, keys, signatures, Taproot | `/phase6_crypto_notes` |
| **7. Institutional Navigation** | All year | Staff workflow, briefings, communication | (no folder, personal notes) |
| **🏆 CAPSTONE** | **Nov – Dec 2026** | **Integrate ALL skills: Research paper on Bitcoin fees, macro factors, and Lightning Network** | `/capstone_project` |

---

# 🎯 Skills Progression & Prerequisites

Each phase builds on the last. Here's what you need to know:

| Phase | Python Level | Domain Knowledge | Prep Time Needed |
|-------|-------------|------------------|------------------|
| **Phase 1** | None | None | Jump right in (but learn Python alongside) |
| **Phase 2** | Beginner+ | None | Ready if you learned Python during Phase 1 |
| **Phase 3** | Intermediate | LN concepts | Read LN resources alongside |
| **Phase 4 (Lite)** | Intermediate | **Econ concepts** (light math) | 1 week refresher (late May) |
| **Phase 5 (Lite)** | Intermediate | **Basic statistics** | 1-2 weeks refresher (August) |

### 📚 Key Resources Referenced Throughout:
- **Python:** Kaggle courses, Python for Everybody, Corey Schafer YouTube
- **Calculus:** 3Blue1Brown, Khan Academy (just derivatives)
- **Econ Models:** Saylor ECON302, MRU videos, Cobb-Douglas refreshers
- **Statistics:** StatQuest (Josh Starmer), Saylor MA121, Intro to Statistical Learning
- **Lightning:** Mastering the Lightning Network, Andreas Antonopoulos talks

**All resources are FREE and linked in each phase's guide file.**

📖 **[→ See LEARNING_RESOURCES.md for complete list of courses, videos, and books](./LEARNING_RESOURCES.md)**

📘 **[→ Read 2026_LITE_APPROACH.md to understand the "breadth first" strategy](./2026_LITE_APPROACH.md)**

### 🗓️ Suggested Prep Schedule:
- **Jan-Mar 2026 (during Phase 1):** Learn Python basics in parallel with policy writing (3-5 hrs/week)
- **Late May 2026:** Calculus + Production function refresher (before Phase 4)
- **August 2026:** Statistics + Regression refresher (before Phase 5)

### 💡 Key Insight:
**Phase 1 (policy writing) requires no coding.** Use that time to learn Python alongside your memo work so you're ready for Phase 2 (data viz). This parallel approach saves time and keeps momentum.

### 📊 Self-Evaluation:
Each phase has a **self-evaluation rubric** with "good enough" checkpoints so you know when you're ready to move on. No guessing!

### 🎯 2026 Strategy: Breadth Over Depth
**Phases 4-5 are "Lite" versions** - you'll learn to USE tools and UNDERSTAND models, not build them from scratch. This gives you 80% of the career value with 20% of the effort. Go deeper in 2027 if you want.

**What "Lite" means:**
- **Phase 4:** Understand economic models, apply them, run scenarios (not build models from scratch)
- **Phase 5:** Run regressions, interpret results, use existing tools (not build data pipelines from scratch)

---

# 🟦 Phase 1 – Policy Skills & Communication  
**Timeline:** November 2025 – January 2026  
**Folder:** [`/phase1_policy_memos`](./phase1_policy_memos)

This is the most important starting phase — it determines how fast I become useful in D.C.

### 🎯 Core Goals
- Learn to write **Senate-ready briefing memos**  
- Translate complex Bitcoin topics into **clear, neutral policy language**
- Understand how chiefs/staffers use memos  
- Produce my **first real policy memo on The Clarity Act**

### 📘 Required Reading
- **The Clarity Act (full text)**  
- **Past Cato/Coin Center memos**  
- **Brookings memo handbook**

### 📄 Example Deliverables (Flexible)
- 1–2 page briefing memo: *What the Clarity Act actually does*  
- Talking points sheet: *Key implications for digital asset companies*  
- 3–5 page policy brief: *Legal, economic, and regulatory impacts*  
- Rewrite a Bitcoin technical concept into a staff-usable brief

*(These can all change — the skills are what matter.)*

### ✔️ Checkpoints Before Leaving Phase 1
- I can outline a briefing memo in <10 minutes  
- I can explain Clarity Act implications clearly  
- Chiefs/staffers can read my memos without asking "What does this mean?"

**📊 [Self-Evaluation Rubric](./phase1_policy_memos/PHASE1_RUBRIC.md)** - Use this to grade your work and know when you're ready  

---

# 🟦 Phase 2 – Data Visualization & Python Cleanliness  
**Timeline:** January – April 2026 (runs parallel to Phase 1)  
**Folder:** [`/phase2_viz`](./phase2_viz)

### 🎯 Core Goals
Become the person who can quickly turn messy Bitcoin/Lightning/miner data into clean charts that staffers and researchers love.

### 🛠️ Skills
- matplotlib, seaborn (later plotly/altair)  
- log scales, smoothing  
- readable, honest labeling  
- clean Python scripts

### 📄 Example Deliverables
- Bitcoin fee revenue chart (raw + smoothed)  
- Miner revenue breakdown (stackplot)  
- Lightning channel imbalance visualization

**📊 [Self-Evaluation Rubric](./phase2_viz/PHASE2_RUBRIC.md)** - Know when your charts are good enough

---

# 🟦 Phase 3 – Lightning Network Mechanics  
**Timeline:** March – July 2026  
**Folder:** [`/phase3_lightning`](./phase3_lightning)

### 🎯 Core Goals
Understand LN deeply enough to explain it to staffers and model it later.

### 🛠️ Skills
- Channels, HTLCs, timelocks  
- Source routing  
- Inbound vs outbound liquidity  
- Node basics (lncli, bos)

### 📄 Example Deliverables
- LN concept cheatsheet (explaining channels, HTLCs, liquidity)  
- Channel imbalance explorer notebook  
- Routing intuition notes

**📊 [Self-Evaluation Rubric](./phase3_lightning/PHASE3_RUBRIC.md)** - Test your Lightning Network knowledge

---

# 🟦 Phase 4 – Economic Analysis (Lite Version)
**Timeline:** June – October 2026  
**Folder:** [`/phase4_econ_models`](./phase4_econ_models)

**🆕 2026 Approach: Applied Economics, Not Building Models from Scratch**

### 🎯 Core Goals
Understand and apply economic models to Bitcoin - you're a user, not a builder (for now).

### 🛠️ Skills (Simplified)
- Reading and understanding economic models
- Running scenario analysis with existing models
- Interpreting economic results
- Basic cost/benefit analysis
- Understanding mining economics

### 📄 Example Deliverables (Achievable)
- Analyze existing Bitcoin security budget models
- Use online calculators + your own analysis for mining profitability
- Apply economic reasoning to Lightning liquidity questions
- Write economic analysis memos (not build models)

### 💡 What "Lite" Means:
Instead of building a Cobb-Douglas production function from scratch, you'll:
- Understand what production functions are
- Use existing models/tools
- Adjust parameters and see what changes
- Interpret results for policy work

**In 2027, if you want:** Go deeper and build models from scratch.

**📊 [Self-Evaluation Rubric](./phase4_econ_models/PHASE4_RUBRIC.md)** - Grade your economic analysis skills

---

# 🟦 Phase 5 – Data Analysis (Lite Version)
**Timeline:** September – December 2026  
**Folder:** [`/phase5_stats_pipelines`](./phase5_stats_pipelines)

**🆕 2026 Approach: Run Analysis, Not Build Pipelines from Scratch**

### 🎯 Core Goals
Be able to run regressions and interpret data - you're analyzing, not engineering (for now).

### 🛠️ Skills (Simplified)
- Load data from CSVs or simple APIs
- Clean data (basic)
- Run regressions with statsmodels
- Interpret p-values, R², coefficients
- Make charts showing regression results
- Understand correlation vs causation

### 📄 Example Deliverables (Achievable)
- Download mempool data → run regression → interpret results
- Analyze fee trends with simple statistical tests
- Create regression charts with confidence intervals
- Write data-driven memos

### 💡 What "Lite" Means:
Instead of building automated ETL pipelines, you'll:
- Manually download data or use simple API calls
- Clean it in pandas (basic filtering)
- Run regressions using statsmodels
- Focus on INTERPRETATION not engineering

**In 2027, if you want:** Build automated data pipelines and ETL systems.

**📊 [Self-Evaluation Rubric](./phase5_stats_pipelines/PHASE5_RUBRIC.md)** - Know when you're ready for the Capstone

---

# 🟦 Phase 6 – Basic Cryptography  
**Timeline:** All year (sprinkled)  
**Folder:** [`/phase6_crypto_notes`](./phase6_crypto_notes)

### 🎯 Core Goals
Understand cryptography behind Bitcoin/LN well enough to speak accurately.

### 🛠️ Skills
- Hashes  
- ECDSA basics  
- Merkle trees  
- Taproot privacy and signature aggregation

### 📄 Example Deliverables
- Crypto concept notes  
- Hash/sign/verify Python demo  

---

# 🟦 Phase 7 – Institutional Navigation  
**Timeline:** All year  
**Folder:** *(none — personal notes)*

### 🎯 Core Goals
Learn how to actually get things done inside a Senate office.

### Topics
- Staffer workflows  
- When to send emails vs memos  
- Coalition building  
- 2–5 minute verbal briefings  

---

# 🔗 Repo & Folder Structure

```
2026-bitcoin-skills-roadmap/
│
├── README.md
├── GETTING_STARTED.md        ← **START HERE on Day 1!**
├── LEARNING_RESOURCES.md     ← Master list of all courses, videos, tutorials
├── 2026_LITE_APPROACH.md     ← Why "Lite" versions + 2026 vs 2027 strategy
├── CAPSTONE_RESEARCH_PAPER.md  ← Final year-end research paper (integrates all skills)
│
├── capstone_project/          ← Your final research paper goes here
│
├── phase1_policy_memos/
│   ├── PHASE1_GUIDE.md
│   ├── PHASE1_RUBRIC.md   ← Self-evaluation rubric
│   ├── clarity_act_briefing_memo.md
│   ├── memo_templates/
│   ├── drafts/
│   └── projects/          ← Your completed personal project goes here
│
├── phase2_viz/
│   ├── JUPYTER_GUIDE.md
│   ├── PHASE2_RUBRIC.md   ← Self-evaluation rubric
│   ├── btc_fee_revenue.ipynb
│   ├── miner_revenue_breakdown.ipynb
│   ├── ln_imbalance_heatmap.ipynb
│   └── projects/          ← Your completed personal project goes here
│
├── phase3_lightning/
│   ├── JUPYTER_GUIDE.md
│   ├── PHASE3_RUBRIC.md   ← Self-evaluation rubric
│   ├── ln_concepts.md
│   ├── channel_imbalance_explorer.ipynb
│   ├── routing_intuition_notes.md
│   └── projects/          ← Your completed personal project goes here
│
├── phase4_econ_models/
│   ├── JUPYTER_GUIDE.md
│   ├── PHASE4_RUBRIC.md   ← Self-evaluation rubric
│   ├── PRODUCTION_FUNCTION_MODULE.md  ← Optional deep dive with essay assignment
│   ├── blockspace_production_function.ipynb
│   ├── ln_yield_capital_model.ipynb
│   ├── miner_mnav_v2.ipynb
│   └── projects/          ← Your completed personal project goes here
│
├── phase5_stats_pipelines/
│   ├── JUPYTER_GUIDE.md
│   ├── PHASE5_RUBRIC.md   ← Self-evaluation rubric
│   ├── mempool_fee_regression.ipynb
│   ├── btc_data_pipeline.py
│   ├── ln_activity_analysis.ipynb
│   └── projects/          ← Your completed personal project goes here
│
└── phase6_crypto_notes/
    ├── hashing_vs_encryption.md
    ├── ecdsa_basics.md
    └── taproot_notes.md
```

