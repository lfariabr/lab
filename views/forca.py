
import streamlit as st
import random

#### NOVO: FORCA

st.title("Forca")
lista_palavras = []

# Abrindo o arquivo de palavras
with open('content/palavras.txt', 'r') as arquivo:
    for line in arquivo:
        lista_palavras.append(line.strip())

# Creates a random list
palavra_secreta = random.choice(lista_palavras)
palavra_chutada = []

# Temporarily display the word
st.write(palavra_secreta)

# Create a list to store the guessed letters
for letra in palavra_secreta:
  # st.write(letra)
  palavra_chutada.append("_")

# Parameters:
acertos = 0
tentativas = 5
acertou = False
letras_chutadas = []

# For loop do jogo:
while acertos < len(palavra_secreta) and tentativas > 0:
  
  # Asking for 1 guess:
  chute = st.text_input("Chute uma letra:", max_chars=1)
  acertou = False

  # Checking if guess is correct
  for index, letra in enumerate(palavra_secreta):
    if chute == letra:
      palavra_chutada[index] = chute
      acertou = True
      acertos += 1
      
  if acertou == False:
    tentativas -=1
    lista_letras_chutadas.append(chute)

  if acertos == len(palavra_secreta):
    st.write("Você ganhou!")
    st.write(palavra_secreta)

  if tentativas == 0:
    st.write("Você perdeu!")
    st.write(palavra_secreta)

  palavra_chutada_print = " ".join(palavra_chutada)
  st.write(palavra_chutada_print)



# if st.button("Chutar"):
#   if chute in palavra_secreta:
#     st.write(chute)
    # Inserir Loop do Jogo


# Se já inicializei, não será reiniciado novamente
# if 'palavra_secreta' not in st.session_state:
#   st.session_state['palavra_secreta'] = palavra_secreta

# if st.button("Mudar palavra"):
#   palavra_secreta = random.choice(lista_palavras)
#   st.session_state['palavra_secreta'] = palavra_secreta
