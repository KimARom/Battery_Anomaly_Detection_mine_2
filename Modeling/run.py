import os
import sys
import pandas as pd
from preprocessing import *
from preprocessing2 import *
from Inference1 import *
import streamlit as st

def load_data(file_name):
    # file_list = os.listdir("./Data")
    # file = [file for file in file_list if str(data_num) in file]
    # df_dir = "./Data/" + file[0]
    return pd.read_csv('./Dashboard/test.csv')

def calculate_score(df_test, file_name):
    preprocess = PreprocessPipe()
    df = preprocess.fit_transform(df_test)
    X, index = time_segments_aggregate(df, interval = 1, time_column = 'date')
    X = simple_minmax(X)
    X, y, X_index, y_index = rolling_window_sequences(X, index, window_size = 10,   target_size = 1, step_size =1, target_column=0)
    y_hat, critic = predict(X)
    final_result = anomaly(X, y_hat, critic, X_index)
    final_result["file_name"] = file_name
    final_result.to_csv("./Dashboard/result.csv")
    # open('./Dashboard/result.csv', 'w').write(final_result.to_csv())

file_name = sys.argv[1]
df_test = load_data(file_name)
calculate_score(df_test, file_name)
