import curses
from datetime import datetime
import time


def get_screen_size():
    return (curses.LINES - 1, curses.COLS - 1)


def progress_bar(pre_message, nlines, ncols, begin_y, begin_x):
    my_window = curses.newwin(nlines, ncols, begin_y, begin_x)
    pre_message = pre_message + '['
    my_window.addstr(0, ncols - 2, ']')
    my_window.addstr(0,0, pre_message)
    for i in range(ncols - len(pre_message) - 3):
        my_window.addstr(0,i + len(pre_message), '#')
        my_window.refresh()
        time.sleep(0.1)


def update_datetime(window):
    window.clear()
    now = datetime.now()
    date_time = now.strftime("%m/%d/%Y, %H:%M:%S")
    window.addstr(f'date and time: {date_time}')
    window.refresh()
