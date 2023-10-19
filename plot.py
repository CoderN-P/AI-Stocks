import matplotlib.pyplot as plt
from run import predict
from utils.get_parent_path import get_parent_path
from utils.prepare_data import prepare_data
from scipy.interpolate import interp1d


def plot(x, y, title, xlabel, ylabel):
    plt.plot(x, y)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.show()


def plot_data(stock, start, model_type):
    x, y = prepare_data(stock, [], [1, 2, 3, 4, 5, 6, 7], [4])

    x = x[start:]
    y = y[start:]
    # print files in this dir
    prev = x[:, [1, 2, 3, 4, 5, 6]][-1]

    prev = [x[-1][-1] + 1, *prev]

    pred = predict(str(get_parent_path()) + f'/models/{stock}.{model_type}', [prev])
    x_plot = x[:, 6]

    future_x_plot = [x_plot[-1] + 1]
    future_y_plot = [pred[0]]

    plt.plot([float(x_plot[-1]), float(future_x_plot[0])], [float(y[-1]), float(future_y_plot[0])], color='red', label='Future Predictions')

    # create a line graph but all timestamps > x[-1][-1] are yellow

    plt.plot(x_plot, y, color='blue', label='Actual Data')
    plt.title(f'{stock} Stock Price')
    plt.xlabel('Days')
    plt.ylabel('Price')
    plt.legend()
    plt.show()


if __name__ == "__main__":
    plot_data(input(), int(input()), input())
