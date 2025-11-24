# Lê a string do usuário
texto = input("Digite uma frase: ")

# Separa a string em palavras (usando espaço como separador)
palavras = texto.split()

# Imprime cada palavra em uma linha
for palavra in palavras:
    print(palavra)