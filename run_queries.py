import sqlite3

db_file = "online_retail.db"
conn = sqlite3.connect(db_file)
cur = conn.cursor()

queries = {
    "1_row_count": """
        SELECT COUNT(*) AS total_rows
        FROM online_retail;
    """,

    "2_cancelled_orders": """
        SELECT COUNT(DISTINCT InvoiceNo) AS cancelled_orders
        FROM online_retail
        WHERE InvoiceNo LIKE 'C%';
    """,

    "3_top_10_countries_by_revenue": """
        SELECT
            Country,
            ROUND(SUM(Quantity * UnitPrice), 2) AS revenue
        FROM online_retail
        WHERE Quantity > 0
          AND UnitPrice > 0
          AND InvoiceNo NOT LIKE 'C%'
        GROUP BY Country
        ORDER BY revenue DESC
        LIMIT 10;
    """,

    "4_top_10_customers_by_revenue": """
        SELECT
            CustomerID,
            ROUND(SUM(Quantity * UnitPrice), 2) AS revenue
        FROM online_retail
        WHERE Quantity > 0
          AND UnitPrice > 0
          AND InvoiceNo NOT LIKE 'C%'
          AND CustomerID IS NOT NULL
          AND CustomerID != ''
        GROUP BY CustomerID
        ORDER BY revenue DESC
        LIMIT 10;
    """,

    "5_top_10_products_by_revenue": """
        SELECT
            StockCode,
            Description,
            ROUND(SUM(Quantity * UnitPrice), 2) AS revenue
        FROM online_retail
        WHERE Quantity > 0
          AND UnitPrice > 0
          AND InvoiceNo NOT LIKE 'C%'
        GROUP BY StockCode, Description
        ORDER BY revenue DESC
        LIMIT 10;
    """,

    "6_monthly_revenue": """
        SELECT
            SUBSTR(InvoiceDate, 7, 4) || '-' || SUBSTR(InvoiceDate, 4, 2) AS month,
            ROUND(SUM(Quantity * UnitPrice), 2) AS revenue
        FROM online_retail
        WHERE Quantity > 0
          AND UnitPrice > 0
          AND InvoiceNo NOT LIKE 'C%'
        GROUP BY month
        ORDER BY month;
    """,

    "7_average_order_value": """
        SELECT
            ROUND(AVG(order_value), 2) AS avg_order_value
        FROM (
            SELECT
                InvoiceNo,
                SUM(Quantity * UnitPrice) AS order_value
            FROM online_retail
            WHERE Quantity > 0
              AND UnitPrice > 0
              AND InvoiceNo NOT LIKE 'C%'
            GROUP BY InvoiceNo
        );
    """
}

for name, query in queries.items():
    print(f"\n--- {name} ---")
    rows = cur.execute(query).fetchall()
    for row in rows:
        print(row)

conn.close()