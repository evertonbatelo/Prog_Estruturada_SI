# Lê a string do usuário
texto = input("Digite uma string: ")

# Lê a letra que queremos contar
letra = input("Digite a letra que deseja contar: ")

# Conta quantas vezes a letra aparece na string
quantidade = texto.count(letra)

# Mostra o resultado
print(f"A letra '{letra}' aparece {quantidade} vezes na string.")