'''Ex05 - Verificador de Palíndromos: Solicite ao usuário que digite uma palavra ou frase 
e verifique se é um palíndromo (ou seja, pode ser lida de frente para trás e de trás para frente da mesma forma).
'''

frase = input("Digite uma palavra ou frase: ")

def palindromo(frase):
    frase = frase.replace(" ", "").lower()
    frase_inversa = frase[::-1]

    if frase_inversa == frase:
        print("É um palíndromo!")
    else:
        print("Não é um palíndromo.")

palindromo(frase)