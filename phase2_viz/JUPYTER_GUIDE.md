# Jupyter Notebooks Guide - Phase 2 (Data Visualization)

## What are Jupyter Notebooks?

Jupyter notebooks (`.ipynb` files) are interactive documents that let you mix:
- **Code** (Python) that you can run cell-by-cell
- **Output** (charts, tables, numbers) that appears right below the code
- **Text/notes** (markdown cells) for explanations

Think of it like a lab notebook for data analysis — you write code, run it, see results, and document your thinking all in one place.

---

## 🎓 Prerequisites & Learning Resources

### Python Skills Needed for Phase 2:
✅ **Must know before starting:**
- Python basics (variables, lists, dictionaries, loops)
- How to import libraries
- Basic pandas (DataFrames, reading CSV files)

⚠️ **Will learn during this phase:**
- matplotlib and seaborn plotting
- Data smoothing techniques
- Log scales and chart styling

### 📚 Free Python Courses (if you're new or rusty):

**Python Basics:**
- **[Saylor Academy CS101](https://learn.saylor.org/course/view.php?id=6)** - Introduction to Computer Science (Python modules)
- **[Python for Everybody (py4e)](https://www.py4e.com/)** - Free course by Dr. Chuck (University of Michigan)
- **[Kaggle: Python Course](https://www.kaggle.com/learn/python)** - Quick, interactive, free

**Pandas Basics:**
- **[Kaggle: Pandas Course](https://www.kaggle.com/learn/pandas)** - Free, 4 hours
- **[Pandas Documentation: 10 Minutes to Pandas](https://pandas.pydata.org/docs/user_guide/10min.html)**

📺 **YouTube Playlists:**
- **[Corey Schafer: Matplotlib Tutorials](https://www.youtube.com/playlist?list=PL-osiE80TeTvipOqomVEeZ1HRrcEvtZB_)** - Best matplotlib series
- **[Data School: Pandas](https://www.youtube.com/playlist?list=PL5-da3qGB5ICCsgW1MxlZ0Hq8LL5U3u9y)** - Excellent pandas intro

### Time Estimate:
- **If Python beginner:** 2-3 weeks of prep before Phase 2 exercises
- **If you know Python basics:** Jump right in, learn plotting as you go

## How to Use Them

1. Open the `.ipynb` file in VS Code or Jupyter Lab
2. Run cells one at a time (Shift + Enter)
3. Edit code, re-run, iterate
4. Charts appear inline below your code

## What to Focus On for Phase 2

**This phase is about making clean, readable visualizations.**

For each notebook in this folder:
- **Start simple:** Load data, make a basic chart
- **Iterate:** Add labels, adjust colors, smooth data
- **Ask yourself:** Would a staffer understand this chart in 5 seconds?

### Key Skills to Practice:
- `matplotlib` and `seaborn` basics
- Clear axis labels and titles
- Log scales when appropriate
- Smoothing noisy data (rolling averages)
- Honest, non-misleading charts

### Workflow:
1. Sketch what you want the chart to look like (on paper or in your head)
2. Write rough code to get the data
3. Make a basic chart
4. Refine: labels, colors, style
5. Export as PNG for memos

**Remember:** The goal is to build your own visualization intuition, not just copy code.

---

## 🎯 Phase 2 Personal Project (Required)

**Once you've completed all exercises and reading, do ONE original project that demonstrates your visualization skills.**

### Link to Your Completed Project:
`[Project title here - add when done]` → `[Link or file path]`

### Project Ideas (pick one or create your own):
1. **Bitcoin Fee Market Dashboard** - Create a multi-chart dashboard showing fee trends, mempool size, and miner revenue over the past year
2. **Halving Impact Visualization** - Chart how miner revenue composition changed across the 2020 and 2024 halvings (subsidy vs fees)
3. **Lightning Capacity Growth** - Visualize Lightning Network total capacity growth vs Bitcoin price over time

**Better yet:** After completing the exercises, come up with your own project idea based on what you found interesting or what would be useful for policy work.

### Why This Matters:
Staffers and researchers need to see you can take a question and turn it into a clear chart without hand-holding. This project proves that.

---

## 📁 Note on Repository Structure

**For now:** Your personal project can live in this phase folder (create a `/projects` subfolder if needed).

**Later (optional):** If you want a polished portfolio piece, you can move it to a separate repository (e.g., `bitcoin-fee-market-dashboard`) with clean README, organized notebooks, and exported charts. Link it back in the main roadmap README.

**Reminder to Cursor AI:** This phase can eventually become its own repository if the user chooses to split their work for portfolio purposes. Support either approach based on what the user asks for.

