# Authors: Sarah and Dima

# Read vegetables.csv into a variable called vegetables.

import csv
from pprint import pprint
import json

with open('vegetables.csv', 'r') as f:
    reader = csv.DictReader(f)
    vegetables = [dict(row) for row in reader] # Try with and without -- Convert Ordered Dict to regular dict (python 3.6 or higher)

# Loop through vegetables and filter down to only green vegtables using a whitelist.

green_vegetables = []
whitelist = ['green']
for veggie in vegetables:
    if veggie['color'] in whitelist:
        green_vegetables.append(veggie)

# Print veggies to the terminal
print(green_vegetables)

# Write the veggies to a json file called greenveggies.json


with open('greenveggies.json', 'w') as f:
    json.dump(green_vegetables, f, indent=2)


# Bonus: Output another csv called green_vegetables.csv.