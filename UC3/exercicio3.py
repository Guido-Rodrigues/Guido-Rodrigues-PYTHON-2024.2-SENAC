# Faça uma consulta na tabela aluno onde retorne todos os alunos homens e cariocas, depois retorne todas as alunas mulheres e paulistas .

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
query = "select nome, sexo, naturalidade from aluno;"
cursor.execute(query)

resultados = cursor.fetchall()

# printando os homens cariocas:
print('\nPRIMEIRA QUERY:\n')
for nome, sexo, naturalidade in resultados:
    if sexo == "M" and naturalidade == "Rio de Janeiro":
        print(f"O aluno {nome} é um homem carioca")
print('\nSEGUNDA QUERY:\n')
for nome, sexo, naturalidade in resultados:
    if sexo == "F" and naturalidade == "São Paulo":
        print(f"A aluna {nome} é uma mulher paulistana")

# Fechando o cursor e a conexão
cursor.close()
cnx.close()