'''
Ex03 - Contador de Vogais e Consoantes: Peça ao usuário para digitar uma frase e retorne o número de vogais e consoantes na frase.
'''

frase = input("Digite uma frase: ")

def contar_letras(frase):
    vogal = 'aeiouAEIOU'
    vogais = 0
    consoantes = 0

    for letra in frase:
        if letra.isalpha():
            if letra in vogal:
                vogais += 1
            else:
                consoantes += 1

    print("Número de vogais na frase:", vogais)
    print("Número de consoantes na frase:", consoantes)

contar_letras(frase)