import csv

with open("online_retail_cleaned.csv", "r", encoding="utf-8-sig", errors="replace", newline="") as f:
    reader = csv.DictReader(f)
    print(reader.fieldnames)