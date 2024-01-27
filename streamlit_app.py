import streamlit as st
import pandas as pd


APP_TITLE = "Fraud and Identity Theft Report"
APP_SUB_TITLE = 'Source: Federal Trade Commission'

def display_fraud_facts(df,year,quarter,state_name,report_type,
                         field_name,metric_title,
                         currency_sign='', is_median=False):
    
    df = df[(df['Year'] == year) & (df['Quarter'] == quarter)\
             & (df['Report Type'] == report_type)]
    if state_name:
        df=df[df['State Name']==state_name]
    df.drop_duplicates(inplace =True)
    if is_median:
        total = df[field_name].sum()/len(df) \
            if len(df) else 0
    else:
        total = df[field_name].sum()
    st.metric(metric_title,'{}{:,}'.format(currency_sign,round(total)))

def main():
    st.set_page_config(APP_TITLE)
    st.title(APP_TITLE)
    st.caption(APP_SUB_TITLE)

    # load Data
    df_fraud= pd.read_csv('data\AxS-Fraud Box_Full Data_data.csv')
    df_median = pd.read_csv('data\AxS-Median Box_Full Data_data.csv')
    df_loss = pd.read_csv('data\AxS-Losses Box_Full Data_data.csv')


    year   = 2022
    quarter = 1
    state_name = ''
    report_type = 'Fraud'
    metric_title = f'# {report_type} of Reports'
    currency_sign = '$'


    # Display filters and Map




    # Display Metrics
    st.subheader(f'{state_name} {report_type} Facts')
    col1,col2,col3 = st.columns(3)
    with col1:
        display_fraud_facts(df_fraud, year,quarter,state_name,report_type,
                         'State Fraud/Other Count',metric_title)
    with col2:
        display_fraud_facts(df_median, year,quarter,state_name,report_type,
                         'Overall Median Losses Qtr','Median $ loss',
                         currency_sign, is_median=True)
    with col3:
        display_fraud_facts(df_loss, year,quarter,state_name,report_type,
                         'Total Losses','Total $ loss',currency_sign)



if __name__ =="__main__":
    main()