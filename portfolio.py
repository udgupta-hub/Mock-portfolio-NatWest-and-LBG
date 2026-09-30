"""Mock portfolio tracker - learning exercise, not investment advice.
Equal-weight start, buy-and-hold, month-end prices, price-only.
Run: python portfolio.py
"""
import csv, statistics

prices = list(csv.DictReader(open("data/prices.csv")))
holdings = list(csv.DictReader(open("data/holdings.csv")))
months = [r["month"] for r in prices]

def series(t): return [float(r[t]) for r in prices]

units = {h["ticker"]: float(h["start_value_gbp"]) / series(h["ticker"])[0] for h in holdings}
port = [sum(units[t] * series(t)[i] for t in units) for i in range(len(months))]
bench_units = port[0] / series("FTSE100")[0]
bench = [bench_units * p for p in series("FTSE100")]

def rets(v): return [v[i] / v[i-1] - 1 for i in range(1, len(v))]
def max_dd(v):
    peak, worst = v[0], 0
    for x in v:
        peak = max(peak, x); worst = min(worst, x / peak - 1)
    return worst

print(f"{'':10}{'Start':>10}{'End':>10}{'Return':>9}{'Worst mth':>11}{'Max DD':>9}{'Mth SD':>8}")
def row(name, v):
    r = rets(v)
    print(f"{name:10}{v[0]:>10,.0f}{v[-1]:>10,.0f}{v[-1]/v[0]-1:>9.1%}{min(r):>11.1%}{max_dd(v):>9.1%}{statistics.stdev(r):>8.1%}")
for h in holdings:
    t = h["ticker"]; row(t, [units[t] * p for p in series(t)])
print("-" * 57)
row("PORTFOLIO", port); row("FTSE 100", bench)
gain = port[-1] - port[0]
print("\nShare of total gain by holding:")
for h in holdings:
    t = h["ticker"]; g = units[t] * series(t)[-1] - float(h["start_value_gbp"])
    print(f"  {t:5}{g:>8,.0f}  ({g/gain:.0%})")
