-- 1. Total row count
SELECT COUNT(*) AS total_rows
FROM online_retail;

-- 2. Number of cancelled orders
SELECT COUNT(DISTINCT InvoiceNo) AS cancelled_orders
FROM online_retail
WHERE InvoiceNo LIKE 'C%';

-- 3. Top 10 countries by revenue
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

-- 4. Top 10 customers by revenue
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

-- 5. Top 10 products by revenue
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

-- 6. Monthly revenue trend
SELECT
    SUBSTR(InvoiceDate, 7, 4) || '-' || SUBSTR(InvoiceDate, 4, 2) AS month,
    ROUND(SUM(Quantity * UnitPrice), 2) AS revenue
FROM online_retail
WHERE Quantity > 0
  AND UnitPrice > 0
  AND InvoiceNo NOT LIKE 'C%'
GROUP BY month
ORDER BY month;

-- 7. Average order value
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
