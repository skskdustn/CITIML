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
import input
from input import *


def ml_module():

    ml_model = LinearRegression()
    ml_model.fit(input.x_trainset, input.y_trainset)
    ml_accuracy = ml_model.score(input.x_testset, input.y_testset)
    return ml_accuracy

