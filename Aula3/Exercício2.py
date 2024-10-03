#Peça para o usuario o seu peso em Quilos e sua altura em Metros.
#Com base nisso, retorne para ele o seu IMC
print("Por favor, insira seu peso em quilogramas (KG)")
peso = float(input())
print("Por favor, insira sua altura em metros (M)")
altura = float(input())
IMC = peso/(altura*altura)
print(f"Seu índice de massa corporal é de `{IMC}")