import matplotlib.pyplot as plt
from run import predict
import numpy as np
from utils.get_parent_path import get_parent_path
from utils.prepare_data import prepare_lstm, prepare_data


def plot(x, y, title, xlabel, ylabel):
    plt.plot(x, y)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.show()


def plot_data(stock, start, model_type, predict_n=1):
    if predict_n > 1 and model_type == "joblib":
        print("Cannot predict more than 1 day with a joblib model")
        return
    x, y = prepare_data(stock, ['Open', 'High', 'Low', 'Close', 'Adj Close', 'Volume'], [1, 2, 3, 5, 6, 7, 8, 9, 10, 11, 12, 13], [4])

    x = x[start:]
    y = y[start:]

    # print files in this dir
    t_data = []
    # Add the data for the past n days including today.
    for i in range(int(x[-1][5]) - 9, int(x[-1][5]) + 1):
        t_data.append(x[i-start-1])

    print(t_data)

    if model_type == "joblib":
        scaler = None
    else:
        scaler = str(get_parent_path()) + f'/scalers/{stock}.save'

    pred = predict(str(get_parent_path()) + f'/models/{stock}.{model_type}', np.array([t_data]), scaler)
    x_plot = x[:, 5]

    future_x_plot = [x_plot[-1] + 1]
    future_y_plot = pred[0]

    plt.plot([float(x_plot[-1]), *future_x_plot], [float(y[-1]), *future_y_plot], color='red', label='Future Predictions')

    # create a line graph but all timestamps > x[-1][-1] are yellow

    plt.plot(x_plot, y, color='blue', label='Actual Data')
    plt.title(f'{stock} Stock Price')
    plt.xlabel('Days')
    plt.ylabel('Price')
    plt.legend()
    plt.show()


if __name__ == "__main__":
    plot_data(input(), int(input()), input())