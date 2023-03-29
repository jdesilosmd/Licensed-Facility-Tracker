

import pandas as pd
import streamlit as st

df = pd.read_csv(r"C:\Users\Asus\OneDrive - De La Salle Medical and Health Sciences Institute\Documents\Data Science\active health facilities\activefacilities.csv")
facilities = df.loc[:, ['Health Facility Code', 'Health Facility Code Short',
                        'Facility Name', 'Facility Major Type', 'Health Facility Type', 
                        'Ownership Major Classification', 'Region Name', 'Province Name',
                        'City/Municipality Name', 'Barangay Name', 'Licensing Status',
                        'License Validity Date']]
province_list = facilities['Province Name'].astype(str)
province_list = province_list.explode().unique().tolist()
province_list.sort()



# Streamlit Dashboard

st.title('Licensed Facility Tracker')
st.write('Version 1.0')

province = st.selectbox('Select Province', province_list)


city_list = facilities.loc[facilities['Province Name']== province, 'City/Municipality Name']
city_list = city_list.explode().unique().tolist()
city_list.sort()

container = st.container()
all = st.checkbox("Select All")
if all:
    city = container.multiselect('Select City or Municipality', city_list, city_list)
else:
    city = container.multiselect('Select City or Municipality', city_list)


filtered_list = facilities[facilities['City/Municipality Name'].isin(city)]
st.dataframe(filtered_list)
