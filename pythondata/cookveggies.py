# read vegetables.csv

import csv
import json

# read vegetables.csv
with open('vegetables.csv', 'r') as f:
    reader = csv.DictReader(f)
    vegetables = [dict(row) for row in reader] # Convert Ordered Dict to regular dict (python 3.6 or higher)

# write vegetables.json

import json

with open('vegetables.json', 'w') as f:
    json.dump(vegetables, f, indent = 2)