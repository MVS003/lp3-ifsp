'''Ex03 - Crie um programa em Python que recebe como entrada o valor de uma compra 
e apresenta como saída o valor final com desconto e o desconto aplicado com base nas seguintes regras:

    Compras entre R$ 0,01 e R$ 9,99 - 0% de desconto
    Compras entre R$ 10,00 e R$ 99,99 - 5% de desconto
    Compras entre R$ 100,00 e R$ 499,99 - 10% de desconto
    Compras iguais ou superiores a R$ 500,00 - 15% de desconto'''

valor = float(input("Digite o valor da compra: "))
desconto = 0

if valor >= 0.01 and  valor <= 9.99:
    print(f"Valor final da compra: R${valor}")
elif valor >=10.00 and valor <= 99.99:
    desconto = valor * 0.05
    v_final = valor - desconto
    print(f"Valor final da compra: R${v_final}, desconto de R${desconto}")
elif valor >=100.00 and valor <= 499.99:
    desconto = valor * 0.1
    v_final = valor - desconto
    print(f"Valor final da compra: R${v_final}, desconto de R${desconto}")
elif valor >=500.00:
    desconto = valor * 0.15
    v_final = valor - desconto
    print(f"Valor final da compra: R${v_final}, desconto de R${desconto}")
else:
    print("Valor inserido é invalido")