import logging
import matplotlib.pyplot as plt
import os
import pandas as pd
def backtest(prices, sp500):
    logging.info('Backtesting beggining strategy')
    dates = prices.index.get_level_values('Date').unique()
    results = pd.DataFrame(index=dates)
    results['strategy'] = 0
    results['benchmark'] = sp500.loc[dates, 'monthly_return'].values
    for date in dates:
        signals = prices.loc[date, 'signal']
        
        if not isinstance(signals, pd.Series):
            signals = pd.Series(signals, index=prices.loc[date].index)
        if not signals.any():
            continue
        selected_stocks = signals[signals].index
        monthly_returns = prices.loc[date, selected_stocks].filter(like='monthly_future_return')
        
        if not monthly_returns.empty:
            results.loc[date, 'strategy'] = monthly_returns.mean().mean()
    results['strategy_cum'] = (1 + results['strategy']).cumprod()
    results['benchmark_cum'] = (1 + results['benchmark']).cumprod()
    
    results.to_csv('results/results.txt')
    
    # Graphic building
    plt.figure(figsize=(10, 6))
    plt.plot(results.index, results['strategy_cum'], label='Strategy')
    plt.plot(results.index, results['benchmark_cum'], label='S&P 500')
    plt.xlabel('Date')
    plt.ylabel('Cumulative Return')
    plt.title('Strategy vs S&P 500')
    plt.legend()
    plt.grid(True)
    
    # directory existing prof
    os.makedirs('results/plots', exist_ok=True)
    plt.savefig('results/plots/performance_plot.png')
    plt.close()
    
    logging.info('Завершение бэктестинга стратегии')
    return results
