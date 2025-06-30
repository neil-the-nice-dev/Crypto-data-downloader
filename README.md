# Cryptocurrency Historical Data Fetcher 

This repository contains a Python script that allows users to fetch historical OHLCV (Open, High, Low, Close, Volume) data for cryptocurrencies from Binance, both for the **Spot** and **Futures** markets. The user can choose the market type, trading pair, and timeframe through input prompts.

## Features

- Fetch historical data for **Spot** or **Futures** markets.
- Choose any trading pair available on Binance (e.g., **BTC/USDT**).
- Select the desired timeframe (e.g., **1m**, **5m**, **1h**, **1d**).
- Save the fetched data to a CSV file for further analysis.

## Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/yourusername/Cryptocurrency-Historical-Data-Fetcher.git
    ```

2. **Install the required packages:**

    ```bash
    pip install ccxt pandas

    ```

## Usage

Run the script using Python:

```bash
python fetch_data.py
```


## OUTPUT :

```bash

Choose the market type (spot/futures): spot

Enter the trading pair symbol (e.g., BTC/USDT): BTC/USDT

Enter the timeframe (e.g., 1m, 5m, 1h, 1d): 1d

Do you want to save the data to CSV? (yes/no): yes

Retrieved 1000 candles for BTC/USDT
Retrieved 2000 candles for BTC/USDT
Retrieved 2087 candles for BTC/USDT

Data for BTC/USDT:
DateTime        Open        High         Low       Close        Volume
2022-01-01  46206.4375  47813.6670  45556.3989  47722.8294  46377.424080
2022-01-02  47722.8294  47800.5637  46826.6468  47250.4769  37250.472650
2022-01-03  47250.4769  47532.5591  45894.3174  46400.1234  48200.562390
2022-01-04  46400.1234  46800.1237  45500.1231  45800.1237  50200.123450
2022-01-05  45800.1237  47000.1234  45600.1234  46700.1234  52200.123450

Do you want to save the data to CSV? (yes/no): yes

Data saved to BTC_USDT_spot_1d.csv
```
