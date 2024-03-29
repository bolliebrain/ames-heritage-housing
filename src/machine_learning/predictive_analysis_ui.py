import streamlit as st

def predict_sale_price(X_live, house_features, sale_price_pipeline):

	# from live data, subset features related to this pipeline
	X_live_sale_price = X_live.filter(house_features)

	# predict
	sale_price_prediction = sale_price_pipeline.predict(X_live_sale_price)

	# create a logic to display the results
	price = float(sale_price_prediction.round(0))
	price = '${:,.2f}'.format(price)
	statement = (
		f'### With the values given, we estimate this house to be worth {price[0]} '
	)

	st.write(statement)
		
	st.write(sale_price_prediction)