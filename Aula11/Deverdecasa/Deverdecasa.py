#Crie um programa em Python que simule uma calculadora básica. O programa deve permitir que o usuário escolha entre as seguintes operações: soma, subtração, multiplicação ou #divisão. Após a escolha, o programa deve solicitar ao usuário que insira dois números, realizar a operação escolhida e exibir o resultado. O programa deve utilizar funções #pré-definidas (somar, subtrair, multiplicar, dividir) importadas

# MAIN

from funcoes import somar, subtrair, multiplicar, dividir

entrada = input("Qual operação deseja realizar, soma, subtração, multiplicação ou divisão?\n-->")

print("Insira dois numeros:")
n1,n2 = float(input("-->")), float(input("-->"))

if entrada == "soma" or entrada == "somar":
    resultado = somar(n1,n2)
elif entrada == "subtração" or entrada == "subtrair":
    resultado = subtrair(n1,n2)
elif entrada == "multiplicação" or entrada == "mutiplicar":
    resultado = multiplicar(n1,n2)
elif entrada == "divisão" or entrada == "dividir":
    resultado = dividir(n1,n2)

print(f"O resultado da operação é {resultado}.")