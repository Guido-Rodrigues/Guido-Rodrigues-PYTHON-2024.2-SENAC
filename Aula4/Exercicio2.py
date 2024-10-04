#Faça um programa que pergunte quantas rodas tem um veiculo, 
#Se tiver 1 diga que é um monociclo
#Se tiver 2 diga que é uma moto ou bicicleta
#se tiver 4 diga que é um carro ou van. 
#Se tiver 6 rodas é um onibus. 
#Se tiver entre 8 e 20 rodas, provavelmente é um caminhão. 
#Caso o contrario, avise o usuario que não foi encontrado um veiculo correspondente ao numero de rodas
quantRoda = int(input("Insira a quantidade de rodas em seu veículo: "))
if quantRoda == 4:
    print("Seu veículo provavelmente é um carro ou van")
elif (quantRoda == 1):
    print("Seu veículo provavelmente é um monociclo")
elif (quantRoda ==2):
    print("Seu veículo provavelmente é uma moto ou bicicleta")
elif (quantRoda ==6):
    print("Seu veículo provavelmente é um ônibus")
elif (quantRoda >=8 and quantRoda <=20):
    print("Seu veículo provavelmente é um caminhão")
else:
    print("Não foi possível encontrar um veículo correspondente ao numero de rodas fornecido")


#Responda: Se eu colocar rodas e RoDAS dentro de uma condição é a mesma coisa?
    
rodas = input("insira rodas: ")
RoDAS = input("Insira RoDAS: ")

print(f"{rodas} e {RoDAS}")

#Não, a caixa alta importa e diferencia as duas.