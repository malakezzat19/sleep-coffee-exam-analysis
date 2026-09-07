# Sleep, Coffee & Exam Scores — A Correlation vs Causation Story

A small, story-driven data analysis project that looks at a question every student has asked: **does coffee actually improve grades?**

## Why this project?

This project isn't just about running numbers — it's built around a core data science lesson: **correlation is not causation**. It's easy to look at a dataset, spot a strong correlation, and jump to the wrong conclusion. This project deliberately walks through that trap and shows how to avoid it.

## The data

A simulated survey of 500 students, tracking:
- Hours of sleep
- Cups of coffee
- Hours spent studying
- Exam score

## What the analysis found

- **Coffee cups vs exam score correlation: 0.76** — looks strong at first glance!
- **Study hours vs exam score correlation: 0.92** — even stronger.
- The catch: students who study more *also* drink more coffee (to stay awake) and sleep less. **Study hours is the real hidden driver** behind both coffee consumption and exam performance. Coffee isn't causing the better grades — it's just moving alongside the real cause.

## Files in this repo

- `exam_habits_analysis.py` — the analysis script
- `student_survey_data.csv` — the full raw dataset (500 rows)
- `summary_report.csv` — a one-row summary of the key findings
- `correlation_plots.png` — scatter plots comparing Study Hours vs Exam Score and Coffee Cups vs Exam Score

## What it does

1. Loads and inspects the survey data
2. Builds a correlation matrix between all variables and exam score
3. Walks through the "naive conclusion" someone might jump to, and explains why it's wrong
4. Groups students by study-time level (Low / Medium / High) to show the pattern more clearly
5. Plots both relationships side by side so you can *see* the difference, not just read the numbers
6. Saves a one-row summary report to `summary_report.csv`

## Tech used

- Python
- Pandas
- NumPy
- Matplotlib

## How to run it

```bash
pip install pandas numpy matplotlib
python exam_habits_analysis.py
```

## Note

The dataset is **simulated** to intentionally demonstrate a correlation-vs-causation scenario, for educational and portfolio purposes.
