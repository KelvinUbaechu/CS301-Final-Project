import csv

with open("./leading_retailers_2021.csv", "r", encoding="latin-1") as f_in, open(
    "partially_cleaned_dataset.csv", "w", newline=""
) as f_out:
    reader = csv.reader(f_in)
    writer = csv.writer(f_out)
    for row in reader:
        row[3] = row[3].replace(",", "")  # remove commas from 4th column
        row[4] = row[4].replace(",", "")  # remove commas from 5th column
        # remove extra spaces from all columns
        row = [col.strip() for col in row]
        writer.writerow(row)
