import logging
import pandas as pd
import numpy as np
def preprocess_prices(prices):
    logging.info('Price data processing beggining')
    # Transform'Date' to datetime and insert index
    prices['Date'] = pd.to_datetime(prices['Date'])
    prices.set_index('Date', inplace=True)
    # Resample data on month and keep the last value
    prices = prices.resample('M').last()
    # Filter prices outliers: Remove prices outside the range 0.1$, 10k$
    prices = prices[(prices >= 0.1) & (prices <= 10000)]
    # Compute monthly returns
    monthly_past_return = prices.pct_change()
    monthly_future_return = prices.pct_change(-1)
    # Identify and replace return outliers
    outlier_condition = (monthly_future_return > 1) | (monthly_future_return < -0.5)
    monthly_future_return[outlier_condition] = np.nan
    monthly_future_return.fillna(method='ffill', inplace=True)
    # Concatenate new columns
    prices = pd.concat([prices, monthly_past_return.add_suffix('_monthly_past_return'), monthly_future_return.add_suffix('_monthly_future_return')], axis=1)
    logging.info('Price data processing done')
    return prices
def preprocess_sp500(sp500):
    logging.info('Data processing beggining SP500')
    # Transform 'Date' вto datetime and insert index
    sp500['Date'] = pd.to_datetime(sp500['Date'])
    sp500.set_index('Date', inplace=True)
    # Resample data on month and keep the last value
    sp500 = sp500.resample('M').last()
    # Compute historical monthly returns on the adjusted close
    sp500['monthly_return'] = sp500['Adjusted Close'].pct_change().fillna(0)
    logging.info('Data processing done SP500')
    return sp500
