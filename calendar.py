import datetime


def print_calendar(year, month):
    first_day = datetime.date(year, month, 1)
    last_day = datetime.date(year, month + 1, 1) - datetime.timedelta(days=1)
    month_name = first_day.strftime("%B")
    first_weekday = first_day.weekday()
    days_in_month = last_day.day

    print(month_name, year)
    print("Mo Tu We Th Fr Sa Su")

    for i in range(first_weekday):
        print("   ", end="")


    day = 1
    while day <= days_in_month:
        print("{:2} ".format(day), end="")
        if (day + first_weekday) % 7 == 0:
            print()
        day += 1

    print()




year = int(input('Введите год:'))
month = int(input('Введите месяц:'))
print(year, month)

print_calendar(year, month)
