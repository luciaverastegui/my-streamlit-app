import pandas as pd
import streamlit as st

selected_cryptocurrency = st.text_input("Enter cryptocurrency (i.e. BTC):")
currency = st.text_input("Enter fiat currency (i.e. EUR):")
threshold = st.number_input("Enter a threshold value (i.e. €300):",
                          min_value = 0 , max_value=999999999)

import requests
import json

headers = {
  'Accepts': 'application/json',
  'X-CMC_PRO_API_KEY': '...',
}

if selected_cryptocurrency and currency and threshold: 
    response = requests.get(f"https://pro-api.coinmarketcap.com/v2/cryptocurrency/quotes/latest?symbol={selected_cryptocurrency}&convert={currency}"
                        , headers=headers)
    
    if response.status_code in [200,201]:
        print("success")
        print(json.dumps(response.json(),indent=4))
    else:
        print(f"error {response.status_code} with error: {response.text}")
    
    price = response.json()["data"][selected_cryptocurrency][0]["quote"][currency]['price']
else:
    st.info("Check the fields and fill them all")


if st.button("Notify me"):
    st.write(f"The current price of {selected_cryptocurrency} is {price}{currency}. We will notify you when the {selected_cryptocurrency} reaches {threshold}{currency}.")



