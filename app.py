import streamlit as st

from src.currency import CURRENCIES
from src.functions import get_exchange_rate, convert_currency

col1, col2 = st.columns(2)

with col1:
    base_currency = st.selectbox('Base Currency', CURRENCIES)
    target_currency = st.selectbox('Target Currency', CURRENCIES)

    target_value = get_exchange_rate(base_currency, target_currency)
    st.write(target_value, target_currency)

with col2:
    currency = st.selectbox('Currency', CURRENCIES)
    mount = st.number_input('Mount')
    finall_value = convert_currency(currency, mount)
    st.write(finall_value, 'USD')