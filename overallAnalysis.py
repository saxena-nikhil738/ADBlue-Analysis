import streamlit as st
import pandas as pd
import preprocessor

def OverallAnalysis():
    df = preprocessor.preprocess()
    st.header('Overall analysis')
    st.dataframe(df)
    st.write("Records shape : ", df.shape)