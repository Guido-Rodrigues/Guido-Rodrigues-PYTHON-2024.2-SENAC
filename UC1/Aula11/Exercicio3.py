# Faça um programa que tenha uma função chamada converter. Essa função deve receber uma temperatura em celcius e retornar fahreinheit.
#F=C*9/5​+32
def converter(grausCelsius):
    return grausCelsius*9/5+32

entrada = float(input("Digite o valor para ser convertido para Fahrenheit: "))
resultado = converter(entrada)

print(f"{entrada} graus celsius são {resultado} fahrenheit")