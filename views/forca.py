
#### NOVO: FORCA

elif page == "Forca":

  st.title("Forca")
  import random
  lista_palavras = []

  # Abrindo o arquivo de palavras
  with open('content/palavras.txt', 'r') as arquivo:
      for line in arquivo:
          lista_palavras.append(line.strip())

  #
  palavra_secreta = random.choice(lista_palavras)
  st.write(palavra_secreta)

  st.button("TESTE")
