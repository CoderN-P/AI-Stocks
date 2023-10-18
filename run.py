from joblib import load
from keras.models import load_model


def predict(file, lag_data):
    if file.split('.')[-1] == 'joblib':
        model = load(file)
    else:
        model = load_model(file)
    return model.predict(lag_data)


def main():
    stock = input()
    lag_data = input().split(',')
    lag_data = [float(i) for i in lag_data]
    print(predict(stock, [lag_data]))

if __name__ == "__main__":
    main()


