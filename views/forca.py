
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
if st.button("Jogo da Forca..."):
  st.write("Começar")
