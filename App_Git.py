import streamlit as st
import numpy as np

st.write("# oieeee!!")

st.write("#Novo Aplicativo")

btn1 = st.button("Novo botao")

if btn1 == True:
    st.write("### Sua aplicacao esta funcionando!")

l = np.random.randint(5,20,10)
st.write(l)

title = st.text_input('Movie title', 'Life of Brian')
st.write('The current movie title is', title)
