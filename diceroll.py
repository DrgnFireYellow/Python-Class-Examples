import streamlit as st
import random

st.write("Welcome to Dice Roll!")

sides = st.slider("Choose a number of sides", 2, 20)

def roll_dice():
    st.write(random.randint(1, sides))

st.button("Roll The Dice", on_click=roll_dice)