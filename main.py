import csv

csvlt = '\n'
csvdel = ','
csvquo = '"'

with open('in/tables/source.csv', mode='rt', encoding='utf-8') as inFile, open('out/tables/destination.csv', mode='wt', encoding='utf-8') as outFile:
    writer = csv.DictWriter(outFile, fieldnames = ['number', 'someText', 'doulber_number'], lineterminator=csvlt, delimiter = csvdel, quotechar = csvquo)
    writer.writeheader()

    lazyLines = (line.replace('\0', '') for line in inFile)
    csvReader = csv.DictReader(lazyLines, lineterminator=csvlt, delimiter = csvdel, quotechar = csvquo)
    for row in csvReader:
        # do something and write row
        writer.writerow({'number': row['number'], 'someText': row['someText'], 'double_number': int(row['number']) * 2})
