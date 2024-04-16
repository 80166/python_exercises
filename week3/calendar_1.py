import calendar 
m, d, y = map(int, input().split())

week_day = calendar.weekday(y, m, d)
day_Name = calendar.day_name[week_day]

print(day_Name.upper())