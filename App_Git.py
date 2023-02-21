import streamlit as st
import numpy as np
import pandas as pd


st.title("Mapa search!")

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
        
#---------------------------------------------------------------

st.title("Words Frequency!")

text = st.text_area('Digite um texto:')

btn2 = st.button("Analisar texto:")

if btn2 == True:
    if text != "":
        #cleaning
        text = text.lower()
        words = text.split()
        words = [word.strip('.,!;()[]') for word in words]
        words = [word.replace("'s", '') for word in words]

        #finding unique
        unique = []
        for word in words:
            if word not in unique:
                unique.append(word)

        word_frequency = []
        new_list = []
        for i in range(len(unique)):
            a = unique[i]
            if len(a) >= 3:
                new_list.append(a)
                word_frequency.append(text.count(a))

        df = pd.DataFrame({'Palavra' : new_list,
                                        'Frequência' : word_frequency}, 
                                        columns=['Palavra','Frequência'])
        df
    else:
        st.write("Insira um texto")
