import streamlit as st
import pandas as pd
import preprocessor

def LastFilling():
    df = preprocessor.preprocess()
    st.header('Last filling')
    st.sidebar.header('Last filling status')
    number = st.sidebar.text_input("Enter vehicle number")
    if number:
        # Filter DataFrame by vehicle number
        df_filtered = df[df['Vehicle no'] == number].sort_values('Date', ascending=False).head(1)

        # Display the filtered DataFrame
        if not df_filtered.empty:
            st.dataframe(df_filtered)
            st.write("Records shape : ", df_filtered.shape)
        else:
            st.write(f"No records found for vehicle number: {number}")
    else:
        st.write('Please enter vehicle number')