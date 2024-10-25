#Faça um programa que peça dois numeros e faça uma operação com base no seguinte menu:
# 1- Soma dois numeros
# 2- Subtrai dois numeros
# 3- Multiplica dois numeros
# 4- Divide dois numeros
n1 = float(input("Selecione o primeiro numero: "))
n2 = float(input("Selecione o segundo numero: "))
opSelect = int(input("Selecione a operação desejada\n1- Somar\n2- Subtrair \n3- Multiplicar\n4- Dividir\n"))
check = 0
while check == 0:
    #SOMA
    if(opSelect ==1):
        print(f"A soma entre os dois numeros é {n1+n2}")
        check = 1
    #SUBTRAÇÃO
    elif(opSelect ==2):
        print(f"A subtração entre os dois numeros é {n1-n2}")
        check = 1
    #MULTIPLICAÇÃO
    elif(opSelect ==3):
        print(f"A multiplicação entre os números é {n1*n2}")
        check = 1
    #DIVISÃO
    elif(opSelect ==4):
        print(f"A divisão entre os números é {n1/n2}")
        check = 1
    else:
        print("Entrada inválida! Selecione novamente:\n")
        opSelect = int(input())