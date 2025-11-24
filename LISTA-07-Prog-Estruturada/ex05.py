#5: Crie uma função converte_fahrenheit que receba uma temperatura em Celsius
#e a converta para Fahrenheit. Teste com 25°C.

def converte_fahrenheit(celsius):
    temp_f = (celsius * 9/5) + 32
    print(f"{celsius}°C equivale a {temp_f}°F")

celsius = float(input("Digite a temperatura em Graus Celcius: "))

converte_fahrenheit(celsius)