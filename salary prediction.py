import numpy as np
import pandas as pd

# Load dataset
df = pd.read_excel('/content/salary slr.xlsx')

# Basic EDA
print("Dataset shape:", df.shape)
df.info()
print("\nMissing values:\n", df.isnull().sum())

# Features and target
x_original = df[['YearsExperience']]  # Keep as DataFrame
y = df['Salary']

# ----------------------------
# Statsmodels (requires manual constant)
# ----------------------------
import statsmodels.api as sm

x_sm = sm.add_constant(x_original)  # Add constant only for statsmodels
model_sm = sm.OLS(y, x_sm).fit()
print("\nSTATSMODELS SUMMARY:")
print(model_sm.summary())

# ----------------------------
# Scikit-learn (no manual constant needed)
# ----------------------------
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score, mean_squared_error

# Use original x (without constant) for sklearn
x_train, x_test, y_train, y_test = train_test_split(
    x_original, y, test_size=0.2, random_state=42
)

lr = LinearRegression()
lr.fit(x_train, y_train)
y_pred = lr.predict(x_test)

mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f"\nSCIKIT-LEARN RESULTS:\nR²: {r2:.4f} | MSE: {mse:.2f}")