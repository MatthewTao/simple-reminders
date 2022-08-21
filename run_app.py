from curses import wrapper

from src.app.curses_ui import main

print('Application starting')

wrapper(main)

print('Application finished successfully')
