'''#Faça um programa usando for que peça 4 numeros e some apenas os numeros primos.
soma = 0
print("Por favor insira 4 números:")
for i in range(4):
    checkprimo = 1
    entrada = int(input("->"))
    for fator in range(2,entrada):
        if entrada%fator == 0:
            checkprimo = 0
    if (checkprimo == 1):
        soma += entrada
print(f"A soma dos numeros primos na sequencia é de: {soma}")'''

#Faça um programa usando for que peça 4 numeros e some apenas os numeros IMPARES:

soma = 0
print("Por favor insira 4 números:")
for i in range (4):
    entrada = int(input("->"))
    if entrada%2 != 0:
        soma += entrada
print(f"A soma dos numeros impares na sequencia dada é {soma}")