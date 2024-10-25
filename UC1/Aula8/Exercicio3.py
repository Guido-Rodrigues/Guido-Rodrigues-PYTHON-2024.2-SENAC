#Utilizando for, faça um programa que peça 5 numeros ao usuario e no final de sua soma
soma = 0
print("Por favor, insira 5 números")
for i in range (5):
    n = float(input("->"))
    soma += n
print(f"A soma é {soma}!")

