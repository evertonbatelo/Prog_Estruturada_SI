#7: Crie uma função eh_primo que receba um número e retorne True se ele é primo
#e False caso contrário. Teste com 11.

def eh_primo(numero):
    if numero < 2:
        return False
    for i in range(2,numero):
        if numero % i == 0:
            return False
    return True


numero = int(11)
eh_primo(numero)
print(f"O número {numero} é primo? {eh_primo(numero)}")