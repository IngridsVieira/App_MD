import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
#import matplotlib.pyplot as plt


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
        
  #-----------------------------------------------------------------------      
st.title("Graph Plot!")    
            

from io import StringIO

df2 = st.file_uploader("Choose a file")
btn3 = st.button("Gerar tabela:")
if btn3 == True:
    if df2 != "":
        dataframe = pd.read_csv(df2, sep = ";")
        st.write(dataframe)
else: 
    st.write("Insira um arquivo.")
    
#btn4 = st.button("Gerar gráfico:")
#if btn4 == True:
    #fig, ax = plt.subplots(1,1)
    #ax.plot(df2)
    #st.pyplot(fig)
    
    
#---------------------------------------------------------------
st.title("Media Page") 

st.video("https://www.youtube.com/watch?v=4bHUsy74Fss")
