# Solicita ao usuário uma string
texto = input("Digite uma string: ")

# Solicita a letra que será substituída
antiga = input("Digite a letra que deseja substituir: ")

# Solicita a nova letra
nova = input("Digite a nova letra: ")

# Substitui todas as ocorrências
resultado = texto.replace(antiga, nova)

# Exibe o resultado
print("String modificada:", resultado)