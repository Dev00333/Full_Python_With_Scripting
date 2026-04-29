import datetime
import pytz
# this pytz module or python timezone module is used to work with timezones in python 
# the datetime module is used to work with dates and times in python but it is inferiour to pytz moduld when it comes to the timezones
d = datetime.date(2025,7,24)
print(d)
d = datetime.date.today()
print(d)
print(d.year)
print(d.weekday())
tdelta = datetime.timedelta(days=7)
print(d + tdelta)
# the timedelta tells us what day of the week it will be in 7 days time (here)

# we will do time delta 
# date2= date1 + timedelta
# timedelta = date2 -/+ date1

bday = datetime.date(d.year+1, 1, 10)
print(bday)
till_bday = bday - d
print(till_bday.total_seconds())

t = datetime.time(9, 30, 45, 100000)
print(t)
print(t.hour)
print(t.minute)
print(t.second)

x = datetime.datetime(2025, 7, 24, 9, 30, 45, 100000)
print(x)

y = datetime.datetime.now()
print(y)

dt = datetime.datetime.now(tz=pytz.UTC)
dt_mtn = dt.astimezone(pytz.timezone('US/Mountain'))

for tz in pytz.all_timezones:
    print(tz)

print(pytz.country_timezones['US'])
print(pytz.country_timezones['IN'])

print(pytz.timezone('Asia/Kolkata').localize(datetime.datetime.now()))

# iso format is a standard format for representing date and time in a machine readable format

print(dt_mtn.strftime('%B %d, %Y')) # this will print the date in the format of month day, year
print(dt_mtn.strftime('%I:%M %p')) # this will print the time in