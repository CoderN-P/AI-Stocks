from skopt import BayesSearchCV
import xgboost as xgb

xgb_param_grid = {
    'n_estimators': [100, 200, 300],  # Number of boosting rounds
    'learning_rate': [0.01, 0.1, 0.2, 0.3],  # Step size shrinkage to prevent overfitting
    'max_depth': [3, 4, 5, 6, 7],  # Maximum depth of a tree
    'min_child_weight': [1, 2, 3],  # Minimum sum of instance weight (hessian) needed in a child
    'subsample': [0.7, 0.8, 0.9, 1.0],  # Fraction of samples used for each boosting round
    'colsample_bytree': [0.7, 0.8, 0.9, 1.0],  # Fraction of features used for each boosting round
    'gamma': [0, 0.1, 0.2, 0.3],  # Minimum loss reduction required to make a further partition
    'reg_alpha': [0, 0.1, 0.5, 1.0],  # L1 regularization term on weights
    'reg_lambda': [0, 0.1, 0.5, 1.0],  # L2 regularization term on weights
    'objective': ['reg:squarederror'],  # Regression task
}

lstm = {
    'n_lstm_units': [50, 100, 150],  # Number of LSTM units (neurons) in the layer
    'n_lstm_layers': [1, 2, 3],  # Number of LSTM layers
    'dropout': [0.0, 0.2, 0.5],  # Dropout rate to prevent overfitting
    'batch_size': [16, 32, 64],  # Mini-batch size for training
    'learning_rate': [0.001, 0.01, 0.1],  # Learning rate for optimization
    'epochs': [50, 100, 200],  # Number of training epochs
}


def tune(param_grid, X, y, model):
    # Run bayes search
    bayes_cv_tuner = BayesSearchCV(
        estimator=model,
        search_spaces=lstm,
        scoring='r2',
        cv=5,
        n_jobs=-1,
        n_iter=40,
        verbose=0,
        refit=True,
        random_state=42
    )

    result = bayes_cv_tuner.fit(X, y)

    return result.best_params_