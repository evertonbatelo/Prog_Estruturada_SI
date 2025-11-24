#Escreva uma função conta_caracteres que receba uma string e retorne o
#número de caracteres. Teste com "Python".


def conta_caracteres(palavra):
     ncaracteres = len(palavra)
     print(f"A palavra tem {ncaracteres} caracteres")


palavra = str(input("Digite uma palavra: "))

conta_caracteres(palavra)

