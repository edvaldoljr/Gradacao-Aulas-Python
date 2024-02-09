#O seu programa de solicitar o nivel de acesso de uma pessoa que pode ser: ADM, USR OU GUEST eo gênero dessa
#pessoa, caso o nivel seja AMD , ele deve exibir "Olá administrador" para os homens ou
# "Olá administradora" para mulheres.
#Se o niver for USR, deverá exibir "Olá usuário" para os homes e "Olá usruaria" para mulheres. Se o nível for GUEST,
#a mensagem deverá ser "Olá visitante". E se o nível digitado for diferente de ADM, USR, GUEST deverá exibir a mensagem "Olá desconhecido(a)".

nivel=input("Olá qual seu nível de acesso? ").upper()
if nivel=="ADM" or nivel=="USR":
    genero=input("Qual o seu genero? ")
    if nivel=="ADM":
        if genero=="FEMININO":
            print("Olá Administradora")
        else:
            print("Olá Administrador")
    else:
        if genero=="FEMININO":
            print("Olá Usuária")
        else:
            print("Olá Usuário")
elif nivel=="GUEST":
    print("Olá Visitante")
else:
    print("Olá DESCONHECIDO")