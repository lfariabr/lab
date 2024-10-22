
import streamlit as st
import random

#### NOVO: FORCA

# Abrindo e populando o arquivo de palavras
lista_palavras = []
with open('content/palavras.txt', 'r') as arquivo:
    for line in arquivo:
        lista_palavras.append(line.strip())

st.title("Jogo da Forca")

# Inicializar variáveis no session_state, caso não existam
if "palavra_secreta" not in st.session_state:
  st.session_state["palavra_secreta"] = random.choice(lista_palavras)
  st.session_state["palavra_chutada"] = ["_" for letra in st.session_state["palavra_secreta"]]
  st.session_state["letras_chutadas"] = []
  st.session_state["acertos"] = 0
  st.session_state["tentativas"] = 5

# Mostrar a palavra atual e chute
st.write("Palavra atual" + " ".join(st.session_state["palavra_chutada"]))
chute = st.text_input("Chute uma letra:", max_chars=1)

# Processar o chute ao clicar no botão:
if st.button("Chutar"):
  palavra_secreta = st.session_state["palavra_secreta"]
  palavra_chutada = st.session_state["palavra_chutada"]
  letras_chutadas = st.session_state["letras_chutadas"]
  acertos = st.session_state["acertos"]
  tentativas = st.session_state["tentativas"]
