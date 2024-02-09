nome=input("Digite o nome do paciente: ")
idade=int(input("Digite a idade do paciente: "))
doenca_infectocontagiosa=input("Suspeita de doença Infecto-contagiosa? ").upper()

#Primeiro desafio saber se tem doença infecto-contagiosa
while doenca_infectocontagiosa!="SIM" and doenca_infectocontagiosa!="NAO":
    print("Digite SIM ou NAO ")
    doenca_infectocontagiosa=input("Suspeita de doença infecto-contagiosa").upper()

if doenca_infectocontagiosa=="SIM":
    print("Encaminhe o paciente para sala AMARELA.")
else:
    print("Encaminhe o paciente para sala BRANCA.")

#Sengundo desafio saber se é mulher e esta grávida
if idade>=65:
    print("O paciente tem PRIORIDADE")
else:
    genero=input("Digite o genero do paciente: ").upper()
    if genero=="FEMININO" and idade>10:
        gravidez=input("A paciente está gravida?: ").upper()
        if gravidez=="SIM":
            print("O paciente tem PRIORIDADE")
        else:
            print("Paciente SEM prioridade.")
    else:
        print("Paciente  SEM prioridade")