import curses

from src.app.ui_utils import get_screen_size, progress_bar, update_datetime

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

    scr_size = get_screen_size()
    scr_size_win = curses.newwin(1, 50, 7, 0)
    scr_size_win.addstr(f'Current screen size is {scr_size}')
    scr_size_win.refresh()

    datetime_window = curses.newwin(1, 40, 8, 0)
    while True:
        update_datetime(datetime_window)
        
        if stdscr.getch() == ord('q'):
            break
        
        stdscr.refresh()
        curses.napms(100)

    progress_bar(
        pre_message='Will quit soon ',
        nlines=1,
        ncols=100,
        begin_y=9,
        begin_x=0)
