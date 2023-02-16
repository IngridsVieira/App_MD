import streamlit as st
import numpy as np

st.write("# Novo aplicativo")

st.write("#Novo Aplicativo")

btn1 = st.button("Novo botao")

if btn1 == True:
    st.write("### Sua aplicacao esta funcionando!")

l = np.random.randint(5,20,10)
st.write(l)