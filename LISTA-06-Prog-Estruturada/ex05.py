# Dados de entrada
nome = input("Digite seu nome: ")
idade = input("Digite sua idade: ")

# Dicionário vazio
clientes = {}

# Armazenar no dicionário
clientes["nome"] = nome
clientes["idade"] = idade

print(clientes)

#removendo a chave idade

del clientes ["idade"]

print(clientes)


