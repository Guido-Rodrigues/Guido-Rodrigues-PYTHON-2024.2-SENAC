#Faça um programa que calcule o tamanho do sapato de um cachorro sabendo que sempre será o dobro do tamanho da coleira dele. 
#Calcule também o tamanho da pata do cachorro
#Calcule também o tamanho da fucinheira sabendo que é o triplo do tamanho do sapato.
#O programa deverá pedir o tamanho da coleira do cachorro do usuário e retornar o tamanho do sapato e da fucinheira que o dono deverá comprar.

print("Olá, insira o tamanho da coleira de seu cachorro")
valorColeira = float(input())
valorSapato = 2*valorColeira
valorFucinheira = 3*valorSapato
print(f"Seu cachorro veste Sapato tamanho {valorSapato} e Fucinheira tamanho {valorFucinheira} ")
