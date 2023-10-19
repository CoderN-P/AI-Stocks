from utils.generate_lag import generate_lag
import pandas as pd
from pathlib import Path


def prepare_data(stock, lag_features, train_features, test_features):
    # Get absolute path to CSV file

    csv_path = Path(__file__).parent.parent / f'stock_data/{stock}.csv'
    DF = pd.read_csv(csv_path)
    DF = generate_lag(DF, lag_features)

    X = DF.to_numpy()[:, train_features].astype(float)
    y = DF.to_numpy()[:, test_features].astype(float)
    return X, y