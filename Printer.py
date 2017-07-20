import curses

class Printer(object):
    stdscr = curses.initscr()
    old = 0.0

    def __init__(self, ver):
        self.stdscr.addstr(0, 0, 'mzbot v' + ver +' by Matteo Zoia')

    def refresh_header(self, val_price, val_24low, val_24high, hl_gap, price_gap):
        # Visual feedback for changed price
        if self.old == val_price:
            self.stdscr.addstr(1, 0, 'ETH-EUR {0:.2f}'.format(val_price))
        else:
            self.stdscr.addstr(1, 0, 'ETH-EUR {0:.2f}'.format(val_price), curses.A_REVERSE)

        self.stdscr.addstr(1, 15,' | Low {0:.2f} | High {1:.2f} | H/L {2:.2f}% | H/P {3:.2f}%'.format(val_24low,val_24high,hl_gap, price_gap))
        self.stdscr.refresh()
        self.old = val_price

    # reset the terminal as before
    def exit(self):
        curses.nocbreak()
        self.stdscr.keypad(0)
        curses.echo()
        curses.endwin()
