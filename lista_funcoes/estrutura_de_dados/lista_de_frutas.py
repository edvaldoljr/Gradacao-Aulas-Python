frutas=["maça", "banana", "uva","laranja", "morango"] #criando uma lista de frutas.
print(frutas) #imprimindo nossa lista de frutas.

print(frutas[2]) #imprime a frutas na posição 2 da lista.

fruta=frutas[0] #armazena na variável somente a fruta da posição 0
print(fruta) #mostra o valor da variável

copia=frutas[:3]  #faz o fatiamento do inicio até a posição 2 da lista
print(copia)

frutas.append("damasco")  #o append adiciona um novo elemento a lista
print(frutas)
