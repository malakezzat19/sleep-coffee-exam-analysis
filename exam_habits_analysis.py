"""
Sleep, Coffee & Exam Scores — A Correlation vs Causation Story
----------------------------------------------------------------
Author: Malak

This project explores a simple question every student asks:
"Does more coffee actually mean better grades? Does more sleep?"

We look at a (simulated) survey of students: how many hours they slept,
how many cups of coffee they drank, how many hours they studied, and
what score they got on an exam.

The twist: this project isn't just about finding correlations — it's
about being careful NOT to confuse correlation with causation, a
concept every data scientist needs to respect before drawing conclusions.
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


#1: Create a simulated student survey dataset

np.random.seed(7)
n_students = 500

# Study hours is the real driver of exam score (the "hidden" true cause)
study_hours = np.round(np.random.uniform(1, 8, n_students), 1)

# Students who study more also tend to sleep less and drink more coffee
# (this creates a *fake* correlation between coffee and score later)
sleep_hours = np.round(np.clip(9 - study_hours * 0.5 + np.random.normal(0, 0.8, n_students), 3, 9), 1)
coffee_cups = np.round(np.clip(study_hours * 0.4 + np.random.normal(0, 0.5, n_students), 0, 6), 0)

# Exam score depends mainly on study hours (+ some randomness)
exam_score = np.clip(40 + study_hours * 7 + np.random.normal(0, 6, n_students), 0, 100)
exam_score = np.round(exam_score, 1)

df = pd.DataFrame({
    "Student_ID": range(1, n_students + 1),
    "Sleep_Hours": sleep_hours,
    "Coffee_Cups": coffee_cups,
    "Study_Hours": study_hours,
    "Exam_Score": exam_score
})

print("Sample of the dataset:")
print(df.head())

# Save the full raw dataset too (all 500 rows), not just the summary
df.to_csv("student_survey_data.csv", index=False)
print("\nFull raw dataset saved to student_survey_data.csv")


#2: Basic inspection
print("\nDataset shape:", df.shape)
print("\nSummary statistics:")
print(df.describe())

#3: Correlation matrix

correlations = df[["Sleep_Hours", "Coffee_Cups", "Study_Hours", "Exam_Score"]].corr()
print("\nCorrelation matrix:")
print(correlations["Exam_Score"].sort_values(ascending=False))


#4: The naive (wrong) conclusion someone might jump to

coffee_corr = correlations.loc["Coffee_Cups", "Exam_Score"]
study_corr = correlations.loc["Study_Hours", "Exam_Score"]

print(f"\nCoffee vs Score correlation: {coffee_corr:.2f}")
print(f"Study hours vs Score correlation: {study_corr:.2f}")

print("""
Naive conclusion someone might make:
"Coffee is correlated with higher exam scores, so drinking more
coffee causes better grades!"

Why that's wrong:
Students who study more hours ALSO tend to drink more coffee
(to stay awake) and sleep less. Study hours is the hidden factor
driving both coffee consumption AND exam score. Coffee itself
isn't the cause -- it's just moving alongside the real cause.
""")


#5: Grouping students into study-time buckets

df["Study_Level"] = pd.cut(
    df["Study_Hours"],
    bins=[0, 3, 6, 10],
    labels=["Low (0-3h)", "Medium (3-6h)", "High (6h+)"]
)

avg_by_level = df.groupby("Study_Level", observed=True)[["Coffee_Cups", "Exam_Score"]].mean()
print("\nAverage coffee and score by study level:")
print(avg_by_level)


#6: Visualize the story (this is the whole point!)

fig, axes = plt.subplots(1, 2, figsize=(12, 5))

# Left plot: Study Hours vs Exam Score (the REAL relationship)
axes[0].scatter(df["Study_Hours"], df["Exam_Score"], alpha=0.5, color="#2E86AB")
axes[0].set_xlabel("Study Hours")
axes[0].set_ylabel("Exam Score")
axes[0].set_title(f"Study Hours vs Exam Score (r = {study_corr:.2f})")

# Right plot: Coffee Cups vs Exam Score (the MISLEADING relationship)
axes[1].scatter(df["Coffee_Cups"], df["Exam_Score"], alpha=0.5, color="#E76F51")
axes[1].set_xlabel("Coffee Cups")
axes[1].set_ylabel("Exam Score")
axes[1].set_title(f"Coffee Cups vs Exam Score (r = {coffee_corr:.2f})")

plt.tight_layout()
plt.savefig("correlation_plots.png", dpi=150)
print("\nPlots saved to correlation_plots.png")


#7: Save a summary report

summary = pd.DataFrame({
    "Coffee_vs_Score_Correlation": [round(coffee_corr, 2)],
    "Study_vs_Score_Correlation": [round(study_corr, 2)],
    "Average_Exam_Score": [round(df["Exam_Score"].mean(), 1)],
    "Average_Study_Hours": [round(df["Study_Hours"].mean(), 1)]
})
summary.to_csv("summary_report.csv", index=False)
print("\nSummary report saved to summary_report.csv")
