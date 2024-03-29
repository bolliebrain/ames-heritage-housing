import pandas as pd
import numpy as np
import streamlit as st
from src.data_management import load_house_prices_data
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style("whitegrid")


def page_sales_price_analysis():

    # load data
    df = load_house_prices_data()
    # The variable most strongly correlated with Sale Price/target
    
    vars_to_study = ['1stFlrSF', 'GarageArea', 'GrLivArea', 'OverallQual', 'TotalBsmtSF', 'YearBuilt']

    st.info("### Property Sale Price Analysis")
    st.success(
        f"* The client is interested in understanding the correlation "
        f" between a property's attributes/features and the sale price."
        f" Therefore, the client expects data visualization of the correlated"
        f" variables against the sale prices for illustration "
        f" (Business Requirement 1), \n"
    )

    # inspect data
    if st.checkbox("Inspect Sale Price Dataset"):
        st.write(
            f"* The dataset has {df.shape[0]} rows and {df.shape[1]} columns, "
            f"find below the first 15 rows.")
        st.write(df.head(15))

    st.write("---")

    st.info("### Correlation Study")
    # Correlation Study Summary
    st.info(
        f"As per the clients request, a correlatiom study was\n"
        f"performed to better understand how the attributes\n"
        f"are correlated to sale prices.\n\n"
        f"The study concluded that the most correlated\n"
        f"variables were: **{vars_to_study}**"
        )

    # code copied from sales price study notebook
    df_eda = df.filter(vars_to_study + ['SalePrice'])

    if st.checkbox("Sale Price Study Visualizations"):
        sale_price_per_var(df_eda, vars_to_study)

        # copied from house sales analysis notebook
        st.write(
            f"Findings:\n"
            f"* The correlation analysis suggests that the the ground floor living area\n"
            f"(GrLivArea), first floor area (1stFlrSF), basement (TotalBsmtSF),\n"
            f"and garage area (GarageArea) strongly influence the SalePrice of a house.\n"
            f"* The analysis also suggets that the year of the house (YearBuilt),\n"
            f"and quality of materials used/finishes (OverallQual)\n"
            f"have a moderate influence on the (SalePrice) of a house.\n\n"
            f"**These findings match our hypothesis we made.**"
        )

def sale_price_per_var(df_eda, vars_to_study):
    target_var = 'SalePrice'

    for col in vars_to_study:
        if df_eda[col].dtype == 'object':
            plot_catgorical(df_eda, col, target_var)
            st.write("\n\n")
        else:
            plot_numerical(df_eda, col, target_var)
            st.write("\n\n")

def plot_categorical(df_eda, col, target_var):

    plt.figure(figsize=(8, 5))
    sns.regplot(data=df_eda, x=col, y=target_var, order=df_eda[col].value_counts().index)
    plt.xticks(rotation=90)
    plt.title(f"{col}", fontsize=20)
    plt.show()

def plot_numerical(df, col, target_var):

    fig, axes = plt.subplots(figsize=(15,8))
    sns.regplot(data=df, x=col, y=target_var)
    plt.title(f"{col}", fontsize=20)
    st.pyplot(fig)