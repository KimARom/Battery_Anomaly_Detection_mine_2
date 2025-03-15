import os, sys
import pandas as pd

path = '/Dashboard/result.csv'
path_2 = '/Dashboard/test.csv'

def result_true():
    return os.path.exists(path)

def load_result():
    return pd.read_csv(path)

def remove_result():
    os.remove(path)
    os.remove(path_2)
    