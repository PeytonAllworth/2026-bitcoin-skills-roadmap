# Phase 5 Self-Evaluation Rubric
**Data Analysis (Lite Version)**

Use this rubric to evaluate your statistical analysis skills throughout Phase 5.

---

## 📋 Evaluation Categories

### 1. Data Skills (25 points)

| Criteria | Needs Work (1-2) | Getting There (3) | Good (4) | Excellent (5) | Your Score |
|----------|------------------|-------------------|----------|---------------|------------|
| **Data loading** | Struggles | Basic loading | Comfortable | Advanced | __/5 |
| **Data cleaning** | Poor cleaning | Basic cleaning | Good cleaning | Excellent cleaning | __/5 |
| **Data manipulation** | Struggles with pandas | Basic pandas | Comfortable | Advanced pandas | __/5 |
| **Missing data** | Doesn't handle | Handles poorly | Handles well | Handles expertly | __/5 |
| **Data quality** | Doesn't check | Basic checks | Good checks | Rigorous checks | __/5 |

**Subtotal: __/25**

---

### 2. Statistical Analysis (30 points)

| Criteria | Needs Work (1-2) | Getting There (3) | Good (4) | Excellent (5) | Your Score |
|----------|------------------|-------------------|----------|---------------|------------|
| **Running regressions** | Can't run | Basic regressions | Good regressions | Advanced regressions | __/5 |
| **Interpreting p-values** | Wrong interpretation | Mostly correct | Correct | Expert interpretation | __/5 |
| **Understanding R²** | Doesn't understand | Basic understanding | Good understanding | Expert understanding | __/5 |
| **Coefficients** | Can't interpret | Basic interpretation | Good interpretation | Expert interpretation | __/5 |
| **Assumptions** | Doesn't check | Checks poorly | Checks well | Rigorous checking | __/5 |
| **Correlation vs causation** | Confuses them | Mostly gets it | Gets it | Always careful | __/5 |

**Subtotal: __/30**

---

### 3. Communication (25 points)

| Criteria | Needs Work (1-2) | Getting There (3) | Good (4) | Excellent (5) | Your Score |
|----------|------------------|-------------------|----------|---------------|------------|
| **Explaining results** | Confusing | Somewhat clear | Clear | Very clear | __/5 |
| **Regression charts** | Poor charts | Okay charts | Good charts | Excellent charts | __/5 |
| **Statistical writing** | Too technical | Somewhat accessible | Accessible | Very accessible | __/5 |
| **Caveats/limitations** | Ignores limitations | Mentions some | Good discussion | Thorough discussion | __/5 |
| **Policy relevance** | No connection | Weak connection | Good connection | Strong connection | __/5 |

**Subtotal: __/25**

---

### 4. Practical Application (20 points)

| Criteria | Needs Work (1-2) | Getting There (3) | Good (4) | Excellent (5) | Your Score |
|----------|------------------|-------------------|----------|---------------|------------|
| **Real data analysis** | Can't do it | Basic analysis | Good analysis | Advanced analysis | __/5 |
| **Problem-solving** | Struggles | Some success | Good success | Expert level | __/5 |
| **Insight quality** | Obvious/none | Some insights | Good insights | Novel insights | __/5 |
| **Reproducibility** | Can't reproduce | Somewhat reproducible | Reproducible | Highly reproducible | __/5 |

**Subtotal: __/20**

---

## 📊 Total Score: __/100

### Score Interpretation:

- **90-100:** Excellent! Can do rigorous statistical analysis.
- **75-89:** Good! Solid data analysis skills.
- **60-74:** Getting there. Practice more regressions.
- **Below 60:** Needs work. Review StatQuest videos.

---

## ✅ "Good Enough" Checkpoints

**You're ready for the Capstone when you can answer YES to all:**

### Checkpoint 1: Data Handling
- [ ] I can load CSV files and simple API data
- [ ] I can clean data (remove NaN, filter outliers)
- [ ] I can merge datasets with different timestamps
- [ ] I can check for data quality issues
- [ ] I understand my data before analyzing

### Checkpoint 2: Regression Skills
- [ ] I can run a simple OLS regression with statsmodels
- [ ] I can interpret p-values correctly
- [ ] I can interpret R² correctly
- [ ] I can interpret coefficients correctly
- [ ] I can make regression plots with confidence intervals

### Checkpoint 3: Statistical Thinking
- [ ] I know correlation doesn't mean causation
- [ ] I check regression assumptions (linearity, normality, etc.)
- [ ] I understand statistical significance vs practical significance
- [ ] I can spot suspicious results
- [ ] I'm honest about limitations

### Checkpoint 4: Communication
- [ ] I can explain regression results to non-statisticians
- [ ] My regression charts are clear
- [ ] I write about statistics accessibly
- [ ] I connect data to policy questions
- [ ] I discuss caveats and limitations

### Checkpoint 5: Portfolio
- [ ] I've completed at least one full data analysis
- [ ] I have regression results I can explain
- [ ] I have regression visualizations
- [ ] My analysis is reproducible (clean code)
- [ ] My work is policy-relevant

---

## 🎯 Phase 5 (Lite) Minimum Viable Skills

**Before starting the Capstone, you MUST be able to:**

1. ✅ **Load and clean Bitcoin/macro data**
2. ✅ **Run OLS regressions with statsmodels**
3. ✅ **Interpret p-values, R², and coefficients correctly**
4. ✅ **Make regression plots**
5. ✅ **Explain results in plain English**
6. ✅ **Understand correlation vs causation**
7. ✅ **Write data-driven analysis**

**Note:** You do NOT need to build production data pipelines (that's the "Lite" approach)

**If you can do all 7 → You're ready for the Capstone!**

---

## 📝 Self-Evaluation Template

**Test your understanding:**

```
Date: _______________________________
Score: __/100

Can I do (Yes/No):
- [ ] Load Bitcoin data from CSV/API?
- [ ] Clean data (remove NaN, filter)?
- [ ] Run a regression?
- [ ] Interpret p-values?
- [ ] Interpret R²?
- [ ] Interpret coefficients?
- [ ] Make regression plots?

Analysis completed:
Research question: _______________________________
Key finding:
_______________________________
P-value: _______
R²: _______

Was the relationship significant? [Yes/No]
Was it causal? [Yes/No/Maybe]
How do I know?
_______________________________

Am I ready for the Capstone? [Yes/No]
```

---

## 💡 Testing Your Knowledge

**The "Regression Interpretation Test":**

Given these regression results:
```
Dependent Variable: Bitcoin Fees (sat/vB)
Independent Variable: Mempool Size (MB)

Coefficient: 2.5
P-value: 0.001
R²: 0.65
```

**Can you answer:**
1. Is the relationship statistically significant?
2. What does the coefficient mean?
3. How much variation is explained?
4. Does mempool size CAUSE higher fees?
5. What could explain the remaining 35% of variation?

**If you can answer all 5 correctly → You understand regressions!**

---

## 🚨 Red Flags (Need More Work)

**If you see these, you're NOT ready for the Capstone:**

- ❌ You can't run a regression without extensive googling
- ❌ You misinterpret p-values
- ❌ You think correlation = causation
- ❌ You can't load and clean data
- ❌ You haven't completed any full analysis
- ❌ Your code is a mess (can't reproduce results)

**Solution:** Watch more StatQuest videos, do more practice regressions, get feedback.

---

## ✨ Signs You're Crushing Phase 5

**You're ready for the Capstone if:**

- ✅ You run regressions confidently
- ✅ You interpret results correctly
- ✅ You catch your own statistical errors
- ✅ You think critically about causation
- ✅ You're excited to apply this to your research question!

**Congratulations! Start the Capstone!** 🎉

---

**Remember:** Phase 5 Lite is about RUNNING and INTERPRETING analysis, not building production systems.

If you can load data, run regressions, and explain results clearly → **You passed Phase 5 Lite.**

**The Capstone will integrate everything:** Your policy writing + viz + Lightning knowledge + economic thinking + statistical skills = One comprehensive research paper!

**You're ready!** 🚀

