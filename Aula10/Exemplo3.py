import random
#Gerando 4 numeros aleatorios e armazenando em uma lista
numeros = [random.randint(20,50) for i in range(40)]
#Exibindo os numeros gerados
print(f"Numeros gerados: {numeros}")
#Ordenando os numeros com a função sort
numeros.sort()
numeros.reverse()

print(f"Numeros ordenados: {numeros}")