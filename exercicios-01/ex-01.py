#Ex01 - Escreva um programa em Python que solicita ao usuário um número inteiro e apresenta seu antecessor e sucessor.

numero = int(input("Digite um número: "))

def sucessor(numero):
    return numero + 1

def antecessor(numero):
    return numero - 1

mensagem = f"O sucessor de {numero} é: {sucessor(numero)} \nO antecessor de {numero} é: {antecessor(numero)}"
print(mensagem)
