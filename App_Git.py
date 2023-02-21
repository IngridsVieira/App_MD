import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

st.write("# oieeee!!")

st.write("#Novo Aplicativo")

btn1 = st.button("Novo botao")

if btn1 == True:
    st.write("### Sua aplicacao esta funcionando!")

l = np.random.randint(5,20,10)
st.write(l)

Latitude = st.text_input('Latitude:', 'Digite as coordenadas da sua latitude.')
Longitude = st.text_input('Longitude:', 'Digite as coordenadas da sua longitude.')
st.write("Suas coordenadas são {} de Latitude e {} de Longitude".format(Latitude,Longitude))

st.write("### Sua localização no mapa:")

dic_map = {"lat": [-25.45012,-25.43462],
    "lon": [-49.23315,-49.25334]}

df_mapa = pd.DataFrame(dic_map)
st.map(df_mapa)
