import curses
from datetime import datetime

class Printer(object):
    stdscr = curses.initscr()
    old = 0.0
    i = 4

    def __init__(self, ver):
        self.stdscr.addstr(0, 0, 'mzbot v' + ver +' by Matteo Zoia')
        self.stdscr.addstr(3, 0, 'Log:')

    def refresh_header(self, val_price, val_24low, val_24high, hl_gap, price_gap):
        # Visual feedback for changed price
        if self.old == val_price:
            self.stdscr.addstr(1, 0, 'ETH-EUR {0:.2f}'.format(val_price))
        else:
            self.stdscr.addstr(1, 0, 'ETH-EUR {0:.2f}'.format(val_price), curses.A_REVERSE)

        self.stdscr.addstr(1, 15,' | Low {0:.2f} | High {1:.2f} | H/L {2:.2f}% | H/P {3:.2f}%'.format(val_24low,val_24high,hl_gap, price_gap))
        self.stdscr.refresh()
        self.old = val_price

    def log(self, msg):
        self.stdscr.addstr(self.i, 0, '[{0}] {1}'.format(datetime.now().strftime("%Y-%m-%d %H:%M:%S"),msg))
        self.stdscr.refresh()
        self.i = self.i + 1
        if self.i == 13:
            self.i = 3

    # reset the terminal as before
    def exit(self):
        curses.nocbreak()
        self.stdscr.keypad(0)
        curses.echo()
        curses.endwin()
