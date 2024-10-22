
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
    palavra_secreta = random.choice(lista_palavras)  # Selecionar uma palavra aleatória
    st.session_state["palavra_secreta"] = palavra_secreta
    st.session_state["letras_chutadas"] = []  # Lista vazia para as letras chutadas
    st.session_state["tentativas"] = 5  # Iniciar tentativas com 5
    st.session_state["acertos"] = 0  # Contador de acertos

    palavra_chutada = []  # Criar uma lista com os chutes

    for letra in palavra_secreta:
        palavra_chutada.append("_")  # Iniciar a palavra de chutes com traços

    st.session_state["palavra_chutada"] = palavra_chutada

# Exibir a palavra secreta temporariamente (para depuração, pode remover depois)
st.write(st.session_state["palavra_secreta"])

# Entrada para o chute
chute = st.text_input("Chute uma letra:", max_chars=1)

# Botão de chute
if st.button("Chutar"):
    palavra_secreta = st.session_state["palavra_secreta"]
    palavra_chutada = st.session_state["palavra_chutada"]
    letras_chutadas = st.session_state["letras_chutadas"]
    tentativas = st.session_state["tentativas"]
    acertos = st.session_state["acertos"]
    
    acertou = False  # Variável para verificar se o chute está correto

    # Checar se o chute está correto
    for index, letra in enumerate(palavra_secreta):
        if chute == letra:
            palavra_chutada[index] = letra
            acertos += 1
            acertou = True

    # Se o chute estiver incorreto
    if not acertou:
        if chute not in letras_chutadas:  # Verificar se a letra já foi chutada
            tentativas -= 1
            letras_chutadas.append(chute)
    
    # Atualizar session_state com os novos valores
    st.session_state["palavra_chutada"] = palavra_chutada
    st.session_state["letras_chutadas"] = letras_chutadas
    st.session_state["tentativas"] = tentativas
    st.session_state["acertos"] = acertos

    # Mostrar estado atual do jogo
    st.write("Palavra: " + " ".join(palavra_chutada))
    st.write(f"Tentativas restantes: {tentativas}")
    st.write(f"Letras chutadas: {', '.join(letras_chutadas)}")

    # Verificar se o jogador ganhou ou perdeu
    if acertos == len(palavra_secreta):
        st.success("Parabéns! Você acertou a palavra!")
    elif tentativas == 0:
        st.error(f"Você perdeu! A palavra era: {palavra_secreta}")
