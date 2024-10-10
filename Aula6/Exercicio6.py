#Faça um programa que mostre todos os numeros impares entre 50 e 100.

n1 = int(input("Selecione o primeiro numero: "))
n2 = int(input("Selecione o segundo numero: "))

print(f"Os numeros impares entre {n1} e {n2} são:")
if(n1<n2):
    while n1<=n2:
        if n1%2 !=0:
            print(n1)
            n1 += 1
        else:
            n1 +=1
else:
    while n2<=n1:
        if(n2%2 !=0):
            print(n2)
            n2 += 1
        else:
            n2 += 1