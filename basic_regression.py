import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import xgboost as xgb
from joblib import dump, load
from sklearn.metrics import r2_score
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler


def trainRegression(stock):
    s = f'./{stock}.csv'
    DF = pd.read_csv(s)

    # Specify columns for which you want to create lag features
    columns_to_lag = ['Open', 'High', 'Low', 'Close', 'Adj Close', 'Volume']

    # Create lag features for selected columns
    for column in columns_to_lag:
        DF[f'{column}_lag'] = DF[column].shift(1)

    DF = DF.drop(0)

    X = DF.to_numpy()[:, [7, 8, 9, 10, 11, 12, 13]]
    y = DF.to_numpy()[:, 4]

    model = xgb.XGBRegressor()

    """
    scaler = StandardScaler()
    X_train = scaler.fit_transform(X_train)
    x_test_data = scaler.transform(X_test)
    """
    # Fit the model to the data (find the coefficients)
    model.fit(X, y)
    dump(model, f'{stock}.joblib')
    return model


if __name__ == "__main__":
    trainRegression(input())