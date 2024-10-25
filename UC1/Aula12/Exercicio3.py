# Após a aventura da aula passada, o aventureiro resolveu treinar mais seu combate; faça uma simulação onde o aventureiro tem uma lista [100,20], onde 100 é a vida dele e 20 é o poder de ataque dele e a cada 7 segundos de treino, ele aumenta o seu poder de ataque em 1 com o limite máximo de 30 para o seu poder de ataque.
import time

playerStats = [100,20]

treinando = True
print("Começando treinamento...")
while treinando == True and playerStats[1]<30:
    time.sleep(7)
    playerStats[1] += 1
    print(f"O ataque do aventureiro aumentou +1!\nAtaque: {playerStats[1]}")
print("O aventureiro terminou seu treino!")