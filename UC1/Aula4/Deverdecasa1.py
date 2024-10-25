#Faça um programa que diga se um número é divisível por 3 
#e que diga se um numero é divisível por 5

numero = int(input("Por favor, insira um número: "))

if (numero%3 == 0):
    print(f"O número {numero} é divisível por 3")
else:
    print(f"O número {numero} não é divisível por 3")

if (numero%5 ==0):
    print(f"O número {numero} é divisível por 5")
else:
    print(f"O número {numero} não é divisível por 5")