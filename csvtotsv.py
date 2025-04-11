import csv

# Open the input CSV file for reading and output TSV file for writing
with open('Data.csv', 'r', newline='') as csvin, open('Data.tsv', 'w', newline='') as tsvout:
    # Create CSV reader and TSV writer objects
    csv_reader = csv.reader(csvin)
    tsv_writer = csv.writer(tsvout, delimiter='\t')

    # Write each row from CSV to TSV using tab delimiter
    for row in csv_reader:
        tsv_writer.writerow(row)
