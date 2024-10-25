#multiplica numeros 
x = 0
multiplica = 1 #importante porque na multiplicação o elemento neutro é 1
while x<3:
    numero = float (input("Entre com numero:"))

    multiplica *= numero
    print(f"A multiplicação é {multiplica}")
    x+=1