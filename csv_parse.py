import sys
import csv
import json

if __name__ == '__main__':
    csvfile = sys.argv[1]
    reader = csv.DictReader(open(csvfile, 'rb'))
    rows = [row for row in reader]
    print json.dumps(rows, indent=2)
