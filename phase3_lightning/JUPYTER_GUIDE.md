# Jupyter Notebooks Guide - Phase 3 (Lightning Network)

## What are Jupyter Notebooks?

Interactive documents where you write Python code, run it, and see results immediately. Perfect for exploring data and testing ideas.

**Structure:**
- **Code cells:** Write and run Python
- **Markdown cells:** Add explanations and notes
- **Output cells:** Charts, data, results appear automatically

---

## 🎓 Prerequisites & Learning Resources

### Python Skills Needed for Phase 3:
✅ **Must know before starting:**
- Everything from Phase 2 (Python basics, pandas, matplotlib)
- API calls with `requests` library (can learn quickly)
- JSON data handling

⚠️ **Will learn during this phase:**
- Lightning Network concepts
- Working with LN node data
- Network analysis and visualization

### 📚 Lightning Network Learning Resources:

**Core LN Concepts:**
- **[Lightning Network Whitepaper](https://lightning.network/lightning-network-paper.pdf)** - Original paper (skim first, deep read later)
- **[Mastering the Lightning Network (free book)](https://github.com/lnbook/lnbook)** - Comprehensive LN guide
- **[Bitcoin Optech: LN Topics](https://bitcoinops.org/en/topics/lightning-network/)** - Technical but accessible

📺 **YouTube:**
- **[Andreas Antonopoulos: Lightning Network Explained](https://www.youtube.com/results?search_query=andreas+antonopoulos+lightning+network)** - Search for his LN talks
- **[chaincode labs: Lightning Network Seminar](https://www.youtube.com/playlist?list=PLpLH33TRghT17_U3as2P3vHfAGL8pSOOY)** - Technical but excellent

**Python API Skills:**
- **[Real Python: API Tutorial](https://realpython.com/python-api/)** - Learn API calls
- **[Working with JSON in Python](https://realpython.com/python-json/)** - JSON handling

### Time Estimate:
- **LN concept reading:** 1-2 weeks alongside exercises
- **Python API skills (if new):** 2-3 days

## What to Focus On for Phase 3

**This phase is about understanding Lightning Network mechanics through data.**

For each notebook in this folder:
- **Explore first:** Pull channel data, look at it, understand what you're seeing
- **Build intuition:** How do channels work? What does "imbalanced" mean?
- **Visualize patterns:** Where is liquidity stuck? Why?

### Key Skills to Practice:
- Fetching LN data (APIs or node commands)
- Understanding channel states (local/remote balance)
- Calculating imbalances
- Visualizing network topology
- Connecting data to concepts (HTLCs, routing, liquidity)

### Workflow:
1. Read `ln_concepts.md` first to understand the theory
2. Open a notebook and fetch real LN data
3. Explore the data (print it, look at it)
4. Analyze: Calculate metrics like channel imbalance
5. Visualize: Make charts that show patterns
6. Document: Write markdown cells explaining what you learned

**Goal:** By the end, you should be able to explain LN mechanics to a staffer using your own charts and analysis.

---

## 🎯 Phase 3 Personal Project (Required)

**Once you've completed all exercises and reading, do ONE original project that demonstrates your Lightning Network knowledge.**

### Link to Your Completed Project:
`[Project title here - add when done]` → `[Link or file path]`

### Project Ideas (pick one or create your own):
1. **Node Liquidity Analysis** - Pick 5 major Lightning nodes and analyze their channel balance distribution, routing potential, and connectivity
2. **Channel Fee Economics Study** - Analyze how routing fees vary across the network and what makes a "profitable" routing node
3. **LN vs On-Chain Cost Comparison** - Model when it makes sense to use Lightning vs on-chain for different transaction sizes/frequencies

**Better yet:** After completing the exercises, come up with your own project idea based on what you found interesting or what would help explain LN to policymakers.

### Why This Matters:
LN is complex. Being able to explain it clearly with your own analysis makes you valuable in policy discussions about Bitcoin's scaling and payments.

---

## 📁 Note on Repository Structure

**For now:** Your personal project can live in this phase folder (create a `/projects` subfolder if needed).

**Later (optional):** If you want to showcase your Lightning Network expertise, you can move it to a separate repository (e.g., `lightning-liquidity-analysis`) that serves as a standalone research piece. Link it back in the main roadmap README.

**Reminder to Cursor AI:** This phase can eventually become its own repository if the user chooses to split their work for portfolio purposes. Support either approach based on what the user asks for.

