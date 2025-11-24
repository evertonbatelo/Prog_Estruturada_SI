#Exercício 14: Solicite ao usuário que digite dois números. Verifique se um deles é zero
#e se a soma deles é maior que 10.
num1=float(input('Digeite o primeiro número: '))
num2=float(input('Digite o segundo numero: '))

if num1==0 or num2==0:
    print('Um dos numeros digitados é igual a zero')
else:
    print('Nenhum dos nuemros é igual a zero')

soma=num1+num2
if soma>10:
     print('A soma dos nuemros é maior que 10')
else:
     print('A soma dos nuemros é menor que 10')