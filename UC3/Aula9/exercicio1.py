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

idademenor = input("Digite a menor idade a ser buscada")
idademaior = input("Digite a maior idade a ser buscada")
query1 = "SELECT nome,idade,idturma,alergias FROM aluno WHERE idade >= %s and idade <= %s order by idade"
cursor.execute(query1, (idademenor,idademaior,))

resultados = cursor.fetchall()
if resultados:
    for nome,idade,idturma,alergias in resultados:
        if(alergias != "Leite"):
            print(f"Nome: {nome}, idade: {idade}, Turma: {idturma}")
else:
    print("Nenhum(a) aluno(a) encontrado(a) com esse intervalo de idade")


cursor.close()
cnx.close()