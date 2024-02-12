def soma(a,b):
    return a+b

valor1=int(input("Digite um valor: "))
valor2=int(input("Digite um valor: "))
resultado=soma(valor1,valor2)

print(resultado)

#Função Lambda

soma=lambda a,b : a+b
print(soma(valor1,valor2))