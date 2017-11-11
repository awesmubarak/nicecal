#!/usr/bin/env python3
#coding=utf-8

"""Nicecal.

Create good looking plain text calendars using box-drawing characters.

"""

from calendar import month as cal_month

def month(year, month, show_month_info=1, show_days=1):
    """Returns a month's calendar.

    Args:
        show_month_info (integer) (default 1)
            0: No month information header
            1: Only month name centered as header
            2: Both month name and year centered as header
        show_days (integer) (defaut 1)
            0: Day names are not shown
            1: Day names are shown

    """
    # variables
    calendar_width = 22
    raw_calendar = cal_month(year, month).split("\n")
    nice_calendar = []
    nicer_calendar = []
    # month and year title information
    if show_month_info == 1:
        # month
        nice_calendar.append((" " * 3) + raw_calendar[0][:-5])
    elif show_month_info == 2:
        # month and year
        nice_calendar.append(raw_calendar[0])
    # day names
    if show_days:
        nice_calendar.append(raw_calendar[1])
    # main calendar
    for line in raw_calendar[2:]:
        if line != "":
            nice_calendar.append(line)
    # wrap in box drawing characters
    for line in nice_calendar:
        nicer_calendar.append(("│ " + line).ljust(22) + " │")
    nicer_calendar.insert(0, "┌" + ("─" * calendar_width) + "┐")
    nicer_calendar.append("└" + ("─" * calendar_width) + "┘")
    # Join list items and return
    return "\n".join(nicer_calendar)
