import streamlit as st
from app_pages.multipage import MultiPage

from app_pages.page_project_summary import page_project_summary
from app_pages.page_sales_price_analysis import page_sales_price_analysis
from app_pages.page_predict_price_ml import page_predict_price_ml
from app_pages.page_predict_price_prediction import page_sale_price_prediction
from app_pages.page_project_hypothesis import page_project_hypothesis

app = MultiPage(app_name= "Ames Heritage Housing")

app.add_page("Project Summary", page_project_summary)
app.add_page("Sale Price Analysis", page_sales_price_analysis)
app.add_page("Sale Price Prediction", page_sale_price_prediction)
app.add_page("Hypothesis and Validation", page_project_hypothesis)
app.add_page("ML: Sale Price Prediction", page_predict_price_ml)

app.run() # Run the  app