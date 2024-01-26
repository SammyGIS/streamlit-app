import streamlit as st
import pandas as pd


APP_TITLE = "Fraud and Identity Theft Report"
APP_SUB_TITLE = 'Source" Federal Trade Commission'

def display_fraud_facts(year,quarter,state_name,report_type,
                         field_name,metric_title):
    
    metric_title = f'# {report_type} of Reports'

    df = df[(df['Year'] == year) & (df['Quarter'] == quarter)\
             & (df['Report Type'] == report_type)]
    if state_name:
        df=df[df['State Name']==state_name]
    df.drop_duplicates(inplace =True)
    total = df[field_name].sum()
    st.metric(metric_title,'{:,}'.format(total))














def main():
    st.set_page_config(APP_TITLE)
    st.title(APP_TITLE)
    st.caption(APP_SUB_TITLE)

    # load Data
    df = pd.read_csv('data\AxS-Fraud Box_Full Data_data.csv')

    year   = 2022
    quarter = 1
    state_name = 'Texas'
    report_type = 'Fraud'
    field_name  = 'State Fraud/Other Count'

    display_fraud_facts(year,quarter,state_name,report_type,
                         field_name,metric_title)

    st.write(df.head())
    st.write(df.columns)

    



    # Display filters and Map




    # Display Metrics


if __name__ =="__main__":
    main()