from joblib import dump

def store_model(model, stock):
    dump(model, f'./models/{stock}.joblib')
    return model