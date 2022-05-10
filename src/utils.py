import json
import math


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
    """
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

