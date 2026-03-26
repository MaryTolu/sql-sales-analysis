import csv
import sqlite3

csv_file = "online_retail_cleaned.csv"
db_file = "online_retail.db"

conn = sqlite3.connect(db_file)
cur = conn.cursor()

cur.execute("DROP TABLE IF EXISTS online_retail")

cur.execute("""
CREATE TABLE online_retail (
    InvoiceNo TEXT,
    StockCode TEXT,
    Description TEXT,
    Quantity INTEGER,
    InvoiceDate TEXT,
    UnitPrice REAL,
    CustomerID TEXT,
    Country TEXT
)
""")

with open(csv_file, "r", encoding="utf-8-sig", errors="replace", newline="") as f:
    reader = csv.DictReader(f)
    reader.fieldnames = [h.strip() if h else h for h in reader.fieldnames]

    rows = []
    for row in reader:
        clean_row = {k.strip() if k else k: v for k, v in row.items()}

        rows.append((
            clean_row.get("InvoiceNo"),
            clean_row.get("StockCode"),
            clean_row.get("Description"),
            int(float(clean_row["Quantity"])) if clean_row.get("Quantity") else None,
            clean_row.get("InvoiceDate"),
            float(clean_row["UnitPrice"]) if clean_row.get("UnitPrice") else None,
            clean_row.get("CustomerID"),
            clean_row.get("Country")
        ))

cur.executemany("""
INSERT INTO online_retail (
    InvoiceNo, StockCode, Description, Quantity, InvoiceDate,
    UnitPrice, CustomerID, Country
) VALUES (?, ?, ?, ?, ?, ?, ?, ?)
""", rows)

conn.commit()

count = cur.execute("SELECT COUNT(*) FROM online_retail").fetchone()[0]
print(f"Done. Rows loaded into SQLite: {count}")
print(f"Database file created: {db_file}")

conn.close()