'''Ex03 - Crie um programa em Python que recebe como entrada o valor de uma compra e apresenta como saída o valor final com desconto 
e o desconto aplicado com base nas seguintes regras:

    Compras entre R$ 0,01 e R$ 9,99 - 0% de desconto
    Compras entre R$ 10,00 e R$ 99,99 - 5% de desconto
    Compras entre R$ 100,00 e R$ 499,99 - 10% de desconto
    Compras iguais ou superiores a R$ 500,00 - 15% de desconto'''

valor = float(input("Digite o valor da compra: "))

if valor >= 0.01 and  valor <= 9.99:
    print("criança")
elif idade <= 17:
    print("adolecente")
elif idade <= 59:
    print("adulto")
else:
    print("idoso")