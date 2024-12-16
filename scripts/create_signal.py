import logging
def create_signal(prices):
    logging.info('create signals')
    
    # create row average_return_1y
    prices['average_return_1y'] = prices.filter(like='monthly_past_return').mean(axis=1)
    
    # create row signal
    signal = prices.groupby(prices.index)['average_return_1y'].transform(lambda x: x >= x.nlargest(20).min())
    prices['signal'] = signal
    
    logging.info('create signals done')
    return prices
