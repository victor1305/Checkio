from datetime import datetime
import calendar
formato = "%d.%m.%Y %H:%M"

def date_time(time: str) -> str:
    time = datetime.strptime(time, formato)
    monthNumber = time.month
    monthName = calendar.month_name[monthNumber]

    if time.hour == 1:
        hours = "hour"

    else:
        hours = "hours"

    if time.minute == 1:
        minutes = "minute"

    else:
        minutes = "minutes"

    finalTime = "{} {} {} year {} {} {} {} "

    return finalTime.format(time.day, monthName, time.year, time.hour, hours, time.minute, minutes)

if __name__ == '__main__':
    print("Example:")
    print(date_time('01.01.2000 00:00'))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert date_time("01.01.2000 00:00") == "1 January 2000 year 0 hours 0 minutes", "Millenium"
    assert date_time("09.05.1945 06:30") == "9 May 1945 year 6 hours 30 minutes", "Victory"
    assert date_time("20.11.1990 03:55") == "20 November 1990 year 3 hours 55 minutes", "Somebody was born"
    print("Coding complete? Click 'Check' to earn cool rewards!")