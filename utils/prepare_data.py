from utils.generate_lag import generate_lag
import pandas as pd

def prepare_data(stock, lag_features, train_features, test_features):
    DF = pd.read_csv(f'./stock_data/{stock}.csv')
    DF = generate_lag(DF, lag_features)

    X = DF.to_numpy()[:, train_features].astype(float)
    y = DF.to_numpy()[:, test_features].astype(float)
    return X, y