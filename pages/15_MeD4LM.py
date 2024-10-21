import streamlit as st
import pandas as pd
import numpy as np

st.title('Upload Excel File')

DATA_DIR = "MLLM Dataset.xlsx"

@st.cache_data
def load_data(nrows):
    data = pd.read_excel(DATA_DIR, nrows=nrows)
    data.index += 1
    return data

data = load_data(68)

if st.checkbox('Show raw data'):
    st.subheader('Raw data')
    st.write(data)