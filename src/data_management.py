import streamlit as st
import pandas as pd
import numpy as np
import joblib

# this file is based on code found in the CI walkthrough projects
@st.cache(suppress_st_warning=True, allow_output_mutation=True)
def load_house_prices_data():
    df = pd.read_csv("outputs/datasets/collection/house_prices_records.csv")
    return df

@st.cache(suppress_st_warning=True, allow_output_mutation=True)
def load_inherited_data():
    df = pd.read_csv("inputs/datasets/raw/house-price-20211124T154130Z-001/house-price/inherited_houses.csv")
    return df


def load_pkl_file(file_path):
    return joblib.load(filename=file_path)