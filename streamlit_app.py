import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium


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

def dispaly_map(df,year,quarter):

    df = df[(df['Year'] == year) & (df['Quarter'] == quarter)]

    map = folium.Map(location = [38,-96.5], zoom_start=4, 
                     scrollWheelZoom=False, tiles='CartoDB positron')
    choropleth = folium.Choropleth(
        geo_data='data/us-state-boundaries.geojson', data=df,
        columns=('State Name','State Total Reports Quarter'),
        key_on='feature.properties.name',
        line_opacity= 0.8,
        highlight=True,
           )
    choropleth.geojson.add_to(map)

    df = df.set_index('State Name')
    state_name = "North Carolina"
      
    for features in choropleth.geojson.data['features']:
        state_name = features['properties']['name']
        features['properties']['population'] = 'population:' + \
            str('{:,}'.format(df.loc[state_name,'State Pop'][0]) if state_name in list(df.index) else 'N/A')
        features['properties']['per_100k'] = 'Report per 100k Population:'+ \
            str('{:,}'.format(round(df.loc[state_name,'Reports per 100K-F&O together'][0])) if state_name in list(df.index) else 'N/A')
        
    # add tooltip so map so that when we over it it will shows all this information in the list
    choropleth.geojson.add_child(
        folium.features.GeoJsonTooltip(['name','population','per_100k'], labels=False)
        )
    
    # set map properties
    st_map = st_folium(map, width=700, height=450)

    # confirm if a field is actively clicked then filter activenss to that sepcfic area
    if st_map['last_active_drawing']:
                state_name = st_map['last_active_drawing']['properties']['name']
    return state_name

def display_time_filters(df):
    # add the side bar of our dashboard
    # get all the unique in the data
    year_list = list(df['Year'].unique())
    quarter_list = [1 ,2 ,3, 4]
    # add year to the side bar
    year = st.sidebar.selectbox('Year',year_list, len(year_list)-1)
    # add quarter to the sidebar
    quarter = st.sidebar.selectbox('Quarter',quarter_list)
    st.header(f'{year} Q{quarter}')
    return year, quarter



def main():
    st.set_page_config(APP_TITLE)
    st.title(APP_TITLE)
    st.caption(APP_SUB_TITLE)

    # load Data
    df_continenetal = pd.read_csv('data\AxS-Continental_Full Data_data.csv')
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
    # add state name automatically as a filter from the map display let the click state name over write the default above
    state_name = dispaly_map(df_continenetal,year,quarter)

    # display Filer by sidebar
    year, quarter = display_time_filters(df_continenetal)


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