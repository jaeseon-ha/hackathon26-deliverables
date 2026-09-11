# Flowcharts for every program

One diagram per file. Diamonds are decisions, rectangles are actions.
Each Part 1 program has the same outer shape: run the tests if started with `test`, otherwise run `main()`.

## The shared outer structure (all Part 1 files)

```mermaid
flowchart TD
    A([python file.py ...]) --> B{started with<br>argument "test"?}
    B -- yes --> C[run_tests: every assert must hold]
    C --> D[print "all tests passed"]
    B -- no --> E[main: read input, call the function, print result]
```

## speedingticket.py — `ticket_amount(limit, speed)`

```mermaid
flowchart TD
    A[read limit, read speed] --> B[diff = speed - limit]
    B --> C{diff <= -10 ?}
    C -- yes --> T50[ticket = 50]
    C -- no --> D{6 <= diff <= 20 ?}
    D -- yes --> T75[ticket = 75]
    D -- no --> E{21 <= diff <= 40 ?}
    E -- yes --> T150[ticket = 150]
    E -- no --> F{diff > 40 ?}
    F -- yes --> T300[ticket = 300]
    F -- no --> T0[ticket = 0]
    T50 & T75 & T150 & T300 & T0 --> P[print ticket]
```

## heatingcooling.py — `main()` loop and `classify(temp)`

```mermaid
flowchart TD
    A[temps = empty list] --> B[ask: Enter the average daily temperature]
    B --> C{temp < -459 ?}
    C -- yes: stop signal --> H[heating, cooling = count_days temps]
    C -- no --> D[append temp to temps] --> B
    H --> I[print Heating days / Cooling days]

    subgraph classify one day
        X[temp] --> Y{temp < 60 ?}
        Y -- yes --> Y1[heating]
        Y -- no --> Z{temp > 80 ?}
        Z -- yes --> Z1[cooling]
        Z -- no --> Z2[neither]
    end
```

## countinput.py — `countchars(st)`

```mermaid
flowchart TD
    A[count = 0] --> B{more characters<br>in the string?}
    B -- no --> Z[return count]
    B -- yes --> C[take next character ch]
    C --> D{ch is one of<br>space . ! , ?}
    D -- yes: skip it --> B
    D -- no --> E[count = count + 1] --> B
```

Example: `Listen, Mr. Jones, calm down.` has 29 characters; 4 spaces, 2 periods and 2 commas are skipped, leaving 21.

## stocktrading.py — `maxProfit(prices)`

```mermaid
flowchart TD
    A{fewer than 2 prices?} -- yes --> R0[return 0]
    A -- no --> B[lowest_so_far = prices at day 0<br>best_profit = 0]
    B --> C{more days left?}
    C -- no --> Z[return best_profit]
    C -- yes --> D[price = next day's price]
    D --> E[profit_today = price - lowest_so_far]
    E --> F{profit_today > best_profit?}
    F -- yes --> G[best_profit = profit_today]
    F -- no --> H
    G --> H{price < lowest_so_far?}
    H -- yes --> I[lowest_so_far = price] --> C
    H -- no --> C
```

Walk-through for `[7, 1, 5, 3, 6, 4]`:

| day | price | lowest so far | profit today | best so far |
|---|---|---|---|---|
| 0 | 7 | 7 | – | 0 |
| 1 | 1 | 1 | -6 | 0 |
| 2 | 5 | 1 | 4 | 4 |
| 3 | 3 | 1 | 2 | 4 |
| 4 | 6 | 1 | 5 | **5** |
| 5 | 4 | 1 | 3 | 5 |

## discovery.py — Part 2 program

```mermaid
flowchart TD
    A([python discovery.py save]) --> M1[model_one: x = arange 0..2 step 0.01<br>y = sin 2πx → plot → label axes → save/show]
    M1 --> M1b[same with 1 cycle, step 0.15, marker 'o']
    M1b --> M7[model_seven: y = x² - 1 from -2 to 2]
    M7 --> M2[model_two n: make n random numbers<br>hist → label → save/show, for n = 100 … 100000]
    M2 --> M3[model_three]

    subgraph model_three
        R1[open scorecard.csv, csv.reader, skip header] --> R2{more rows?}
        R2 -- yes --> R3{row 290 is NA / NULL / empty?}
        R3 -- yes: skip --> R2
        R3 -- no --> R4[append int value to ugds] --> R2
        R2 -- no --> R5[hist ugds with 50 bins → save/show]
        R5 --> R6[same again with log y axis]
    end
```

## discovery_notebook.ipynb

Same steps as `discovery.py`, but each step is its own cell so the plot appears right under the code that made it.
