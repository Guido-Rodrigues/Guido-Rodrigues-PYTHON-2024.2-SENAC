#Faça uma consulta simples na tabela aluno onde retorne o nome e o endereço dos alunos

import mysql.connector

# Conexão com o banco de dados
cnx = mysql.connector.connect(
    user="python",
    password="aula@123",
    host="exemploaula.mysql.database.azure.com",
    port=3306,
    database="exemploaula",  
    ssl_disabled=True     
)

# Criação do cursor
cursor = cnx.cursor()

# Consulta
query = "select nome, endereco from aluno;"

cursor.execute(query)

# Processar os resultados
resultados = cursor.fetchall()

# Printando nome e endereço dos alunos
for nome, endereco in resultados:
    print(f"Nome: {nome} | Endereço: {endereco}")



# Fechando o cursor e a conexão
cursor.close()
cnx.close()