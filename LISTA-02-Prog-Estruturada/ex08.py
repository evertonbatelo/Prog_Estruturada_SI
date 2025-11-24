#Exercício 8: Leia um número e imprima "Positivo" se ele for maior que zero,
#"Negativo" se for menor que zero e "Zero" se for igual a zero.
num1 = float(input('Digeite um número: '))
if num1 > 0:
    print('positivo')
elif num1 <0:
    print('negativo')
else:
    print('zero')