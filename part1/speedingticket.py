"""
speedingticket.py

Author(s): Jaeseon Ha
Created:   2026-09-11
Purpose:   Read a speed limit and a driving speed (both integers, in mph)
           from standard input and print the traffic ticket amount:
             - 10 mph or more UNDER the limit ........ $50
             -  6 to 20 mph OVER the limit ........... $75
             - 21 to 40 mph OVER the limit ........... $150
             - more than 40 mph OVER the limit ....... $300
             - anything else ......................... $0 (no ticket)

Run normally:   python speedingticket.py      (reads two lines, prints amount)
Run the tests:  python speedingticket.py test
"""

import sys


def ticket_amount(limit, speed):
    """Return the ticket amount (int) for driving `speed` mph in a `limit` zone."""
    diff = speed - limit          # positive = over the limit, negative = under

    if diff <= -10:               # 10 mph under the limit or slower
        return 50
    elif 6 <= diff <= 20:         # 6-20 mph over
        return 75
    elif 21 <= diff <= 40:        # 21-40 mph over
        return 150
    elif diff > 40:               # more than 40 mph over
        return 300
    else:                         # -9 .. +5 mph: no ticket
        return 0


def run_tests():
    """Black-box and clear-box tests for ticket_amount()."""
    # --- black-box tests (based on the specification / examples only) ---
    assert ticket_amount(35, 45) == 75      # example from the assignment
    assert ticket_amount(35, 26) == 0       # example from the assignment
    assert ticket_amount(65, 120) == 300    # way over the limit
    assert ticket_amount(55, 30) == 50      # crawling far below the limit
    assert ticket_amount(30, 30) == 0       # exactly at the limit

    # --- clear-box tests (chosen by looking at the boundaries in the code) ---
    assert ticket_amount(50, 40) == 50      # diff == -10  -> $50 (boundary)
    assert ticket_amount(50, 41) == 0       # diff == -9   -> no ticket (boundary)
    assert ticket_amount(50, 55) == 0       # diff == +5   -> no ticket (boundary)
    assert ticket_amount(50, 56) == 75      # diff == +6   -> $75 (boundary)
    assert ticket_amount(50, 70) == 75      # diff == +20  -> $75 (boundary)
    assert ticket_amount(50, 71) == 150     # diff == +21  -> $150 (boundary)
    assert ticket_amount(50, 90) == 150     # diff == +40  -> $150 (boundary)
    assert ticket_amount(50, 91) == 300     # diff == +41  -> $300 (boundary)
    assert ticket_amount(0, 0) == 0         # zero inputs
    print("speedingticket.py: all tests passed")


def main():
    """Read the two integers (no prompts) and print the ticket amount."""
    limit = int(input())
    speed = int(input())
    print(ticket_amount(limit, speed))


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "test":
        run_tests()
    else:
        main()
