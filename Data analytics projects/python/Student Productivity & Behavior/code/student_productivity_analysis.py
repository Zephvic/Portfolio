# ==========================================
# STUDENT PRODUCTIVITY ANALYSIS
# ==========================================

import pandas as pd
import matplotlib.pyplot as plt

# Load Dataset
df = pd.read_csv("dataset.csv")

# ------------------------------------------
# DATA OVERVIEW
# ------------------------------------------
print(df.head())
print(df.info())
print(df.describe())

# Missing Values
print("\nMissing Values:")
print(df.isnull().sum())

# ------------------------------------------
# PRODUCTIVITY DISTRIBUTION
# ------------------------------------------
plt.figure()
df['productivity_score'].hist(bins=30)
plt.title("Distribution of Productivity Score")
plt.xlabel("Productivity Score")
plt.ylabel("Students")
plt.savefig("productivity_distribution.png")
plt.show()

# ------------------------------------------
# STUDY HOURS VS FINAL GRADE
# ------------------------------------------
plt.figure()
plt.scatter(df['study_hours_per_day'], df['final_grade'])
plt.title("Study Hours vs Final Grade")
plt.xlabel("Study Hours")
plt.ylabel("Final Grade")
plt.savefig("study_vs_grade.png")
plt.show()

# ------------------------------------------
# SLEEP HOURS VS PRODUCTIVITY
# ------------------------------------------
plt.figure()
plt.scatter(df['sleep_hours'], df['productivity_score'])
plt.title("Sleep Hours vs Productivity")
plt.xlabel("Sleep Hours")
plt.ylabel("Productivity Score")
plt.savefig("sleep_vs_productivity.png")
plt.show()

# ------------------------------------------
# PHONE USAGE IMPACT
# ------------------------------------------
plt.figure()
plt.scatter(df['phone_usage_hours'], df['productivity_score'])
plt.title("Phone Usage vs Productivity")
plt.xlabel("Phone Usage Hours")
plt.ylabel("Productivity Score")
plt.savefig("phone_vs_productivity.png")
plt.show()

# ------------------------------------------
# ATTENDANCE VS FINAL GRADE
# ------------------------------------------
plt.figure()
plt.scatter(df['attendance_percentage'], df['final_grade'])
plt.title("Attendance vs Final Grade")
plt.xlabel("Attendance %")
plt.ylabel("Final Grade")
plt.savefig("attendance_vs_grade.png")
plt.show()

# ------------------------------------------
# CORRELATION ANALYSIS
# ------------------------------------------
correlation = df.corr(numeric_only=True)

plt.figure(figsize=(10,8))
plt.imshow(correlation)
plt.colorbar()
plt.title("Correlation Matrix")
plt.savefig("correlation_matrix.png")
plt.show()

print("\n✅ Analysis Completed")