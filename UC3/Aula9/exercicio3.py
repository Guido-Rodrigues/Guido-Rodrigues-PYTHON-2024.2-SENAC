import mysql.connector

config = {
  'user': 'python',
  'password': 'aula@123',
  'host': 'exemploaulacaio.mysql.database.azure.com',
  'database': 'escolasenac',
  'raise_on_warnings': True
}
cnx = mysql.connector.connect(**config)
cursor = cnx.cursor()

consultaUsuario = input("Insira o nome do usuario\n")
consultaSenha = input("Insira a senha do usuario\n")

query1 = ("SELECT nome,senha FROM usuario_secretaria WHERE nome=%s AND senha=%s")
cursor.execute(query1,(consultaUsuario,consultaSenha))

resultados = cursor.fetchone()
if resultados:
    print(f"Bem vindo(a) {resultados[0]}")
    # for nome,senha in resultados:
    #     print(f'Bem vindo(a) {nome}')
else:
    print("NENHUM USUARIO ENCONTRADO")

cursor.close()
cnx.close()