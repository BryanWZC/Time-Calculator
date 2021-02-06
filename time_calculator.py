import math

def add_time(start, duration, day=None):
    # start date details
    hours = ''
    mins = ''
    period = ''

    # iterate start to get date details
    for i, char in enumerate(start):
        if char.isdigit() and i < 2: 
            hours += char
        elif char.isdigit(): 
            mins += char
        
        if char.isalpha(): 
            period += char

    # get number of hours and mins to add to start date times
    add_hours, add_mins = duration.split(':')

    # add start and add times together
    hours = int(hours) + int(add_hours) + 12 if period == 'PM' else int(hours) + int(add_hours)
    mins = int(mins) + int(add_mins)

    # convert normalize minutes to hours if over 60
    hours += math.floor(mins / 60)
    mins %= 60

    # get number of days that have passed since start
    number_of_days = math.floor(hours / 24)
    hours %= 24

    # result date strings to be concatenated
    res_hours = ''
    res_mins = str(mins).rjust(2, '0')
    res_period = 'PM'

    # checks resulting hours and converts from 24 hours to 12 hours
    if hours == 0:
        res_hours = '12'
    elif hours <= 12:
        res_hours = str(hours)
    else:
        res_hours = str(hours - 12)
    
    # checks hours and converts from the default PM only during morning hours
    if hours < 12:
        res_period = 'AM'

    # convert number of days into str form
    number_of_days_str = ''
    
    if number_of_days == 1:
        number_of_days_str = ' (next day)'
    elif number_of_days > 1:
        number_of_days_str = f' ({number_of_days} days later)'

    # array with string constant of days
    DAYS = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']

    # if day is given, assuming that an actual day is used, show the resulting day in results
    if day:
        day_index = DAYS.index(day.lower())
        added_days = number_of_days % 7
        res_day = DAYS[day_index + added_days] if day_index + added_days < 7 else DAYS[day_index + added_days - 7]

        return f'{res_hours}:{res_mins} {res_period}, {res_day.capitalize()}{number_of_days_str}'

    return f'{res_hours}:{res_mins} {res_period}{number_of_days_str}'