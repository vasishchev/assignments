# Authors: Dima and Sarah
import csv
from pprint import pprint
import json

# Read vegtables.csv into a variable called vegtables.

with open('vegetables.csv', 'r') as f:
    reader = csv.DictReader(f)
    vegetables = [dict(row) for row in reader] # Try with and without -- Convert Ordered Dict to regular dict (python 3.6 or higher)



# Group vegtables by color as a variable vegtables_by_color.

vegetables_by_color = {}
for vegetable in vegetables:
    color = vegetable['color']
    if color in vegetables_by_color:
        vegetables_by_color[color].append(vegetable)
    else:
        vegetables_by_color[color] = [vegetable]

pprint(vegetables_by_color)


# Output vegtables_by_color into a json called vegtables_by_color.json.

with open('vegetables_by_color.json', 'w') as f:
    json.dump(vegetables_by_color, f, indent=2)