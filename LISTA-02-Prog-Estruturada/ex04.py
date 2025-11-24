#Exercício 4: Peça ao usuário para digitar dois números e verifique se a soma deles é
#maior que 10.
num1 = float(input('Digeite o primeiro número: '))
num2 = float(input('Digite o segundo numero: '))
soma = num1 + num2
if soma > 10:
    print('A soma é maior que 10')
else:
    print('A soma é menor que 10')