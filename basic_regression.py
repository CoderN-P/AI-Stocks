import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import xgboost as xgb
from joblib import dump, load
from sklearn.metrics import r2_score
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from hyperparameter_tuning import xgb_param_grid, tune


# NVDA: OrderedDict([('colsample_bytree', 0.7), ('gamma', 0.0), ('learning_rate', 0.1), ('max_depth', 5), ('min_child_weight', 2), ('n_estimators', 200), ('objective', 'reg:squarederror'), ('reg_alpha', 0.5), ('reg_lambda', 1.0), ('subsample', 0.8)])
# AAPL: OrderedDict([('colsample_bytree', 0.8), ('gamma', 0.2), ('learning_rate', 0.1), ('max_depth', 7), ('min_child_weight', 3), ('n_estimators', 200), ('objective', 'reg:squarederror'), ('reg_alpha', 0.5), ('reg_lambda', 0.5), ('subsample', 1.0)])
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

    best_params = tune(xgb_param_grid, X, y)
    print(best_params)

    new_model = xgb.XGBRegressor(**best_params)

    # Fit the model to the data (find the coefficients)
    new_model.fit(X, y)
    dump(new_model, f'{stock}.joblib')
    return new_model


if __name__ == "__main__":
    trainRegression(input())