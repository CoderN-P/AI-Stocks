from joblib import load
import numpy as np
from keras.models import load_model
from sklearn.preprocessing import MinMaxScaler

from utils.prepare_data import prepare_data


def predict(file, lag_data, scaler1=None):
    if file.split('.')[-1] == 'joblib':
        model = load(file)
        res = model.predict(lag_data)
    else:
        model = load_model(file)
        scaler = load(scaler1)
        p = model.predict(lag_data)[0]
        p = [[float(i)] for i in p]
        p = np.array(p, dtype='float64')
        res = scaler.inverse_transform(p)
        print(res)

    return res


def main():
    stock = input()
    lag_data = input().split(',')
    lag_data = [float(i) for i in lag_data]
    scaler = input()
    print(predict(stock, [lag_data]))

if __name__ == "__main__":
    main()


