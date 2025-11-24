
# dicionário com frutas e quantidades
frutas = {
    "maçã": 10,
    "banana": 5,
    "laranja": 8
}

chave = input("Digite o nome de uma fruta: ")


if chave in frutas:
    print("A fruta é comercializda.")
else:
    print("A fruta não é comercializda.")