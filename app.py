import streamlit as st
import pandas as pd
import preprocessor
from datetime import date

# df = pd.read_excel("ADBLUE_NEW_SHEET.xlsx")
df = preprocessor.preprocess()

st.sidebar.title("Analysis")


def updateRecord(new_row):
    updated_df = df.append(new_row, ignore_index=True)
    updated_df.drop_duplicates(inplace=True)

    # updating original file
    updated_df.to_excel("ADBLUE_NEW_SHEET.xlsx", index=False, engine='openpyxl')

    # returning file
    return updated_df

# filling options
Options = st.sidebar.radio(
    'Select an option',
    ('Overall analysis', 'Filling status', 'Last filling', 'Refill information', 'Fill now')
)

if Options == 'Overall analysis':
    st.dataframe(df)

if Options == 'Filling status':
    st.sidebar.header('Filling status')
    number = st.sidebar.text_input("Enter vehicle number")
    if number:
        # Filter DataFrame by vehicle number
        df_filtered = df[df['Vehicle no'] == number].sort_values('Date', ascending=False)

        # Display the filtered DataFrame
        if not df_filtered.empty:
            st.dataframe(df_filtered)
        else:
            st.write(f"No records found for vehicle number: {number}")
    else:
        st.write('Please enter vehicle number')


if Options == 'Last filling':
    st.sidebar.header('Last filling status')
    number = st.sidebar.text_input("Enter vehicle number")
    if number:
        # Filter DataFrame by vehicle number
        df_filtered = df[df['Vehicle no'] == number].sort_values('Date', ascending=False).head(1)

        # Display the filtered DataFrame
        if not df_filtered.empty:
            st.dataframe(df_filtered)
        else:
            st.write(f"No records found for vehicle number: {number}")
    else:
        st.write('Please enter vehicle number')

if Options == 'Refill information':
    st.sidebar.header('Refill information')
    flag = 0
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

    if df_last_updated.empty:
        flag = 1
        st.write(f"No records found for vehicle number: {number}")
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
        st.dataframe(result_df)

    else:
        if flag == 0 :
            st.write("Please enter vehicle number and kilimeters.")


if Options == 'Fill now':

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
        if st.button('Update'):
            updated_df = updateRecord(new_row)
            st.dataframe(updated_df)

    except ValueError as e:
        print(f"Error: {e}")

# st.dataframe(df)