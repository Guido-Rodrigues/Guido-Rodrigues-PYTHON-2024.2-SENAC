# Um aluno precisa de trasnfusao de sangue, consulte e retorne o nome e idade dos possiveis doadores sabendo que seu sangue é B+

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
query = "select nome, idade from aluno where tipo_sanguineo = 'B+' or tipo_sanguineo = 'B-' or tipo_sanguineo = 'O-' or tipo_sanguineo = 'O+';"

cursor.execute(query)

# Processar os resultados
resultados = cursor.fetchall()

# Printando nome e idade dos alunos
print('\nOs seguintes alunos são compatíveis:\n')
for nome, idade in resultados:
    print(f"{nome} - {idade} anos")



# Fechando o cursor e a conexão
cursor.close()
cnx.close()