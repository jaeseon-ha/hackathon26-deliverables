"""
fill_worksheet.py

Author(s): Jaeseon Ha
Created:   2026-09-11
Purpose:   Fill the fillable fields of "MatPlotLib discovery.pdf" with our
           team's answers and write "MatPlotLib discovery - filled.pdf".
           Team-member names are set at the top; re-run to regenerate.

Usage:  python fill_worksheet.py  [path/to/MatPlotLib discovery.pdf]
Needs:  pip install pypdf
"""

import sys
from pypdf import PdfReader, PdfWriter

# ---- team roles (edit here) -------------------------------------------
MANAGER   = "Jaeseon Ha"
PRESENTER = "Jaeseon Ha"
RECORDER  = ""
REFLECTOR = ""

ANSWERS = {
    # page 1: roles
    "ans1": MANAGER, "ans2": RECORDER, "ans3": PRESENTER, "ans4": REFLECTOR,

    # ---- Model 1 -------------------------------------------------------
    "ans5": "",                       # start time
    "ans6": "5-6",                    # 1a generated the data
    "ans7": "8-9",                    # 1b set the axes properties
    "ans8": "10",                     # 1c displayed the window
    "ans9": "7",                      # 1d plotted the actual data
    "ans10": ("A sine wave: y = sin(2*pi*x) for x from 0.0 up to (not including) 2.0 in "
              "steps of 0.01, i.e. 200 points. Because the frequency is 1 cycle per unit "
              "of x, the plot shows two full cycles of a 1 Hz wave, with time in seconds "
              "on the x axis and voltage in millivolts on the y axis."),
    "ans11": "x = np.arange(0.0, 1.0, .01)",
    "ans12": ("Only 14 points are generated (0, 0.15, 0.30, ... 1.95), so the curve is "
              "drawn with straight line segments between far-apart samples and looks "
              "jagged/angular instead of a smooth sine wave."),
    "ans13": ("plt.plot(x, y, 'o') draws each data point as a circle marker with no "
              "connecting line, so the sine wave appears as a series of dots (200 of "
              "them with step 0.01; only 14 with step 0.15)."),
    "ans14": ("It is the step (spacing) between consecutive x values, so it controls how "
              "many points are sampled: a small step (0.01) gives many points and a "
              "smooth curve; a large step (0.15) gives few points and a coarse, jagged plot."),
    "ans15": ("x = np.arange(-2.0, 2.01, .01)   # -2 to +2 inclusive\n"
              "y = x ** 2 - 1\n"
              "plt.plot(x, y); plt.xlabel('x'); plt.ylabel('y = x^2 - 1'); plt.show()"),
    "ans16": ("matplotlib (https://matplotlib.org) - a comprehensive library for creating "
              "static, animated and interactive 2D plots and charts in Python. "
              "NumPy (https://numpy.org) - the fundamental package for numerical computing "
              "in Python, providing fast N-dimensional arrays and math functions such as "
              "np.arange, np.sin and np.pi. The third library is the Python standard "
              "library / built-ins (and matplotlib.pyplot is itself the sub-module that "
              "gives the MATLAB-style plotting interface)."),

    # ---- Model 2 -------------------------------------------------------
    "ans17": "",                      # start time
    "ans18": "0.0 <= x < 1.0",        # 9a range of random()
    "ans19": "100",                   # 9b how many values
    "ans20": "10",                    # 10a bars
    "ans21": "0.1 (approx.)",         # 10b width
    "ans22": "100",                   # 10c sum of heights
    "ans23": ("x axis: 'random value' (the value of the number, 0 to 1, split into bins); "
              "y axis: 'count' / 'frequency' (how many of the 100 random numbers fall "
              "into each bin)."),
    "ans24": ("The bars get taller (their heights sum to n) and much more even in height. "
              "With 100 numbers the bars vary a lot (e.g. 5 to 16); with 1000 they are "
              "roughly 100 each; with 10000 and 100000 the histogram is nearly flat, "
              "showing that random.random() is uniform on [0, 1)."),
    "ans25": ("The second argument is the number of bins: the range 0-1 is split into 50 "
              "equal-width bins (width 0.02) instead of 10, so 50 narrower bars are drawn "
              "and each bar's height is the count of numbers in that 0.02-wide interval "
              "(about 2 each for n=100, so the plot looks much noisier)."),
    "ans26": ("hist() finds the min and max of the list, divides that range into equal-"
              "width intervals (bins, 10 by default), counts how many values fall into "
              "each interval, and draws one bar per bin whose height is that count. It "
              "returns the counts and the bin edges."),

    # ---- Model 3 -------------------------------------------------------
    "ans27": "",                      # start time
    "ans28": "It is the header: column names, not data",   # 15a
    "ans29": "5",                     # 15b rows
    "ans30": "4",                     # 15b columns
    "ans31": "yes",                   # 16a quotes in data.csv
    "ans32": "no",                    # 16a quotes in output
    "ans33": "So a comma inside a cell is not a separator",
    "ans34": "names = next(data)",    # 17a
    "ans35": "a list of strings (one string per column)",   # 17b
    "ans36": "6,274 (1 header + 6,273 data rows)",  # 18a
    "ans37": "3,308",                 # 18b
    "ans38": "0 to 163,164 students", # 19a
    "ans39": "Southern New Hampshire University",  # 19b
    "ans40": "No: 795 rows are 'NA', 5,478 are ints",  # 19c
    "ans41": "import matplotlib.pyplot as plt\nimport csv",
    "ans42": ("infile = open('scorecard.csv', newline='', encoding='utf-8')\n"
              "data = csv.reader(infile)\n"
              "names = next(data)   # skip/keep the header row"),
    "ans43": ("ugds = []\n"
              "for row in data:\n"
              "    ugds.append(row[290])   # 290 == names.index('UGDS'), column KE"),
    "ans44": ("ugds = []\n"
              "for row in data:\n"
              "    if row[290] not in ('NULL', 'NA', ''):   # skip missing values\n"
              "        ugds.append(int(row[290]))"),
    "ans45": "plt.hist(ugds, 50)\nplt.show()",
    "ans46": ("The distribution is extremely right-skewed. Almost all institutions are "
              "small: the very first bar (0 to ~3,000 students) holds the vast majority of "
              "the 5,478 schools, and the bars fall off so quickly that schools above "
              "~20,000 are almost invisible; only a handful of giant (mostly online) "
              "universities such as SNHU (163k), WGU (155k) and Univ. of Phoenix (86k) "
              "form a long thin tail. A log-scaled y axis or a cap on the x range is "
              "needed to see the typical school size."),
    "ans47": ("Histograms: distribution of admission rate (ADM_RATE), average SAT (SAT_AVG), "
              "cost of attendance, or graduation rate; compare public vs private (CONTROL) "
              "by overlaying two histograms. Scatter plots: does cost relate to graduation "
              "rate? admission rate vs SAT_AVG? enrollment vs median earnings? Line charts: "
              "sort schools by size and plot cumulative enrollment share, or plot average "
              "cost by state (STABBR) in order, or trends over years if multiple yearly "
              "files are combined."),
}

src = sys.argv[1] if len(sys.argv) > 1 else "MatPlotLib discovery.pdf"
reader = PdfReader(src)
writer = PdfWriter()
writer.append(reader)
for page in writer.pages:
    writer.update_page_form_field_values(page, ANSWERS, auto_regenerate=False)
writer.set_need_appearances_writer(True)    # let the viewer render the text
out = "MatPlotLib discovery - filled.pdf"
with open(out, "wb") as f:
    writer.write(f)
print("wrote", out)
