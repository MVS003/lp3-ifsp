'''Ex04 - Simulador de Eleições: Crie um programa que simule uma votação com três candidatos.
O programa deve pedir ao usuário para votar várias vezes e, no final, mostrar o número de votos de cada candidato e quem foi o vencedor.
'''
#não concluido
print("Digite 1 para votar no candidato A \nDigite 2 para votar no candidato B \nDigite 3 para votar no candidato C")
print("Vote várias vezes em quantos candidatos quiser, ao finalizar digite 0")



def votacao():
    a=0
    b=0
    c=0

    while True:
        candidato = input("Informe seu voto: ")

        if candidato == 0:
            break

        if candidato == 1:
            a += 1
        elif candidato == 2:
            b += 1
        elif candidato == 3:
            c += 1
        else:
            print("Invalido")

    print("Número de votos no candidato A:", a)
    print("Número de votos no candidato B:", b)
    print("Número de votos no candidato C:", c)

votacao()


