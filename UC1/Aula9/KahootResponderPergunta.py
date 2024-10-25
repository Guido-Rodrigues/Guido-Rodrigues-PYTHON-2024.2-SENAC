# Exercicio simbolico de gerenciadores de projetos, no caso é o trello
#O sistema deve mostrar perguntas para o usuário e depois retornar se ele acertou ou errou.

jogarNovamente = True
while jogarNovamente == True:
    ponto = 0
    resposta = input("Python é uma linguagem de programação de alto nível?: ")
    if resposta == "verdadeiro":
        print("Acertou!")
        ponto+=1
    else:
        print("Errou! Python é projetada para ser fácil de ler e escrever, com uma sintaxe pouco parecida com as linguagens de baixo nível como C ou Assembly.")

    resposta = input("O símbolo # é usado para comentários em Python?: ")
    if resposta == "verdadeiro":
        print("Acertou!")
        ponto+=1
    else:
        print("Errou! O símbolo # é sim usado para destacar qualquer texto após como comentário")

    resposta = input("Listas em Python podem conter elementos de diferentes tipos?: ")
    if resposta == "verdadeiro":
        print("Acertou!")
        ponto+=1
    else:
        print("Errou! Listas em python podem sim conter elementos de diferentes tipos. Exemplo: minha_lista = [1, 'texto', 3.14, True, [1, 2, 3]]")

    if ponto >= 1.5:
        print("Você ganhou! :)")
    else:
        print("Você perdeu! :(")

    x = input("Deseja jogar novamente? 'sim' ou 'não'\n").lower()
    if x == "não":
        jogarNovamente = False

print("Fim de jogo!")