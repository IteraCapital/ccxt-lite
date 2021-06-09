
"""
# -- --------------------------------------------------------------------------------------------------- -- #
# -- ccxt-lite - A light-weighted python wrapper of ccxt library for historical information              -- #
# -- --------------------------------------------------------------------------------------------------- -- #
# -- Description: it is user friendly wrapper of ccxt for historical information retrieval               -- #
# -- main.py: python script with main method                                                             -- #
# -- Author: IFFranciscoME - if.francisco.me@gmail.com                                                   -- #
# -- license: GPL-3.0 License                                                                            -- #
# -- Repository: https://github.com/IteraCapital/ccxt-lite                                               -- #
# -- --------------------------------------------------------------------------------------------------- -- #
"""

# -- Load libraries for script
import os

# -- Load other scripts
import functions as fn

# Load from environment variables two tokens
s1 = os.environ['K1']
s2 = os.environ['K2']

p_class = fn.ini_binance(p_s1=s1, p_s2=s2)
p_ini_date = '2021-03-01 00:00:00'
p_end_date = '2021-03-22 23:59:00'
p_asset = 'ETH/USDT'
p_freq = '1m'
p_verbose = True

# -- RUN ONLY IF YOU WANT TO FETCH A LARGE HISTORICAL DATA
df_prices = fn.massive_ohlcv(p_class, p_ini_date, p_end_date, p_asset, p_freq, p_verbose)
