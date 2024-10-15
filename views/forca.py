
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
  st.session_state['palavra_secreta'] = palavra_secreta

  chute = st.text_input("Chute uma letra:", max_chars=1)
  if st.button("Chutar"):
    if chute in palavra_secreta:
      st.write(chute)

if st.button("Mudar palavra"):
  palavra_secreta = random.choice(lista_palavras)
  st.session_state['palavra_secreta'] = palavra_secreta
