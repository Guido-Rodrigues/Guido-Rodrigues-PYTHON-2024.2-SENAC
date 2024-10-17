#Jogo do palpite:
#O sistema gera 1 numero aleatorio entre 1 e 200. O usuario tem 10 palpites para tentar acertar. O sistema sempre dá um feedback dizendo se o "Número secreto" é maior ou menor que o palpite do usuário.
#Adicione niveis de dificuldade:
#   fácil -> 10 tentativas
#   médio -> 7 tentativas
#   Difícil -> 5 tentativas
#Para casa: Adicione ao jogo da adivinhação a opção de colocar mais 1 ou 2 números para serem advinhados simultaneamente
import random
numero_secreto1, numero_secreto2, numero_secreto3 = random.randint(1, 200), random.randint(1, 200), random.randint(1, 200)
numeros_secretos = [numero_secreto1, numero_secreto2, numero_secreto3]
pontuavel = [True, True, True] #Mantem registro se o nº número secreto pode ou não dar pontos ao usuário. EVITA ABUSOS
##print (numero_secreto1, numero_secreto2, numero_secreto3) #TESTE VISUALIZAR RESPOSTAS
#-------------------------------Seleção de dificuldade------------------------------------------
selecTent = int(input("Selecione o nível de dificuldade:\n1- Fácil\n2- Médio\n3- Difícil\n-->"))
if selecTent == 1:
    palpites = 10
elif selecTent == 2:
    palpites = 7
elif selecTent == 3:
    palpites = 5
else:
    print("Entrada inválida!")
    exit()
#-------------------------------Opção de colocar mais 1 ou 2 números----------------------------
selecNum = int(input("Selecione o modo de jogo.\n1- 1 número\n2- 2 números\n3- 3 números\n-->"))
if selecNum != 1 and selecNum != 2 and selecNum != 3:
    print("Entrada inválida!")
    exit()
#-------------------------------Loop de jogatina------------------------------------------------
acertos = 0
while palpites > 0 and acertos < selecNum:
    #---------------------------Pede entrada do usuario até 3 vezes----------------------------- #Caso queira adicionar mais numeros, vai precisar alterar os tamanhos das listas pontuavel e numeros_secretos.
    entradas = []
    for i in range (selecNum):
        if pontuavel[i] == True:
            entrada = int(input(f"Você tem {palpites} palpites restantes! Insira o palpite para o {i+1}º número:\n-->"))
            entradas.append(entrada)
        else:
            entradas.append(0)
##        print(f"=={entradas}==") #TESTE VISUALISAR ENTRADAS DO USUARIO
    #---------------------------Compara nª entrada com nº numero secreto------------------------
    for i in range(selecNum):
        if pontuavel[i] == True:
            if entradas[i] == numeros_secretos[i]:
                print(f"Você acertou o {i+1}º número! A resposta era {numeros_secretos[i]}!")
                acertos += 1
                pontuavel[i] = False
##                print(pontuavel) #TESTE VISUALISAR LISTA PONTUAVEL
            elif entradas[i] > numeros_secretos[i]:
                print(f"O {i+1}º número secreto é MENOR que {entradas[i]}")
            elif entradas[i] < numeros_secretos[i]:
                print(f"O {i+1}º número secreto é MAIOR que {entradas[i]}")
    palpites -= 1
print(f"Fim de jogo! Você utilizou {10-palpites} palpites!")