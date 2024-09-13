import pandas as pd

def preprocess():
    df = pd.read_excel("ADBLUE_NEW_SHEET.xlsx")
    # preprocess
    df_cleaned = df.loc[:, ~df.columns.str.contains('^Unnamed')]
    df_cleaned.drop_duplicates(inplace=True)
    df_cleaned['Date'] = pd.to_datetime(df_cleaned['Date']).dt.date
    # df_cleaned['Avg'] = df_cleaned['Avg'].fillna(1200)
    # df_cleaned['Avg'] = df.loc[df['Avg'] < 0, 'Avg'] = 1200
    # df_cleaned = df_cleaned.rename(columns={'NAME': 'Name'})
    # df_cleaned.drop(['Date:', 'Name'], axis=1, inplace=True)
    # df_cleaned.to_excel("ADBLUE_NEW_SHEET.xlsx", index=False, engine='openpyxl')

    return df_cleaned
