#Exercício 13: Leia três números e imprima se todos são diferentes.
num1=float(input('Digeite o primeiro número: '))
num2=float(input('Digite o segundo numero: '))
num3=float(input('Digite o terceiro numero: '))

if num1!=num2 and num1!=num3 and num2!=num3:
    print('Os três numeros digitados são diferentes')
else:
    print('Pelo menos algum dos numeros digitados é igual')