#Exercício 15: Leia uma letra e imprima se ela é uma vogal e está em maiúscula.
letra=input('Digeite uma letra: ')
if letra==str('a') or letra==str('e') or letra==str('i') or letra==str('o') or letra==str('u'):
    print('Vogal Minuscula')
elif letra==str('A') or letra==str('E') or letra==str('I') or letra==str('O') or letra==str('U'):
    print('Vogal Maiuscula')
else:
    print('Consoante')