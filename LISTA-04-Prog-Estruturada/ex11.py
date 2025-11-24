# recebe os números do usuário (separados por espaço)
entrada = input("Digite os números separados por espaço: ")

# transforma a entrada em lista de inteiros
numeros = [int(x) for x in entrada.split()]

# filtra apenas os números pares
pares = [n for n in numeros if n % 2 == 0]

# calcula a média se houver pares
if pares:
    media = sum(pares) / len(pares)
    print("Média dos números pares:", media)
else:
    print("Não há números pares na lista.")