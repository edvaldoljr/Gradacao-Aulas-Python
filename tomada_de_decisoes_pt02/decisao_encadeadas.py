#Situcção problema: O paciente chega á triagem que o direcionará a sala de espera da consulta. O funcionário
#da triagem poderá direcionar o paciente para uma das duas salas de espera, sãp elas:
#Branca: para os pacientes sem risco de doença infecto-contafiosas, mas com ou sem prioridade
#Amarela: para os pacientes com risco de doença infecto-contafiosa, mas ou sem prioridade

nome=input("Digite o nome do paciente: ")
idade=int(input("Digite a idade: "))
doenca_infectocontagioa=input("Suspeita de doença infecto-contagiosa? ").upper()
if idade>=65:
    print("Paciente com PRIORIDADE.")
    if doenca_infectocontagioa =="SIM":
        print("Encaminhe o paciente para a sala AMARELA.")
    elif doenca_infectocontagioa=="NAO":
        print("Encaminhe o paciente para sala BRANCA.")
    else:
        print("Responda a suspeita de doença infecto-contagiosa com SIM ou NAO.")
else:
    print("Paciente SEM prioridade")
    if doenca_infectocontagioa=="SIM":
        print("Encaminhe o paciente para sala AMARELA.")
    elif doenca_infectocontagioa=="NAO":
        print("Encaminhe o paciente para sala BRANCA.")
    else:
        print("Responda a suspeita de doença infecto-contagiosa com SIM ou NAO.")