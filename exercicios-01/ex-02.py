#Ex02 - Escreva um programa em Python que solicita ao usuário três números e apresenta a média aritmética dos números informados.

numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))
numero3 = float(input("Digite o terceiro número: "))

def media(numero1, numero2, numero3):
    return (numero1 + numero2 + numero3) / 3

mensagem = f"A média dos números informados é:{media(numero1, numero2, numero3)}."
print(mensagem)