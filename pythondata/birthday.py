from datetime import datetime

birthday = "1-May-12"
date_format = "%d-%B-%y"

# read date
parsed_date = datetime.strptime(birthday, date_format)
date_str = parsed_date.strftime("%-m/%-d/%Y") # 01/11/17
print(date_str)