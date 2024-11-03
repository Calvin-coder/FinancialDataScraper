import yfinance as yf
import pandas as pd

def get_historical_data(stock_symbol, start_date, end_date):
    # Download historical stock data
    stock_data = yf.download(stock_symbol, start=start_date, end=end_date)
    
    # Save the data to a DataFrame
    df = pd.DataFrame(stock_data)
    return df


stock_symbol = "AAPL"  # Example: Apple's stock symbol
start_date = "2020-01-01"  # Start date for historical data
end_date = "2024-01-01"  # End date for historical data

df = get_historical_data(stock_symbol, start_date, end_date)
print(df)
