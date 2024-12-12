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
cursor.execute("SET sql_safe_updates=0;")

# Confirmar a alteração
cnx.commit()
Nusuario = input('Insira o nome do usuario a ser adicionado\n')
Nsenha = input('Insira a senha do usuario a ser adicionado\n')


query1 = "INSERT INTO usuario_secretaria (usuario,senha) VALUES (%s,%s)"
cursor.execute(query1, (Nusuario,Nsenha,))
cnx.commit()

query2 = "SELECT * FROM usuario_secretaria"
cursor.execute(query2)
resultados = cursor.fetchall()
if resultados:
    for id,nome,senha in resultados:
        print(f'ID = {id}, NOME = {nome}, SENHA = {senha}')
else:
    print('Nenhum usuario encontrado')

cursor.close()
cnx.close()