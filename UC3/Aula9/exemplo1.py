import mysql.connector

config = {
  'user': 'python',
  'password': 'aula@123',
  'host': 'exemploaula.mysql.database.azure.com',
  'database': 'exemploaula',
  'raise_on_warnings': True
}
cnx = mysql.connector.connect(**config)

cursor = cnx.cursor()

idade_aluno = input("Digite a idade dos alunos que deseja buscar:")

#Consulta parametrizada
query1 = "SELECT nome, CPF, endereco FROM aluno WHERE idade = %s"
cursor.execute(query1, (idade_aluno,))

#armazenando os resultados da consulta
resultados = cursor.fetchall()
if resultados:
    for nome, cpf, endereco in resultados:
        print(f"Aluno: ({nome}), CPF: ({cpf}), Endereço: ({endereco})")
else:
    print("Nenhum aluno encontrado com essa idade.")

cursor.close()
cnx.close()