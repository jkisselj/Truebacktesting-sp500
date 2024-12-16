SP500 Backtesting Project
Project Overview

This project aims to perform a backtest on the SP500 constituents, representing the 500 largest companies by market capitalization in the United States. The goal is to preprocess the data, generate trading signals, and compare the performance of a stock-picking strategy with the SP500 benchmark.
Project Structure

project │ README.md │ requirements.txt │ └───data │ │ sp500.csv │ │ stock_prices.csv │ └───notebook │ │ analysis.ipynb │ └───scripts │ │ memory_reducer.py │ │ preprocessing.py │ │ create_signal.py │ │ backtester.py │ │ main.py │ │ init.py │ └───results │ plots │ results.txt │ outliers.txt

    Create a virtual environment and activate it:

    python -m venv env
    source env/bin/activate  # On Windows use `env\Scripts\activate`

   

Install the dependencies:

pip install -r requirements.txt

Running the Project

