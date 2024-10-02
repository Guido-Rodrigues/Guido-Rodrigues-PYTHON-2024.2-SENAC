#Faça um programa que calcule o IPVA de um carro com base no valor do mesmo. O IPVA é 4% do valor do carro.
print("Insira o valor do carro")
valorcarro = float(input())
valorIPVA = valorcarro*0.04
print(f"O valor do IPVA é de R${valorIPVA}")