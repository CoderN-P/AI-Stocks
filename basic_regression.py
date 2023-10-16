import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler


def calculate_date_difference(row):
    date = row['Date']
    return (date - pd.Timestamp('2010-01-01')).days

stock = input()
data = list(map(float, input().split(',')))

s = f'./{stock}.csv'
DF = pd.read_csv(s, parse_dates=['Date'])
DF['date'] = DF.apply(calculate_date_difference, axis=1)

# Specify columns for which you want to create lag features
columns_to_lag = ['Open', 'High', 'Low', 'Adj Close', 'Volume']

# Create lag features for selected columns
for column in columns_to_lag:
    DF[f'{column}_lag'] = DF[column].shift(1)


DF = DF.drop(0)

X = DF.to_numpy()[:, [7, 8, 9, 10, 11, 12]]
y = DF.to_numpy()[:, 4]

X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=42)

model = LinearRegression()

"""
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
x_test_data = scaler.transform(X_test)
"""
# Fit the model to the data (find the coefficients)
model.fit(X, y)

# Get predictions

predicted_y_values = model.predict(np.array([data]))

print(predicted_y_values)
