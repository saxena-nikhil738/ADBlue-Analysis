import pandas as pd
import streamlit as st
from datetime import date
import preprocessor

def UploadFile():
    st.header('Upload File')
    uploaded_file = st.file_uploader("Upload a xlsx file", type=["xlsx"])

    if uploaded_file is not None:
        # Read the file into a pandas DataFrame
        new_filename = "ADBLUE_NEW_SHEET.xlsx"

        # Read the uploaded file into a pandas DataFrame
        df = pd.read_excel(uploaded_file)

        required_columns = ['Date', 'Vehicle no', 'Name', 'Adblue', 'Quantity (LTR)', 'KM', 'Avg']
        file_columns = df.columns.tolist()

        # Save the uploaded file with the new name
        if set(required_columns).issubset(df.columns.tolist()):
            with open(new_filename, "wb") as f:
                f.write(uploaded_file.getbuffer())

            # st.success(f"File has been renamed to {new_filename}")

            # Display the DataFrame
            st.write("File imported")
            # st.dataframe(df)

            if st.button('Upload'):
                df.to_excel("ADBLUE_NEW_SHEET.xlsx", index=False, engine='openpyxl')
                st.write('File uploaded successfully!')
                # st.write("Records shape : ", file_uploaded.shape)

        else:

            st.error("~Required attributes not found in uploaded file!")

            st.write("Required attributes")
            required_df = pd.DataFrame(columns=required_columns)
            st.dataframe(required_df)
            st.write('Uploaded attributes')
            required_df = pd.DataFrame(columns=file_columns)
            st.dataframe(required_df)