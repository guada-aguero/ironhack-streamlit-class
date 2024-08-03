import requests
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import fetch_california_housing

# Load our data

@st.cache_data #streamlit python decorator that allows us to store the data and not need to reload/re-run it every single time.
def load_data():
    """ 
    Function that loads and store data
    """

    cali = fetch_california_housing()
    data = pd.DataFrame(cali.data, columns = cali.feature_names)
    data['MedianHouseValue'] = cali.target

    data.columns = [col.lower() for col in data.columns]

    return data

data = load_data()


# Page 1: DataFrame showcase and add interactivity with plots
def page1():
    """
    Function that encapsulates page 1's logic:
    - Displays dataframe
    - Displays map chart
    - Allows user interactivity
    """
    st.title("Califotnia Housing Prices Dataset")
    st.write(" ## Dataframe showcase")
    st.dataframe(data)

    # Map plot:
    st.write("Map plot of housing in California")
    st.map(data[['latitude','longitude']])

    # Scatter plot:
    x_axis = st.selectbox("Choose a variable for the x-axis",data.columns)
    y_axis = st.selectbox("Choose a variable for the y-axis",data.columns)

    plt.figure(figsize=(10,6))
    plt.scatter(data[x_axis], data[y_axis], alpha=0.5)
    plt.title(f"Scatter plot of {x_axis} by {y_axis}:")
    plt.xlabel(x_axis)
    plt.ylabel(y_axis)
    st.pyplot(plt)

if __name__ == '__main__':
    page1()