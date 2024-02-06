#Este é um caso que verdadeiro ou um falso na idade não resolve, pois precisamos verificar se a idade do paciente é
#maior ou igual a 65 anos e, se a resposta for FALSA, devemos verificar ainda se o paciente está com suspeita de doença
#infecto-contagiosa. E se, ainda assim for FALSA  a condição, então podemos considerar que o paciente deve aguardar sem
#prioridade na sala comum de espera

nome=input("Digite o nome: ")
idade=int(input("Digite a idade: "))
doenca_infectocontagiosa=input("Suspeita de doença infecto-contagiosa? ").upper()
if idade>=65:
    print("O paciente " + nome + " POSSUI atendimento prioritario")
elif doenca_infectocontagiosa=="SIM":
    print("O paciente " + nome + " deve ser direciondo para a sala de espera reservada")
else:
    print("O paciente " + nome + " NÃO possui atendimetno prioritario e pode aguardar na sala comum!")