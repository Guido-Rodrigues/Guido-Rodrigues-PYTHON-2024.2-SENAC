#Continuação exercicio2
#Enquanto você segue seu caminho na floresta, um bandido armado surge e exige sua poção.
#Você tem a opção de sacar sua espada e enfrentar o bandido ou entregar a sua poção ao bandido.
#Se tentar lutar contra ele sem espada, você perde a batalha e o jogo.
#Se tiver com você, ganha e segue o jogo.
#Se entregar a poção, você fica sem e segue o jogo.
#Mas se disser que irá entregar a poção sem tê-la no inventário, o bandido ficará furioso e será fim de jogo.
# Caso escolha uma opção inválida o baniddo se aproveita de sua hesitação e lhe ataca, resultado em fim de jogo.

import time
import random

conteudoMochila = ["Espada","Poção","Escudo"]
conteudoAchavel = ["Arco","Espada"]

#for i in range (3):
#    time.sleep(1)
#    print(f"{i+1}...")

conteudoAchado = random.choice(conteudoAchavel)
entrada = input(f"Você encontrou um {conteudoAchado}! Deseja coloca-lo na mochila?\n-->").lower()
if entrada == "sim":
    if conteudoAchado in conteudoMochila: #Aqui o if in que foi pedido no exercicio.
        print(f"{conteudoAchado} já está na mochila! Nada será feito...")
        exit()
    if len(conteudoMochila) == 3:
        entrada2 = int(input(f"Sua mochila está cheia! Escolha um item para descartar:\n1- {conteudoMochila[0]}\n2- {conteudoMochila[1]}\n3- {conteudoMochila[2]}.\n-->"))
        loop = True
        while loop == True:
            if entrada2 == 1:
                removerEscolha = conteudoMochila[0]
                loop = False
            elif entrada2 == 2:
                removerEscolha = conteudoMochila[1]
                loop = False
            elif entrada2 == 3:
                removerEscolha = conteudoMochila[2]
                loop = False
            else:
                entrada2 = int(input("Escolha inválida! Tente novamente!\n-->"))
        conteudoMochila.remove(removerEscolha)
#        for i in range (3):
#            time.sleep(1)
#            print(f"{i+1}...")
        print(f"{removerEscolha} foi removido da mochila!")
        print(conteudoMochila) # TESTE
    
    conteudoMochila.append(conteudoAchado)
#    for i in range (3):
#        time.sleep(1)
#        print(f"{i+1}...")
    print(f"{conteudoAchado} foi adicionado à mochila!")
    print(conteudoMochila) #TESTE
        
elif entrada == "não":
    print(f"Você escolheu não colocar {conteudoAchado} na mochila!")
else:
    print("Entrada inválida!")
#--------------COMEÇO EXERCICIO 2.1------------#
print("Enquanto você segue seu caminho na floresta, um bandido armado surge e exige sua poção!")
entrada = int(input(f"O que você fará?\n1- Sacar sua espada e atacar primeiro!\n2- Você conhece suas limitações, entregar a poção...\n-->"))

if entrada == 1:
    if "Espada" in conteudoMochila:
        print("Você saca sua espada e ataca o bandido!\nVocê vence a batalha e poupa consegue poupar sua poção!")
    else:
        print("Você tenta sacar sua espada mas não a encontra!! O bandido usa a oportunidade e te ataca em seu momento de hesitação!\n\n FIM DE JOGO \n\n")
        exit()
elif entrada == 2:
    if "Poção" in conteudoMochila:
        print("Você abre sua mochila e tenta pegar a poção...\nVocê encontra a poção e a entrega para o bandido, ele lhe deixa ir embora sem nenhum arranhão.")
        conteudoMochila.remove("Poção")
        print(conteudoMochila) #TESTE
    else:
        print("Você abre sua mochila e tenta pegar a poção mas não encontra!\nO bandido percebeu que você não tem o que ele quer e ficou furioso!\nO bandido decidiu que não quer testemunhas...\n\n FIM DE JOGO \n\n")
        exit()
else:
    print("Você escolheu uma opção inválida, o bandido se aproveitou de seu momento de indecisão e lhe atacou primeiro!\n\n FIM DE JOGO \n\n")
    exit()

print("To be continued...")