# -*- coding: utf-8 -*-
"""
Created on Sat Jan 28 15:18:08 2023

@author: Lenovo
"""

import pandas as pd
import streamlit as st

st.header('Billionaire Dataset')


#file = r'C:\Users\Lenovo\Desktop\Class 1 Python\Billionaire.csv'
df = pd.read_csv(Billionaire.csv)

#df = st.file_uploader(lebel= 'Upload Your File', type='csv')
#button = st.button('Upload')

# reading the file


# find count of billionaires by country
Total_billionaires = df.groupby('Country')['Name'].count().sort_values(ascending=False).head(10)

st.bar_chart(Total_billionaires)

# find the most popular source of income
popular_source = df.groupby('Source')['Name'].count().nlargest(10)
st.dataframe(popular_source)

#interactivity
all_countries = df['Country'].unique()

selection = st.selectbox('Select Country', all_countries)
subset = df[df['Country'] == selection]
st.dataframe(subset)


# get the cumulative wealth of billionaires belonging to US
NetWorth_New = df['NetWorth'].apply(lambda x: float(x.replace('$', '').replace(' B', '')))
all_countries = sorted(df['Country'].unique())
col1, col2 = st.columns(2)

# Column 1
#Display on streamlit
selected_country = col1.selectbox('Select Your Country', all_countries)
#subset on selected country
subset_country = df[df['Country'] == selected_country]

#get unique sources from the selected country
sources = sorted(subset_country['Source'].unique())

#display multiselect option on source
selected_source = col1.multiselect('Select Source of Income', sources)
#subset on selected source
subset_source = subset_country[subset_country['Source'].isin[selected_source]

#Column 2
main_string = '{} - Billionaires'.format(selected_country)
col2.header(main_string)
col2.table(subset_country)
col2.header('Source wise info')
col2.table(subset_source)

#df['NetWorth ($B)'] = NetWorth_New


#cumulative_wealth_usa = df.groupby('Country')df['Country')].isin(['United States'])['NetWorth ($B)'].sum()

