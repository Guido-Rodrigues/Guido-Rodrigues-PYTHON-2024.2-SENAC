#Faça um programa que calcule o IMC do usuário e de a classificação conforme a seguinte tabela:
#18,5>imc => magreza
#24,9>imc>18,5 => normal
#29,9>imc>25 => sobrepeso
#39,9>imc>30 => obesidade
#imc>=40 => obesidade grave

#Calculo do IMC: imc = peso/altura^2

peso = float(input("Favor, insira o seu peso: "))
altura = float(input("Favor, insira sua altura: "))
imc = peso/(altura*altura)

print(f"Seu IMC é {imc}")
if (imc < 18.5 and imc>0):
    print("Isso indica MAGREZA")
elif(imc>=18.5 and imc <25):
    print("Isso indica situação NORMAL")
elif(imc>=25 and imc<30):
    print("Isso indica SOBREPESO, grau de obesidade 1")
elif(imc>=30 and imc<40):
    print("Isso indica OBESIDADE, grau de obesidade 2")
elif(imc<=0):
    print("IMC invalido!!")
else:
    print("Isso indica OBESIDADE GRAVE, grau de obesidade 3")