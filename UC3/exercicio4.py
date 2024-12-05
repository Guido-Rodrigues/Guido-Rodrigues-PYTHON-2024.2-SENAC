# Faça uma consulta que retorne o cpf dos estudantes que tem os 2 responsaveis cadastrados no BD.

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
query = "select nome, CPF, cpf_responsavel1, cpf_responsavel2 from aluno;"
cursor.execute(query)

resultados = cursor.fetchall()

# printando os homens cariocas:
print('\nOs seguintes alunos possuem ambos os responsáveis cadastrados no DB:\n')
for nome, cpf, cpf_responsavel1, cpf_responsavel2 in resultados:
    if cpf_responsavel2 != "NULL" and cpf_responsavel1 != "NULL":
        print(f"{nome} - CPF: {cpf}")

# Fechando o cursor e a conexão
cursor.close()
cnx.close()