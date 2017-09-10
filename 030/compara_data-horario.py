import datetime


time_1 = datetime.time(13, 44, 55)
time_2 = datetime.time(13, 44, 55)

print (" Times:", time_1, time_2)

date_1 = datetime.date.today()
date_2 = date_1 + datetime.timedelta(days=1)

print (" Dates:", date_1, date_2)

datetime_1 = datetime.datetime.combine(date_1, time_1)
datetime_2 = datetime.datetime.combine(date_2, time_2)

print (" Datetime Difference:", datetime_2 - datetime_1)