#Faça um programa para um lava rapido onde:
#1- Lavagem completa a R$50.00
#2- Lavagem básica a R$35.00
#Caso o usuário queira, o pretinho custa mais R$ 5.00
#Retorne o serviço + o valor dele


#Cria variavel para acompanhar o estado da seleção do serviço pretinho e o valor do pedido:
Selecpretinho = 0
Vpedido = 0
#Pede o input do usuário, o valor deve ser 1 ou 2.
print("Olá escolha um serviço:\n1- Lavagem completa: R$ 50.00\n2- Lavagem básica: R$ 35.00")
entrada = int(input())
#Retorna erro caso o valor não seja 1 ou 2
if(entrada <1 or entrada >2):
    print("Entrada inválida!")
#Caso o valor seja 1 registra o preço na variavel do valor do pedido e oferece o "pretinho"
else:
    if(entrada ==1):
        Vpedido = Vpedido + 50
        print("Gostaria de adicionar o pretinho por mais R$ 5.00? (S ou N)")
        #Espera input do usuario, S ou N, caso S adiciona o valor na variavel citada e depois apresenta o total.
        Selecpretinho = input()
        if(Selecpretinho == "S"):
            Vpedido = Vpedido + 5
            print(f"Você escolheu Lavagem completa com pretinho. Total: R$ {Vpedido}")
        elif(Selecpretinho == "N"):
            print(f"Você escolheu Lavagem completa sem pretinho Total: R$ {Vpedido}")
            #Retorna erro caso o valor do input não seja S ou N
        else:
            print("Entrada inválida!!!")
            #Caso o valor não seja 1, o pedido só pode ser Lavagem básica, é adicionado então o valor à variável e oferece o "pretinho"
    else:
        Vpedido = Vpedido + 35
        print("Gostaria de adicionar o pretinho por mais R$ 5.00? (S ou N)")
        #Espera input do usuario, S ou N, caso S adiciona o valor na variavel citada e depois apresenta o total.
        Selecpretinho = input()
        if(Selecpretinho == "S"):
            Vpedido = Vpedido + 5
            print(f"Você escolheu Lavagem básica com pretinho. Total: R$ {Vpedido}")
        elif(Selecpretinho =="N"):
            print(f"Você selecionou lavagem básica sem pretinho. Total: R$ {Vpedido}")
            #Retorna erro caso o valor do input não seja S ou N
        else:
            print("Entrada inválida!!!")