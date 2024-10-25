#Faça um programa que gera 4 numeros aleatorios e depois os ordena de forma decrescente
import random
n1,n2,n3,n4 = random.randint(1,100),random.randint(1,100),random.randint(1,100),random.randint(1,100)
print(n1,n2,n3,n4) #TESTE
loop = 1

while loop == 1:
    if n1 < n2:
        n1,n2 = n2,n1
    if n2 < n3:
        n2,n3 = n3,n2
    if n3 < n4:
        n3,n4 = n4,n3
    if n1>n2 and n2>n3 and n3>n4:
        loop = 0

print(n1,n2,n3,n4) #TESTE