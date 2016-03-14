import csv

# CSV format settings
csvlt = '\n'
csvdel = ','
csvquo = '"'

# open the input and output files
with open('in/tables/source.csv', mode='rt', encoding='utf-8') as inFile, open('out/tables/destination.csv', mode='wt', encoding='utf-8') as outFile:
    # write output file header
    writer = csv.DictWriter(outFile, fieldnames = ['number', 'someText', 'double_number'], lineterminator=csvlt, delimiter = csvdel, quotechar = csvquo)
    writer.writeheader()

	# read input file line-by-line
    lazyLines = (line.replace('\0', '') for line in inFile)
    csvReader = csv.DictReader(lazyLines, lineterminator=csvlt, delimiter = csvdel, quotechar = csvquo)
    for row in csvReader:
        # do something and write row
        writer.writerow({'number': row['number'], 'someText': row['someText'], 'double_number': int(row['number']) * 2})
