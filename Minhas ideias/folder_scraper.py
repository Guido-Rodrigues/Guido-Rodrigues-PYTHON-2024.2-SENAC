import glob
import os

print("Esse script irá extrair os nomes de todos os itens dentro de um endereço e escreve-los em um arquivo determinado. Tenha em mente que pastas também serão consideradas, se quiser impedir um arquivo ou pasta de ter seu nome escrito, renomeie-o colocando um '.' no inicio do arquivo")
pasta = str(input("Insira o caminho da pasta a ser analisada.\n-->"))
caminho_alvo = str(input("Insira o caminho do arquivo a ser injetado com os nomes.\n-->"))

arquivos = glob.glob(f'{pasta}/*')
arquivos2 = ""


# Pega o nome de todos os arquivos no endereço dentro da variavel "pasta" e os escreve em um arquivo no endereço dentro da variavel "caminho_arquivo"
for i in arquivos:
    arquivos2 += os.path.basename(i) + "\n"

print(arquivos2)

with open(caminho_alvo, 'w', encoding='utf-8') as arquivo:
    arquivo.write(arquivos2)

print("FIM!")