import streamlit as st


def page_project_hypothesis():

    st.write("### Project Hypothesis and Validation")

    st.success(
        f"**Hypothesis One:**\n\n"
        f"* We believe that a property's sale price correlates strongly"
        f" with the square footage of property features" 
        f" and the overall quality of the home. \n\n"
        f"  * The correlation study of the dataset supports that. \n\n"
        f"  * The correlation study confirmed this and showed that the "
        f" sale price correlates most strongly with Overall Quality "
        f" (OverallQual), Groundlevel Living area (GrLivArea), Garage "
        f" Area (GarageArea), Total Basement Area (TotalBsmtSF), "
        f" These are all features which are common to most "
        f" properties. \n\n"

        f"**Hypothesis Two:**\n\n"
        f"* We hypothesize that we are able to predict a sale price with an "
        f" R2 value of at least 0.8.\n\n"
        f"  * The R2 analysis on the train and test sets confirms this."
    )