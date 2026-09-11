"""
stocktrading.py

Author(s): Jaeseon Ha, Tanishq Kishnani
Created:   2026-09-11
Purpose:   Define maxProfit(prices), where prices[i] is a stock's price on
           day i. Choosing ONE day to buy and a LATER day to sell, return the
           maximum profit possible. If no profitable trade exists, return 0.

           Approach: scan the prices once, remembering the lowest price seen
           so far; on each day the best sale is (today's price - lowest so far).

Run normally:   python stocktrading.py        (runs the example)
Run the tests:  python stocktrading.py test
"""

import sys


def maxProfit(prices):
    """Return the max profit from one buy followed by one later sell (or 0)."""
    if len(prices) < 2:          # need at least two days to buy and then sell
        return 0

    lowest_so_far = prices[0]    # cheapest price seen up to today
    best_profit = 0              # best profit found so far (never below 0)

    for price in prices[1:]:     # day 0 can only be a buy day, so start at day 1
        profit_today = price - lowest_so_far   # sell today, bought at the low
        if profit_today > best_profit:
            best_profit = profit_today
        if price < lowest_so_far:              # new low -> future buy point
            lowest_so_far = price

    return best_profit


def run_tests():
    """Black-box and clear-box tests for maxProfit()."""
    # --- black-box tests (from the specification) ---
    assert maxProfit([7, 1, 5, 3, 6, 4]) == 5      # assignment example: buy 1, sell 6
    assert maxProfit([7, 6, 4, 3, 1]) == 0         # always falling -> no profit
    assert maxProfit([1, 2, 3, 4, 5]) == 4         # always rising -> buy first, sell last
    assert maxProfit([3, 3, 3]) == 0               # flat prices -> no profit
    assert maxProfit([2, 4, 1, 10]) == 9           # best trade after a new low

    # --- clear-box tests (paths and edge cases inside the code) ---
    assert maxProfit([]) == 0                      # empty list -> early return
    assert maxProfit([5]) == 0                     # one day -> can't buy and sell
    assert maxProfit([5, 1]) == 0                  # two days, price drops
    assert maxProfit([1, 5]) == 4                  # two days, price rises
    assert maxProfit([9, 1, 3, 2, 8, 0, 1]) == 7   # best profit is NOT from the global min
    print("stocktrading.py: all tests passed")


def main():
    """Show the function on the example from the assignment."""
    prices = [7, 1, 5, 3, 6, 4]
    print("prices =", prices)
    print("max profit =", maxProfit(prices))


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "test":
        run_tests()
    else:
        main()
