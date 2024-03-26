'''
Ex07 - Jogo da Forca: Implemente uma versão simples do jogo da forca. 
O programa começa com uma palavra oculta (o usuário não vê) e o usuário tenta adivinhar a palavra, letra por letra.
 O usuário tem um número limitado de tentativas para adivinhar toda a palavra.
'''

def jogo_da_forca(palavra_secreta, max_tentativas):
    letras_certas = ['_'] * len(palavra_secreta)
    letras_erradas = []
    tentativas_restantes = max_tentativas

    print("Bem-vindo ao Jogo da Forca!")
    print("Adivinhe a palavra secreta. Você tem", max_tentativas, "tentativas.")

    while tentativas_restantes > 0:
        # Mostrar letras corretas e espaços para letras ainda não reveladas
        print("Palavra: ", end="")
        for letra in letras_certas:
            print(letra, end=" ")
        print("\n")

        # Pedir ao usuário para fazer uma tentativa
        tentativa = input("Digite uma letra: ").lower()

        if len(tentativa) != 1 or not tentativa.isalpha():
            print("Por favor, digite apenas uma letra.")
            continue

        if tentativa in palavra_secreta:
            print("Você acertou uma letra!")
            for i in range(len(palavra_secreta)):
                if palavra_secreta[i] == tentativa:
                    letras_certas[i] = tentativa
        else:
            print("Letra errada!")
            letras_erradas.append(tentativa)
            tentativas_restantes -= 1

        # Verificar se o jogador adivinhou todas as letras
        if '_' not in letras_certas:
            print("Parabéns! Você adivinhou a palavra secreta:", palavra_secreta)
            return

        print("Letras erradas:", letras_erradas)
        print("Tentativas restantes:", tentativas_restantes)

    print("Fim de jogo! A palavra secreta era:", palavra_secreta)


# Palavra secreta para o jogo
palavra_secreta = "python"
# Número máximo de tentativas
max_tentativas = 6

# Iniciar o jogo
jogo_da_forca(palavra_secreta, max_tentativas)