nome=input("Digite um funcionário: ") #input permit usuario final possa digitar um conteudo.
empresa=input("Digite a intituição: ")
qtde_funcionarios=int(input("Digite a quantidade de funcionários: ")) #Convertendo String para int
mediaMensalidade=float(input("Digite a media da mensalidade: ")) #Convertendo String para float
print(nome + " trabalha na empresa " + empresa) #print exibe a mensagem na tela "+" concatena Strings
print("Possui: " , qtde_funcionarios, " funcionarios")
print("A média da mensalidade é de: " + str(mediaMensalidade)) #Converte a mediaMensalidade float para string
print("==================Verifique os tipos de dados abaixo==================")
print("O tipo de dado da variavel [nome] é: ",type(nome)) #A função type() nos retorna o tipo de dado que estiver dentrod os seus parênteses.
print("O tipo de dado da variavel [empresa] é: ",type(empresa))
print("O tipo de dado da variavel [qtde_funcionarios] é: ",type(qtde_funcionarios))
print("O tipo de dado da variavel [mediaMensalidade] é: ",type(mediaMensalidade))

