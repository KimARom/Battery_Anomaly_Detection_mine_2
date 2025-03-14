import pandas as pd
import os, sys
import streamlit as st

def load_data(file_name):
    # file_list = os.listdir("./Data")
    # file = [file for file in file_list if str(data_num) in file]
    # df_dir = "./Data/" + file[0]
    return pd.read_csv('./Dashboard/test.csv')

def save_uploaded_file(directory, file):
    if not os.path.exists(directory):
        os.makedirs(directory)
    
    with open(os.path.join(directory, 'test.csv'), 'wb') as f:
        f.write(file.getbuffer())
    return st.success('파일 업로드 성공!')
