'''Faça um programa que peça ao usuário para inserir 5 números. O programa deve calcular a soma acumulada desses números e exibir o resultado final.

Peça ao usuário para inserir 5 números.
Requisito:
Use uma variável acumuladora para armazenar a soma dos números.
Após o usuário inserir todos os números, exiba a soma total.'''


#Utilizando variavel acumuladora "soma"
print("Por favor insira 5 numeros")
n1 = float(input())
soma = n1
n2 = float(input())
soma += n2
n3 = float(input())
soma += n3
n4 = float(input())
soma += n4
n5 = float(input())
soma +=n5
print(f"A soma dos números é {soma}")

#Solução 2
print("Por favor insira 5 numeros")
n1 = float(input())
n2 = float(input())
n3 = float(input())
n4 = float(input())
n5 = float(input())
soma2 = n1+n2+n3+n4+n5
print(f"A soma dos números é {soma2}")

#Solução 3 com loop
contEntrada = 0
soma3 = 0
print("Por favor insira 5 numeros")
while contEntrada < 5:
    entrada = float(input())
    soma3 += entrada
    contEntrada += 1
print(f"A soma dos números é {soma3}")