import yfinance as yf
import pandas as pd
import datetime
from utils.get_parent_path import get_parent_path

# Define the stock symbol and date range

def get_stock_data(stock_symbol):
    start_date = "2010-01-01"
    end_date = datetime.date.today().strftime("%Y-%m-%d")

    # Fetch the historical stock data
    stock_data = yf.download(stock_symbol, start=start_date, end=end_date)

    # Convert the data to a CSV file
    parent_path = str(get_parent_path())
    CSV_PATH = parent_path+f"/stock_data/{stock_symbol}.csv"
    stock_data.to_csv(CSV_PATH)

    # Create a new column in the CSV file
    # This column will contain the number of market days since 2010-01-01
    # This will be used to create lag features
    df = pd.read_csv(CSV_PATH)
    df["days"] = df.index
    df.to_csv(CSV_PATH, index=False)

if __name__ == "__main__":
    get_stock_data(input())
