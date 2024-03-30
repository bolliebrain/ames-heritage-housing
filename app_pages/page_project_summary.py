import streamlit as st
import pandas as pd

def page_project_summary():
    
    st.write("#### Project Summary")

    st.info(
        f"**Background information:**\n\n"
        f"You have been requested by your friend, who has received\n"
        f"an inheritance from a deceased great-grandfather located in\n"
        f"Ames, Iowa, to help in maximising the sales price for\n"
        f"the inherited properties.\n\n"
        f"Although your friend has an excellent understanding of property prices\n"
        f"in her own state and residential area, she fears that basing her\n"
        f"estimates for property worth on her current knowledge might lead to\n"
        f"inaccurate appraisals.\n"
        f"What makes a house desirable and valuable where she comes from might\n"
        f"not be the same in Ames, Iowa.\n"
        f"She found a public dataset with house prices for Ames, Iowa,\n"
        f"and will provide you with that.\n\n"
        f"**Quick Summary**:\n\n"
        f"*This is a sales prediction app that will predict property prices in\n"
        f"Ames, Iowa, based on certain features, as well as predict the\n"
        f"inherited house prices.*\n\n"
        f"**About the Dataset:**\n\n"
        f"The dataset has almost 1.5 thousand rows and represents housing\n"
        f"records from Ames, Iowa, indicating house profile (Floor Area,\n"
        f"Basement, Garage, Kitchen, Lot, Porch, Wood Deck, Year Built)\n"
        f"and its respective sale price for houses built\n"
        f"between 1872 and 2010.\n\n"
        f"Click on the Kaggle link to view the dataset content\n"
        f"[Kaggle](https://www.kaggle.com/datasets/codeinstitute/housing-prices-data)")

    # link to readme
    st.write(
        f"For any additional information, please visit and\n"
        f"**read**:\n"
        f"[Project README](https://github.com/bolliebrain/ames-heritage-housing/blob/main/README.md)"
    )

    # business requirements taken from readme
    st.success(
        f"The project contains ** 2 Business Requirements**:\n"
        f"* 1 - The client is interested in discovering how the house attributes\n"
        f"correlate with the sale price.\n"
        f"Therefore, the client expects data visualisations of\n"
        f"the correlated variables against the sale price to show that.\n\n"
        f"* 2 - The client is interested in predicting the house sale price\n"
        f"from her four inherited houses and any other house in Ames, Iowa."
    )