from sklearn.preprocessing import MinMaxScaler

from utils.generate_lag import generate_lag
import pandas as pd
from pathlib import Path
import numpy as np


def prepare_data(stock, lag_features, train_features, test_features):
    # Get absolute path to CSV file

    csv_path = Path(__file__).parent.parent / f'stock_data/{stock}.csv'
    DF = pd.read_csv(csv_path)
    DF = generate_lag(DF, lag_features)

    X = DF.to_numpy()[:, train_features].astype(float)
    y = DF.to_numpy()[:, test_features].astype(float)

    return X, y


def prepare_lstm(stock, lag_features, train_features, test_features, num_timesteps):
    csv_path = Path(__file__).parent.parent / f'stock_data/{stock}.csv'
    DF = pd.read_csv(csv_path)

    DF = generate_lag(DF, lag_features)

    X = DF.to_numpy()[:, train_features].astype(float)
    y = DF.to_numpy()[:, test_features].astype(float)

    x = []
    for i in range(0, X.shape[0] - num_timesteps):
        l = []
        for j in range(0, num_timesteps):
            l.append(X[i + j])
        x.append(l)

    x = np.array(x)

    return x, y
