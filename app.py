import streamlit as st
from app_pages.multipage import MultiPage

from app_pages.page_summary import page_summary_body
from app_pages.page_sales_price_analysis import page_sales_price_analysis_body
from app_pages.page_predict_price import page_predict_price_body
from app_pages.page_hypothesis import page_project_hypothesis_body
from app_pages.page_predict_price_ml import page_predict_price_ml_body

app = MultiPage(app_name= "Ames Heritage Housing")
app.add_page("Project Summary", page_summary_body)
app.add_page("Sale Price Correlation Analysis", page_sales_price_analysis_body)
app.add_page("Sale Price Prediction", page_predict_price_body)
app.add_page("Hypothesis and Validation", page_project_hypothesis_body)
app.add_page("ML: Sale Price Prediction", page_predict_price_ml_body)

app.run() # Run the  app