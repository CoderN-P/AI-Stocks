from keras.src.losses import MeanSquaredError
from keras.src.metrics import RootMeanSquaredError
from keras.src.optimizers import Adam
from keras.models import Sequential
from keras.layers import LSTM, Dense
from keras.callbacks import EarlyStopping
from keras.layers import InputLayer

# Read the data
from utils.prepare_data import prepare_data
from keras.models import Sequential, save_model



def main(stock):
    TRAIN = [7, 8, 9, 10, 11, 12, 13]
    LAG = ['Open', 'High', 'Low', 'Close', 'Adj Close', 'Volume']
    RESULT = 4

    X, y = prepare_data(stock, LAG, TRAIN, RESULT)

    # split data into train and validation
    X_val = X[-30:]
    y_val = y[-30:]
    X = X[:-30]
    y = y[:-30]

    model1 = Sequential()
    print(X_val.shape)
    model1.add(InputLayer(input_shape=(X.shape[-1], 1)))
    model1.add(LSTM(100, return_sequences = True))
    model1.add(LSTM(100, return_sequences = True))
    model1.add(LSTM(50))
    model1.add(Dense(8, activation = 'relu'))
    model1.add(Dense(1, activation = 'linear'))

    model1.summary()

    early_stop = EarlyStopping(monitor='val_loss', patience=2)

    model1.compile(loss=MeanSquaredError(),
                   optimizer=Adam(learning_rate=0.0001),
                   metrics=RootMeanSquaredError())

    model1.fit(X, y,
               validation_data=(X_val, y_val),
               epochs=50,
               callbacks=[early_stop])

    save_model(model1, f'./models/{stock}.h5')

    print('Completed')


if __name__ == "__main__":
    main(input())
