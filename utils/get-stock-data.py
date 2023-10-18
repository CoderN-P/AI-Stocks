import yfinance as yf
import pandas as pd
import datetime

# Define the stock symbol and date range
stock_symbol = input()
start_date = "2010-01-01"
end_date = datetime.date.today().strftime("%Y-%m-%d")

# Fetch the historical stock data
stock_data = yf.download(stock_symbol, start=start_date, end=end_date)

# Convert the data to a CSV file
stock_data.to_csv(f"./stock_data/{stock_symbol}.csv")

# Create a new column in the CSV file
# This column will contain the number of market days since 2010-01-01
# This will be used to create lag features
df = pd.read_csv(f"./stock_data/{stock_symbol}.csv")
df["days"] = df.index
df.to_csv(f"./stock_data/{stock_symbol}.csv", index=False)


