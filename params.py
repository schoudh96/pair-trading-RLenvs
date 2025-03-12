import pandas as pd
from utils.read2df import read2df
from datetime import datetime, timedelta

'''
Download historical data for `symbols` after `start_date` with selected `freqs` from [`binance-public-data`](https://github.com/binance/binance-public-data/tree/master/python)
We will train data from `start_date` until `trade_date`, and start trade after `trade_date`.
'''

symbols = ['BTCUSDT', 'BTCGBP', 'BTCEUR']

date_format = '%Y-%m-%d'
start_date = '2023-10-01'
trade_date = '2023-12-01'
end_date = '2023-12-31'

# freqs = {'1m': 1, '3m':3, '5m':5, '15m':15, '30m':30, '1h':60, '2h':120, '4h':240, '6h':360, '8h':480, '12h':720, '1d':1440}
# Because we want as much data as possible, it makes sense to use only 1m
freqs = {'1m': 1, '3m':3, '5m':5}