# Dados de entrada
nome = input("Digite seu nome: ")
idade = input("Digite sua idade: ")

# Dicionário vazio
clientes = {}

# Armazenar no dicionário
clientes["nome"] = nome
clientes["idade"] = idade

# Imprimindo a idade antiga
print(clientes["idade"])

# atualizando a idade
clientes["idade"] = 25

# Imprimindo a idade nova
print(clientes["idade"])