#Faça um programa que gera 3 numeros aleatórios (float) entre 1 e 15 e você tem 1 tentativa para descobrir qual é o maior.
import random

n1, n2, n3 = random.uniform(1, 15),random.uniform(1, 15),random.uniform(1, 15)
#print(n1,n2,n3) #TESTE
if n1>n2 and n1>n3:
    maior = n1
    maiortexto = "1º"
elif n2>n1 and n2>n3:
    maior = n2
    maiortexto = "2º"
else:
    maior = n3
    maiortexto = "3º"
#print(maior) #TESTE
entrada = int(input("Três numeros ponto flutuante foram gerados, qual deles é o maior?\n1- 1º\n2- 2º\n3- 3º\n-->"))
if entrada != 1 and entrada != 2 and entrada != 3:
    print("Entrada inválida!")
elif entrada == 1 and maior == n1:
    print("Você acertou!")
elif entrada == 2 and maior == n2:
    print("Você acertou!")
elif entrada == 3 and maior == n3:
    print("Você acertou!")
else:
    print("Você errou!")
print(f"O maior numero era o {maiortexto} de valor {maior}")