# import datetime
#
# current_date = datetime.datetime.now()
# print(current_date)

from datetime import datetime, timedelta

now = datetime.now()
print(now)
print(now.year)
print(now.month)
print(now.day)
#formatted date:
formatted_date = now.strftime("%Y-%m-%d %H:%M:%S")
print(formatted_date)

future_date = now - timedelta(days=12)
print(future_date)