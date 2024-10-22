
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
  st.session_state["tentativas"] = len(st.session_state["palavra_secreta"])

# Mostrar a palavra atual e chute
st.write(st.session_state["palavra_secreta"])
st.write(f"A palavra atual tem {len(st.session_state['palavra_secreta'])} letras. Boa sorte!")
# st.markdown("# " + " ".join(st.session_state["palavra_chutada"]))
chute = st.text_input("Chute uma letra:", max_chars=1)

# Processar o chute ao clicar no botão:
if st.button("Chutar"):
  palavra_secreta = st.session_state["palavra_secreta"]
  palavra_chutada = st.session_state["palavra_chutada"]
  letras_chutadas = st.session_state["letras_chutadas"]
  acertos = st.session_state["acertos"]
  tentativas = st.session_state["tentativas"]

  # Verificar se o chute já foi feito
  if chute in letras_chutadas:
    st.warning("Você já chutou essa letra. Tente outra.")
  else:
    acertou = False

    # Verificar se o chute está correto
    for index, letra in enumerate(palavra_secreta):
      if chute == letra:
        palavra_chutada[index] = letra
        acertos += 1
        acertou = True
    
    # Se o chute estiver incorreto
    if not acertou:
      tentativas -= 1
      letras_chutadas.append(chute)
      st.warning(f"{chute} não está na palavra. Tentativas restantes: {tentativas}")

    # Atualizar o estado do jogo com novos valores
    st.session_state["palavra_chutada"] = palavra_chutada
    st.session_state["letras_chutadas"] = letras_chutadas
    st.session_state["acertos"] = acertos
    st.session_state["tentativas"] = tentativas

    # Verificar se o jogador ganhou ou perdeu
    if acertos == len(palavra_secreta):
      st.success(f"Parabéns! A palavra era {palavra_secreta}. Você venceu!")
    elif tentativas == 0:
      st.error(f"Você perdeu! A palavra era {palavra_secreta}")
    else:
      st.write(f"Palavra atual: {' '.join(palavra_chutada)}")
      st.write(f"Tentativas restantes: {tentativas}")
      st.write(f"Letras chutadas: {', '.join(letras_chutadas)}")
