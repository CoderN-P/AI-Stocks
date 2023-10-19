from pathlib import Path
import csv
import yfinance
import datetime
import pandas_market_calendars as mcal
from basic_regression import trainRegression
from utils.get_parent_path import get_parent_path


def get_stock_today(stock_symbol, start_date, end_date):
    # get length of csv file
    # get last date in csv file
    csv_path = get_parent_path() / f'stock_data/{stock_symbol}.csv'
    lis = list(csv.reader(open(csv_path)))
    prev = int(lis[-1][-1])

    stock_data = yfinance.download(stock_symbol, start=start_date, end=end_date)

    # Add new column to stock data
    stock_data['days'] = prev + 1
    # remove column headers

    f = open(csv_path, 'a')
    f.write(stock_data.to_csv().split('\n', 1)[1])
    f.close()


def main():
    # Check if the market is open today
    today = datetime.date.today()
    yesterday = today - datetime.timedelta(days=1)
    tomorrow = today + datetime.timedelta(days=1)
    nyse = mcal.get_calendar('NYSE')

    if today != nyse.valid_days(start_date=today, end_date=today)[0].to_pydatetime().date():
        print("The market is closed today.")
        return

    stocks = input().split(',')

    for stock in stocks:
        get_stock_today(stock, today, tomorrow)
        trainRegression(stock)


if __name__ == "__main__":
    main()

