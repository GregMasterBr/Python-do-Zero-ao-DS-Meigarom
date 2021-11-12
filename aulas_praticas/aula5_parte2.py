import pandas as pd
import numpy as np
import streamlit as st
import plotly.express as px




st.title('House Rocket Company')
#n =input('Qual o seu nome?')

st.markdown(f'Seja bem vindo a House Rocket')

st.header('Load Data')


@st.cache(allow_output_mutation=True)

def get_data(path):
    data = pd.read_csv(path)
    data['date'] = pd.to_datetime(data['date'])
    return data

data = get_data('ds/kc_house_data.csv')

st.dataframe(data.head())


bedrooms = st.sidebar.multiselect(
    'Number of Bedrooms',
    data['bedrooms'].unique()
)

st.write('Sua escolha foi ',bedrooms[0])


st.title('House Rocket Map')

is_check= st.checkbox('Mostrar o Mapa')


price_min = int(data['price'].min())
price_max = int(data['price'].max())
price_avg = int(data['price'].mean())


price_slider = st.slider('Prince Range',
                         price_min,price_max,price_avg)
data['level'] ='NA'
for i in range(len(data)):
    if (data.loc[i,'price'] <=321950):
        data.loc[i,'level'] = 0
    elif ((data.loc[i,'price'] > 321950) & (data.loc[i,'price'] <=450000)):
        data.loc[i,'level'] = 1
    elif ((data.loc[i,'price'] > 450000) & (data.loc[i,'price'] <=645000)):
        data.loc[i,'level'] = 2
    else:
         data.loc[i,'level'] = 3

if is_check:
    houses = data[data['price']<price_slider][['id','lat','long','price','level']]
    st.dataframe(houses.head())

    fig = px.scatter_mapbox(houses,
                           lat='lat',
                           lon='long',
                           color='level',
                           size='price',
                           color_continuous_scale=px.colors.cyclical.IceFire,
                           size_max=15,
                           zoom=10)
    fig.update_layout(mapbox_style='open-street-map')
    fig.update_layout(height=600,margin={'r':0,'l':0,'b':0,'t':0})

    fig.show()