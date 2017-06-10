=======
Nicecal
=======

Create simple, nice looking ascii calendars.

Usage
=====

Return a simple, formatted calendar:

``nicecal(2038, 1)``
::

    ┌──────────────────────┐
    │        January       │
    │ Mo Tu We Th Fr Sa Su │
    │              1  2  3 │
    │  4  5  6  7  8  9 10 │
    │ 11 12 13 14 15 16 17 │
    │ 18 19 20 21 22 23 24 │
    │ 25 26 27 28 29 30 31 │
    └──────────────────────┘

The calendar outoput can also be modified in the following ways:

Options:

- ``show_month_info`` (default 1)
    - 0: No month information header
    - 1: Only month name centered as header
    - 2: Both month name and year centered as header
- ``show_days`` (defaut 1)
    - 0: Day names are not shown
    - 1: Day names are shown

Examples
--------

``>>>nicecal(2038, 1, show_month_info=0)``
::

    ┌──────────────────────┐
    │ Mo Tu We Th Fr Sa Su │
    │              1  2  3 │
    │  4  5  6  7  8  9 10 │
    │ 11 12 13 14 15 16 17 │
    │ 18 19 20 21 22 23 24 │
    │ 25 26 27 28 29 30 31 │
    └──────────────────────┘

``>>>nicecal(2038, 1, show_month_info=2)``
::

    ┌──────────────────────┐
    │     January 2038     │
    │ Mo Tu We Th Fr Sa Su │
    │              1  2  3 │
    │  4  5  6  7  8  9 10 │
    │ 11 12 13 14 15 16 17 │
    │ 18 19 20 21 22 23 24 │
    │ 25 26 27 28 29 30 31 │
    └──────────────────────┘


``>>>nicecal(2038, 1, show_days=0)``
::

    ┌──────────────────────┐
    │        January       │
    │              1  2  3 │
    │  4  5  6  7  8  9 10 │
    │ 11 12 13 14 15 16 17 │
    │ 18 19 20 21 22 23 24 │
    │ 25 26 27 28 29 30 31 │
    └──────────────────────┘

``>>>nicecal(2038, 1, show_month_info=2, show_days=0)``
::

    ┌──────────────────────┐
    │     January 2038     │
    │              1  2  3 │
    │  4  5  6  7  8  9 10 │
    │ 11 12 13 14 15 16 17 │
    │ 18 19 20 21 22 23 24 │
    │ 25 26 27 28 29 30 31 │
    └──────────────────────┘

``>>>nicecal(2038, 1, show_month_info=0, show_days=0)``
::

    ┌──────────────────────┐
    │              1  2  3 │
    │  4  5  6  7  8  9 10 │
    │ 11 12 13 14 15 16 17 │
    │ 18 19 20 21 22 23 24 │
    │ 25 26 27 28 29 30 31 │
    └──────────────────────┘
