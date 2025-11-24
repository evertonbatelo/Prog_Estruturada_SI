#Exercício 9: Solicite ao usuário que digite uma letra. Se a letra for uma vogal, imprima
#"Vogal", caso contrário, imprima "Consoante".
letra=input('Digeite uma letra: ')
if (letra == "a" or letra == "A" or
    letra == "e" or letra == "E" or
    letra == "i" or letra == "I" or
    letra == "o" or letra == "O" or
    letra == "u" or letra == "U"):
    print("Vogal")
else:
    print("Consoante")


