# Imagine que você precisará coletar o nome de pacientes que serão attendidos em uma sala de
# emergência em um hospital, porém algumas deverão ser identificadas pela idade maior ou igual a 65 anos.
# Nosso código precisará saber o nome e a idade da pessoa para que possamos definir se terá atendimento
# preferencial ou não.

nome=input("Nome da Pessoa: ")
idade=int(input("Idade: "))
if idade>=65:
    prioridade= "SIM"
print("O paciente " + nome + " possue atendimento prioritário? " + prioridade)
