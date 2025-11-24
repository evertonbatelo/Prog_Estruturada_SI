def string_mais_longa(lista):
    mais_longa = lista[0]
    for i in lista:
        if len(i) > len(mais_longa):
            mais_longa = i
    return mais_longa


lista = ["Python", "Java", "C", "JavaScript"]

mais_longa = string_mais_longa(lista)

print("A string mais longa é:", mais_longa)