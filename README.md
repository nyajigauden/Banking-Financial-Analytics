# Banking Financial Analytics

## Project Overview

Banking Financial Analytics is a data analytics project that explores banking transaction data to identify transaction patterns, monitor transaction amounts, and highlight potentially suspicious transactions.

The project demonstrates how SQL, Python, Excel, and Power BI can be used together to clean, analyze, and visualize financial data to support data-driven decision-making.

## Objectives

- Analyze banking transaction amounts and volumes.
- Examine transaction patterns by type, channel, and location.
- Identify and analyze flagged transactions.
- Create visualizations to communicate key findings.
- Develop an interactive Power BI dashboard for financial data analysis.

## Tools and Technologies

- **SQL** — Data querying and transaction analysis.
- **Python** — Data analysis and visualization.
- **Pandas** — Data manipulation and analysis.
- **Matplotlib** — Charts and visualizations.
- **Microsoft Excel** — Data review and spreadsheet analysis.
- **Power BI** — Interactive dashboards and reporting.
- **Git and GitHub** — Version control and project sharing.

## Repository Structure

```text
Banking-Financial-Analytics/
├── documentation/
│   └── banking_analytics_report.txt
├── excel/
│   ├── Banking_Financial_Analytics.csv
│   ├── Banking_Financial_Analytics.xlsx
│   └── bank_transactions.csv
├── powerbi/
│   └── Banking_Financial_Analytics.pbix
├── python/
│   ├── analysis.py
│   ├── daily_transactions.png
│   ├── flagged_transactions_chart.png
│   └── transaction_type_chart.png
├── sql/
│   ├── banking_analysis.sql
│   └── transactions_clean.csv
└── README.md
```

## Dashboard Highlights

The Power BI dashboard presents the following indicators:

| Metric | Result |
|---|---:|
| Total transaction amount | TZS 34,050,000 |
| Total transactions | 100 |
| Average transaction amount | TZS 340,500 |
| Largest transaction | TZS 2,500,000 |
| Flagged transactions | 11 |
| Total amount of flagged transactions | TZS 14,800,000 |

The dashboard also explores transactions by location, transaction type, and channel, with slicers for filtering by transaction date, type, and location.

*These figures are based on the current project dataset and should be interpreted in the context of the data provided.*

## How to Use the Project

1. Clone or download this repository.
2. Open the Excel files to inspect the transaction data.
3. Review `sql/banking_analysis.sql` to understand the SQL analysis.
4. Run `python/analysis.py` in a Python environment with the required packages installed.
5. Open `powerbi/Banking_Financial_Analytics.pbix` using Microsoft Power BI Desktop to explore the dashboard.

### Python Requirements

Install the main Python libraries with:

```bash
pip install pandas matplotlib
```

## Key Learning Outcomes

- Data cleaning and preparation.
- SQL-based data analysis.
- Financial transaction summarization.
- Python-based data visualization.
- Interactive dashboard development.
- Communicating analytical findings through reports and visualizations.

## Data Disclaimer

This repository is intended for educational and portfolio purposes. Ensure that all published datasets are synthetic or properly anonymized and contain no confidential banking or personal information.

## Author

**Gaudencia Nyaji**

- GitHub: [nyajigauden](https://github.com/nyajigauden)

