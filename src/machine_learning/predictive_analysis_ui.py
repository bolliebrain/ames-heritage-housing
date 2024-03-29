import streamlit as st

def predict_sale_price(X_live, property_features, sale_price_pipeline):
    # live data
    X_live_sale_price = X_live.filter(property_features)

    # predict
    sale_price_prediction = sale_price_pipeline.predict(X_live_sale_price)

    statement = (
        f"* Given the features provided for the property, the model has "
        f"  predicted a sale value of:"
    )
    # Format the value written to the page
    # Formating learned from
    # https://github.com/t-hullis/milestone-project-heritage-housing-issues/tree/main
    if len(sale_price_prediction) == 1:
        price = float(sale_price_prediction.round(1))
        price = '${:,.2f}'.format(price)

        st.write(statement)
        st.write(f"**{price}**")
    else:
        st.write(
            f"* Given the features provided for the inherited properties, "
            f" the model has predicted sale values of:")
        st.write(sale_price_prediction)

    return sale_price_prediction