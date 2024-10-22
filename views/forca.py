
import streamlit as st
import random

#### NOVO: FORCA

# Abrindo e populando o arquivo de palavras
lista_palavras = []
with open('content/palavras.txt', 'r') as arquivo:
    for line in arquivo:
        lista_palavras.append(line.strip())

st.title("Jogo da Forca")

# Inicializar variáveis no session_state se elas não existirem
if "palavra_secreta" not in st.session_state:
    palavra_secreta = random.choice(lista_palavras)  # Selecionar uma palavra aleatória
    st.session_state["palavra_secreta"] = palavra_secreta
    st.session_state["letras_chutadas"] = []  # Inicializar a lista vazia de letras chutadas
    st.session_state["tentativas"] = 5  # Inicializar tentativas
    st.session_state["acertos"] = 0  # Inicializar acertos

    # Criar a lista de traços para a palavra chutada
    palavra_chutada = ["_" for letra in palavra_secreta]
    st.session_state["palavra_chutada"] = palavra_chutada

# Mostrar a palavra secreta temporariamente (para depuração, pode remover depois)
st.write(st.session_state["palavra_secreta"])

# Entrada para o chute
chute = st.text_input("Chute uma letra:", max_chars=1)

# Verificar se o chute foi feito e processar
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
