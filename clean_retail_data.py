import csv

input_file = "Online_Retail.csv"
output_file = "online_retail_cleaned.csv"
bad_rows_file = "bad_rows.csv"

expected_columns = 8
good_rows = 0
bad_rows = 0

with open(input_file, "r", encoding="utf-8", errors="replace", newline="") as infile, \
     open(output_file, "w", encoding="utf-8", newline="") as outfile, \
     open(bad_rows_file, "w", encoding="utf-8", newline="") as badfile:

    reader = csv.reader(infile)
    writer = csv.writer(outfile)
    bad_writer = csv.writer(badfile)

    header = next(reader)
    writer.writerow(header)
    bad_writer.writerow(["row_number", "row_data"])

    for row_number, row in enumerate(reader, start=2):
        if len(row) == expected_columns:
            writer.writerow(row)
            good_rows += 1
        else:
            bad_writer.writerow([row_number, row])
            bad_rows += 1

print(f"Cleaning complete.")
print(f"Good rows written: {good_rows}")
print(f"Bad rows skipped: {bad_rows}")
print(f"Clean file saved as: {output_file}")
print(f"Bad rows saved as: {bad_rows_file}")