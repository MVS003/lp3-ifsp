'''Ex01 - Jogo de Adivinhação: Peça ao usuário para adivinhar um número entre 1 e 100 que o programa escolheu aleatoriamente. 
Informe ao usuário se o palpite está alto ou baixo, até que ele acerte o número.
'''

import random

def numero_aleatorio():
    numero = random.randint(1, 100)
    tentativas = 0
    
    
    while True:
        palpite = int(input("Digite o seu palpite: "))
        tentativas += 1

        if palpite < numero:
            print("Seu palpite está baixo")
        elif palpite > numero:
            print("Seu palpite está alto")
        else:
            print("Seu palpite está correto")
            break
    
numero_aleatorio()