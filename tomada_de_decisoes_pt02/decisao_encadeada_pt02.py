#Mulheres gravidas também são consideradas o atendimento prioritario(SALA BRANCA OU AMARELA). Você, não pricisa pergunta
# para todos os pacientes se estão grávidos? Nao apenas para mulheres. Então, você perguntaria para todas as mulheres?
#Não. você não precisa perguntar para as mulheres com idade igual ou superior a 65 anos, assim também poderia descartar
#crianças com menos de 10 anos.

nome=input("Digite o nome do paciente: ")
idade=int(input("Digite a idade do paciente: "))
doenca_infectocontagiosa=input("Suspeita de doença Infecto-contagiosa? ").upper()

#Primeiro desafio saber se tem doença infecto-contagiosa
if doenca_infectocontagiosa=="SIM":
    print("Encawminhe o paciente para sala AMARELA.")
elif doenca_infectocontagiosa=="NAO":
    print("Encaminhe o paciente para sala BRANCA.")
else:
    print("Responda a suspeita de doençça infectocontagiosa com SIM ou NAO.")

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