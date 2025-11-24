#Exercício 6: Escreva um programa que leia um número e imprima "Par" se ele for par e
#"Ímpar" se for ímpar
num1 = float(input('Digeite um número inteiro: '))
resto=num1%2
#print(resto)
if resto == 0:
    print('O numero é par')
else:
    print('O numero é impar')