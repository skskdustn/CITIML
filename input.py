# CITIML module
#
#
# ver 0
# powered by skskdustn
# ---------------------------------------

# using module
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# inside module


class data:

    def xtrain():
        return pd.read_csv('/Users/skskdustn/Downloads/citydata/x_trainset.csv'
                           , encoding='utf-8'
                           , sep='\t')

    def ytrain():
        return pd.read_csv('/Users/skskdustn/Downloads/citydata/y_trainset.csv'
                           , encoding='utf-8'
                           , sep='\t')


    def xtest():
        return pd.read_csv('/Users/skskdustn/Downloads/citydata/x_testset.csv'
                           , encoding='utf-8'
                           , sep='\t')

    def ytest():
        return pd.read_csv('/Users/skskdustn/Downloads/citydata/y_testset.csv'
                           , encoding='utf-8'
                           , sep='\t')


x_train_data = data.xtrain()
y_train_data = data.ytrain()
x_test_data = data.xtest()
y_test_data = data.ytest()

x_trainset = x_train_data.to_numpy()
y_trainset = y_train_data.to_numpy()
x_testset = x_test_data.to_numpy()
y_testset = y_test_data.to_numpy()

# ppu  : population per unit(area)
# gpp  : grdp(Gross regional domestic product) per one(person)
# fi   : financial independence
# eppu : estate price per unit(area)

