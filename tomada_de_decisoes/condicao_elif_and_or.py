#Situcção problema: O paciente chega á triagem que o direcionará a sala de espera da consulta. O funcionário
#da triagem poderá direcionar o paciente para uma das duas salas de espera, sãp elas:
#Branca: para os pacientes sem risco de doença infecto-contafiosas, mas com ou sem prioridade
#Amarela: para os pacientes com risco de doença infecto-contafiosa, mas ou sem prioridade

nome=input("Digite o nome do paciente: ")
idade=int(input("Digite a idade:"))
doenca_infecto_contagiosa=input("Suspeita de doença infecto-contagiosa? ").upper()
if idade>=65 and doenca_infecto_contagiosa=="SIM":
    print("O paciente será direcionado para a sala AMARELA - COM  prioridade.")
elif idade < 65 and doenca_infecto_contagiosa=="SIM":
   print("O paciente será direcionado para a sala AMARELA - SEM  prioridade.")
elif idade >= 65 and doenca_infecto_contagiosa =="NAO":
    print("O paciente será direcionado para a sala BRANCA - COM prioridade.")
elif idade < 65 and doenca_infecto_contagiosa == "NAO":
    print("O paciente será direcionado para a sala BRANCA - SEM  prioridade.")
else:
    print("Responda a suspeira de doença infectocontagiosa com SIM ou NAO.")