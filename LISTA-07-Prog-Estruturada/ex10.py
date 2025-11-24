def fatorial (numero):
    if numero == 0:
        return 1
    else:
        resultado = 1
        for i in range(1, numero + 1):
            resultado = resultado * i
        return resultado

numero = 5
fatorial = fatorial(numero)
print(f"O fatorial de {numero} é {fatorial}")
