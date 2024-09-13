import pandas as pd
import streamlit as st
from datetime import date
import preprocessor

def Refilling():
    df = preprocessor.preprocess()
    st.header('Refill information')
    st.sidebar.header('Refill information')

    # Input for vehicle number and kilometers
    number = st.sidebar.text_input("Enter vehicle number")
    kms_input = st.sidebar.text_input("Enter vehicle km")

    # Convert kilometers input to integer
    try:
        kms = int(kms_input)
    except ValueError:
        kms = None
        # st.sidebar.write("Please enter a valid number for kilometers.")

    # Filter the dataframe for the latest entry based on vehicle number
    df_last_updated = df[df['Vehicle no'] == number].sort_values('Date', ascending=False).head(1)

    if not df_last_updated.empty and kms is not None:
        # Extract the first values and convert them
        v_no = df_last_updated['Vehicle no'].iloc[0]  # Get the first value
        adb = df_last_updated['Adblue'].iloc[0]  # Get the first value
        qnty = df_last_updated['Quantity (LTR)'].iloc[0]  # Get the first value
        km = int(df_last_updated['KM'].iloc[0])  # Convert to integer
        avg = float(df_last_updated['Avg'].iloc[0])  # Convert to float

        # Calculate expected and remaining kms
        expected_kms = km + avg
        remaining_kms = expected_kms - kms

        # Create a DataFrame for displaying the results
        result_df = pd.DataFrame({
            'Description': ['Vehicle Number', 'Adblue', 'Quantity Filled', 'Kilometers', 'Average Value',
                            'Expected Kms to Refill', 'Remaining Kms to Refill'],
            'Value': [v_no, adb, qnty, km, avg, expected_kms, remaining_kms]
        })

        # Display the results as a table
        if result_df.shape[0] == 0:
            st.write(f"No records found for vehicle number: {number}")
        else:
            st.dataframe(result_df)
            st.write("Records shape : ", result_df.shape)

    else:
        st.write("Please enter vehicle number and kilimeters.")