# Refaça o programa do exericico1 usando "if in"

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
