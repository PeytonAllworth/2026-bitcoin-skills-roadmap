# Jupyter Notebooks Guide - Phase 5 (Data Analysis - Lite Version)

**🆕 2026 Approach: Run Analysis, Not Build Engineering Pipelines**

## What are Jupyter Notebooks?

Interactive coding environments where you:
- Load data (CSVs or simple API calls)
- Clean it (basic filtering and handling missing values)
- Run regressions and statistical tests
- Make charts and interpret results

**This phase is about ANALYZING data and INTERPRETING results, not building production data pipelines.**

---

## 🎓 Prerequisites & Learning Resources

### Python Skills Needed for Phase 5 (Lite):
✅ **Must know before starting:**
- Everything from Phases 2-3 (Python, pandas, matplotlib)
- Basic data loading (read_csv, simple API calls)
- That's it! No SQL or complex pipelines needed.

⚠️ **Will learn during this phase:**
- statsmodels library for regressions
- Basic data cleaning techniques
- Interpreting regression output (p-values, R², coefficients)
- Making regression plots with confidence intervals

### Statistics Knowledge Needed:

**Core concepts you need:**
- What is regression?
- How to interpret coefficients, p-values, R²
- Correlation vs causation
- Basic hypothesis testing

📚 **Free Statistics Courses:**

**Best Starting Point:**
- **[Saylor Academy: MA121 - Introduction to Statistics](https://learn.saylor.org/course/view.php?id=28)** - Full intro course
- **[Khan Academy: Statistics & Probability](https://www.khanacademy.org/math/statistics-probability)** - Interactive, good refresher

**For Regression (Your Main Focus):**
- **[StatQuest: Linear Regression](https://www.youtube.com/watch?v=nk2CQITm_eo)** - ⭐ START HERE. Josh Starmer is amazing. WATCH THIS.
- **[StatQuest: P-values](https://www.youtube.com/watch?v=vemZtEM63GY)** - Essential for interpretation
- **[StatQuest: R-squared](https://www.youtube.com/watch?v=2AQKmw14mHM)** - Understanding model fit

📖 **Quick Reference (Pick One):**
- **[Introduction to Statistical Learning - Chapter 3](https://www.statlearning.com/)** - Linear regression chapter only
- **[Real Python: Linear Regression in Python](https://realpython.com/linear-regression-in-python/)** - Practical tutorial

### Python for Statistics (Simple Approach):
- **[Real Python: Linear Regression Tutorial](https://realpython.com/linear-regression-in-python/)** - Learn by doing
- **[statsmodels Getting Started](https://www.statsmodels.org/stable/gettingstarted.html)** - Official docs (skim)

### Time Estimate (Lite Version):
- **Watch StatQuest videos:** 2-3 hours (MUST DO)
- **Read one tutorial:** 2-3 hours
- **Practice running regressions:** 3-5 hours
- **Total prep before Phase 5:** ~1-2 weeks (do this in August)

### What You're Skipping (Can Learn in 2027):
- ❌ Building automated ETL pipelines
- ❌ SQLite databases and data engineering
- ❌ Async API calls and production systems
- ❌ Advanced statistical methods

### What You're Focusing On:
- ✅ Running regressions with statsmodels
- ✅ Interpreting results correctly
- ✅ Making regression plots
- ✅ Writing data-driven analysis

## What to Focus On for Phase 5

**This phase is about becoming data-capable: regressions, ETL, structured datasets.**

For each notebook in this folder:
- **ETL mindset:** Extract data, Transform it, Load it (into a DataFrame or SQLite)
- **Statistical rigor:** Run proper regressions, check assumptions, interpret correctly
- **Automation:** Write code that can run daily/weekly to update data
- **Reproducibility:** Document everything so you can re-run later

### Key Skills to Practice (Lite Version):
- Loading data from CSV or simple API calls
- Basic data cleaning (handling missing data, basic filtering)
- Running regressions with statsmodels
- **Interpreting results** (p-values, R², coefficients)
- Making regression plots
- Understanding correlation vs causation

### Workflow (Lite Approach):
1. **Get data:** Download CSV or make simple API call
2. **Clean basics:** Remove NaN values, filter obvious outliers
3. **Run regression:** Use statsmodels OLS
4. **Check results:** Look at p-values, R², coefficients
5. **Make chart:** Scatter plot with regression line
6. **Interpret:** What does this mean? Write it up clearly

### Example Structure (Lite Approach):
```python
import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm

# 1. Load data (download CSV manually or use simple API call)
df = pd.read_csv('bitcoin_fees.csv')  # You downloaded this
# Or: df = pd.read_json('https://api.example.com/data')

# 2. Basic cleaning
df = df.dropna()  # Remove missing values
df = df[df['fee'] > 0]  # Filter out zeros

# 3. Run regression
X = df[['mempool_size']]
y = df['fee']
X = sm.add_constant(X)  # Add intercept

model = sm.OLS(y, X).fit()
print(model.summary())  # Look at p-values, R²

# 4. Make chart
plt.scatter(df['mempool_size'], df['fee'], alpha=0.5)
plt.plot(df['mempool_size'], model.predict(X), color='red', linewidth=2)
plt.xlabel('Mempool Size (MB)')
plt.ylabel('Fee (sat/vB)')
plt.title('Mempool Size vs Transaction Fees')
plt.show()

# 5. Interpret: Write in markdown cell what the results mean
```

**Goal:** Be able to load data, run regressions, and write data-driven policy analysis.

### What Makes This "Lite":
- You manually download or do simple data pulls (no automated pipelines)
- You focus on ONE regression technique (OLS)
- You skip database engineering
- You focus on INTERPRETATION over ENGINEERING

**If you love this in 2027:** Then build automated data pipelines and production systems.

---

## 🎯 Phase 5 Personal Project (Required)

**Once you've completed all exercises and reading, do ONE original data analysis project that demonstrates your stats/pipeline skills.**

### Link to Your Completed Project:
`[Project title here - add when done]` → `[Link or file path]`

### Project Ideas (pick one or create your own - Lite versions):
1. **Ordinals Impact Analysis (Simple)** - Download historical fee data and ordinals activity data. Run a regression: Do ordinals correlate with higher fees? Make charts. Write interpretation. (No automated pipeline needed)
2. **Fee Trend Analysis** - Download mempool size and fee data for the past year. Run regression. Do bigger mempools = higher fees? How strong is the relationship? Chart it and explain.
3. **Lightning Activity Analysis** - Get public Lightning Network stats (capacity, channels). Get on-chain fee data. Analyze: Do high fees correlate with more Lightning growth? Simple correlation/regression analysis.

**Better yet:** After completing the exercises, pick a policy question and do simple statistical analysis to answer it.

### Why This Matters:
Being able to run statistical analysis and interpret results yourself means you can evaluate claims in policy debates. You can say "I ran the numbers and here's what they show."

### Deliverable (Achievable):
- Jupyter notebook with clear analysis
- Data loaded from CSV or simple API call
- One solid regression with interpretation
- 2-3 clean charts
- Brief write-up (1-2 pages) in markdown cells explaining findings

### What Makes This "Lite":
- Manual data downloads (not automated pipelines)
- Simple regression analysis (not complex statistical methods)
- Focus on interpretation (not engineering)
- Still produces valuable, credible analysis

**This is enough to be useful in policy work! If you want to build production data pipelines in 2027, you'll have the foundation.**

---

## 📁 Note on Repository Structure

**For now:** Your personal project can live in this phase folder (create a `/projects` subfolder if needed).

**Later (optional):** Data analysis projects with working pipelines make excellent standalone repositories (e.g., `ordinals-impact-analysis`). If your analysis is solid, a separate repo with clean code, documented pipeline, and write-up serves as a strong portfolio piece. Link it back in the main roadmap README.

**Reminder to Cursor AI:** This phase can eventually become its own repository if the user chooses to split their work for portfolio purposes. Support either approach based on what the user asks for.

