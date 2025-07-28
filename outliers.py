import streamlit as st
import pandas as pd
import numpy as np

st.title("Outliers in Data")

df = pd.read_csv("C:/Users/acer/Documents/kiran-python/data.csv")
st.dataframe(df)
method=st.selectbox("Which Way do u want?",
                    ["IQR Method","Median Max Method"])
st.write(method,"Steps:")
if method=="IQR Method":
    st.write('1- Calculate Q1 (25th percentile) and Q3 (75th percentile)')
    colum=st.text_input("Enter Column")


    if st.button("apply"):
        Q3=df[colum].quantile(0.75)
        Q1=df[colum].quantile(0.25)
        IQR=Q3-Q1
        st.write(IQR)
        st.session_state["Q1"] = Q1
        st.session_state["Q3"] = Q3
        st.session_state["IQR"] = IQR   
    if "IQR" in st.session_state and st.button("Get Lower Limit"):
        lower_limit = st.session_state["Q1"] - 1.5 * st.session_state["IQR"]
        st.write("Lower Limit =", lower_limit)

    if "IQR" in st.session_state and st.button("Get Upper Limit"):
        upper_limit = st.session_state["Q3"] + 1.5 * st.session_state["IQR"]
        st.write("Upper Limit =", upper_limit)
    if st.button("Show Outliers"):
        Q1 = df[colum].quantile(0.25)
        Q3 = df[colum].quantile(0.75)
        IQR = Q3 - Q1
        lower_limit = Q1 - 1.5 * IQR
        upper_limit = Q3 + 1.5 * IQR

        outliers = df[(df[colum] < lower_limit) | (df[colum] > upper_limit)]
        st.write("IQR:",IQR)
        st.write("Lower Limit:", lower_limit)
        st.write("Upper Limit:", upper_limit)
        st.write("Outliers:")
        st.dataframe(outliers)

elif method == "Median Max Method":
    colum = st.text_input("Enter Column Name for Median-Max Method")
    if st.button("Find Outliers (Median-Max Method)"):
            median = df[colum].median()
            maximum = df[colum].max()
            threshold = median * 1.5    
    
            outliers = df[df[colum] > threshold]

            st.write("Median:", median)
            st.write("Maximum:", maximum)
            st.write("Threshold (Median × 1.5):", threshold)
            st.write("Outliers:")
            st.dataframe(outliers)        