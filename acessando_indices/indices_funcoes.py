texto=("Análise de Dados em Python")
print(texto)
print(texto[0]) #imprime o primeiro caracter do texto armazenado na váriavel
print(texto[2]) #irá acessar o índice 3 e mostrará “á”
texto2=texto[1:] #indica que iremos capturar a partir da posição 1 até o final
print(texto2)
texto2=texto[:6] #indica que iremos capturar a string do inicio até a posição 6-1
print(texto2)

#Podemos ainda utilizar valores negativos para acessar de trás para frente, exemplo:

print(texto[-1])
print(texto[-2])

#Para encerrarmos o conceito de strings, temos ainda a opção de fazer uma
#repetição com a string, por exemplo, se você precisar atribuir para uma variável o
#valor “www”, pode utilizar o operador *, exemplo:

valor="W"*3
print(valor)

x="curso ead"
print(x.upper()) #transforma a string para letras maiúsculas

print(x.lower()) #transforma a string para letras minusculas

print(x.capitalize()) #transforma a primeira letra da string

print(x.split())  #divide a string em uma lista

print(x.count("o")) #conta a quantidade de ocorrência de um ou mais caracteres

print(x.find("x")) #procura um ou mais caracteres retornando o índice inicial e retorna -1 caso não encontre

print(x.find("c")) #retorna a posição 0
