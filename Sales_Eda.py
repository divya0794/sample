# Sales Data Exploratory Data Analysis (EDA)
# This script loads sales data, performs basic cleaning, computes key metrics,
# and generates visualizations to understand sales trends by product, category, and region.
# Author: Diviabhi
# Dependencies: pandas, numpy, matplotlib, seaborn

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Load the dataset
df = pd.read_csv('/content/sales_data.csv')

# Display the full dataset
df

# Check for missing values
df.isnull().sum()
df.isnull()

# Remove rows with any missing values
df.dropna(inplace=True)
df.isnull().sum()

# Summary statistics
df.describe()
df.info()
df.count()
df.columns
df.head()
df

# Group by 'Sales' and sum (note: grouping by a continuous variable like 'Sales' may not be meaningful—likely intended for other columns)
df.groupby('Sales').sum()
df.groupby('Sales').sum()

# Calculate and print average sales
print('The average sales is :')
print(df['Sales'].mean())

# Sum of Quantity and Category (note: Category is likely categorical—sum may not apply meaningfully)
df[['Category','Quantity']].sum()

# Total quantity sold
print(df['Quantity'].sum())

# Sort data by sales (descending)
df.sort_values(by='Sales', ascending=False)

# Find the top-selling product by total quantity
df.groupby('Product')['Quantity'].sum().sort_values(ascending=False).head(1)

# Visualizations
sns.boxplot(x='Category', y='Sales', data=df)
plt.show()

plt.hist(df['Sales'])
plt.show()

plt.boxplot(df['Sales'])
plt.show()

sns.barplot(x='Quantity', y='Product', data=df)
plt.show()

sns.countplot(x='Region', data=df)
plt.ylabel('Orders')
plt.show()

sns.boxplot(x='Region', y='Sales', data=df)
plt.show()

sns.violinplot(x='Region', y='Sales', data=df)
plt.show()