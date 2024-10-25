#Jogo do palpite:
#O sistema gera 1 numero aleatorio entre 1 e 200. O usuario tem 10 palpites para tentar acertar. O sistema sempre dá um feedback dizendo se o "Número secreto" é maior ou menor que o palpite do usuário.
#Adicione niveis de dificuldade:
#   fácil -> 10 tentativas
#   médio -> 7 tentativas
#   Difícil -> 5 tentativas
#Para casa: Adicione ao jogo da adivinhação a opção de colocar mais 1 ou 2 números para serem advinhados simultaneamente
import random
numero_secreto1, numero_secreto2, numero_secreto3 = random.randint(1, 200), random.randint(1, 200), random.randint(1, 200)
print (numero_secreto1, numero_secreto2, numero_secreto3)
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
if selecNum == 1:
    #-------------------------------Loop de jogatina 1------------------------------------------
    while palpites > 0:
        escolha = int(input(f"Escolha um número, você tem {palpites} palpites restantes!\n-->"))
        palpites -= 1
        if escolha > numero_secreto1:
            print(f"NÃO! Numero secreto é MENOR que {escolha}!")
        elif escolha < numero_secreto1:
            print(f"NÃO! Numero secreto é MAIOR que {escolha}!")
        else:
            print("Você acertou!")
            break
    print(f"Fim de jogo! Você utilizou {10-palpites} palpites!")
elif selecNum == 2:
    #-------------------------------Loop de jogatina 2------------------------------------------
    acertos = 0
    while palpites > 0 and acertos < 2:
        escolha = int(input(f"Escolha dois números, você tem {palpites} palpites restantes!\n-->"))
        escolha2 = int(input("-->"))
        palpites -= 1
        if escolha > numero_secreto1:
            print(f"O 1º número secreto é MENOR que {escolha}!")
        elif escolha < numero_secreto1:
            print(f"O 1º número secreto é MAIOR que {escolha}!")
        else:
            print("Você acertou o 1º número secreto!")
            acertos += 1
        if escolha2 > numero_secreto2:
            print(f"O 2º número secreto é MENOR que {escolha2}!")
        elif escolha2 < numero_secreto2:
            print(f"O 2º número secreto é MAIOR que {escolha2}!")
        else:
            print("Você acertou o 2º número secreto!")
            acertos += 1
    print(f"Fim de jogo! Você utilizou {10-palpites} palpites!")
elif selecNum == 3:
    #-------------------------------Loop de jogatina 3------------------------------------------
    acertos = 0
    while palpites > 0 and acertos < 3:
        escolha = int(input(f"Escolha três números, você tem {palpites} palpites restantes!\n-->"))
        escolha2 = int(input("-->"))
        escolha3 = int(input("-->"))
        palpites -= 1
        if escolha > numero_secreto1:
            print(f"O 1º número secreto é MENOR que {escolha}!")
        elif escolha < numero_secreto1:
            print(f"O 1º número secreto é MAIOR que {escolha}!")
        else:
            print("Você acertou o 1º número secreto!")
            acertos += 1
        if escolha2 > numero_secreto2:
            print(f"O 2º número secreto é MENOR que {escolha2}!")
        elif escolha2 < numero_secreto2:
            print(f"O 2º número secreto é MAIOR que {escolha2}!")
        else:
            print("Você acertou o 2º número secreto!")
            acertos += 1
        if escolha3 > numero_secreto3:
            print(f"O 3º número secreto é MENOR que {escolha3}")
        elif escolha3 < numero_secreto3:
            print(f"O 3º número secreto é MAIOR que {escolha3}")
        else:
            print("Você acertou o 3º número secreto!")
            acertos += 1
    print(f"Fim de jogo! Você utilizou {10-palpites} palpites!")
else:
    print("Entrada inválida!")



#FALTA: parar de acrescentar valor á variavel acertos caso o numero já tenha sido descoberto, do jeito que está o usuario pode descobrir apenas um e abusar escrevendo o mesmo numero varias vezes pra ganhar
#Talvez seja melhor reescrever o programa inteiro