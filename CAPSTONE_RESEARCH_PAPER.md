# Capstone Research Paper - End of Year 2026
**Integrating All Skills: Technical, Economic, Statistical, and Policy Analysis**

## 🎯 Overview

This is your **final major project for 2026** - a comprehensive research paper that demonstrates everything you've learned across all phases.

**Timeline:** November-December 2026 (6-8 weeks)  
**Target completion:** End of December 2026

---

## 📄 Research Paper Topic

### **"Bitcoin's Fee Market: A Multi-Factor Analysis of Blockspace Demand, Macroeconomic Conditions, and Lightning Network Adoption"**

**Alternative titles:**
- "Analyzing Bitcoin Fee Dynamics: The Role of Macro Factors and Layer 2 Adoption"
- "Blockspace Demand in Context: Connecting On-Chain Activity to Economic Conditions"

**Research Question:**  
How do Bitcoin transaction fees and blockspace demand correlate with:
1. Fed interest rates and monetary policy
2. Global liquidity conditions
3. Lightning Network adoption and usage
4. Traditional on-chain activity metrics

**Why this matters for policy:**
- Understanding Bitcoin's sensitivity to macro conditions
- Evaluating Lightning Network as a scaling solution
- Analyzing Bitcoin's role in the broader financial system
- Providing data-driven insights for digital asset policy

---

## 🎓 Skills Integration Map

This capstone uses skills from ALL phases:

| Phase | Skills Used in Capstone |
|-------|------------------------|
| **Phase 1** | Research paper writing, clear policy communication |
| **Phase 2** | Time series charts, multi-panel visualizations, clean graphics |
| **Phase 3** | Lightning Network data collection, understanding LN metrics |
| **Phase 4** | Economic framework for analysis, interpreting macro factors |
| **Phase 5** | Regression analysis, correlation studies, data pipelines |
| **Phase 6** | Understanding on-chain data, technical accuracy |

---

## 📊 Data You'll Collect

### 1. **Bitcoin On-Chain Data** (Technical - Node Connection)

**What to collect:**
- Daily average transaction fees (sat/vB)
- Daily mempool size
- Block fullness (% of 4MB weight used)
- Number of transactions per day
- UTXO set size (advanced)

**Data sources:**
- **Your own Bitcoin node** (if running one) via RPC calls
- **Bitcoin Core RPC API** - [Documentation](https://developer.bitcoin.org/reference/rpc/)
- **Mempool.space API** - https://mempool.space/docs/api
- **Blockchain.info API** - https://www.blockchain.com/api
- **Glassnode** (free tier) - https://glassnode.com/

**Technical setup:**
```python
# Example: Connecting to Bitcoin Core node
from bitcoinrpc.authproxy import AuthServiceProxy

# Connect to local node
rpc_connection = AuthServiceProxy("http://user:pass@127.0.0.1:8332")

# Get mempool info
mempool_info = rpc_connection.getmempoolinfo()
print(f"Mempool size: {mempool_info['size']} transactions")

# Get block data
block_hash = rpc_connection.getbestblockhash()
block = rpc_connection.getblock(block_hash)
```

**Timeline:** 2-3 weeks (Jan 2024 - Dec 2026 data)

---

### 2. **Lightning Network Data** (Phase 3 Skills)

**What to collect:**
- Total network capacity (BTC)
- Number of channels
- Number of nodes
- Average channel size
- Routing volume (if available)

**Data sources:**
- **1ML.com API** - https://1ml.com/
- **Amboss.space API** - https://amboss.space/api
- **Lightning Network Explorer APIs**
- **mempool.space Lightning stats** - https://mempool.space/lightning

**Example:**
```python
import requests

# Get Lightning Network stats from 1ML
response = requests.get('https://1ml.com/statistics')
data = response.json()

ln_capacity = data['capacity']
ln_channels = data['channelcount']
```

**Timeline:** Monthly or weekly snapshots (2024-2026)

---

### 3. **Macroeconomic Data** (Phase 4 Skills)

**What to collect:**
- Federal Funds Rate (Fed interest rate)
- M2 Money Supply (US)
- Global M2 (if available)
- DXY (US Dollar Index)
- Gold prices (as comparison)
- S&P 500 (risk-on sentiment)

**Data sources:**
- **FRED (Federal Reserve Economic Data)** - https://fred.stlouisfed.org/
  - Free API access
  - Excellent for Fed rates, M2, economic indicators
- **Yahoo Finance API** - For market data
- **World Bank Data** - For global metrics

**Example:**
```python
from fredapi import Fred

fred = Fred(api_key='your_api_key_here')

# Get Federal Funds Rate
fed_funds = fred.get_series('DFF')

# Get M2 Money Supply
m2_supply = fred.get_series('M2SL')
```

**Timeline:** Monthly data (2021-2026 for context)

---

## 📚 Learning Assignments (Before You Start)

### Week 1-2: Macro Factors & Bitcoin

**Reading Assignments:**
1. **[Lyn Alden: Bitcoin and Macro](https://www.lynalden.com/bitcoin-monetary-policy/)** - Understanding Bitcoin in macro context
2. **[Fed Monetary Policy Basics](https://www.federalreserve.gov/monetarypolicy.htm)** - How Fed policy works
3. **[Bitcoin & Liquidity](https://insights.glassnode.com/)** - Search Glassnode for liquidity analysis articles

**Video Assignments:**
- 📺 **[Lyn Alden: Bitcoin and Macro Environment](https://www.youtube.com/results?search_query=lyn+alden+bitcoin+macro)** - Search for her recent talks (~30-60 min)
- 📺 **[Fed Rate Impact on Markets](https://www.youtube.com/watch?v=lss1WMgjbm4)** - Understanding interest rate effects
- 📺 **[Bitcoin Correlations Explained](https://www.youtube.com/results?search_query=bitcoin+correlation+macro)** - How Bitcoin relates to other assets

**Take detailed notes on these questions:**

### 1. Liquidity & Bitcoin Adoption
- **What is "liquidity" in macro terms?** (M2 money supply, central bank balance sheets)
- **Theory:** When there's more money in the system, does Bitcoin price go up? Why?
- **Mechanism:** More liquidity → more money seeking assets → Bitcoin demand increases?
- **Evidence:** Look at 2020-2021 (QE period) vs 2022-2023 (QT period) - what happened?
- **Your hypothesis:** If liquidity increases Bitcoin *price*, does it also increase Bitcoin *usage* (transactions/fees)?
- **Alternative view:** Maybe liquidity affects price but not actual network usage?

### 2. Bitcoin & Interest Rates
- **The theory:** When Fed raises rates, what happens to "risk assets"?
- **Traditional view:** Higher rates → money flows to bonds → out of risky assets
- **Bitcoin question:** Is Bitcoin a "risk asset" like tech stocks? Or something different?
- **Mechanism to understand:**
  - High rates → strong dollar → Bitcoin down? (Bitcoin priced in USD)
  - High rates → less speculation → less Bitcoin trading → lower fees?
  - High rates → less borrowing → less leverage → less crypto activity?
- **Historical patterns:** What happened to Bitcoin in 2022-2023 when Fed hiked aggressively?
- **Note any lag effects:** Do interest rate changes affect Bitcoin immediately or with delay?

### 3. Risk-On vs Risk-Off
- **Define the terms:**
  - Risk-on: Investors buying risky assets (stocks, crypto, junk bonds)
  - Risk-off: Investors fleeing to safe assets (bonds, gold, cash)
- **Where does Bitcoin fit?**
  - Does it move with stocks (Nasdaq)? If yes, it's "risk-on"
  - Does it move with gold? If yes, maybe it's "digital gold" (safe haven)
  - Does it do its own thing? Maybe it's uncorrelated
- **How to measure:** Look at correlations between Bitcoin and S&P 500 or gold
- **Why this matters for your paper:** 
  - If Bitcoin is risk-on, then Fed policy → risk sentiment → Bitcoin price → maybe fees?
  - If Bitcoin is uncorrelated, then macro factors might not affect fees much
- **Note changes over time:** Bitcoin's correlation with stocks has changed. When? Why?

### 4. Connection to Fee Markets (The Key Question!)
**This is your research question - think through the logic:**

- **Direct mechanism:**
  - More Bitcoin activity → more transactions → higher demand for blockspace → higher fees
  - So: macro factors → Bitcoin activity → fees
  
- **Possible chains of causation:**
  - **Chain A:** Fed rate ↓ → more liquidity → Bitcoin price ↑ → more speculation → more on-chain activity → higher fees
  - **Chain B:** Fed rate ↓ → risk-on sentiment → more crypto trading → more on-chain activity → higher fees
  - **Chain C:** High fees → users move to Lightning → Lightning adoption increases
  
- **Things to consider:**
  - Do fee spikes come from speculation (DeFi, NFTs, memecoins) or from actual payment usage?
  - 2021 had high fees during bull market - was that macro liquidity or just hype?
  - 2023 had high fees from Ordinals/BRC-20 - unrelated to macro?
  - When fees are high, do users wait or move to Lightning?

- **Your hypothesis to form:**
  - "I expect Bitcoin fees to [increase/decrease/stay same] when Fed rates rise because..."
  - "I expect Lightning adoption to [increase/decrease] when on-chain fees are high because..."
  - "I expect [strong/weak/no] correlation between M2 and Bitcoin fees because..."

### 5. Alternative Explanations (Be ready for these!)
**Fees might be driven by factors OTHER than macro:**
- Technical events (Bitcoin upgrades, halving hype)
- Specific use cases (Ordinals, DeFi, exchanges moving funds)
- Mining dynamics (hashrate changes, difficulty adjustment timing)
- Seasonal patterns (end of quarter, tax deadlines)
- Pure speculation waves unrelated to fundamentals

**Note these so you can control for them in your analysis!**

### 6. What Good Notes Look Like

**For each reading/video, write:**
1. **Main argument:** What's the author's thesis?
2. **Evidence cited:** What data do they use?
3. **Time periods discussed:** When did X happen?
4. **Connections to your research:** How does this relate to fee markets?
5. **Questions raised:** What am I still unclear on?
6. **Counterarguments:** What's the opposite view?

**Example good notes:**
```
Lyn Alden article (Date read: X)
- Main point: Bitcoin tends to rise when global M2 increases
- Evidence: Chart showing correlation 2013-2022
- But: Correlation broke down in 2022-2023 when M2 fell but Bitcoin was flat
- My question: Does M2 affect Bitcoin PRICE or Bitcoin USAGE? Different things!
- For my paper: Need to test if M2 correlates with transaction volume or fees, not just price
- Counterargument: Maybe 2022 was unique due to FTX collapse, not representative
```

### 7. Framework to Develop

**By the end of your reading, you should be able to draw this causal chain:**

```
Macro Factor (Fed Rate/M2) 
    ↓
Risk Sentiment / Liquidity Conditions
    ↓
Bitcoin Price Movement?
    ↓
Bitcoin Network Activity (transactions)?
    ↓
Blockspace Demand
    ↓
Transaction Fees
    ↓ (maybe)
Lightning Network Adoption?
```

**Each arrow is a hypothesis to test with data.**

**Note which links are strong vs weak based on your reading.**

### 8. Policy Angle (Don't Forget This!)

**While reading, note policy implications:**
- If Bitcoin fees are sensitive to Fed policy, what does that mean?
- Does Lightning Network matter as a policy solution for high fees?
- Should policymakers care about Bitcoin fee volatility?
- What if fees make Bitcoin unusable during certain macro conditions?
- Is Lightning adoption a natural response to fee pressure (market working) or do policies help/hurt?

**This becomes your "Policy Implications" section later!**

---

## 🔬 Research Methodology

### Step 1: Data Collection (2 weeks)

Create a master dataset with aligned timestamps:

```python
import pandas as pd

# Combine all data sources
df = pd.DataFrame({
    'date': date_range,
    'btc_avg_fee': btc_fees,
    'mempool_size': mempool_data,
    'ln_capacity': ln_data,
    'fed_funds_rate': fed_rate,
    'm2_supply': m2_data,
    'sp500': sp500_prices
})

# Save to CSV for reproducibility
df.to_csv('bitcoin_macro_dataset.csv', index=False)
```

### Step 2: Exploratory Data Analysis (1 week)

**Visualizations to create:**
1. Time series of all variables (separate charts)
2. Bitcoin fee trends over time
3. Lightning Network growth chart
4. Macro indicators over the same period
5. Initial scatter plots (fee vs each variable)

### Step 3: Statistical Analysis (2 weeks)

**Correlations:**
```python
import seaborn as sns

# Correlation matrix
correlation_matrix = df.corr()
sns.heatmap(correlation_matrix, annot=True)
plt.title('Correlation Matrix: Bitcoin Fees vs Macro Factors')
```

**Regressions to run:**

**Model 1: Baseline**
```python
import statsmodels.api as sm

# Simple regression: Fees ~ Fed Rate
X = sm.add_constant(df['fed_funds_rate'])
y = df['btc_avg_fee']
model1 = sm.OLS(y, X).fit()
print(model1.summary())
```

**Model 2: Multi-factor**
```python
# Multiple regression
X = df[['fed_funds_rate', 'm2_supply', 'ln_capacity', 'mempool_size']]
X = sm.add_constant(X)
y = df['btc_avg_fee']
model2 = sm.OLS(y, X).fit()
print(model2.summary())
```

**Model 3: Time lags**
```python
# Test if macro factors affect Bitcoin with a lag
df['fed_rate_lag_1m'] = df['fed_funds_rate'].shift(30)  # 30-day lag
# Then run regression with lagged variables
```

**Statistical tests:**
- Granger causality (does Fed rate predict fee changes?)
- Cointegration tests (are variables related long-term?)
- Rolling correlations (do relationships change over time?)

### Step 4: Interpret & Write (3 weeks)

Write the research paper with your findings.

---

## 📝 Research Paper Structure

**Length:** 6,000-8,000 words (~20-25 pages double-spaced)

### Outline:

**I. Executive Summary** (1 page)
- Key findings in bullet points
- Written for policy audience
- No jargon

**II. Introduction** (2-3 pages)
- Why this question matters
- Policy relevance
- Brief literature review
- Your hypothesis
- Paper structure overview

**III. Background & Theory** (3-4 pages)
- Bitcoin fee market mechanics
- Lightning Network as scaling solution
- Macro factors and asset prices (theory)
- Expected relationships and why

**IV. Data & Methodology** (3-4 pages)
- Data sources (with citations)
- Time period covered
- Variables defined
- Statistical methods used
- Limitations

**V. Results** (5-6 pages)
- Descriptive statistics
- Correlation analysis
- Regression results
- Charts and tables (6-10 total)
- Interpretation of findings

**VI. Discussion** (3-4 pages)
- What do the results mean?
- Which factors matter most?
- Does Lightning Network adoption affect fees?
- Are fees sensitive to macro conditions?
- Limitations and caveats
- Alternative explanations

**VII. Policy Implications** (2-3 pages)
- What this means for digital asset policy
- Lightning Network as a policy solution?
- Bitcoin's relationship with traditional finance
- Recommendations for policymakers

**VIII. Conclusion** (1-2 pages)
- Summary of findings
- Contribution to policy discussions
- Future research questions

**IX. References** (2-3 pages)
- Properly cited sources
- Academic papers, policy documents, data sources

**X. Appendices** (as needed)
- Technical documentation
- Additional charts
- Code snippets (optional)
- Robustness checks

---

## 📊 Required Visualizations (Minimum 10)

### Time Series Charts (Phase 2 Skills):
1. **Bitcoin average fees over time** (2021-2026)
2. **Lightning Network capacity over time**
3. **Fed Funds Rate over time** (with recession bands)
4. **M2 Money Supply growth rate**

### Analytical Charts:
5. **Scatter plot: Fees vs Fed Rate** (with regression line)
6. **Scatter plot: Fees vs Lightning Capacity**
7. **Correlation heatmap** of all variables
8. **Rolling correlation chart** (fees vs macro factors over time)

### Multi-Panel Comparisons:
9. **4-panel chart:**
   - Top left: BTC fees
   - Top right: Fed rate
   - Bottom left: LN capacity
   - Bottom right: Mempool size

10. **Regression results visualization:**
    - Coefficient plot with confidence intervals

**All charts must be:**
- Publication quality
- Clear labels and titles
- Properly sourced
- Interpretable by non-technical readers

---

## 🎯 Evaluation Criteria

### Technical Execution (30%)
- ✅ Successfully collected data from multiple sources
- ✅ Clean, reproducible analysis code
- ✅ Appropriate statistical methods
- ✅ Proper interpretation of results
- ✅ Acknowledged limitations

### Economic & Policy Understanding (25%)
- ✅ Understands macro factors
- ✅ Applies economic reasoning correctly
- ✅ Connects findings to policy
- ✅ Realistic policy recommendations
- ✅ Acknowledges complexity

### Bitcoin/Lightning Expertise (20%)
- ✅ Accurate description of Bitcoin fee market
- ✅ Correct Lightning Network understanding
- ✅ Technical accuracy throughout
- ✅ Understands on-chain dynamics

### Writing & Communication (15%)
- ✅ Clear, professional writing
- ✅ Logical structure
- ✅ Accessible to policy audience
- ✅ Proper citations
- ✅ No major errors

### Visualizations (10%)
- ✅ Clean, publication-quality charts
- ✅ Appropriate chart types
- ✅ Clear interpretation
- ✅ Properly labeled

---

## 💻 Technical Setup Guide

### Prerequisites:
- Completed Phases 1-5
- Python environment with:
  - pandas, numpy, matplotlib, seaborn
  - statsmodels
  - requests (API calls)
  - fredapi (for Fed data)
  - Optional: bitcoinrpc (if running own node)

### Setup Checklist:

**Week 1:**
- [ ] Install required Python packages
- [ ] Get API keys (FRED, Mempool.space, etc.)
- [ ] Test data connections
- [ ] Create project folder structure

**Week 2-3:**
- [ ] Collect Bitcoin on-chain data
- [ ] Collect Lightning Network data
- [ ] Collect macro data
- [ ] Align all timestamps

**Week 4:**
- [ ] Create exploratory visualizations
- [ ] Calculate basic statistics
- [ ] Check for data quality issues

**Week 5-6:**
- [ ] Run correlation analysis
- [ ] Run regression models
- [ ] Test different specifications
- [ ] Document all results

**Week 7-8:**
- [ ] Write paper draft
- [ ] Create final visualizations
- [ ] Revise and polish
- [ ] Get feedback (optional)

---

## 📚 Key References to Cite

### Bitcoin Fee Market:
- Bitcoin whitepaper (Nakamoto, 2008)
- "The Bitcoin Fee Market" research papers (search Google Scholar)
- Mempool.space documentation

### Lightning Network:
- Lightning Network whitepaper (Poon & Dryja, 2016)
- "Mastering the Lightning Network" book
- Academic papers on Lightning adoption

### Macro & Bitcoin:
- Lyn Alden's articles
- "Bitcoin as Digital Gold" research
- Federal Reserve publications on monetary policy

### Statistical Methods:
- "Introduction to Statistical Learning" (for methods)
- Any academic papers using similar analysis

---

## 🎖️ What Success Looks Like

After completing this capstone, you'll have:

✅ **A portfolio piece** - Impressive research paper to show employers  
✅ **Technical chops** - Demonstrated ability to collect and analyze data  
✅ **Policy relevance** - Connected Bitcoin to macro policy questions  
✅ **Statistical credibility** - Rigorous analysis with proper methods  
✅ **Communication skills** - Clear writing for policy audience  

**This paper proves you can:**
- Do original research
- Handle technical Bitcoin data
- Apply economic reasoning
- Write for policy audiences
- Use statistical tools properly

---

## 💡 Tips for Success

### Before You Start:
1. **Plan your timeline** - 6-8 weeks is realistic
2. **Set up your environment early** - Test all data sources
3. **Start with exploratory analysis** - Understand your data first
4. **Don't expect perfect correlations** - Real data is messy

### While Working:
1. **Document everything** - Save your code and notes
2. **Make charts as you go** - Don't wait until the end
3. **Write incrementally** - Start with methods section first
4. **Get feedback early** - Show drafts to colleagues

### Common Pitfalls:
- ❌ Overstating correlations (correlation ≠ causation!)
- ❌ Ignoring Bitcoin's extreme volatility
- ❌ Too technical for policy audience
- ❌ Not enough charts/visualizations
- ❌ Forgetting to discuss limitations
- ❌ Cherry-picking time periods

---

## 📤 Final Deliverables

**Save in:** `/capstone_project/`

**Required files:**
1. `research_paper.pdf` - Final paper (20-25 pages)
2. `analysis.ipynb` - Jupyter notebook with all analysis
3. `data/` folder - All datasets used (with documentation)
4. `charts/` folder - All visualizations (high-res PNG or PDF)
5. `README.md` - Overview of the project and how to reproduce

**Optional but impressive:**
6. `slides.pdf` - 10-slide presentation of findings
7. `policy_brief.pdf` - 2-page exec summary for busy staffers

---

## 🏆 Why This Capstone Matters

**For your career:**
- Demonstrates you can do original research
- Shows technical + policy skills
- Portfolio piece for future jobs
- Proves you can finish complex projects

**For policy work:**
- Actually answers an important question
- Provides data for policy debates
- Connects Bitcoin to macro policy
- Shows how Lightning fits in

**For Bitcoin community:**
- Contributes real analysis
- Policy-relevant research
- Could be published/shared

---

## 🚀 After Completion

**Consider:**
- Share on GitHub (public or private)
- Present to BPI colleagues
- Submit to Bitcoin policy journals/publications
- Turn into a blog post series
- Use as writing sample for future jobs

**Optional follow-ups:**
- Expand to full working paper
- Update quarterly with new data
- Collaborate with economists on peer review
- Present at Bitcoin conferences

---

## 🤝 Getting Help

**Stuck on:**
- **Data collection:** Check API documentation, Stack Overflow
- **Statistics:** Review Phase 5 materials, ask BPI economists
- **Writing:** Review Phase 1 guides, get peer feedback
- **Interpretation:** This is the hard part - think carefully, be honest about uncertainty

**Remember:** It's OK if results don't show what you expected. Good research reports what the data shows, not what you hoped to find.

---

**This capstone integrates everything you learned in 2026. It's ambitious, but after completing all phases, you're ready for it. Good luck!** 🚀

---

## 📅 Suggested Timeline (6-8 weeks)

| Week | Task | Hours |
|------|------|-------|
| 1 | Setup + reading assignments | 8-10 |
| 2-3 | Data collection | 15-20 |
| 4 | Exploratory analysis | 10-12 |
| 5-6 | Statistical analysis | 15-20 |
| 7 | Writing first draft | 12-15 |
| 8 | Revisions + final charts | 10-12 |

**Total: 70-90 hours over 6-8 weeks**

That's **10-15 hours/week** - your final push to finish 2026 strong!

