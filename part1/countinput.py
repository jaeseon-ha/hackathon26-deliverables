"""
countinput.py

Author(s): Jaeseon Ha
Created:   2026-09-11
Purpose:   Define countchars(st), which returns the number of characters in a
           string EXCLUDING spaces, periods, exclamation points, and commas.
           Every other character (letters, digits, '?', '-', tabs, ...) counts.
           The main program asks the user for a string, calls countchars()
           on it, and prints the result.

Run normally:   python countinput.py
Run the tests:  python countinput.py test
"""

import sys

EXCLUDED = " .!,"        # characters that are NOT counted


def countchars(st):
    """Return the number of characters in `st` that are not in EXCLUDED."""
    count = 0
    for ch in st:                # look at every character one by one
        if ch not in EXCLUDED:   # skip space, period, '!' and ','
            count += 1
    return count


def run_tests():
    """Black-box and clear-box tests for countchars()."""
    # --- black-box tests (from the specification) ---
    assert countchars("Listen, Mr. Jones, calm down.") == 21   # assignment example
    assert countchars("") == 0                                 # empty string
    assert countchars("hello") == 5                            # nothing to exclude
    assert countchars("What? 2+2=4") == 10                     # '?', digits, symbols count
    assert countchars("a b c d e") == 5                        # spaces removed

    # --- clear-box tests (each excluded character and only excluded chars) ---
    assert countchars(" .!,") == 0            # string made only of excluded chars
    assert countchars("!!!Wow!!!") == 3       # exclamation points removed
    assert countchars("1,000,000") == 7       # commas removed, digits kept
    assert countchars("end.") == 3            # trailing period removed
    assert countchars("tab\there") == 8       # a tab is NOT excluded, so it counts (8 chars)
    print("countinput.py: all tests passed")


def main():
    """Ask the user for a string and display the character count."""
    text = input("Enter a string: ")
    print(countchars(text))


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "test":
        run_tests()
    else:
        main()
