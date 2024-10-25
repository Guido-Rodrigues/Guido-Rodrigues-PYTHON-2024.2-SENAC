'''
Peça ao usuário o tamanho do aro da bicicleta que ele quer comprar e com base nisso: 
Recomende o tamanho do guidão, da manete e do quadro da bicicleta
O tamanho do guidão será metade do tamanho do aro da roda
O tamanho da manete será 1/4 do tamanho do aro da roda
O tamanho do quadro será o mesmo do aro
'''
tamanhoAro = float(input("Por favor insira o tamanho do aro desejado: "))

tamanhoGuidao = tamanhoAro/2
tamanhoManete = tamanhoAro/4
tamanhoQuadro = tamanhoAro

print(f"O tamanho do guidão compatível é {tamanhoGuidao}")
print(f"O tamanho da manete compatível é {tamanhoManete}")
print(f"O tamanho do quadro compatível é {tamanhoQuadro}")