import streamlit as st

query = st.text_input('Query', placeholder='Enter a search term')

if query:
    st.write([query])