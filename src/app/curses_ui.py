import curses

from src.app.ui_utils import get_screen_size, progress_bar, update_datetime
from src.reminder.reminder import Reminder

TITLE = """
  ___ _            _                       _         _            
 / __(_)_ __  _ __| |___     _ _ ___ _ __ (_)_ _  __| |___ _ _ ___
 \__ | | '  \| '_ | / -_)   | '_/ -_| '  \| | ' \/ _` / -_| '_(_-<
 |___|_|_|_|_| .__|_\___|   |_| \___|_|_|_|_|_||_\__,_\___|_| /__/
             |_|                                                  
Q to exit"""
def main(stdscr):
    # Sets that the screen will not wait for key presses
    stdscr.nodelay(1)

    # curser not visible when set to 0, visible when set to 1
    curses.curs_set(0)
    
    # start the application off with a blank screen
    stdscr.clear()
    
    # 0, 0 is the top left corner
    # Coordinates are always passed in the order y, x
    stdscr.addstr(
        0, 0,
        TITLE,
        curses.A_BOLD)
    stdscr.refresh()

    # scr_size = get_screen_size()
    # scr_size_win = curses.newwin(1, 50, 7, 0)
    # scr_size_win.addstr(f'Current screen size is {scr_size}')
    # scr_size_win.refresh()

    datetime_window = curses.newwin(1, 40, 8, 0)
    reminder = Reminder()
    reminders = reminder.determine_time_remaining()

    windows = {}
    i = 1
    last_free_row = 9
    first_free_row = 9
    for _reminder in reminders:
        windows[i] = curses.newwin(1, 100, first_free_row + i, 0)
        windows[i].addstr(f'{_reminder.get("description")} in {_reminder.get("due_in")}')
        windows[i].refresh()
        i += 1
        last_free_row += 1

    refreshes = 0
    while True:
        update_datetime(datetime_window)
        
        if stdscr.getch() == ord('q'):
            break

        if refreshes % 10 == 0:
            reminders = reminder.determine_time_remaining()
            i = 1
            for _reminder in reminders:
                window = windows.get(i)
                if window is not None:
                    window.clear()
                else:
                    # make new window
                    windows[i] = curses.newwin(1, 100, first_free_row + i, 0)
                    last_free_row += 1
                    window = windows.get(i)
                window.addstr(f'{_reminder.get("description")} in {_reminder.get("due_in")}')
                window.refresh()
                i += 1
            refreshes = 0

        # stdscr.refresh()
        refreshes += 1
        curses.napms(100)

    progress_bar(
        pre_message='Will quit soon ',
        nlines=1,
        ncols=100,
        begin_y=last_free_row + 2,
        begin_x=0)
