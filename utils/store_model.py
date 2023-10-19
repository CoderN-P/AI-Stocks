from pathlib import Path

from joblib import dump

from utils.get_parent_path import get_parent_path


def store_model(model, stock, type):
    if type == "h5":
        model_path = get_parent_path() / f'models/{stock}.h5'
        model.save(model_path)

    elif type == "joblib":
        model_path = get_parent_path() / f'models/{stock}.{type}'
        dump(model, model_path)
    return model