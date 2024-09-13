import streamlit as st
import pandas as pd
import fillingStatus
import overallAnalysis
import preprocessor
from datetime import date
import lastFilling
import refilling
import updateRecord
import uploadXlsxFile
import fillNow

# df = pd.read_excel("ADBLUE_NEW_SHEET.xlsx")
df = preprocessor.preprocess()

st.sidebar.title('Menu options')
selectOptions = st.sidebar.selectbox(
    'Select option',
    ('Analysis', 'Updation')
)

if selectOptions == 'Analysis':
    df = preprocessor.preprocess()
    st.sidebar.title("Analysis")
    Options = st.sidebar.radio(
        'Choose an option',
        ('Overall analysis', 'Filling status', 'Last filling', 'Refill information', 'Fill now')
    )

    if Options == 'Overall analysis':
        overallAnalysis.OverallAnalysis()

    if Options == 'Filling status':
        fillingStatus.FillingStatus()

    if Options == 'Last filling':
        lastFilling.LastFilling()

    if Options == 'Refill information':
        refilling.Refilling()

    if Options == 'Fill now':
        fillNow.FillNow()

if selectOptions == 'Updation':
    st.sidebar.title('Updation')
    updateOptions = st.sidebar.radio(
        'Choose an option',
        ('Update one record', 'Upload xlsx file')
    )

    if updateOptions == 'Update one record':
        updateRecord.updateOneRecord()


    if updateOptions == 'Upload xlsx file':
        uploadXlsxFile.UploadFile()



