#Faça um programa que simule o armario de uma escola e permita colocar o nome do aluno responsável/pagante da gaveta. o armario tem a dimensão 5x5.
"""
armario = [
    ["","","","",""],
    ["","","","",""],
    ["","","","",""],
    ["","","","",""],
    ["","","","",""]
]

nome = input("Qual o nome do responsável/pagante da gaveta?\n-->")
linhaArmario = int(input("Qual a fileira do armario em que a gaveta está?\n-->"))
colunaArmario = int(input("Qual a coluna do armario em que a gaveta está?\n-->"))

armario[linhaArmario][colunaArmario] = nome

#print(armario)

for i in armario:
    print (i)
"""
#A escola adicionou um novo armario 3x3 perto das salas de aula e o chamou de armario vip. Caso o aluno adquira uma gaveta no armario comum, custará R$ 30,00 ai mês. O vip custará R$ 50,00. Adicione no sistema essa seleção e retorne para o usuario o custo
    
armario = [
    ["","","","",""],
    ["","","","",""],
    ["","","","",""],
    ["","","","",""],
    ["","","","",""]
]
armarioVip = [
    ["","",""],
    ["","",""],
    ["","",""]
]

loop = True
while loop == True:
    modo = int(input("Em qual armario deseja alugar uma gaveta?\nDigite 1 para armario comum (R$ 30,00/m)\nDigite 2 para armario vip (R$ 50,00/m)\n-->"))
    if modo not in (1,2):
        print("Entrada inválida! Por favor tente novamente: ")
    else:
        loop = False

nome = input("Qual o nome do responsável/pagante da gaveta?\n-->")

loop = True
while loop == True:    
    linhaArmario = int(input("Qual a fileira do armario em que a gaveta está?\n-->"))
    colunaArmario = int(input("Qual a coluna do armario em que a gaveta está?\n-->"))
    if modo == 1:
        if linhaArmario >= len(armario) or colunaArmario >= len(armario):
            print("A gaveta selecionada não existe! Por favor tente novamente: ")
        else:
            loop = False
    if modo == 2:
        if linhaArmario >= (len(armarioVip)) or linhaArmario >= len(armarioVip):
            print("A gaveta selecionada não existe! Por favor tente novamente: ")
        else:
            loop = False

print("Este é o armario e gaveta que selecionou:")
if modo ==1:
    armario[linhaArmario][colunaArmario] = nome
    subtotal = 30
    print("===Armario comum===")
    for i in armario:
        print (i)
    print("===================")
elif modo ==2:
    armarioVip[linhaArmario][colunaArmario] = nome
    subtotal = 50
    print("===Armario VIP===")
    for i in armarioVip:
        print (i)
    print("===================")
print(f"O valor final do pedido é R$ {subtotal}!")