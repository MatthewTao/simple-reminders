import json
import math

from datetime import timedelta


def read_config():
    with open('config.json') as f:
        config = json.load(f)
    return config


def read_reminder_list(config):
    list_location = config.get('list_location')
    if list_location == 'local':
        local_list_loc = config.get('local_list_loc')
        with open(local_list_loc) as f:
            reminder_list = json.load(f).get('reminders')
    elif list_location == 'online':
        # TODO: Interesting to be able to possibly implement something online
        raise NotImplemented
    
    return reminder_list


def round_up(n, decimals=0):
    multiplier = 10 ** decimals
    return int(math.ceil(n * multiplier) / multiplier)


def determine_number_suffix(number):
    """
    Return appropriate suffix for each number
    'st' if number ends with 1 --> 51st
    'nd' if number ends with 2 --> 2nd, 32nd
    'rd' if number ends with 3 --> 3rd, 43rd
    'th' for all other cases   --> 7th, 19th

    '' if None is passed in
    """
    if isinstance(number, int) is False:
        # Short circuit return
        return ''

    last_digit = str(number)[-1]
    if int(last_digit) > 3:
        suffix = 'th'
    else:
        mapping = {
            '1': 'st',
            '2': 'nd',
            '3': 'rd'
        }
        suffix = mapping[last_digit]

    return suffix


def next_day_of_week(desired_day, date):
    """
    Returns the next date of a particular day of week (e.g. friday)
    desired_day should be an integer where 0 is monday and 6 is sunday
    date is the date that the search will begin
    """
    while date.weekday() != desired_day:
        date += timedelta(days=1)

    return date


def str_fmt_minutes(minutes):
    """
    Returns minutes as a string formatted time
    e.g. 6 hours 34 minutes
    """
    hours = int(minutes // 60)
    # Determine if there should be an 's' after hour
    hr_plural = 's' if hours != 1 else ''

    minute = ((minutes / 60) - hours) * 60
    min_plural = 's' if minute != 1 else ''

    return f"{hours} hour{hr_plural} {round(minute)} min{min_plural}"


def str_fmt_days(time_delta):
    """
    Returns minutes as a string formatted time
    e.g. 3 days, 6 hours and 34 minutes
    """
    days = int(time_delta.days)
    day_plural = 's' if days != 1 else ''

    if days < 10:
        remaining_minutes = time_delta.seconds / 60
        hours = int(remaining_minutes // 60)
        # Determine if there should be an 's' after hour
        hr_plural = 's' if hours != 1 else ''
        remainder = remaining_minutes / 60 - hours

        minute = int(remainder * 60)
        min_plural = 's' if minute != 1 else ''
        time_remaining = f"{days} day{day_plural}, {hours} hour{hr_plural} and {round(minute)} min{min_plural}"
    elif days >= 10:
        time_remaining = f"{days} day{day_plural}"

    return time_remaining
