#Faça um programa onde o pikachu começa com uma lista de 4 poderes:
#Poderes = ["Choque do trovão","Calda de ferro","Ataque rapido","Esquiva"]
#Faça um programa que você ao aidiconar um novo poder, precisa remover outro. Ou seja, o Pikachu precisa ter sempre apenas 4 poderes!
import random
Poderes = ["Choque do trovão","Calda de ferro","Ataque rapido","Esquiva"]
listaPoderes = ["Growl","Nasty Plot","Nuzzle","Play Nice","Sweet Kiss","Tail Whip","Thunder Wave","Double Team","Electro Ball","Feint","Spark","Agility","Discharge","Thunderbolt","Light Screen","Thunder"]
novoPoder = random.choice(listaPoderes)
escolha = int(input(f"Pikachu está tentando aprender {novoPoder}!, deseja substituir um movimento?\n1- Choque do trovão |   2- Calda de ferro\n3- Ataque rápido |   4- Esquiva\n5- Cancelar\n-->"))
if escolha == 1:
    print(f"Pikachu aprendeu {novoPoder}!")
    Poderes[0] = novoPoder
elif escolha == 2:
    print(f"Pikachu aprendeu {novoPoder}!")
    Poderes[1] = novoPoder
elif escolha == 3:
    print(f"Pikachu aprendeu {novoPoder}!")
    Poderes[2] = novoPoder
elif escolha == 4:
    print(f"Pikachu aprendeu {novoPoder}!")
    Poderes[3] = novoPoder
elif escolha == 5:
    print(f"Pikachu decidiu não aprender {novoPoder}")
print(f"Agora pikachu tem esses poderes: \n1- {Poderes[0]} |   2- {Poderes[1]}\n3- {Poderes[2]} |   4- {Poderes[3]}")