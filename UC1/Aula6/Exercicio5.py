#Faça um programa que peça 1 numero ao cliente e faça sua tabuada até o 10

numero = int(input("Por favor, insira um numero: "))
fator = 1
print(f"Está é a tabuada de {numero}:")
while fator <= 10:
    print(f"{numero} X {fator} =",numero*fator)
    fator += 1