import yfinance as yf
import pandas as pd

# Define the stock symbol and date range
stock_symbol = "NVDA"
start_date = "2010-01-01"
end_date = "2023-10-14"

# Fetch the historical stock data
stock_data = yf.download(stock_symbol, start=start_date, end=end_date)

# Convert the data to a CSV file
stock_data.to_csv("NVDA.csv")

# Change the date in the csv to a number
