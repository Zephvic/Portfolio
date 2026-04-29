# 🎓 Student Performance Analysis

A Python-based data analysis project that evaluates student exam scores, classifies pass/fail outcomes, assigns letter grades, and visualizes performance distributions.

---

## 📌 Objectives

- Load and clean a student exam dataset
- Classify students as Pass or Fail (pass mark: 50)
- Assign letter grades (A–F)
- Identify top and bottom performers
- Visualize score distribution, pass/fail ratio, and gender comparison

---

## 🛠️ Tools & Libraries

- **Python** — core language
- **Pandas** — data loading, cleaning, transformation
- **Matplotlib** — chart generation

---

## 📂 Project Structure

```
student-performance-analysis/
├── analysis.py          # Main analysis script
├── students.csv         # Dataset
├── score_distribution.png
├── pass_fail.png
└── avg_score_by_gender.png
```

---

## 📊 Visual Outputs

### Score Distribution
![Score Distribution](score_distribution.png)

### Pass vs Fail
![Pass vs Fail](pass_fail.png)

### Average Score by Gender
![Avg Score by Gender](avg_score_by_gender.png)

---

## 🔍 Key Findings

- Overall pass rate and average score computed from the dataset
- Top 5 and bottom 5 students identified by score
- Grade distribution (A through F) summarized
- Male vs female average scores compared

---

## ▶️ How to Run

```bash
pip install pandas matplotlib
python analysis.py
```

---

## 🧠 What This Demonstrates

- CSV data loading and cleaning with Pandas
- Creating derived columns (pass/fail, grade)
- Generating summary statistics programmatically
- Building and saving charts with Matplotlib
- Structuring a complete, documented analysis project
