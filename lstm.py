from keras.src.losses import MeanSquaredError
from keras.src.metrics import RootMeanSquaredError
from keras.src.optimizers import Adam
from keras.models import Sequential
from keras.layers import LSTM, Dense
from keras.callbacks import EarlyStopping
from keras.layers import InputLayer
import numpy as np
# Read the data
from sklearn.preprocessing import MinMaxScaler

from utils.get_parent_path import get_parent_path
from utils.prepare_data import prepare_lstm
from keras.models import Sequential
from utils.store_model import store_model
from joblib import dump


def main(stock):
    TRAIN = [1, 2, 3, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    LAG = ['Open', 'High', 'Low', 'Close', 'Adj Close', 'Volume']
    RESULT = 4

    X, y = prepare_lstm(stock, LAG, TRAIN, RESULT, 10)
    y = y[10:]
    y = y.reshape(-1, 1)
    y = np.array(y, dtype='float')

    scaler = MinMaxScaler()
    y = scaler.fit_transform(y)

    scaler_path = str(get_parent_path()) + f'/scalers/{stock}.save'
    dump(scaler, scaler_path)
    model = Sequential()
    model.add(LSTM(50, input_shape=X.shape[1:], return_sequences=False))
    model.add(Dense(1))
    model.compile(loss='mean_squared_error', optimizer='adam')

    # Train the model
    model.fit(X, y, epochs=100, batch_size=64, verbose=1)

    store_model(model, stock, "h5")

    print('Completed')


if __name__ == "__main__":
    main(input())
