#Criando uma lista simples com 3 pokemons
pokemons = ["Pikachu","Charmander","Bulbasaur"]

#Exibindo a lista
print("Lista de pokemons:", pokemons)

#Acessando o primeiro Pokemon da lista
print("Primeiro pokemon:", pokemons[0])

#Adicionando um novo Pokemon à lista
pokemons.append("Squirtle")
print("Lista de pokemons após adicionar Squirtle:", pokemons)

#Removendo o pokemon "Charmander" da lista
pokemons.remove("Charmander")
print("Lista de Pokemons após remover Charmander:", pokemons)

#Exibindo o tamanho da lista
print("Numero de Pokemons na lista:", len(pokemons))