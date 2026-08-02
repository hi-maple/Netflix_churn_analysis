# Import libraries

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Display settings

pd.set_option('display.max_columns', None)
pd.set_option('display.width', 1000)

# Load dataset

df = pd.read_csv("data/netflix_customer_churn.csv")

# -----------------------------------
# Data Cleaning
# -----------------------------------

# Create copy of raw dataset
df_clean = df.copy()

# Remove duplicate rows
df_clean.drop_duplicates(inplace=True)

# Remove spaces from column names
df_clean.columns = df_clean.columns.str.strip()

# Remove spaces from string values
string_columns = df_clean.select_dtypes(include='object').columns

for col in string_columns:
    df_clean[col] = df_clean[col].str.strip()

# Save cleaned dataset
df_clean.to_csv(
    "data/netflix_customer_churn_cleaned.csv",
    index=False
)

# Use cleaned dataset for analysis
df = df_clean

# View data

df.head()

df.tail()

df.sample(5)

df.shape

df.columns

df.dtypes

df.info()

# Shape
print("Dataset Shape:", df.shape)

# Missing Values
print("\nMissing Values:")
print(df.isnull().sum())

# Duplicate Rows
print("\nDuplicate Rows:", df.duplicated().sum())

# Unique Values
print("\nGender:")
print(df['gender'].unique())

print("\nSubscription Type:")
print(df['subscription_type'].unique())

print("\nPayment Method:")
print(df['payment_method'].unique())

print("\nDevice:")
print(df['device'].unique())

print("\nRegion:")
print(df['region'].unique())

print("\nFavorite Genre:")
print(df['favorite_genre'].unique())

# Count of unique values
print("\nUnique Values in Each Column:")
print(df.nunique())


# ------------------ ETA -------------------
# Count churn values
print("Customer Churn Count:")
print(df['churned'].value_counts())

# Churn Percentage
print("\nCustomer Churn Percentage:")
print(df['churned'].value_counts(normalize=True) * 100)

# Active vs Churned
active_customers = (df['churned'] == 0).sum()
churned_customers = (df['churned'] == 1).sum()

total_customers = len(df)

churn_rate = (churned_customers / total_customers) * 100

print("\nBusiness Summary")
print("-------------------------")
print(f"Total Customers : {total_customers}")
print(f"Active Customers : {active_customers}")
print(f"Churned Customers : {churned_customers}")
print(f"Overall Churn Rate : {churn_rate:.2f}%")

# Visualization
plt.figure(figsize=(6,4))

sns.countplot(data=df, x='churned')

plt.title("Customer Churn Distribution")
plt.xlabel("Churn Status")
plt.ylabel("Number of Customers")

plt.show()

# Churn by Gender
gender_churn = pd.crosstab(df['gender'], df['churned'])

print(gender_churn)

gender_churn_percent = pd.crosstab(
    df['gender'],
    df['churned'],
    normalize='index'
) * 100

print(gender_churn_percent)

plt.figure(figsize=(7,5))

sns.countplot(
    data=df,
    x='gender',
    hue='churned'
)

plt.title("Customer Churn by Gender")

plt.xlabel("Gender")

plt.ylabel("Number of Customers")

plt.legend(title="Churned")

plt.show()

subscription_churn = pd.crosstab(
    df['subscription_type'],
    df['churned']
)

print(subscription_churn)

subscription_churn_percent = pd.crosstab(
    df['subscription_type'],
    df['churned'],
    normalize='index'
) * 100

print(subscription_churn_percent)

plt.figure(figsize=(8,5))

sns.countplot(
    data=df,
    x='subscription_type',
    hue='churned'
)

plt.title("Customer Churn by Subscription Type")

plt.xlabel("Subscription Type")
plt.ylabel("Number of Customers")

plt.legend(title="Churned")

plt.show()

# Average Watch Hours by Churn Status
watch_hours = df.groupby('churned')['watch_hours'].mean().round(2)

print(watch_hours)

# Visualization
plt.figure(figsize=(6,5))

sns.boxplot(
    data=df,
    x='churned',
    y='watch_hours'
)

plt.title("Watch Hours vs Customer Churn")

plt.xlabel("Churn Status")
plt.ylabel("Watch Hours")

plt.show()


# Average Last Login Days
last_login = df.groupby('churned')['last_login_days'].mean().round(2)

print(last_login)


plt.figure(figsize=(6,5))

sns.boxplot(
    data=df,
    x='churned',
    y='last_login_days'
)

plt.title("Last Login Days vs Customer Churn")

plt.xlabel("Churn Status")
plt.ylabel("Last Login Days")

plt.show()

# Churn count by payment method
payment_churn = pd.crosstab(
    df['payment_method'],
    df['churned']
)

print(payment_churn)

payment_churn_percent = pd.crosstab(
    df['payment_method'],
    df['churned'],
    normalize='index'
) * 100

print(payment_churn_percent.round(2))

plt.figure(figsize=(8,5))

sns.countplot(
    data=df,
    x='payment_method',
    hue='churned'
)

plt.title("Customer Churn by Payment Method")
plt.xlabel("Payment Method")
plt.ylabel("Number of Customers")

plt.legend(title="Churned")

plt.show()

# Select numerical columns
numerical_df = df.select_dtypes(include=['int64', 'float64'])

# Correlation Matrix
correlation = numerical_df.corr()

print(correlation.round(2))

plt.figure(figsize=(10,6))

sns.heatmap(
    correlation,
    annot=True,
    cmap='coolwarm',
    fmt='.2f'
)

plt.title("Correlation Heatmap")

plt.show()