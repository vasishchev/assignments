# Authors: Dima and Sarah

# Read the data from superheroes.json
import json
import csv

with open('superheroes.json', 'r') as f:
    squad = json.load(f)

# Write header to csv file
with open('superheroes.csv', 'w') as f:
	writer = csv.writer(f)
	#write header
	writer.writerow(['name', 'age', 'secretidentity', 'powers', 'squadName', 'homeTown', 'formed', 'secretBase', 'active'])



	# Loop over members & write 1 row per member
	members = squad['members']  # For this entire dictionary of squad, this accesses the key members
	for member in members:
			name = member['name']
			age = member['age']
			secretidentity = member['secretIdentity']
			powers = member['powers']

			squadName = squad['squadName']
			homeTown = squad['homeTown']
			formed = squad['formed']
			secretBase = squad['secretBase']
			active = squad['active']

			writer.writerow([name, age, secretidentity, powers, squadName, 
				homeTown, formed, secretBase, active])
