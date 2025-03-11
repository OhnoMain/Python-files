import alpaca_trade_api as tradeapi
import numpy as np
import time
import logging
from datetime import datetime, timedelta

# Directly including API keys (replace with your actual keys)
SEC_KEY = 'mtnilqPENgS6bJ8VpMxnc7fZmEBoqe8WgDad5ktZ'
PUB_KEY = 'PK7G2ZEUCYEQOU1TYAM6'
BASE_URL = 'https://paper-api.alpaca.markets'

api = tradeapi.REST(key_id=PUB_KEY, secret_key=SEC_KEY, base_url=BASE_URL)

# Set up logging
logging.basicConfig(filename='trading_bot.log', level=logging.INFO, format='%(asctime)s - %(message)s')
logging.info('Bot started')

symb = "SPY"
pos_held = False

while True:
    try:
        print("\nChecking Price")
        
        end_time = datetime.now()
        start_time = end_time - timedelta(minutes=5)
        
        market_data = api.get_bars(symb, tradeapi.TimeFrame.Minute, start=start_time.isoformat(), end=end_time.isoformat()).df
        close_list = market_data['close'].values[-5:]
        close_list = np.array(close_list, dtype=np.float64)
        ma = np.mean(close_list)
        last_price = close_list[-1]

        print("Moving Average: " + str(ma))
        print("Last Price: " + str(last_price))
        
        if ma + 0.1 < last_price and not pos_held:
            print("Buy")
            api.submit_order(
                symbol=symb,
                qty=1,
                side='buy',
                type='market',
                time_in_force='gtc'
            )
            pos_held = True
            logging.info(f'Bought 1 share of {symb}')
        elif ma - 0.1 > last_price and pos_held:
            print("Sell")
            api.submit_order(
                symbol=symb,
                qty=1,
                side='sell',
                type='market',
                time_in_force='gtc'
            )
            pos_held = False
            logging.info(f'Sold 1 share of {symb}')
        
        time.sleep(60)
    except Exception as e:
        logging.error(f'Error occurred: {e}')
        time.sleep(60)  # Wait a minute before retrying
