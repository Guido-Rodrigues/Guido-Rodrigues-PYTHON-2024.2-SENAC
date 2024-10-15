#Faça um programa que diga quais dos 20 primeiros multiplos de 5 são pares e some os impares
soma = 0
for i in range (5, 101):
    if i%5 == 0:
        if i%2 ==0:
            print(f"{i} é PAR!")
        else:
            soma += i
print(f"A soma dos numeros impares multiplos de 5 até 100 é {soma}")


#Outra solução
soma = 0
for i in range (5, 101, 5):
    if i%2 ==0:
        print(f"{i} é PAR!")
    else:
        soma +=i
print(f"A soma dos numeros impares multiplos de 5 até 100 é {soma}")
'''
#Outra solução!

for i in range (10, 101, 10):
    print(f"{i} é PAR!")

'''