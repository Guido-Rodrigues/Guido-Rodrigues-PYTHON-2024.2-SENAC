#Faça um programa que some infinitamente numeros que o usuario colocar e só pare de somar caso ele escreva "parar"

checkStop = 0
soma = 0

print("Por favor, insira um numero para somar. Insira 'parar' pra finalizar.")
checkStop = input()
while checkStop != "parar":
    soma += float(checkStop)    
    print(f"A soma é {soma}")
    checkStop = input()