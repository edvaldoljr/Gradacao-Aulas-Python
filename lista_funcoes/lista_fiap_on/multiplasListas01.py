equipamentos=[]
valor=[]
numeroSerial=[]
departametno=[]
resposta="S"
while resposta == "S":
    equipamentos.append(input("Equipamento: "))
    valor.append(input("Valor: "))
    numeroSerial.append(input("Numero Serial: "))
    departametno.append(input("Departametno: "))
    resposta=input("Deseja continuar? [S]/[N]")

for equipamento in equipamentos:
    print(equipamento)