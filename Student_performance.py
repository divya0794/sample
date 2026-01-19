import numpy as np
import pandas as pd

# Load the dataset
df = pd.read_excel('/content/student preformance.xlsx')

# Basic EDA
print("First few rows:")
print(df.head())
print("\nDataset shape:", df.shape)
print("\nData types and non-null counts:")
df.info()
print("\nColumn names:", df.columns.tolist())
print("\nMissing values per column:")
print(df.isnull().sum())

# Define features (X) and target (y)
X = df.drop(columns=['Performance Index'])
y = df['Performance Index']

# ----------------------------
# Statsmodels OLS (with intercept)
# ----------------------------
import statsmodels.api as sm

X_sm = sm.add_constant(X)  # ✅ Correctly adds and stores the constant term
ols_model = sm.OLS(y, X_sm)
result = ols_model.fit()
print("\n" + "="*60)
print("STATSMODELS OLS REGRESSION SUMMARY")
print("="*60)
print(result.summary())

# ----------------------------
# Scikit-learn Linear Regression
# ----------------------------
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train model
lr = LinearRegression()
lr.fit(X_train, y_train)

# Predict and evaluate
y_pred = lr.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("\n" + "="*60)
print("SCIKIT-LEARN LINEAR REGRESSION RESULTS")
print("="*60)
print(f"Mean Squared Error (MSE): {mse:.4f}")
print(f"R² Score: {r2:.4f}")