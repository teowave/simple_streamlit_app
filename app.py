#create a simple streamlit app

import streamlit as st
import pandas as pd

st.title("My first streamlit app")

name = st.text_input("Enter your name", '')
st.write(f"Hello {name}!")

x = st.slider("Select an integer", 1, 100)
y = st.slider("Select another integer", 1, 100)

#put it in a dataframe
df = pd.DataFrame({'x': [x], 'y': [y], 'x+y': [x+y]}, index=["addition row"])
st.write(df)
