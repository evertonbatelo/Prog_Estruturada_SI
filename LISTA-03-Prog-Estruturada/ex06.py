# Exercício 6: Leia entradas até o usuário digitar "sair". (com while)

entrada = ""

while entrada != "sair":
    entrada = input("Digite algo (ou 'sair' para encerrar): ")
    if entrada != "sair":
        print("Você digitou:", entrada)