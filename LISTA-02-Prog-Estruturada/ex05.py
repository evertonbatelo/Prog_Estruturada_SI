#Exercício 5: Leia três números e imprima se o primeiro é menor que o segundo e
#maior que o terceiro.
num1 = float(input('Digeite o primeiro número: '))
num2 = float(input('Digite o segundo numero: '))
num3 = float(input('Digite o segundo numero: '))

if num1 < num2 and num1 > num3:
   print('O primeiro numero é menor que o segundo e maior que o terceiro')
else:
    print('Não atende a condição')