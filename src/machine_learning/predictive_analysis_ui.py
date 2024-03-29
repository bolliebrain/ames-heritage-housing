import streamlit as st

def predict_sale_price(X_live, property_features, sale_price_pipeline):

	# from live data, subset features related to this pipeline
	X_live_sale_price = X_live.filter(property_features)

	# predict
	sale_price_prediction = sale_price_pipeline.predict(X_live_sale_price)

	# create a logic to display the results
	price = sale_price_prediction
	value = float(price.round(1))
	amount = '${:,.2f}'.format(value)
	statement = (
		f'### We estimate this house to be worth {amount} '
	)

	st.write(statement)
		
	st.write(price)