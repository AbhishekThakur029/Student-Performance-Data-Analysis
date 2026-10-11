
# MINI PROJECT: STUDENT PERFORMANCE DATA ANALYSIS
# Libraries used: Pandas, NumPy, Matplotlib

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# --------------------------------------------------
# 1. CREATE STUDENT DATASET
# --------------------------------------------------

np.random.seed(42)

n = 120

data = {
    "Student_ID": range(101, 101 + n),
    "Gender": np.random.choice(["Male", "Female"], n),
    "Attendance_Percent": np.random.randint(50, 101, n),
    "Study_Hours_Per_Day": np.round(
        np.random.uniform(1, 8, n), 1
    ),
    "Maths_Marks": np.random.randint(30, 101, n),
    "Science_Marks": np.random.randint(30, 101, n),
    "English_Marks": np.random.randint(30, 101, n)
}

df = pd.DataFrame(data)

# Calculate average marks
subjects = ["Maths_Marks", "Science_Marks", "English_Marks"]
df["Average_Marks"] = df[subjects].mean(axis=1)

# Add performance categories
def get_performance(marks):
    if marks >= 80:
        return "Excellent"
    elif marks >= 65:
        return "Good"
    elif marks >= 50:
        return "Average"
    else:
        return "Needs Improvement"

df["Performance"] = df["Average_Marks"].apply(get_performance)

# Add a few missing values and one duplicate for cleaning practice
df.loc[2, "Attendance_Percent"] = np.nan
df.loc[5, "Maths_Marks"] = np.nan
df.loc[8, "Science_Marks"] = np.nan
df = pd.concat([df, df.iloc[[0]]], ignore_index=True)

print("=" * 55)
print("STUDENT PERFORMANCE DATA ANALYSIS")
print("=" * 55)

# --------------------------------------------------
# 2. DATASET DESCRIPTION
# --------------------------------------------------

print("\n1. FIRST FIVE RECORDS")
print(df.head())

print("\n2. DATASET SHAPE (ROWS, COLUMNS)")
print(df.shape)

print("\n3. COLUMN DATA TYPES")
print(df.dtypes)

print("\n4. DATASET INFORMATION")
df.info()

# --------------------------------------------------
# 3. DATA CLEANING
# --------------------------------------------------

print("\n5. MISSING VALUES BEFORE CLEANING")
print(df.isnull().sum())

print("\n6. DUPLICATE ROWS BEFORE CLEANING")
print(df.duplicated().sum())

# Remove duplicate rows
df = df.drop_duplicates().copy()

# Fill missing numeric values with column medians
numeric_cols = [
    "Attendance_Percent",
    "Study_Hours_Per_Day",
    "Maths_Marks",
    "Science_Marks",
    "English_Marks"
]

for col in numeric_cols:
    df[col] = df[col].fillna(df[col].median())

# Recalculate average marks after cleaning
df["Average_Marks"] = df[subjects].mean(axis=1)

# Recalculate performance category
df["Performance"] = df["Average_Marks"].apply(get_performance)

print("\n7. MISSING VALUES AFTER CLEANING")
print(df.isnull().sum())

print("\n8. DUPLICATE ROWS AFTER CLEANING")
print(df.duplicated().sum())

print("\n9. CLEANED DATASET")
print(df.head())

# Save cleaned dataset (if file saving is supported)
df.to_csv("cleaned_student_performance.csv", index=False)
print("\nCleaned dataset saved as cleaned_student_performance.csv")

# --------------------------------------------------
# 4. DATA ANALYSIS USING PANDAS AND NUMPY
# --------------------------------------------------

print("\n" + "=" * 55)
print("DATA ANALYSIS")
print("=" * 55)

print("\n10. MEAN MARKS IN EACH SUBJECT")
print(df[subjects].mean().round(2))

print("\n11. MEDIAN MARKS IN EACH SUBJECT")
print(df[subjects].median().round(2))

print("\n12. STANDARD DEVIATION OF SUBJECT MARKS")
print(df[subjects].std().round(2))

print("\n13. OVERALL AVERAGE MARKS")
print(round(df["Average_Marks"].mean(), 2))

print("\n14. GENDER-WISE AVERAGE MARKS")
print(df.groupby("Gender")["Average_Marks"].mean().round(2))

print("\n15. PERFORMANCE CATEGORY COUNTS")
print(df["Performance"].value_counts())

print("\n16. SUBJECT-WISE AVERAGE MARKS")
subject_averages = df[subjects].mean()
print(subject_averages.round(2))

print("\n17. TOP 10 STUDENTS")
print(
    df.nlargest(10, "Average_Marks")[
        ["Student_ID", "Gender", "Average_Marks", "Performance"]
    ].round(2)
)

print("\n18. STUDENTS WITH ATTENDANCE OF 75% OR MORE")
print("Number of students:", (df["Attendance_Percent"] >= 75).sum())

print("\n19. CORRELATION MATRIX")
print(
    df[
        ["Attendance_Percent", "Study_Hours_Per_Day"]
        + subjects + ["Average_Marks"]
    ].corr().round(2)
)

attendance_corr = df["Attendance_Percent"].corr(df["Average_Marks"])
study_corr = df["Study_Hours_Per_Day"].corr(df["Average_Marks"])

print("\nAttendance and average marks correlation:", round(attendance_corr, 2))
print("Study hours and average marks correlation:", round(study_corr, 2))

# --------------------------------------------------
# 5. DATA VISUALIZATION USING MATPLOTLIB
# --------------------------------------------------

# Graph 1: Average marks by subject
plt.figure(figsize=(8, 5))
subject_averages.plot(kind="bar")
plt.title("Average Marks by Subject")
plt.xlabel("Subjects")
plt.ylabel("Average Marks")
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()

# Graph 2: Attendance versus average marks
plt.figure(figsize=(8, 5))
plt.scatter(df["Attendance_Percent"], df["Average_Marks"])
plt.title("Attendance vs Average Marks")
plt.xlabel("Attendance Percentage")
plt.ylabel("Average Marks")
plt.tight_layout()
plt.show()

# Graph 3: Distribution of average marks
plt.figure(figsize=(8, 5))
plt.hist(df["Average_Marks"], bins=10, edgecolor="black")
plt.title("Distribution of Student Average Marks")
plt.xlabel("Average Marks")
plt.ylabel("Number of Students")
plt.tight_layout()
plt.show()

# --------------------------------------------------
# 6. FINDINGS
# --------------------------------------------------

print("\n" + "=" * 55)
print("IMPORTANT FINDINGS")
print("=" * 55)

best_subject = subject_averages.idxmax().replace("_Marks", "")
weakest_subject = subject_averages.idxmin().replace("_Marks", "")

print("1. Total students analyzed:", len(df))
print("2. Best-performing subject:", best_subject)
print("3. Lowest average marks subject:", weakest_subject)
print("4. Overall average marks:", round(df["Average_Marks"].mean(), 2))
print("5. Average attendance:", round(df["Attendance_Percent"].mean(), 2), "%")
print("6. Average study hours per day:", round(df["Study_Hours_Per_Day"].mean(), 2))
print("7. Attendance-mark correlation:", round(attendance_corr, 2))
print("8. Study-hour-mark correlation:", round(study_corr, 2))

print("\nCONCLUSION")
print(
    "This project analyzed student marks, attendance and study hours. "
    "Data cleaning removed duplicate records and handled missing values. "
    "Statistical analysis and graphs helped summarize student performance. "
    "The dataset is simulated for educational purposes and does not represent "
    "real students."
)

print("\nPROJECT EXECUTION COMPLETED SUCCESSFULLY!")
