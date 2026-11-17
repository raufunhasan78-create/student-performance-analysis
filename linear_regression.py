import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# 1. Load the dataset
df = pd.read_csv(r'C:\Users\ACER\Downloads\archive\StudentPerformanceFactors.csv')

# 2. Separate input features (X) and target output (y)
X = df[['Hours_Studied']] # Correct column name Hours_Studied
y = df['Exam_Score']

# 3. Split the data into training (80%) and testing (20%) sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 4. Initialize and train the machine learning model
model = LinearRegression()
model.fit(X_train, y_train)

# 5. Predict the exam score for a student who studies for 7 hours
predicted_score = model.predict([[7]])
print(f"Predicted exam score for 7 hours of study: {predicted_score[0]:.2f}")
