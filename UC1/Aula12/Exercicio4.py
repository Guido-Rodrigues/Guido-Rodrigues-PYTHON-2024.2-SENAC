#O aventureiro encontrou outro assaltante no caminho, mas agora que ele está mais treinado, imediatemente foi para o combate!

#Sabendo que cada personagem tem uma quantidade inicial de "Vida" e um valor de "Ataque". seguindo a seguinte estrutura:

aventureiro = [
    ["Vida", "Ataque","Sorte"],
    [1000, 20, 20]
]
assaltante = [
    ["Vida", "Ataque","sorte"],
    [600, 20, 20]
]

#A batalha segue as seguintes regras:

#O aventureiro e o assaltante atacam simultaneamente, causando dano um ao outro com o valor de "Ataque".
#A batalha continua até que a "Vida" de um dos personagens chegue a zero ou abaixo.
#Após cada rodada de ataque, o status de cada personagem (seus valores de "Vida" e "Ataque") deve ser exibido.
#Haverá um intervalo de 4 segundos entre as rodadas de ataque para simular a pausa entre os golpes.
#Ao final da batalha, o loop deve parar e os valores finais de "Vida" de ambos os personagens devem ser mostrados.

#Escreva o código para simular essa batalha e exiba o status de ambos os personagens a cada rodada de ataque.

##Faça uma variavel sorte, onde ela multiplica o ataque por até 20 de ambos os personagens. Aumente a vida deles em 10x

print("O aventureiro encontrou um assaltante! Uma batalha começou!")

import time
import random

while aventureiro[1][0] > 0 and assaltante[1][0] > 0:
    time.sleep(4)
    
    critico = random.randint(1,aventureiro[1][2])#checa critico
    dano = aventureiro[1][1]*critico
    print(f"O aventureiro golpeia! A vida do assaltante diminuiu em {dano}")
    assaltante[1][0] -= dano
    print("Status assaltante:")
    for i in assaltante:
        print(i)
    if assaltante[1][0] <= 0:
        vencedor = "aventureiro"
        break
    time.sleep(4)

    critico = random.randint(1,assaltante[1][2])#checa critico
    dano = assaltante[1][1]*critico
    print(f"O assaltante golpeia! A vida do aventureiro diminuiu em {dano}")
    aventureiro[1][0] -= dano
    print("Status aventureiro:")
    for i in aventureiro:
        print(i)
    if aventureiro[1][0] <= 0:
        vencedor = "assaltante"
        break
print(f"A batalha terminou! O {vencedor} venceu!")