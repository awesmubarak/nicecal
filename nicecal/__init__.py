#!/usr/bin/env python3

import calendar

def nicecal(year, month, show_month_info = 1, show_days = 1):
    """Return a nice calendar.
    Options:
    -   show_month_info (default 1)
        -   0: No month information header
        -   1: Only month name centered as header
        -   2: Both month name and year centered as header
    -   show_days (defaut 1)
        -   0: Day names are not shown
        -   1: Day names are shown
    """
    def wrapped_line(text):
        """Wraps a line in bar characters."""
        return(("│ " + text).ljust(22) + " │")
    # create variables
    raw_calendar  = calendar.month(year, month).split("\n")
    calendar_width = 22
    nice_calendar = []
    # create top bar
    nice_calendar.append("┌" + ("─" * calendar_width) + "┐")
    # month bar
    if show_month_info == 1:
        nice_calendar.append(wrapped_line((" " * 3) + raw_calendar[0][:-5]))
    elif show_month_info == 2:
        nice_calendar.append(wrapped_line(raw_calendar[0]))
    # days bar
    if show_days:
        nice_calendar.append(wrapped_line(raw_calendar[1]))
    # draw main calendar
    for line in raw_calendar[2:]:
        if line != "":
            nice_calendar.append(wrapped_line(line))
    # bottom bar
    nice_calendar.append("└" + ("─" * calendar_width) + "┘")
    return "\n".join(nice_calendar)

print(nicecal(2038, 1, show_month_info=0))
