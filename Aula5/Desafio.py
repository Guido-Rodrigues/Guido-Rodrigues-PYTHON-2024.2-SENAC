#Fala um programa que: pergunte se o usuario quer um combo ou 1 item individual. Onde:
#Hamburguer custa R$ 10.00
#Batata frita custa R$ 10.00
#Refrigerante custa R$ 10.00
#O combo custa R$ 22.00
#O cliente pode adicionar 2 itens, mas caso faça, ofereça o 3o item por R$ 2.00, incentivando e vendendo indiretamente o combo.

Vhamburguer = 10
VBatata = 10
Vrefri = 10
Vcombo = 22

subtotal = 0
entrada = int(input("Olá! Selecione um pedido:\n 0- Combo - R$ 22.00 \n 1- Customizado\n"))
if(entrada == 0):
    print("Você selecionou o Combo!")
    subtotal = subtotal + Vcombo
    print(f"Total: R$ {subtotal}")
elif(entrada <0 or entrada >1):
    print("Entrada inválida!!!")
else:
    contpedido = 0
    entrada2 = int(input("Ok! Selecione até 3 pedidos:\n 1- Hamburguer - R$ 10.00\n 2- Batata frita - R$ 10.00 \n 3- Refrigerante - R$ 10.00\n"))
    while(contpedido <2):
        if(entrada2 ==1):
            print("Você selecionou Hambúrguer")
            subtotal += Vhamburguer
            print(f"Subtotal: R$ {subtotal}")
            contpedido += 1

            
        elif(entrada2 ==2):
            print("Você selecionou Batata frita")
            subtotal += VBatata
            print(f"Subtotal: R$ {subtotal}")
            contpedido += 1
            
            
        elif(entrada2 ==3):
            print("Você selecionou Refrigerante")
            subtotal += Vrefri
            print(f"Subtotal: R$ {subtotal}")
            contpedido += 1
            
        else:
            print("Entrada inválida!!!")
            print(f"Subtotal: R$ {subtotal}")
        if(contpedido < 2):
            entrada2 = int(input())
    entrada3 = int(input(f"Parabéns! Ao fazer dois pedidos o terceiro sai por apenas R$ 2.00!\n0- Não quero pedir mais nada. Fechar pedido\n1- Adicionar hamburguer - R$ 2.00\n2- Adicionar batata frita - R$ 2.00\n3- Adicionar refrigerante - R$ 2.00"))
    while(contpedido <3):
        if(entrada3 < 0 or entrada3 > 3):
            print("Entrada inválida!")
            print(f"Subtotal: R$ {subtotal}")
        elif(entrada3 == 1):
            print("Você adicionou hamburguer")
            subtotal += 2        
            contpedido += 1
        elif(entrada3 == 2):
            print("Você adicionou batata frita")
            subtotal += 2            
            contpedido += 1
        else:
            print("Você adicionou refrigerante")
            subtotal += 2            
        if(contpedido <3):
            entrada3 = int(input())
    print(f"Pedido finalizado! Total: R$ {subtotal}")