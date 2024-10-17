#Jogo do palpite:
#O sistema gera 1 numero aleatorio entre 1 e 200. O usuario tem 10 palpites para tentar acertar. O sistema sempre dá um feedback dizendo se o "Número secreto" é maior ou menor que o palpite do usuário.
#Adicione niveis de dificuldade:
#   fácil -> 10 tentativas
#   médio -> 7 tentativas
#   Difícil -> 5 tentativas
import random
numero_secreto = random.randint(1, 200)
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
#-------------------------------Loop de jogatina------------------------------------------
while palpites > 0:
    escolha = int(input(f"Escolha um número, você tem {palpites} palpites restantes!\n-->"))
    palpites -= 1
    if escolha > numero_secreto:
        print(f"NÃO! Numero secreto é MENOR que {escolha}!")
    elif escolha < numero_secreto:
        print(f"NÃO! Numero secreto é MAIOR que {escolha}!")
    else:
        print("Você acertou!")
        break
print(f"Fim de jogo! Você utilizou {10-palpites} palpites!")