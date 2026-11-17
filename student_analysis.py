import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
df = pd.read_csv("StudentPerformanceFactors.csv")

# Create a figure with 3 subplots side-by-side
plt.figure(figsize=(15, 5))

# Plot 1: Impact of Study Hours on Exam Score
plt.subplot(1, 3, 1)
sns.scatterplot(x='Hours_Studied', y='Exam_Score', data=df, color='blue', alpha=0.5)
plt.title("Study Hours vs Score")

# Plot 2: Impact of Attendance on Exam Score
plt.subplot(1, 3, 2)
sns.scatterplot(x='Attendance', y='Exam_Score', data=df, color='green', alpha=0.5)
plt.title("Attendance vs Score")

# Plot 3: Comparison of Exam Scores by Gender
plt.subplot(1, 3, 3)
sns.boxplot(x='Gender', y='Exam_Score', data=df, palette='Set2')
plt.title("Gender vs Score")

# Adjust layout to prevent overlapping
plt.tight_layout()
