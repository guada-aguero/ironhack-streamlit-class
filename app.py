import requests
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import fetch_california_housing
from my_pages import (
    page_home as home,
    page_california_datasets as page1,
    page_location_information as page2,
    page_weather_information as page3
)

# sidebar element:    
st.sidebar.title("Navigation Bar")

page = st.sidebar.selectbox(
    "Select a page",
    [
     "🏠 Home", 
     "🏡 California Housing Prices", 
     "🌍 Location Information", 
     "☀️ Weather Information", 
     ]
                            )



if page == "🏠 Home":
    # The first home refers to the name of the file, and the last one is the name of the function within the file
    home.home()
elif page  == "🏡 California Housing Prices":
    page1.page1()
elif page == "🌍 Location Information":
    page2.page2()
else:
    page3.page3()
