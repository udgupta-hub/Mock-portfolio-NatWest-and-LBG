# Mock Portfolio + Bank Comparison (learning exercise)

**Not investment advice.** This is a classroom-style exercise using past prices.

## 1. NatWest vs Lloyds Banking Group (calendar years 2023-2025)

| | 2023 | 2024 | 2025 |
|---|---|---|---|
| **NatWest** total income | ~£14.7bn* | £14,703m | £16,641m |
| NatWest operating profit before tax | ~£6.2bn* | £6,195m | £7,708m |
| NatWest profit as % of income | ~42%* | 42.1% | 46.3% |
| **Lloyds** net income (underlying) | ~£18.0bn* | £17,117m | £18,301m |
| Lloyds underlying profit | ~£7.8bn* | £6,343m | £6,777m |
| Lloyds underlying profit as % of net income | ~43%* | 37.1% | 37.0% |
| Lloyds statutory profit before tax | ~£7.5bn | £5,971m | £6,661m |

\*2023 figures for NatWest are back-calculated from reported 2024 changes (income -0.3%, profit +0.3%); Lloyds 2023 net income is back-calculated from the reported 5% fall in 2024. Treat as approximate.

**Why these figures:** income shows scale, profit shows what is left after costs and bad-loan charges, and profit as a % of income is the bank version of profit margin (it is 100% minus the cost:income ratio, less impairments).

**What it shows:** NatWest grew income 13% and profit 24% in 2025; Lloyds grew income 7% and underlying profit 7%. NatWest keeps more of each pound of income as profit.

**What it can't show:**
- The two define income and profit differently: Lloyds' net income is after operating lease depreciation and it reports "underlying" profit; NatWest reports total income and operating profit.
- Lloyds' 2024-25 profit was hit by a charge for motor finance commission arrangements; NatWest had no equivalent.
- Lloyds has a large insurance and leasing business; NatWest has none of the same size.
- Nothing here covers capital strength, return on equity, or share price value.

## 2. Mock portfolio

- Start: £10,000 (£2,000 each), buy-and-hold, month-end prices, **price only** (no dividends; VHVG is an accumulating fund so its price already includes reinvested income).
- Period: 30 Sep 2025 to 30 Jun 2026 (chosen because all six price series cover it).
- Holdings: Tesco, NatWest, Lloyds, BP, Vanguard FTSE Developed World fund.
- Benchmark: FTSE 100 index, same start value.
- Prices from digrin.com monthly history pages. Re-check against an official source before relying on them.

| | Return | Worst month | Max drawdown |
|---|---|---|---|
| Tesco | 3.0% | -10.8% | -10.8% |
| NatWest | 27.9% | -10.6% | -16.8% |
| Lloyds | 32.5% | -9.9% | -15.2% |
| BP | 9.7% | -10.6% | -23.0% |
| Vanguard Developed World | 17.3% | -5.9% | -5.9% |
| **Portfolio** | **18.1% (£11,807)** | -2.3% | -2.3% |
| **FTSE 100** | **12.3% (£11,226)** | -6.7% | -6.7% |

### What to learn from it
- **Diversification worked on volatility:** single holdings fell up to 23% from a peak, but the portfolio's worst month was -2.3%, because they did not all fall together.
- **It was less diversified than it looks:** NatWest and Lloyds were 40% of the money but 67% of the gain. If banks had fallen, the result would be very different.
- **Five UK-heavy holdings are not the market.** Beating the index over nine months says little about skill; a concentrated bet paid off here.
- **Hindsight warning:** I picked these knowing which were popular in 2025-26. A real test would fix holdings before the period starts.
- Monthly data hides big moves inside each month, and nine months is a very short window.

## Run it
```
python portfolio.py
```
Edit `data/holdings.csv` and `data/prices.csv` to try other holdings or dates.
