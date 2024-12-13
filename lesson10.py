import streamlit as st

def on_click_button():
    st.write("Hi")

num = st.slider("Choose a number")
text = st.text_input("Choose some words")

st.write("Hello there, this is a test. " + str(num) +  " " + text)

st.button("Click me please", on_click=on_click_button)