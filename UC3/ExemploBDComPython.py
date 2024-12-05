import mysql.connector

# Connect to server
cnx = mysql.connector.connect(
    user="aluno",
    password="aula@123",
    host="aulabackend.mysql.database.azure.com",
    port=3306,
    database="escoladb",  
)


# Get a cursor
cursor = cnx.cursor()

# Execute a query
query = "SELECT nome FROM alunos WHERE data_nascimento > '2005-01-01';"
cursor.execute(query)

# Fetch and print all results
for row in cursor.fetchall():
    print(row)

cursor.close()
cnx.close()