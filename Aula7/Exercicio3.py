#Faça um programa que receba um numero e diga se ele é primo ou não

entrada = int(input("Por favor, insira um numero:\n"))
checkprimo = 1

for fator in range(2,entrada):
    if entrada%fator == 0:
        checkprimo = 0

if (checkprimo == 0):
    print(f"O número {entrada} não é primo!")

else:
    print(f"O número {entrada} é primo!")