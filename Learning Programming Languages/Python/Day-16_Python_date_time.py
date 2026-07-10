import datetime
print(dir(datetime)) #['MAXYEAR', 'MINYEAR', 'UTC', '__all__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'date', 'datetime', 'datetime_CAPI', 'time', 'timedelta', 'timezone', 'tzinfo']

from datetime import datetime

now = datetime.now()
print(now) #2026-07-10 19:29:41.028987
day = now.day
month = now.month
year = now.year
hour = now.hour
minute = now.minute
second = now.second
timestamp = now.timestamp()
print(f"Day: {day}, Month: {month}, Year: {year}, Hour: {hour}, Minute: {minute}, Second: {second}") #Day: 10, Month: 7, Year: 2026, Hour: 19, Minute: 29, Second: 41
print(f"Timestamp: {timestamp}") #Timestamp: 1783690181.028987
print(f"{day}/{month}/{year}, {hour}:{minute}:{second}") #10/7/2026, 19:29:41

#Formatting Date Output Using strftime
new_year = datetime(2026, 1, 1)
print(new_year) #2026-01-01 00:00:00
#Formatting date time using strftime method
t = now.strftime("%H:%M:%S")
print("time:", t) #time: 19:36:33
time_one = now.strftime("%m/%d/%Y, %H:%M:%S")
# mm/dd/yyyy, H:M:S format
print("time_one:", time_one) #time_one: 07/10/2026, 19:49:28
time_two = now.strftime("%d/%m/%Y, %H:%M:%S")
# dd/mm/yyyy, H:M:S format
print("time_two:", time_two) #time_two: 10/07/2026, 19:49:28

#String to Time Using strptime
date_string = "10 July, 2026"
print("date_string:", date_string) #date_string: 10 July, 2026
date_object = datetime.strptime(date_string, "%d %B, %Y")
print("date_object:", date_object) #date_object: 2026-07-10 00:00:00

#Using date from datetime
from datetime import date
d = date(2022, 6, 23)
print(d) #2022-06-23
print("Current date:", d.today()) #Current date: 2026-07-10
# date object of today's date
today = date.today()
print("Current year:", today.year) #Current year: 2026
print("Current month:", today.month) #Current month: 7
print("Current day:", today.day) #Current day: 10

#Time Objects to Represent Time
from datetime import time
# time(hour = 0, minute = 0, second = 0)
a = time()
print("a =", a) #a = 00:00:00
# time(hour, minute and second)
b = time(10, 30, 50)
print("b =", b) #b = 10:30:50
# time(hour, minute and second)
c = time(hour=10, minute=30, second=50)
print("c =", c) #c = 10:30:50
# time(hour, minute, second, microsecond)
d = time(10, 30, 50, 200555)
print("d =", d) #d = 10:30:50.200555

#Difference Between Two Points in Time Using
today = now.date()
new_year = date(year=2027, month=1, day=1)
time_left_for_newyear = new_year - today
print("Time left for new year:", time_left_for_newyear) #Time left for new year: 175 days, 0:00:00
t1 = datetime.now()
t2 = datetime(year = 2027, month = 1, day = 1, hour = 0, minute = 0, second = 0)
diff = t2 - t1
print("Time left for new year:", diff) #Time left for new year: 174 days, 2:36:12.356981

#Difference Between Two Points in Time Using timedelta
from datetime import timedelta
t1 = timedelta(weeks = 12, days = 10, hours = 4, seconds = 20)
print(t1) #94 days, 4:00:20
t2 = timedelta(days = 7, hours = 5, minutes = 3, seconds = 30)
t3 = t1 - t2
print("t3 =", t3) #t3 = 86 days, 22:56:50


#Exercise: Day 16

#1. Get the current day, month, year, hour, minute and timestamp from datetime module
now = datetime.now()
print("Current date, time and timestamp:", now.strftime("%d-%m-%Y %H:%M:%S"), now.timestamp()) #Current date and time: 10-07-2026 21:54:28 1783698868.378047

#2. Format the current date using this format: "%m/%d/%Y, %H:%M:%S")
print("Formatted current date and time:", now.strftime("%m/%d/%Y, %H:%M:%S")) #Formatted current date and time: 07/10/2026, 21:54:28

#3. Today is 5 December, 2019. Change this time string to time.
date_string = "5 December, 2019"
date_object = datetime.strptime(date_string, "%d %B, %Y")
print("Date object:", date_object) #Date object: 2019-12-05 00:00:00

#4. Calculate the time difference between now and new year.
new_year = datetime(2027, 1, 1, 0, 0, 0)
time_difference = new_year - now
print("Time left for new year:", time_difference) #Time left for new year: 174 days, 2:00:51.322042

#5. Calculate the time difference between 1 January 1970 and now.
epoch = datetime(1970, 1, 1, 0, 0, 0)
time_difference = now - epoch
print("Time difference since epoch:", time_difference) #Time difference since epoch: 20644 days, 22:01:04.090876

#6. Think, what can you use the datetime module for? Examples:
# -Time series analysis
# -To get a timestamp of any activities in an application
# -Adding posts on a blog


#The end