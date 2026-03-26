# SQL Sales Analysis

## Overview
This is a self-initiated portfolio project created to practice SQL, data cleaning, and business analysis using a real-world retail transactions dataset.

## Objective
The goal of this project is to analyze retail sales data and answer business questions related to revenue, customer value, product performance, cancellations, and sales trends over time.

## Dataset
This project uses the UCI Online Retail dataset, a real-world transaction dataset from a UK-based non-store online retailer. https://archive.ics.uci.edu/dataset/352/online%2Bretail? 

## Tools Used
- Python
- SQLite
- SQL
- GitHub

## Project Workflow
- Inspected and cleaned the retail CSV file using Python
- Loaded the cleaned dataset into SQLite
- Wrote SQL queries to analyze sales performance, cancellations, customers, products, countries, and monthly trends
- Summarized key business insights from the query outputs

## Business Questions
- How many rows are in the dataset?
- How many cancelled orders are there?
- Which countries generate the most revenue?
- Which customers generate the most revenue?
- Which products generate the most revenue?
- How does revenue change by month?
- What is the average order value?

## Key Findings
- The dataset contains 541,909 transaction rows.
- There were 3,836 cancelled orders.
- The United Kingdom generated the highest revenue by a large margin.
- The Netherlands, EIRE, Germany, and France were also among the strongest revenue-generating countries.
- Customer 14646 generated the highest revenue.
- Top-performing products included DOTCOM POSTAGE, REGENCY CAKESTAND 3 TIER, and PAPER CRAFT , LITTLE BIRDIE.
- Revenue peaked in November 2011.
- The average order value was approximately 534.40.

## Files
- `analysis.sql` – SQL queries used for analysis
- `online_retail.db` or local SQLite workflow files – used for local SQL analysis
- `images/` – screenshots of query outputs
- `README.md` – project summary and findings

## Notes
During the project, the original CSV presented ingestion issues in BigQuery. To handle this, the data was cleaned and loaded into SQLite using Python before analysis. This reflects a realistic data workflow where raw data often needs preprocessing before querying.

## Status
Completed
