"""
discovery.py  --  "Visualizing Data" discovery activity (Models 1-3)

Author(s): Jaeseon Ha, Tanishq Kishnani
Created:   2026-09-11
Purpose:   Companion program for the MatPlotLib discovery worksheet.
             model_one()   - plots one/two cycles of a sine wave (Model 1)
             model_seven() - plots y = x**2 - 1 from -2 to +2 (question 7)
             model_two(n)  - histogram of n random numbers (Model 2)
             model_three() - reads the UGDS column of scorecard.csv and plots
                             a histogram of undergraduate enrollment (Model 3)

Usage:  python discovery.py            (shows every figure, one after another)
        python discovery.py save       (saves the figures as PNG files instead)

scorecard.csv is the "Most Recent Institution-Level Data" file from
https://collegescorecard.ed.gov/data/ (a local copy ships with the assignment;
it is NOT copied into this repository because it is ~100 MB).
"""

import csv
import random
import sys

import matplotlib
import matplotlib.pyplot as plt
import numpy as np

SAVE = len(sys.argv) > 1 and sys.argv[1] == "save"   # save PNGs instead of showing
if SAVE:
    matplotlib.use("Agg")           # no display window needed when saving


def finish(name):
    """Either save the current figure to <name>.png or show it on screen."""
    if SAVE:
        plt.savefig(name + ".png", dpi=110, bbox_inches="tight")
        plt.close()
    else:
        plt.show()


# ---------------------------------------------------------------- Model 1
def model_one(cycles=2, step=0.01, marker=""):
    """Plot `cycles` cycles of a 1 Hz sine wave sampled every `step` seconds."""
    x = np.arange(0.0, cycles, step)     # generate the data (x values)
    y = np.sin(2 * np.pi * x)            # generate the data (y values)
    plt.plot(x, y, marker) if marker else plt.plot(x, y)   # plot the data
    plt.xlabel("time (s)")               # set axes properties
    plt.ylabel("volts (mV)")
    plt.title(f"Model 1: {cycles} cycle(s), step={step}, marker='{marker}'")
    finish(f"model1_cycles{cycles}_step{step}{'_o' if marker else ''}")


def model_seven():
    """Question 7: plot y = x**2 - 1 for x from -2 to +2."""
    x = np.arange(-2.0, 2.01, 0.01)      # include the right end point +2
    y = x ** 2 - 1
    plt.plot(x, y)
    plt.xlabel("x")
    plt.ylabel("y = x^2 - 1")
    plt.title("Question 7: y = x^2 - 1")
    finish("model1_q7_parabola")


# ---------------------------------------------------------------- Model 2
def model_two(npts, bins=None):
    """Histogram of `npts` uniform random numbers in [0, 1)."""
    numbers = []
    for _ in range(npts):
        numbers.append(random.random())  # random float in [0.0, 1.0)
    if bins is None:
        plt.hist(numbers)                # default: 10 bars
    else:
        plt.hist(numbers, bins)          # e.g. 50 bars
    plt.xlabel("random value")           # question 11: axis labels
    plt.ylabel("count of values in bin")
    plt.title(f"Model 2: {npts} random numbers, bins={bins or 'default (10)'}")
    finish(f"model2_n{npts}_bins{bins or 10}")


# ---------------------------------------------------------------- Model 3
def read_ugds(filename="scorecard.csv"):
    """Return the UGDS column (undergrad enrollment) as a list of ints."""
    infile = open(filename, newline="", encoding="utf-8")   # prepare the file
    data = csv.reader(infile)                                #   for reading
    names = next(data)                                       # column names
    col = names.index("UGDS")                                # == 290 (column KE)

    ugds = []
    for row in data:                     # read the entire column into a list
        value = row[col]
        if value not in ("NULL", "NA", ""):   # skip missing values
            ugds.append(int(value))      # convert the string to an integer
    infile.close()
    return ugds


def model_three():
    """Histogram of undergraduate enrollment (UGDS) for every institution."""
    ugds = read_ugds()
    print(f"UGDS: {len(ugds)} integer values, min={min(ugds)}, max={max(ugds)}")

    plt.hist(ugds, 50)                   # 50 bins so the shape is visible
    plt.xlabel("undergraduate enrollment (UGDS)")
    plt.ylabel("number of institutions")
    plt.title("Model 3: undergraduate enrollment, all institutions")
    finish("model3_ugds_hist")

    # Same data on a log-scaled y axis: the tail of huge schools becomes visible
    plt.hist(ugds, 50)
    plt.yscale("log")
    plt.xlabel("undergraduate enrollment (UGDS)")
    plt.ylabel("number of institutions (log scale)")
    plt.title("Model 3: same histogram, log-scaled y axis")
    finish("model3_ugds_hist_log")


if __name__ == "__main__":
    random.seed(1)                       # repeatable random numbers
    model_one()                          # original: two cycles, step 0.01
    model_one(cycles=1)                  # question 3: one cycle
    model_one(step=0.15)                 # question 4: coarse steps
    model_one(marker="o")                # question 5: dots instead of a line
    model_seven()                        # question 7
    for n in (100, 1000, 10000, 100000): # questions 10 and 12
        model_two(n)
    model_two(100, bins=50)              # question 13
    model_three()                        # questions 20-21
