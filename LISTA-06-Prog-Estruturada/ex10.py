# Dicionário original
dicionario = {'a': 1, 'b': 2, 'c': 3}

# Dicionário ivertido
invertido = {}


for item in dicionario.items():
    valor = item[1]
    invertido[valor] = item[0]

print(dicionario)
print(invertido)