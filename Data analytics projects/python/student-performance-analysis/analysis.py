import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("students.csv")

# Basic cleaning
df["score"] = pd.to_numeric(df["score"], errors="coerce")
df = df.dropna(subset=["score"])

# Add pass/fail + grade
df["status"] = df["score"].apply(lambda x: "Pass" if x >= 50 else "Fail")

def grade(score):
    if score >= 90: return "A"
    if score >= 80: return "B"
    if score >= 70: return "C"
    if score >= 60: return "D"
    if score >= 50: return "E"
    return "F"

df["grade"] = df["score"].apply(grade)

# Summary
pass_rate = (df["status"].eq("Pass").mean()) * 100
avg_score = df["score"].mean()

print("=== Student Performance Summary ===")
print(f"Total Students: {len(df)}")
print(f"Average Score: {avg_score:.2f}")
print(f"Pass Rate: {pass_rate:.1f}%\n")

print("Top 5 Students:")
print(df.sort_values("score", ascending=False).head(5)[["student", "score", "grade"]], "\n")

print("Bottom 5 Students:")
print(df.sort_values("score", ascending=True).head(5)[["student", "score", "grade"]], "\n")

print("Pass/Fail Count:")
print(df["status"].value_counts(), "\n")

print("Grade Distribution:")
print(df["grade"].value_counts().sort_index(), "\n")

# Charts
# 1) Score distribution
plt.figure()
df["score"].plot(kind="hist")
plt.title("Score Distribution")
plt.xlabel("Score")
plt.ylabel("Number of Students")
plt.tight_layout()
plt.savefig("score_distribution.png")
plt.close()

# 2) Pass vs Fail
plt.figure()
df["status"].value_counts().plot(kind="bar")
plt.title("Pass vs Fail")
plt.xlabel("Status")
plt.ylabel("Number of Students")
plt.tight_layout()
plt.savefig("pass_fail.png")
plt.close()

# 3) Average score by gender (if available)
if "gender" in df.columns:
    plt.figure()
    df.groupby("gender")["score"].mean().plot(kind="bar")
    plt.title("Average Score by Gender")
    plt.xlabel("Gender")
    plt.ylabel("Average Score")
    plt.tight_layout()
    plt.savefig("avg_score_by_gender.png")
    plt.close()

print("Charts saved: score_distribution.png, pass_fail.png, avg_score_by_gender.png (if gender exists).")

