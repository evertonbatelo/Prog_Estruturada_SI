# Escreva uma função main que chame duas funções: uma para calcular o 
# quadrado de um número (pedido ao usuário) e outra para verificar se é par ou ímpar.
# Execute com main() .

def main():
    print("Início do programa")
    a = float(input("Digite um número: "))
    quadrado(a)
    verifica_par(a)
    

def quadrado(a):
    a = a**2
    print(f"O numero digitado elevado ao quadrado é, {a}")

def verifica_par(a):
    if a % 2 == 0:
        print(f"O numero digitado,{a}, é PAR")
    else:
        print(f"O numero digitado,{a}, é IMPAR")


main()



    