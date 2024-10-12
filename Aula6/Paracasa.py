import time
import threading

saldoTempo = 2
def encerrar_programa():
    print("\nO tempo acabou! Encerrando o programa...")
    exit()
threading.Timer(saldoTempo,encerrar_programa).start()

print("Bem-vindo ao programa de reciclagem!")
material = int(input("Selecione o tipo de material que deseja reciclar:\n1- Papel\n2- Plástico\n3- Vidro\n4- Metal\n5- Orgânico\n6- Resíduos não recicáveis\n->"))
papel = 0
plastico = 0
vidro = 0
metal = 0
organico= 0
outros = 0
loop = 1

while loop == 1:
    loop2 = 1 #Loop2 para não deixar o usuário passar com material inválido
    while loop2 == 1:
        if material == 1:
            print("O papel deve ser descartado na lixeira azul")
            papel += 1
            loop2 = 0
        elif material == 2:
            print("O plástico deve ser descartado na lixeira vermelha")
            plastico += 1
            loop2 = 0
        elif material == 3:
            print("O vidro deve ser descartado na lixeira verde")
            vidro += 1
            loop2 = 0
        elif material == 4:
            print("O metal deve ser descartado na lixeira amarela")
            metal += 1
            loop2 = 0
        elif material == 5:
            print("O material orgânico deve ser descartado na lixeira marrom")
            organico += 1
            loop2 = 0
        elif material == 6:
            print("Resíduos não recicláveis devem ser descartados na lixeira cinza")
            outros += 1
            loop2 = 0
        else:
            print("Entrada inválida! tente novamente!")
            material = int(input())
    repete = input("Deseja continuar reciclando? (S ou N)").lower()
    loop3 = 1 #Loop3 para não deixar o usuário passar sem escolher S ou N
    while loop3 == 1: 
        if(repete == "s"):
            loop = 1
            loop3 = 0
            material = int(input("Ok! Selecione o material para reciclar:\n->"))
        elif(repete == "n"):
            loop = 0
            loop3 = 0
        else:
            print("Entrada inválida! tente novamente!")
            repete = input()

print(f"Obrigado por contribuir com a reciclagem!\nVocê descartou:\n{papel} papel(is);\n{plastico} plástico(s);\n{vidro} vidro(s);\n{metal} metal(is);\n{organico} orgânico(s) e\n{outros} não recicláveis")