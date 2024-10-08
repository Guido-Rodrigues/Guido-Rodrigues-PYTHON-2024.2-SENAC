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
entrada = int(input("Olá! Selecione um pedido:\n 0- Combo - R$ 22.00 \n 1- Hamburguer - R$ 10.00\n 2- Batata frita - R$ 10.00 \n 3- Refrigerante - R$ 10.00\n"))
if(entrada == 0):
    print("Você selecionou o Combo!")
    subtotal = subtotal + Vcombo
    print(f"Subtotal: R$ {subtotal}")
elif(entrada <0 or entrada >3):
    print("Entrada inválida!!!")
else:
    contpedido = 0
    while(contpedido <1):
        if(entrada ==1):
            print("Você selecionou Hambúrguer")
            subtotal = subtotal + Vhamburguer
            print(f"Subtotal: R$ {subtotal}")
            contpedido = contpedido + 1
        elif(entrada ==2):
            print("Você selecionou Batata frita")
            subtotal = subtotal + VBatata
            print(f"Subtotal: R$ {subtotal}")
            contpedido = contpedido +1
        elif(entrada ==3):
            print("Você selecionou Refrigerante")
            subtotal = subtotal + Vrefri
            print(f"Subtotal: R$ {subtotal}")
