import streamlit as st
import numpy as np

st.write("# oieeee!!")

st.write("#Novo Aplicativo")

btn1 = st.button("Novo botao")

if btn1 == True:
    st.write("### Sua aplicacao esta funcionando!")

l = np.random.randint(5,20,10)
st.write(l)

Latitude = st.text_input('Latitude:', 'Digite as coordenadas da sua latitude.')
Longitude = st.text_input('Longitude:', 'Digite as coordenadas da sua longitude.')
st.write('The current movie title is', title)
