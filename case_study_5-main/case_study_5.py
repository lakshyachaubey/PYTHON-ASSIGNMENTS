import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = {
    "Student": ["Aman", "Riya", "Nikhil", "Priya", "Rahul", "Sneha", "Karan", "Anjali"],
    "Maths": [85, 92, 78, 88, 65, 95, 72, 80],
    "Science": [90, 89, 75, 84, 60, 96, 70, 82],
    "English": [78, 85, 80, 90, 68, 88, 74, 79],
    "Computer": [95, 94, 88, 91, 70, 98, 76, 85]
}

df = pd.DataFrame(data)

df["Total"] = df[["Maths", "Science", "English", "Computer"]].sum(axis=1)
df["Average"] = df["Total"] / 4

print("Student Score Data:")
print(df)

print("\nSubject-wise Mean:")
print(df[["Maths", "Science", "English", "Computer"]].mean())

print("\nSubject-wise Median:")
print(df[["Maths", "Science", "English", "Computer"]].median())

print("\nSubject-wise Standard Deviation:")
print(df[["Maths", "Science", "English", "Computer"]].std())

highest = df[df["Total"] == df["Total"].max()]
lowest = df[df["Total"] == df["Total"].min()]

print("\nHigh Performing Student:")
print(highest)

print("\nLow Performing Student:")
print(lowest)

subject_avg = df[["Maths", "Science", "English", "Computer"]].mean()

plt.figure(figsize=(8, 5))
plt.bar(df["Student"], df["Total"])
plt.title("Total Marks of Students")
plt.xlabel("Students")
plt.ylabel("Total Marks")
plt.show()

plt.figure(figsize=(8, 5))
plt.plot(df["Student"], df["Average"], marker="o")
plt.title("Average Marks of Students")
plt.xlabel("Students")
plt.ylabel("Average Marks")
plt.show()

plt.figure(figsize=(8, 5))
plt.hist(df["Total"], bins=5)
plt.title("Distribution of Total Marks")
plt.xlabel("Total Marks")
plt.ylabel("Number of Students")
plt.show()

plt.figure(figsize=(6, 6))
plt.pie(subject_avg, labels=subject_avg.index, autopct="%1.1f%%")
plt.title("Subject-wise Average Performance")
plt.show()

print("\nInsights:")
print("1. Sneha is the highest-performing student.")
print("2. Rahul is the lowest-performing student.")
print("3. Computer has the highest subject average.")
print("4. Science and Maths performance is also strong.")
print("5. Students with low average marks need extra academic support.")