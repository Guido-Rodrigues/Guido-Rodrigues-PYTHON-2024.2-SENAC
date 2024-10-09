import time
print("Iniciando contagem regressiva")
contador = 5

while contador > 0:
    print(contador)
    time.sleep(1)
    contador -=1

print("Fim da contagem regressiva! Boom!")