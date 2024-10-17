
import streamlit as st
import random

#### NOVO: FORCA

# Abrindo e populando o arquivo de palavras
lista_palavras = []
with open('content/palavras.txt', 'r') as arquivo:
    for line in arquivo:
        lista_palavras.append(line.strip())

st.title("Jogo da Forca")

# Se já inicializei, não será reiniciado novamente
if "palavra_secreta" not in st.session_state:
  palavra_secreta = random.choice(lista_palavras) # Selecionar uma palavra aleatória
  st.session_state["palavra_secreta"] = palavra_secreta
  palavra_chutada = [] # Criar uma lista com os chutes

  for letra in palavra_secreta:
    # iniciar a palavra de chutes com traços
    palavra_chutada.append("_")    

  st.session_state["palavra_chutada"] = palavra_chutada

st.write(st.session_state["palavra_secreta"])
chute = st.text_input("Chute uma letra:", max_chars=1)

acertos = 0
tentativas = 5
acertou = False

letras_chutadas = []

if st.button("Chutar"):
  palavra_secreta = st.session_state["palavra_secreta"]
  palavra_chutada = st.session_state["palavra_chutada"]

  for index, letra in enumerate(palavra_secreta):
    # Checando se a letra está na palavra:
    if chute == letra:
      palavra_chutada[index] = letra
      acertos += 1
  
  palavra_chutada_print = " ".join(palavra_chutada)
  st.write(palavra_chutada_print)




    # Inserir Loop do Jogo

# if st.button("Mudar palavra"):
#   palavra_secreta = random.choice(lista_palavras)
#   st.session_state['palavra_secreta'] = palavra_secreta
