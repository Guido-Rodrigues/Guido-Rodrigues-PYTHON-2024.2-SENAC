#Faça um programa que peça para o usuario 1 numero e imprima todos os numeros menores que esse numero
entrada = int(input("Por favor, insira um número natural:\n"))
print(f"Os seguintes números naturais são menores que {entrada}:")
if(entrada < 0):
    print("Numero inválido!")
else:
    while entrada > 0:
        entrada -= 1
        print(entrada)

#Segunda solução, para que a ela não fique saturada:
#lista = []
#entrada = int(input("Por favor, insira um número natural:\n"))
#print(f"Os seguintes números naturais são menores que {entrada}:")
#if(entrada < 0):
#    print("Numero inválido!")
#else:
#    while entrada > 0:
#        entrada -= 1
#        lista.append(entrada)
#    print(lista)