# import csv

# with open('testwrite.csv', 'w') as f:
#     writer = csv.writer(f)
#     writer.writerow(['col1', 'col2'])
#     writer.writerow(['val1', 'val2'])
#     writer.writerow(['val1', 'val2'])
#     writer.writerow(['val1', 'val2'])


# DATES
# from datetime import datetime

# raw_date = "2017-01-11"
# date_format = "%Y-%m-%d"

# # read date
# parsed_date = datetime.strptime(raw_date, date_format)
# date_str = parsed_date.strftime("%m/%d/%y") # 01/11/17
# print(date_str)


# FILTERING
friends = [
    {"name": "Rachel", "age": 34},
    {"name": "Monica", "age": 34},
    {"name": "Phoebe", "age": 37}
]

# filter to age < 37
cool_people = []
whitelist = ['Rachel', 'Phoebe']
for friend in friends:
	if friend['name'] in whitelist:
        cool_people.append(friend)

print(cool_people)