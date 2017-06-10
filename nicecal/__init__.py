# coding=utf-8
"""Create simple, nice looking ascii calendars."""

import calendar

def month(year, month, show_month_info = 1, show_days = 1):
    """Returns a month's calendar.
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
    # Declare variables
    calendar_width = 22
    nice_calendar = []
    raw_calendar  = calendar.month(year, month).split("\n")
    # Create month and year information
    if show_month_info == 1:
        # Month only
        nice_calendar.append(wrapped_line((" " * 3) + raw_calendar[0][:-5]))
    elif show_month_info == 2:
        # Month and year
        nice_calendar.append(wrapped_line(raw_calendar[0]))
    # Create day name bar
    if show_days:
        nice_calendar.append(wrapped_line(raw_calendar[1]))
    # Create main calendar
    for line in raw_calendar[2:]:
        if line != "":
            nice_calendar.append(wrapped_line(line))
    # Create top and bottom bars
    nice_calendar.insert(0, "┌" + ("─" * calendar_width) + "┐")
    nice_calendar.append("└" + ("─" * calendar_width) + "┘")
    # Join list items and return
    return "\n".join(nice_calendar)
