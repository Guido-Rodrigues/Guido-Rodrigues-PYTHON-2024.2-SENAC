#insira um numero para escolher a classe:

numero=int(input("digite um numero, 1 para barbaro, 2 para mago, 3 para arqueiro: "))

if numero==1:
        print(f"o numero {numero} pertence a classe barbaro")
        classe = "barbaro"
elif numero==2:
        print(f"o numero {numero} pertence a classe mago ")
        classe ="mago"
elif numero==3:
        print(f"o numero {numero} pertence a classe arqueiro")
        classe ="arqueiro"
else:
        print("Classe inválida")
        classe = "inválida"
        
        
print("Agora, insira um número para selecionar um equipamento, 1 para curto alcance e 2 para longo")
numero2 = int(input(""))
if(numero2==1):
        print(f"O numero {numero2} pertence ao equipamento de curto alcance")
        equipamento = "curto alcance"
elif(numero2==2):
        print(f"O numero {numero2} pertence ao equipamento de longo alcance")
        equipamento = "longo alcance"
else:
        print("Equipamento inválido")
        equipamento = "inválido"

if classe == "inválida" or equipamento == "inválido":
        print("Classe ou equipamento inválido, tente novamente!")
else:
        print(f"Você selecionou a classe {classe} e o equipamento de {equipamento}")