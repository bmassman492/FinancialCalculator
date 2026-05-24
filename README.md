# Financial Planner Powered by Monte Carlo Simulation

## Overview

This repository contains Python scripts with the calculations behind a **Debt vs. Investment Decision Driver**. It is meant to inform those who have assumed debt and are looking to maximize future net worth by correctly choosing between:

1. **Investing first** — while debt accumulates, in the hopes that compound growth will outweigh compound interest accumulation.
2. **Paying off debt first** — then investing as soon as debt is paid off, to minimize compound interest accumulation.

## How It Works

The Python script (found at `standalone_script/crystalBallCalculator.py`) is a terminal-based script that prompts users for basic information regarding their debt and anticipated investment type.

A Monte Carlo simulation with a hardcoded number of scenarios is run (typically 10,000 to 1,000,000).

Say the user has specified that they want to invest for the next **Y** years in large-cap stocks, anticipating a yearly average return of 12.2%. As a historical fact, large-cap stock yearly returns have a standard deviation of 19.7%.

1. A random z-score within a normal distribution is generated (e.g., `z = 1.2`).
2. The z-score is multiplied by the investment standard deviation and added to the anticipated mean return (`12.2 + 1.2 × 19.7 = 35.84`). This is the first year's return in the simulated scenario.
3. This is repeated **Y** times, resulting in a full array of yearly returns.
4. The future value of the user's initial investment is calculated after it has experienced all **Y** returns. Then, the accumulated loan principal and interest is subtracted. This account value is compared to the estimated account value from paying off debt immediately and investing afterwards. The net benefit (+ or −) of investing first is returned.
5. This net invest-first benefit is aggregated over all simulation scenarios to inform the user's financial decision over many thousands of realistic futures.

## Prerequisites

- [Python](https://www.python.org/)
- [NumPy](https://numpy.org/)
- [numpy-financial](https://numpy.org/numpy-financial/)

## Installation

```bash
pip install numpy numpy-financial
```

## Usage

```bash
cd standalone_script
python crystalBallCalculator.py
```
