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

# from tqdm import tqdm

# inside module


def comparison_prediction(actual_price, predicted_price):

    plt.scatter(actual_price, predicted_price, alpha=0.4)
    plt.xlabel("Actual Price")
    plt.ylabel("Predicted Price")
    plt.title("MULTIPLE LINEAR REGRESSION")
    plt.show()

