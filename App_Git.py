import streamlit as st
import numpy as np
import pandas as pd


st.write("# Mapa search!")

Latitude = st.number_input('Latitude:',)
Longitude = st.number_input('Longitude:',)

if Latitude != "" and Longitude != "":
    st.write("Suas coordenadas são {} de Latitude e {} de Longitude".format(Latitude,Longitude))
    
btn1 = st.button("Gerar mapa:")

if btn1 == True:
    st.write("### Sua localização no mapa:")
    if Latitude != "" and Longitude != "":
        dic_map = {"lat": [Latitude],"lon": [Longitude]}

        df_mapa = pd.DataFrame(dic_map)
        st.map(df_mapa)

