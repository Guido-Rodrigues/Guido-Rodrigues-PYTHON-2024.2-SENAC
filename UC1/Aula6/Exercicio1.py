#Faça um programa que conte de 0 a 10 e diga no final "Obrigado por esperar! estamos redirecionando sua ligação."
import time

contador = 0

while contador < 10:
    contador += 1
    print(f"{contador}\n")
    time.sleep(1)
print("Obrigado por esperar! estamos redirecionando sua ligação")