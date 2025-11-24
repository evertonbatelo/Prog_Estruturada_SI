# Exercício 7: Crie uma tabuada de 1 a 10 com laços aninhados.

for i in range(1, 11):        
    print("Tabuada do", i)
    
    for j in range(1, 11):      
        resultado = i * j
        print(i, "x", j, "=", resultado)
    
    print()