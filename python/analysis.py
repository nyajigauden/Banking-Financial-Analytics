
import pandas as pd
from pathlib import Path

# ==========================================
# 1. Locate the project folder
# ==========================================
project_folder = Path(__file__).resolve().parent.parent

# ==========================================
# 2. Load the banking transactions CSV file
# ==========================================
file_path = project_folder / "excel" / "bank_transactions.csv"

df = pd.read_csv(file_path)

# ==========================================
# 3. Clean the dataset
# ==========================================

# Rename the first column to TransactionID
df = df.rename(columns={"Unnamed: 0": "TransactionID"})

# Keep only the 9 transaction columns
df = df[
    [
        "TransactionID",
        "CustomerID",
        "AccountType",
        "TransactionType",
        "Amount",
        "TransactionDate",
        "Channel",
        "Location",
        "IsFlagged",
    ]
]
# ==========================================
# 3.1 Convert columns to correct data types
# ==========================================

# Remove commas from amounts and convert to numbers
df["Amount"] = (
    df["Amount"]
    .str.replace(",", "", regex=False)
    .astype(float)
)

# Convert transaction dates to datetime
df["TransactionDate"] = pd.to_datetime(
    df["TransactionDate"],
    errors="coerce"
)

print("\nUpdated data types:")
print(df.dtypes)

# ==========================================
# 4. Display the banking analytics report
# ==========================================
print("BANKING FINANCIAL ANALYTICS")
print("=" * 40)

print("\nFirst 5 transactions:")
print(df.head())

print("\nDataset information:")
print("Number of transactions:", len(df))
print("Number of columns:", len(df.columns))

print("\nColumn names:")
print(df.columns.tolist())

print("\nCleaned dataset shape:", df.shape)

# ==========================================
# 5. Check data types and missing values
# ==========================================
print("\nData types:")
print(df.dtypes)

print("\nMissing values in each column:")

# ==========================================
# 6. Banking transaction summary
# ==========================================

print("\nBANKING TRANSACTION SUMMARY")
print("=" * 40)

print("Total transaction amount (TZS):",
      f"{df['Amount'].sum():,.2f}")

print("Average transaction amount (TZS):",
      f"{df['Amount'].mean():,.2f}")

print("Largest transaction (TZS):",
      f"{df['Amount'].max():,.2f}")

print("Smallest transaction (TZS):",
      f"{df['Amount'].min():,.2f}")

print("Number of flagged transactions:",
      (df["IsFlagged"].str.strip().str.lower() == "yes").sum())


# ==========================================
# 7. Analysis by transaction type
# ==========================================

print("\nTRANSACTION TYPE ANALYSIS")
print("=" * 40)

transaction_summary = df.groupby("TransactionType").agg(
    Number_of_Transactions=("TransactionID", "count"),
    Total_Amount=("Amount", "sum"),
    Average_Amount=("Amount", "mean")
).reset_index()

transaction_summary["Total_Amount"] = (
    transaction_summary["Total_Amount"].map("{:,.2f}".format)
)

transaction_summary["Average_Amount"] = (
    transaction_summary["Average_Amount"].map("{:,.2f}".format)
)

print(transaction_summary.to_string(index=False))


# ==========================================
# 8. Flagged transaction analysis
# ==========================================

print("\nFLAGGED TRANSACTION ANALYSIS")
print("=" * 40)

flagged_df = df[
    df["IsFlagged"].str.strip().str.lower() == "yes"
]

print("Total flagged transactions:", len(flagged_df))

print("\nFlagged transactions by type:")
print(flagged_df["TransactionType"].value_counts())

print("\nTotal amount of flagged transactions (TZS):",
      f"{flagged_df['Amount'].sum():,.2f}")


# ==========================================
# 9. Transaction analysis by location
# ==========================================

print("\nTRANSACTION ANALYSIS BY LOCATION")
print("=" * 40)

location_summary = df.groupby("Location").agg(
    Number_of_Transactions=("TransactionID", "count"),
    Total_Amount=("Amount", "sum")
).reset_index()

location_summary = location_summary.sort_values(
    by="Total_Amount",
    ascending=False
)

location_summary["Total_Amount"] = (
    location_summary["Total_Amount"].map("{:,.2f}".format)
)

print(location_summary.to_string(index=False))


# ==========================================
# 10. Transaction analysis by channel
# ==========================================

print("\nTRANSACTION ANALYSIS BY CHANNEL")
print("=" * 40)

channel_summary = df.groupby("Channel").agg(
    Number_of_Transactions=("TransactionID", "count"),
    Total_Amount=("Amount", "sum"),
    Average_Amount=("Amount", "mean")
).reset_index()

channel_summary = channel_summary.sort_values(
    by="Total_Amount",
    ascending=False
)

channel_summary["Total_Amount"] = (
    channel_summary["Total_Amount"].map("{:,.2f}".format)
)

channel_summary["Average_Amount"] = (
    channel_summary["Average_Amount"].map("{:,.2f}".format)
)

print(channel_summary.to_string(index=False))


# ==========================================
# 11. Transaction analysis by account type
# ==========================================

print("\nTRANSACTION ANALYSIS BY ACCOUNT TYPE")
print("=" * 45)

account_summary = df.groupby("AccountType").agg(
    Number_of_Transactions=("TransactionID", "count"),
    Total_Amount=("Amount", "sum"),
    Average_Amount=("Amount", "mean")
).reset_index()

account_summary = account_summary.sort_values(
    by="Total_Amount",
    ascending=False
)

account_summary["Total_Amount"] = (
    account_summary["Total_Amount"].map("{:,.2f}".format)
)

account_summary["Average_Amount"] = (
    account_summary["Average_Amount"].map("{:,.2f}".format)
)

print(account_summary.to_string(index=False))


# ==========================================
# 12. Daily transaction analysis
# ==========================================

print("\nDAILY TRANSACTION ANALYSIS")
print("=" * 40)

daily_summary = df.groupby("TransactionDate").agg(
    Number_of_Transactions=("TransactionID", "count"),
    Total_Amount=("Amount", "sum")
).reset_index()

daily_summary = daily_summary.sort_values(
    by="TransactionDate"
)

daily_summary["Total_Amount"] = (
    daily_summary["Total_Amount"].map("{:,.2f}".format)
)

print(daily_summary.to_string(index=False))

print("\nNumber of transaction dates:",
      df["TransactionDate"].nunique())


# ==========================================
# 13. Daily transaction amount chart
# ==========================================

import matplotlib.pyplot as plt

# Calculate daily transaction amounts
daily_chart = df.groupby("TransactionDate")["Amount"].sum()

# Create the chart
plt.figure(figsize=(12, 6))
daily_chart.plot(kind="line", marker="o")

plt.title("Daily Banking Transaction Amounts")
plt.xlabel("Transaction Date")
plt.ylabel("Total Amount (TZS)")
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()

# Save the chart
chart_path = project_folder / "python" / "daily_transactions.png"
plt.savefig(chart_path, dpi=150)

print("\nDaily transaction chart saved to:")
print(chart_path)

# Display the chart
plt.show()


# ==========================================
# 14. Transaction type comparison chart
# ==========================================

# Calculate total amount for each transaction type
transaction_chart = df.groupby("TransactionType")["Amount"].sum()

# Create the bar chart
plt.figure(figsize=(10, 6))
transaction_chart.plot(kind="bar")

plt.title("Total Transaction Amount by Type")
plt.xlabel("Transaction Type")
plt.ylabel("Total Amount (TZS)")
plt.xticks(rotation=0)
plt.grid(axis="y")
plt.tight_layout()

# Save the chart
chart_path = project_folder / "python" / "transaction_type_chart.png"
plt.savefig(chart_path, dpi=150)

print("\nTransaction type chart saved to:")
print(chart_path)

# Display the chart
plt.show()


# ==========================================
# 15. Flagged transactions chart
# ==========================================

# Select flagged transactions
flagged_df = df[df["IsFlagged"].str.strip().str.lower() == "yes"]

# Count flagged transactions by type
flagged_chart = flagged_df.groupby("TransactionType").size()

# Create the chart
plt.figure(figsize=(9, 6))
flagged_chart.plot(kind="bar")

plt.title("Flagged Transactions by Type")
plt.xlabel("Transaction Type")
plt.ylabel("Number of Flagged Transactions")
plt.xticks(rotation=0)
plt.grid(axis="y")
plt.tight_layout()

# Save the chart
chart_path = project_folder / "python" / "flagged_transactions_chart.png"
plt.savefig(chart_path, dpi=150)

print("\nFlagged transactions chart saved to:")
print(chart_path)

# Display the chart
plt.show()


# ==========================================
# 16. Banking analytics report
# ==========================================

# Calculate key business metrics
total_amount = df["Amount"].sum()
average_amount = df["Amount"].mean()
largest_amount = df["Amount"].max()
smallest_amount = df["Amount"].min()
total_transactions = len(df)

flagged_df = df[
    df["IsFlagged"].str.strip().str.lower() == "yes"
]

flagged_count = len(flagged_df)
flagged_amount = flagged_df["Amount"].sum()

top_transaction_type = (
    df.groupby("TransactionType")["Amount"]
    .sum()
    .idxmax()
)

top_location = (
    df.groupby("Location")["Amount"]
    .sum()
    .idxmax()
)

# Write the report
report_path = (
    project_folder / "documentation" / "banking_analytics_report.txt"
)

with open(report_path, "w", encoding="utf-8") as report:
    report.write("BANKING & FINANCIAL TRANSACTIONS ANALYTICS REPORT\n")
    report.write("=" * 55 + "\n\n")

    report.write("DATASET OVERVIEW\n")
    report.write(f"Total transactions: {total_transactions}\n")
    report.write(f"Total transaction amount: TZS {total_amount:,.2f}\n")
    report.write(f"Average transaction amount: TZS {average_amount:,.2f}\n")
    report.write(f"Largest transaction: TZS {largest_amount:,.2f}\n")
    report.write(f"Smallest transaction: TZS {smallest_amount:,.2f}\n\n")

    report.write("KEY FINDINGS\n")
    report.write(f"Transaction type with the highest total amount: {top_transaction_type}\n")
    report.write(f"Location with the highest total amount: {top_location}\n")
    report.write(f"Number of flagged transactions: {flagged_count}\n")
    report.write(f"Amount associated with flagged transactions: TZS {flagged_amount:,.2f}\n\n")

    report.write("IMPORTANT NOTE\n")
    report.write(
        "Flagged transactions require further review. "
        "They should not automatically be treated as confirmed fraud.\n"
    )

print("\nBanking analytics report saved to:")
print(report_path)


# ==========================================
# 17. Export clean CSV for PostgreSQL
# ==========================================

clean_csv_path = project_folder / "sql" / "transactions_clean.csv"

df.to_csv(clean_csv_path, index=False)

print("\nClean CSV for PostgreSQL saved to:")
print(clean_csv_path)
print("Number of rows exported:", len(df))
print("Number of columns exported:", len(df.columns))


# ==========================================
# 17. Export clean CSV for PostgreSQL
# ==========================================

clean_csv_path = project_folder / "sql" / "transactions_clean.csv"

df.to_csv(clean_csv_path, index=False)

print("\nClean CSV for PostgreSQL saved to:")
print(clean_csv_path)
print("Number of rows exported:", len(df))
print("Number of columns exported:", len(df.columns))
