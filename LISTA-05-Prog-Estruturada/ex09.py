# Lê a string do usuário
texto = input("Digite uma palavra ou frase: ")

# Remove espaços e coloca tudo em minúsculas para comparação
texto_limpo = texto.replace(" ", "").lower()

# Verifica se é igual ao seu inverso
if texto_limpo == texto_limpo[::-1]:
    print("É um palíndromo!")
else:
    print("Não é um palíndromo.")