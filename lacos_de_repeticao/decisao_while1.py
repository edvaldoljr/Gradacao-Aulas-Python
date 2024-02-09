resposta=input("Gostaria de acessar o sistema? [SIM] / [NAO]: ").upper()
while resposta=="SIM":
    nivel=input("Olá qual seu nível de acesso? [ADM] / [USR] / [OUTRO] ").upper()
    if nivel=="ADM" or nivel=="USR":
        genero=input("Qual o seu genero? [FEMININO] / [MASCULINO] ").upper()
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
    resposta=input("Digite [SIM] para continuar ou [NAO] para encerrar: ").upper()
print("ENCERRANDO O PROGRAMA...")
