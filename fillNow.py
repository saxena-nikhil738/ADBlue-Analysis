import pandas as pd
import streamlit as st
from datetime import date
import preprocessor

def FillNow():
    df = preprocessor.preprocess()
    st.header('Fill new record')
    st.sidebar.header('Fill required details')

    # Get today's date
    today = date.today()

    # Form validation for input fields
    def validate_vehicle_no(number):
        if not number:
            raise ValueError("Vehicle number is required.")
        return number

    def validate_driver_name(name):
        if not name.strip():
            raise ValueError("Driver name cannot be empty.")
        return name

    def validate_adblue(adblue):
        if not adblue.strip():
            raise ValueError("Adblue name cannot be empty.")
        return adblue

    def validate_quantity(quantity):
        if quantity <= 0:
            raise ValueError("Quantity must be a positive integer.")
        return quantity

    def validate_kms(kms):
        if not kms.isdigit() or int(kms) <= 0:
            raise ValueError("Kilometers must be a positive integer.")
        return int(kms)

    def validate_avg(avg):
        if avg < 0:
            raise ValueError("Average cannot be negative.")
        return avg

    # Input values with validation

    try:
        number = st.sidebar.text_input("Enter Vehicle no: ")
        number = validate_vehicle_no(number)

        name = st.sidebar.text_input("Driver name: ")
        name = validate_driver_name(name)

        adblue = st.sidebar.text_input("Adblue name: ")
        adblue = validate_adblue(adblue)

        quantity = int(st.sidebar.text_input("Enter quantity: "))
        quantity = validate_quantity(quantity)

        kms = st.sidebar.text_input("Enter current kms: ")
        kms = validate_kms(kms)

        avg = int(st.sidebar.text_input("Enter avg kms: "))
        avg = validate_avg(avg)

        # If validation passes, print the information
        flag = 1

        new_row = pd.DataFrame({
            'Date': [today],
            'Vehicle no': [number],
            'Name': [name],
            'Adblue': [adblue],
            'Quantity (LTR)': [quantity],
            'KM': [kms],
            'Avg': [avg]
        })

        if new_row.empty:
            st.write('Please enter required details')
        else:
            st.write('Your entered details')

        st.dataframe(new_row)
        st.write("Records shape : ", new_row.shape)
        if st.button('Update'):
            updated_df = pd.concat([df, row], ignore_index=True)
            updated_df.drop_duplicates(inplace=True)
            # updating original file
            updated_df.to_excel("ADBLUE_NEW_SHEET.xlsx", index=False, engine='openpyxl')
            st.dataframe(updated_df)
            st.write('Record shape', updated_df.shape)

    except ValueError as e:
        print(f"Error: {e}")
