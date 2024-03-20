'''Ex06. Crie um programa em Python que recebe como entrada o comprimento, altura 
e a largura de um aquário e calcule as seguintes informações.

    O volume do aquário em litros;
    A potência do termostato necessária para manter a temperatura adequada dentro do aquário;
    A quantidade em litros de filtragem por hora necessária para manter a qualidade da água.

    Volume é dado por (comprimento * altura * largura) / 1000
    A potência do termostato depende do tamanho do aquário e da temperatura ambiente. Para o cálculo utilizar a fórmula: potencia = volume * 0,05 * (temperatura desejada - temperatura ambiente)
    A quantidade de filtragem por hora deve ser no mínimo 2 a 3 vezes o volume do aquário.

Utilize funções.'''

comprimento = float(input("Digite o comprimento do aquário:"))
altura = float(input("Digite a altura do aquário: "))
largura = float(input("Digite a largura do aquário: "))

def calcular_volume(comprimento, altura, largura):
    volume = (comprimento * altura * largura)/100
    return volume

temperatura_ambiente = float(input("Digite a temperatura ambiente: "))
temperatura_desejada = float(input("Digite a temperatura desejada: "))

def calcular_potencia(volume, temperatura_desejada, temperatura_ambiente):
    potencia = volume * 0.05 * (temperatura_desejada - temperatura_ambiente)
    return potencia

def calcular_filtragem(volume):
    filtragem= volume * 2 
    return filtragem

volume = calcular_volume(comprimento, altura, largura)

mensagem = f"O Volume do aquário é: {calcular_volume(comprimento, altura, largura)} \nPotência do termostato necessária: {calcular_potencia(volume, temperatura_desejada, temperatura_ambiente)} \nFiltragem necessária por hora: {calcular_filtragem(volume)}."
print(mensagem)