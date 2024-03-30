## AMES Heritage Housing

This is a machine learning app for house price visualisations and predictions in Ames, Iowa.

The app helps the client to do the following:
- View how house attributes correlate to sale prices.
- Predict future sale prices for specific houses.

You can view the App here [INSERT APP]

## Index
- [Business Requirements](#business-requirements)
- [Dataset Content](#dataset-content)
- [Hypothesis and validation](#hypothesis-and-validation)
- [The rationale to map the business requirements to the Data Visualisations and ML tasks](#the-rationale-to-map-the-business-requirements-to-the-data-visualisations-and-ml-tasks)
- [ML Business Case](#ml-business-case)
- [Dashboard Design](#dashboard-design)
- [Unfixed Bugs](#unfixed-bugs)
- [Deployment](#deployment)
    - [Heroku](#heroku)
    - [Main Data Analysis and Machine Learning Libraries](#main-data-analysis-and-machine-learning-libraries)
- [Credits](#credits)


## Business Requirements
The client has received an inheritance from a deceased great-grandfather located in Ames, Iowa. They have asked us to help in maximising the sales price for the inherited properties.

The client has an excellent understanding of property prices in her own state and residential area, she fears that basing her estimates for property worth on her current knowledge might lead to inaccurate appraisals. What makes a house desirable and valuable where she comes from might not be the same in Ames, Iowa. She found a public dataset with house prices for Ames, Iowa which we will use for this project.

* 1 - USER STORY 1: The client is interested in discovering how the house attributes correlate with the sale price. Therefore, the client expects data visualisations of the correlated variables against the sale price to show that.
* 2 - USER STORY 2: The client is interested in predicting the house sale price from her four inherited houses and any other house in Ames, Iowa. The predictive model should aim to achieve an R2 value of 0.8 or higher.
* 3 - USER STORY 3: Delivery of the final product in form of a deployed app that is easily accessible online and user friendly.

These requirements can also be viewed as the user stories of the client/end user.

## CRISP-DM Workflow

* 1. EPIC 1 - Business Understanding - extensive discussion with the client and their expectations as well as the development of acceptance criteria. These are layed out in the Business Requirements below.
* 2. EPIC 2 - Data Understanding - is the data needed to achieve the business requirements must be identified and understood. Are the data available to answer the business requirements? An initial statistical analysis helps to determine whether the data available are adequate to answer the business requirements. This task is carried out in the Data Cleaning Notebook.
* 3. EPIC 3 - Clean and impute data, carry out feature engineering, such as transformations or scaling, reformat data if needed. This step is very important to ensure the most effective and accurate modelling outcome. This is carried out in the Data Cleaning and Feature Engineering Notebooks.
* 4 EPIC 4 - Determine the model algorithms to be used. Split the data into train and test sets. Use train sets to validate various algorithms and add them using a hyperparamter search. 
* 5 EPIC 5 - Use the test set to evaluate the model performance. Match these with the business acceptance criteria.
* 6 EPIC 6 - Develop the streamlit app that will satisfy the business requirements determined in collaboration with the client and deploy the app online.

## Dataset Content
* The dataset is sourced from [Kaggle](https://www.kaggle.com/codeinstitute/housing-prices-data).
* The dataset has almost 1.5 thousand rows and represents housing records from Ames, Iowa, indicating house profile (Floor Area, Basement, Garage, Kitchen, Lot, Porch, Wood Deck, Year Built) and its respective sale price for houses built between 1872 and 2010.

|Variable|Meaning|Units|
|:----|:----|:----|
|1stFlrSF|First Floor square feet|334 - 4692|
|2ndFlrSF|Second-floor square feet|0 - 2065|
|BedroomAbvGr|Bedrooms above grade (does NOT include basement bedrooms)|0 - 8|
|BsmtExposure|Refers to walkout or garden level walls|Gd: Good Exposure; Av: Average Exposure; Mn: Minimum Exposure; No: No Exposure; None: No Basement|
|BsmtFinType1|Rating of basement finished area|GLQ: Good Living Quarters; ALQ: Average Living Quarters; BLQ: Below Average Living Quarters; Rec: Average Rec Room; LwQ: Low Quality; Unf: Unfinshed; None: No Basement|
|BsmtFinSF1|Type 1 finished square feet|0 - 5644|
|BsmtUnfSF|Unfinished square feet of basement area|0 - 2336|
|TotalBsmtSF|Total square feet of basement area|0 - 6110|
|GarageArea|Size of garage in square feet|0 - 1418|
|GarageFinish|Interior finish of the garage|Fin: Finished; RFn: Rough Finished; Unf: Unfinished; None: No Garage|
|GarageYrBlt|Year garage was built|1900 - 2010|
|GrLivArea|Above grade (ground) living area square feet|334 - 5642|
|KitchenQual|Kitchen quality|Ex: Excellent; Gd: Good; TA: Typical/Average; Fa: Fair; Po: Poor|
|LotArea| Lot size in square feet|1300 - 215245|
|LotFrontage| Linear feet of street connected to property|21 - 313|
|MasVnrArea|Masonry veneer area in square feet|0 - 1600|
|EnclosedPorch|Enclosed porch area in square feet|0 - 286|
|OpenPorchSF|Open porch area in square feet|0 - 547|
|OverallCond|Rates the overall condition of the house|10: Very Excellent; 9: Excellent; 8: Very Good; 7: Good; 6: Above Average; 5: Average; 4: Below Average; 3: Fair; 2: Poor; 1: Very Poor|
|OverallQual|Rates the overall material and finish of the house|10: Very Excellent; 9: Excellent; 8: Very Good; 7: Good; 6: Above Average; 5: Average; 4: Below Average; 3: Fair; 2: Poor; 1: Very Poor|
|WoodDeckSF|Wood deck area in square feet|0 - 736|
|YearBuilt|Original construction date|1872 - 2010|
|YearRemodAdd|Remodel date (same as construction date if no remodelling or additions)|1950 - 2010|
|SalePrice|Sale Price|34900 - 755000|

## Hypothesis and validation
* Hypothesis One: We believe that a property's sale price correlates strongly with the square footage with the square footage of property features and the overall quality of the home.
* Hypothesis One Findings: The correlation study of the dataset supports that. The correlation study confirmed this and showed that the sale price correlates most strongly with Overall Quality (OverallQual), GarageArea (GarageArea), Total Basement Area (TotalBsmtSF), 2ndFlrSF. These are all features which are common to most properties.
* Hypothesis Two: We hypothesize that we are able to predict a sale price with an R2 value of at least 0.8. The R2 analysis on the train and test sets confirms this.

## The rationale to map the business requirements to the Data Visualisations and ML tasks
As a client, I have the following requirements:

Business Requirement 1:

* I want to analyse the house records data to determine which variables have a significant impact on the sale price.
* I want to view the correlation coefficients on a heatmap to prioritize variables based on their importance for the sale price.
* I would like to plot the important variables against the sale price to visually understand their correlation.
Business Requirement 2:
* I need easy access and navigation of the inherited houses data to locate specific house attributes.
* I want an accurate ML model capable of predicting the prices of my four inherited houses in Ames, Iowa.
* I need that the ML model provides precise price predictions for any other house in Ames, Iowa.


## ML Business Case
What are the business requirements?
* The client is interested in discovering how house attributes correlate with sale prices. Therefore, the client expects data visualizations of the correlated variables against the sale price.
* The client is interested in predicting the house sale prices from her 4 inherited houses, and any other house in Ames, Iowa.

Is there any business requirement that can be answered with conventional data analysis?
* Yes, we can use conventional data analysis to investigate how house attributes are correlated with the sale prices.

Does the client need a dashboard or an API endpoint?
* The client needs a dashboard

What does the client consider as a successful project outcome?
* A study showing the most relevant variables correlated to sale prices
* capability to predict the sale price for the 4 inherited houses, as well as any other house in Ames, Iowa.

Can you break down the project into Epics and User Stories?
* Information gathering and data collection.
* Data visualization, cleaning, and preparation.
* Model training, optimization and validation.
* Dashboard planning, designing, and development.
* Dashboard deployment and release.

Ethical or Privacy concerns?
* No. The client found a public dataset.

Does the data suggest a particular model?
* The data suggests a regressor where the target is the sale price.

What are the model's inputs and intended outputs?
* The inputs are house attribute information and the output is the predicted sale price.

What are the criteria for the performance goal of the predictions?
* We agreed with the client on an R2 score of at least 0.75 on the train set as well as on the test set.

How will the client benefit?
* The client will maximize the sales price for the inherited properties.

## Dashboard Design
* Project Summary - This page describes the project, the dataset and the business requirements.
* Sale Price Analysis - This page displays visualisations of the correlation between the house attibutes and house sale prices. (Business Requirement 1)
* Sale Price Prediction - This page completes the two hypothesise. (Business Requirement 1 and 2)
* Hypothesis and Validation - This page completes the two hypothesise.
* ML: Sale Price Prediction - This page details the Machine Learning pipeline and the r2 performance

## Unfixed Bugs
* No unfixed bugs
* Warning - Data Cleaning - CalculateCorrandPPS - This warning is to show that there isnt a strong correlation

## Deployment
### Heroku
Heroku
The App live link is [Here](https://ames-heritage-housing-3d294e81d937.herokuapp.com/)
Heroku might need to be set to Stack 20
The project was deployed to Heroku using the following steps:
Set the runtime.txt Python version to python-3.9.18
Make a Heroku Procfile with runtime instuctions
Make a setup.sh file with Streamlit configuration settings
Create a requirements.txt with all libraries needed
Log in to Heroku and create an App
At the Deploy tab, select GitHub as the deployment method.
Select your repository name and click Search. Once it is found, click Connect.
Select the branch you want to deploy, then click Deploy Branch.
The deployment process should happen smoothly if all deployment files are fully functional. Click the button Open App on the top of the page to access your App.

### Main Data Analysis and Machine Learning Libraries
*(from requirements.txt)*<br>

numpy==1.18.5<br>
pandas==1.4.2<br>
matplotlib==3.3.1<br>
seaborn==0.11.0<br>
ydata-profiling==4.4.0<br>
plotly==4.12.0<br>
ppscore==1.2.0<br>

streamlit==0.85.0<br>

feature-engine==1.0.2<br>
imbalanced-learn==0.8.0<br>
scikit-learn==0.24.2<br>
xgboost==1.2.1<br>
yellowbrick==1.3<br>
Jinja2==3.1.1<br>
MarkupSafe==2.0.1<br>
protobuf==3.20<br>
ipywidgets==8.0.2<br>
altair<5<br>


## Credits 
* Most of the code was adapted from the Churnometer walkthrough project by the Code Institute.
* I have also had inspiration from the following projects:

[annacakes](https://github.com/annacakes281/property-price-predictor)
[knutinator](https://github.com/knutinator/heritage-housing)
[Uriem](https://github.com/URiem/heritage-housing-PP5)
[t-hullis](https://github.com/t-hullis/milestone-project-heritage-housing-issues)
[faridjos](https://github.com/faridjos/milestone-project-heritage-housing-issues)




