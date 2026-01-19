import pandas as pd

# Sample student data
data = {
    "Student": ["Alice", "Bob", "Charlie", "David", "Eva"],
    "Score": [78, 45, 62, 30, 90]
}

# Create DataFrame
df = pd.DataFrame(data)

# Classify pass/fail
df["Status"] = df["Score"].apply(lambda x: "Pass" if x >= 50 else "Fail")

# Sort by score
df_sorted = df.sort_values(by="Score", ascending=False)

# Summary statistics
summary = df["Score"].describe()

print("Student Performance Data:\n")
print(df_sorted)

print("\nSummary Statistics:\n")
print(summary)
