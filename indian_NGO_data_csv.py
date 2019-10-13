
import json,csv

infile = open('indian_NGO_data.json', 'r+')
outfile = open('indian_NGO_data.csv', 'w')

writer = csv.writer(outfile)
loading = json.loads(infile.read())

writer.writerow(loading[0].keys())
for row in loading:
    writer.writerow(row.values())