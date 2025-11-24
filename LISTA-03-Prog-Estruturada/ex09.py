# Exercício 9: Leia números em uma lista até encontrar um negativo (break).

numeros = [4, 7, 2, 9, -3, 10]  

for n in numeros:
    if n < 0:
        break
    print(n)