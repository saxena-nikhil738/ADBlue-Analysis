import pandas as pd
import streamlit as st
from datetime import date
import preprocessor



def updateOneRecord():
    df = preprocessor.preprocess()
    vNumber = st.sidebar.text_input("Enter vehicle number: ")
    st.header(f'Recoreds for vehicle:  {vNumber}')
    df_filtered = df[df['Vehicle no'] == vNumber].sort_values('Date', ascending=False)
    st.dataframe(df_filtered)
    st.write("Records shape : ", df_filtered.shape)

    if not df_filtered.empty:
        st.header("Specify date to update")
        date = st.date_input("Date")
        df_filtered = df[
            (df['Vehicle no'] == vNumber) & (df['Date'] == date)
            ].sort_values('Date', ascending=False)

        if not df_filtered.empty:
            name = df_filtered['Name'].iloc[0]
            adblue = df_filtered['Adblue'].iloc[0]
            quantity = df_filtered['Quantity (LTR)'].iloc[0]
            kms = df_filtered['KM'].iloc[0]
            avg = df_filtered['Avg'].iloc[0]
            st.write('You are updating this record')
            st.dataframe(df_filtered)

            # Placeholder for name
            st.header('Enter updation details')
            newName = st.text_input(label="Name", placeholder=name) or name
            newAdblue = st.text_input(label="Adblue", placeholder=adblue) or adblue
            newQuantity = st.text_input(label="Quantity", placeholder=quantity) or quantity
            newKMs = st.text_input(label="KM", placeholder=kms) or kms
            newAvg = st.text_input(label="Avg", placeholder=avg) or avg

            # st.write(f"Name entered: {newName}")

            st.header('Updated record')
            new_df = pd.DataFrame({
                'Date': [date],
                'Vehicle no': [vNumber],
                'Name': [newName],
                'Adblue': [newAdblue],
                'Quantity (LTR)': [newQuantity],
                'KM': [newKMs],
                'Avg': [newAvg]
            })

            st.dataframe(new_df)
            st.write("Records shape : ", new_df.shape)

            if st.button('Update'):
                st.write('Record updated successfully!')
                df = df.drop(df[(df['Vehicle no'] == vNumber) & (df['Date'] == date)].index)
                df = pd.concat([df, new_df], ignore_index=True)
                df.to_excel('ADBLUE_NEW_SHEET.xlsx', index=False, engine='openpyxl')
                df_filtered = df[df['Vehicle no'] == vNumber]
                st.dataframe(df_filtered)
                st.write("Records shape : ", df_filtered.shape)
                # st.dataframe(df)

        else:
            st.write('No records found for specified date.')
