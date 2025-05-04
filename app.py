import streamlit as st

from src.currency import CURRENCIES
from src.functions import get_exchange_rate, convert_currency

st.title('Currency Converter')
col1, col2 = st.columns(2)

with col1:
    st.subheader('Exchange Rate')
    base_currency = st.selectbox('Base Currency', CURRENCIES)
    target_currency = st.selectbox('Target Currency', CURRENCIES)

    exchange_rate = get_exchange_rate(base_currency, target_currency)
    st.write('1', base_currency, '=', exchange_rate, target_currency)

with col2:
    st.subheader('Convert to USD')
    from_currency = st.selectbox('from_currency', CURRENCIES)
    amount = st.number_input('Amount')
    final_value = convert_currency(from_currency, amount)
    st.write(amount, from_currency, '=', final_value, 'USD')