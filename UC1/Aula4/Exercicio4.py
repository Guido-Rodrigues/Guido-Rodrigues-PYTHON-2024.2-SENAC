#Faça um programa que diga se um numero é par ou impar
numero=int(input("Por favor, insira um número: "))
if (numero%2 == 0):
    print("O número é PAR")
else:
    (print("O número é IMPAR"))




#Outra solução
checkpar = numero/2
Resto = checkpar-int(checkpar)
if (Resto == 0):
    print("O numero é PAR")
else:
    print ("O número é IMPAR")