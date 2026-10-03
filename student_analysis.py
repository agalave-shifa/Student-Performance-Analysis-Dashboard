import pandas as pd

df = pd.read_excel("Student_Performance_Dataset.xlsx")

print(df.head())

print(df.info())

print(df.isnull().sum())

print("Duplicate rows:", df.duplicated().sum())
#remove duplicate rows
df=df.drop_duplicates()
#check data types
print("\ndtypes:")
print(df.dtypes)
#check final dataset shape

print("\nFinal dataset shape:")
print(df.shape)

#data Analysis

print("\nsubject-wise Average marks:")
print("Math:",df["Math"].mean())
print("Science:",
      df["Science"].mean())
print("English:",
      df["English"].mean())
#overall performance

print("\nAverage Percentage:", df["Percentage"].mean())

print("\nTop 5 Students:")
print(df[["Name", "Percentage", "Performance"]]
      .sort_values(by="Percentage", ascending=False)
      .head(5))
# Attendance Analysis

print("\nAverage Attendance:", df["Attendance"].mean())

print("\nStudents with Attendance below 75%:")
print(df[df["Attendance"] < 75][["Name", "Attendance", "Percentage"]])

# Attendance vs Performance

print("\nAttendance vs Percentage:")
print(df[["Name", "Attendance", "Percentage"]].sort_values(
    by="Attendance", ascending=False
).head(10))

# Study Hours vs Performance

print("\nStudy Hours vs Percentage:")
print(df[["Name", "Study_Hours", "Percentage"]].sort_values(
    by="Study_Hours", ascending=False
).head(10))

# Performance Category Analysis

print("\nPerformance Category Count:")
print(df["Performance"].value_counts())



# Students Needing Improvement

print("\nStudents Needing Improvement:")
print(df[df["Percentage"] < 60]
      [["Name", "Attendance", "Study_Hours", "Percentage", "Performance"]])

# Final Project Statistics

print("\n--- Final Project Statistics ---")

print("Total Students:", len(df))

print("Average Math Marks:", round(df["Math"].mean(), 2))
print("Average Science Marks:", round(df["Science"].mean(), 2))
print("Average English Marks:", round(df["English"].mean(), 2))

print("Average Attendance:", round(df["Attendance"].mean(), 2))

print("Average Study Hours:", round(df["Study_Hours"].mean(), 2))

print("Average Percentage:", round(df["Percentage"].mean(), 2))