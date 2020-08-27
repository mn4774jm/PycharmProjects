from datetime import date, datetime, time

today = date.today() #calendar date
jan_8_2021 = date(2021, 1, 8) #arguments are year, month, date
print(jan_8_2021)

print(today < jan_8_2021) #is date in future or past?

date_from_string = date.fromisoformat('2020-09-08') #again, year/month/day
print(date_from_string) # 2020-09-08

print(today.year, today.month, today.day) #2020, 8, 9
# string version day/month/date/year
print(today.strftime('The date is %A %B %d, %Y'))

current_time = datetime.now()
print(current_time) #2020-08-27 10:22:39.863809
ts = current_time.timestamp() #Unix timestamp. Useful for saving dates in a standard format
print(ts) #1598541827.057782

afternoon = time(16,25,3) #24-hour clock
print(afternoon) #16:25:03