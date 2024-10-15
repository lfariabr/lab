
import streamlit as st
import random

#### NOVO: FORCA

st.title("Forca")
lista_palavras = []

# Abrindo o arquivo de palavras
with open('content/palavras.txt', 'r') as arquivo:
    for line in arquivo:
        lista_palavras.append(line.strip())

#
palavra_secreta = random.choice(lista_palavras)
st.write(palavra_secreta)

# If click
contador = 0

# Se já inicializei, não será reiniciado novamente
if 'palavra_secreta' not in st.session_state:
  st.session_state['contador'] = palavra_secreta
  
if st.button("Começar!"):
  st.session_state['contador'] += 1

  st.write(st.session_state['palavra_secreta'])

st.button("Começar!"):
