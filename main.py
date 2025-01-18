# date 
from datetime import date 
d = date(2016, 7, 23)
print(d)
d = date.fromisoformat("2015-07-23")
print(d)

today = date.today()
print(today)

print(today.day)
print(today.month)
print(today.year)
print(today.weekday()) # indexé de 0 à 6
print(today.isoweekday())  # indexé de 1 à 7

one_year_from_today = today.replace(year = today.year + 1)
print(one_year_from_today)

# formatting
import locale 
locale.setlocale(locale.LC_TIME, "fr_FR")
print(f"Le {today: %d %B %Y} tombe un {today:%A} qui est le {today:%j} jour de l'année")
print(today.isoformat(), type(today.isoformat()))

# time 
from datetime import time as datetime_time
t = datetime_time(9, 30, 45)
print(t)
print(t.minute)
print(t.hour)

# datetime 
from datetime import datetime
dt = datetime(2024, 12, 22, 10, 24, 44)
print(dt)
print(dt.year)
print(dt.minute)
print(dt.date())
print(dt.time())

now = datetime.now()
print(now)


# files' date 
import os 
print(os.stat("demo.txt"))
modified_time = os.stat("demo.txt").st_mtime # temps unix, temps en sec depuis 01 janv 1970 
print(datetime.fromtimestamp(modified_time))

# date from string 
date_string = "12 juillet 1997"
date_obj = datetime.strptime(date_string, "%d %B %Y")
print(date_obj)

# date to string 
today_string = today.strftime("Le %A %d %b %Y")
print(today_string)

# time delta 
from datetime import timedelta 
tdelta = timedelta(hours=12)
print(tdelta)
tdelta = timedelta(days=7)
print(tdelta)
print(today + tdelta)

bthday = date.fromisoformat("2025-08-21")
till_birthday = abs(bthday - today)
print(f"Il reste {till_birthday} jours avant mon anniversaire")
print(f"Il reste {till_birthday.total_seconds()} secondes avant mon anniversaire")

# timezone 
from datetime import timezone 
now_utc = datetime.now(tz=timezone.utc)
print(now_utc)

france_offset = timedelta(hours=2)
now_france = now_utc.astimezone(timezone(france_offset))
print(now_france)

import zoneinfo 
available_timezones = zoneinfo.available_timezones()
print(available_timezones)

now_utc = datetime.now(tz=zoneinfo.ZoneInfo("UTC"))
print(now_utc)

now_france = now_utc.astimezone(zoneinfo.ZoneInfo("Europe/Paris"))
print(now_france)

# time 
import time 
print("avant")
time.sleep(1)
print("après")
print(time.ctime(0))
print(time.time())
print(time.ctime(time.time()))
print(time.ctime())

time_struct_utc = time.gmtime()
print(time_struct_utc)
time_struct_local = time.localtime()
print(time_struct_local)
time_tuple = (2020, 4, 20, 20, 30, 0, 0, 111, 1)
time_string = time.asctime(time_tuple)
print(time_string)
unix_time = time.mktime(time_tuple)
print(unix_time)
unix_today = time.mktime(today.timetuple())
print(unix_today)

# calendar 

import calendar 

year = 2024 

for month in range(1, 13):
    print(calendar.month_name[month])
    print(calendar.month(year, month))
    print(calendar.monthrange(year, month))
    print(calendar.monthrange(year, month)[0])
    print(calendar.monthrange(year, month)[1])

# cas concret 
balance = 4000 
monthly_payment = 300 

today = date.today()

days_in_current_month = calendar.monthrange(today.year, today.month)[1]

days_until_end_month = days_in_current_month - today.day 

end_date = today + timedelta(days=days_until_end_month + 1)

while balance > 0 :
    balance -= monthly_payment
    print(end_date, balance)
    days_in_current_month = calendar.monthrange(end_date.year, end_date.month)[1]
    end_date = end_date + timedelta(days= days_in_current_month)
