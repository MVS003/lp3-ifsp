#Ex05 - Crie um programa em Python que solicita ao usuário um identificador 
# e apresenta se o que foi informado é um valor válido ou inválido.

codigo = input("Insira seu codigo: ")

def verificacao(codigo):
    if len(codigo) == 7 and codigo[0:2] == "BR" and codigo[2:6].isnumeric() and codigo[6] == "X":
        print("Código válido")
    else:
        print("Código inválido")
        

verificacao(codigo)