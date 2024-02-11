#Dicionários em Python também representam um conjunto de valores, porém
#essa representação se dá por meio de um mapeamento chave:valor. Os dicionários
#são criados utilizando as chaves { }.
#Imagine que queremos armazenar nomes de pessoas e suas respectivas idade,
#podemos usar um dicionário para fazer isso, veja o exemplo:

nome_idade={"edvaldo":29, "eduardo":29, "ju":30}
print(nome_idade)
print(nome_idade["edvaldo"])
nome_idade["pedro"]=55 #adiconando mais um elemento
print(nome_idade)
print(len(nome_idade))# ordena a lista
print(nome_idade.keys()) #retorna as chaves
print(nome_idade.values()) #retorna apenas os valores
