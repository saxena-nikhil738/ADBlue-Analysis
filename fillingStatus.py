import streamlit as st
import pandas as pd
import preprocessor


def FillingStatus():
    df = preprocessor.preprocess()
    st.header('Filling status')
    st.sidebar.header('Filling status')
    number = st.sidebar.text_input("Enter vehicle number")
    if number:
        # Filter DataFrame by vehicle number
        df_filtered = df[df['Vehicle no'] == number].sort_values('Date', ascending=False)

        # Display the filtered DataFrame
        if not df_filtered.empty:
            st.dataframe(df_filtered)
            st.write("Records shape : ", df_filtered.shape)
        else:
            st.write(f"No records found for vehicle number: {number}")
    else:
        st.write('Please enter vehicle number')