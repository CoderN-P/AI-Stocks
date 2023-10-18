from collections import OrderedDict

import xgboost as xgb

from utils.hyperparameter_tuning import xgb_param_grid, tune
from utils.prepare_data import prepare_data
from utils.store_model import store_model

NVDA = OrderedDict([('colsample_bytree', 0.7), ('gamma', 0.0), ('learning_rate', 0.1), ('max_depth', 5), ('min_child_weight', 2), ('n_estimators', 200), ('objective', 'reg:squarederror'), ('reg_alpha', 0.5), ('reg_lambda', 1.0), ('subsample', 0.8)])
AAPL = OrderedDict([('colsample_bytree', 0.8), ('gamma', 0.2), ('learning_rate', 0.1), ('max_depth', 7), ('min_child_weight', 3), ('n_estimators', 200), ('objective', 'reg:squarederror'), ('reg_alpha', 0.5), ('reg_lambda', 0.5), ('subsample', 1.0)])
WMT = OrderedDict([('colsample_bytree', 0.7), ('gamma', 0.1), ('learning_rate', 0.1), ('max_depth', 4), ('min_child_weight', 2), ('n_estimators', 200), ('objective', 'reg:squarederror'), ('reg_alpha', 0.0), ('reg_lambda', 0.1), ('subsample', 0.8)])

# [177.09044]


def trainRegression(stock):
    TRAIN = [7, 8, 9, 10, 11, 12, 13]
    LAG = ['Open', 'High', 'Low', 'Close', 'Adj Close', 'Volume']
    RESULT = 4
    X, y = prepare_data(stock, LAG, TRAIN, RESULT)

    if stock == 'NVDA':
        best_params = NVDA
    elif stock == 'AAPL':
        best_params = AAPL
    else:
        best_params = tune(xgb_param_grid, X, y)
        print(best_params)
    new_model = xgb.XGBRegressor(**best_params)

    # Fit the model to the data (find the coefficients)
    new_model.fit(X, y)
    store_model(new_model, stock)
    return new_model


if __name__ == "__main__":
    trainRegression(input())