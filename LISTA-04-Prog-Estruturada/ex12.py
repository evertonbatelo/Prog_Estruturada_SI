

lista1 = [1, 2, 3, 4, 5, 5, 6]
lista2 = [4, 5, 6, 7, 8, 8]

# interseção usando conjuntos
comuns = list(set(lista1) & set(lista2))

print("Elementos em ambas as listas (sem repetição):", comuns)


