"""
heatingcooling.py

Author(s): Jaeseon Ha
Created:   2026-09-11
Purpose:   Repeatedly ask the user for an average daily temperature (integer,
           degrees Fahrenheit) and keep running totals of
             - heating days : temperature below 60 F
             - cooling days : temperature above 80 F
           Input stops when the user enters a value lower than -459
           (below absolute zero). The two totals are then printed.

Run normally:   python heatingcooling.py
Run the tests:  python heatingcooling.py test
"""

import sys

SENTINEL = -459          # any value lower than this ends the input
HEATING_BELOW = 60       # a day colder than this is a heating day
COOLING_ABOVE = 80       # a day warmer than this is a cooling day


def classify(temp):
    """Return 'heating', 'cooling', or None for one day's average temperature."""
    if temp < HEATING_BELOW:
        return "heating"
    elif temp > COOLING_ABOVE:
        return "cooling"
    return None            # a mild day: neither heating nor cooling


def count_days(temps):
    """Return (heating_days, cooling_days) for a list of daily temperatures."""
    heating = 0
    cooling = 0
    for t in temps:
        kind = classify(t)
        if kind == "heating":
            heating += 1
        elif kind == "cooling":
            cooling += 1
    return heating, cooling


def run_tests():
    """Black-box and clear-box tests for classify() and count_days()."""
    # --- black-box tests ---
    assert count_days([33, 90, 98, 66, 22]) == (2, 2)   # sample run from the assignment
    assert count_days([]) == (0, 0)                      # no data at all
    assert count_days([70, 65, 75]) == (0, 0)            # only mild days
    assert count_days([-20, 0, 10]) == (3, 0)            # only cold (heating) days
    assert count_days([85, 100, 120]) == (0, 3)          # only hot (cooling) days

    # --- clear-box tests (boundaries used in the code) ---
    assert classify(59) == "heating"     # just below 60 -> heating
    assert classify(60) is None          # exactly 60 -> not heating
    assert classify(80) is None          # exactly 80 -> not cooling
    assert classify(81) == "cooling"     # just above 80 -> cooling
    assert classify(-459) == "heating"   # -459 itself is still valid data
    print("heatingcooling.py: all tests passed")


def main():
    """Prompt for temperatures until the sentinel, then print the totals."""
    temps = []
    while True:
        temp = int(input("Enter the average daily temperature: "))
        if temp < SENTINEL:        # end-of-input signal
            break
        temps.append(temp)

    heating, cooling = count_days(temps)
    print("Heating days:", heating)
    print("Cooling days:", cooling)


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "test":
        run_tests()
    else:
        main()
