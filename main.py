# -*- coding: utf-8 -*-
"""
Created on Mon Nov 20 21:32:52 2017

@author: sky_x
"""
import pandas as pd
from os import listdir
import matplotlib.pyplot as plt
import numpy as np
from sklearn.preprocessing import MinMaxScaler

# Getting data
listdir("./data")
data = pd.read_csv("./data/data_stocks.csv")
n, p = data.shape

# Plot
data.columns
plt.plot(data.SP500)

# Split training & test data
train_start = 0
train_end = int(np.floor(0.8*n))
test_start = train_end + 1
test_end = n
data_train = data.iloc[np.arange(train_start, train_end), :]
data_test = data.iloc[np.arange(test_start, test_end), :]

# Data scaling
scaler = MinMaxScaler()
scaler.fit(data_train)
scaler.transform(data_train)
scaler.transform(data_test)

# Dependent & Independent variables
X_train = data_train.iloc[:, 2:]
y_train = data_train.iloc[:, 1]
X_test = data_test.iloc[:, 2:]
y_test = data_test.iloc[:, 1]