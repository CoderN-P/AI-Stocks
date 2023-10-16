from joblib import dump, load


def predict(stock_symbol, lag_data):
    model = load(f'{stock_symbol}.joblib')
    return model.predict(lag_data)


def main():
    stock = input()
    lag_data = input().split(',')
    lag_data = [float(i) for i in lag_data]
    print(predict(stock, [lag_data]))

if __name__ == "__main__":
    main()


