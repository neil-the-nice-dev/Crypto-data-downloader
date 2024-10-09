import ccxt
import pandas as pd
from datetime import datetime, timedelta


market_type = input("Choose the market type (spot/futures): ").strip().lower()


if market_type == 'spot':
    exchange = ccxt.binance()
elif market_type == 'futures':
    exchange = ccxt.binance({
        'options': {
            'defaultType': 'future',
        },
    })
else:
    print("Invalid market type selected.")
    exit()


symbol = input("Enter the trading pair symbol (e.g., BTC/USDT): ").strip().upper()
timeframe = input("Enter the timeframe (e.g., 1m, 5m, 1h, 1d): ").strip()


def get_historical_data(exchange, symbol, timeframe='1d', limit=1000, start_time=None):
    all_data = []
    

    if start_time is None:

        start_time = exchange.parse8601('2022-01-01T00:00:00Z')
    
    while True:
        try:
            ohlcv = exchange.fetch_ohlcv(symbol, timeframe=timeframe, since=start_time, limit=limit)
        except Exception as e:
            print(f"An error occurred: {e}")
            break
        
        if len(ohlcv) == 0:
            break  
        
        all_data += ohlcv
        start_time = ohlcv[-1][0] + 1  
        print(f"Retrieved {len(all_data)} candles for {symbol}")

    data = pd.DataFrame(all_data, columns=['DateTime', 'Open', 'High', 'Low', 'Close', 'Volume'])
    data['DateTime'] = pd.to_datetime(data['DateTime'], unit='ms')
    
    return data

data = get_historical_data(exchange, symbol, timeframe=timeframe)

print(f"Data for {symbol}:")
print(data.head())

save_to_csv = input("Do you want to save the data to CSV? (yes/no): ").strip().lower()

if save_to_csv == 'yes':
    filename = symbol.replace("/", "_") + f"_{market_type}_historical_data.csv"
    data.to_csv(filename, index=False)
    print(f"Data saved to {filename}")