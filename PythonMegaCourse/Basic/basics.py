from cgi import print_arguments


day_hour = 24
week_days = 7

def weekHours(dayHours, weekDays):
    weekHours = day_hour * week_days
    return weekHours

week_hours = weekHours(day_hour,week_days)

print(week_hours)