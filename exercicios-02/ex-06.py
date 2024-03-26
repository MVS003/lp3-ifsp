'''
Ex06 - Conversor de Notas Escolares: Baseado em uma pontuação fornecida pelo usuário (0 a 100), 
converta para o sistema de notas A, B, C, D, ou F, seguindo os padrões de conversão comuns.
'''
pontuacao = int(input("Digite a pontuação: "))

if pontuacao >= 90 and pontuacao <=100:
    print("Nota A")
elif pontuacao >= 80 and pontuacao <=89:
    print("Nota B")
elif pontuacao >= 70 and pontuacao <=79:
    print("Nota C")
elif pontuacao >= 60 and pontuacao <=69:
    print("Nota D")
elif pontuacao >= 0 and pontuacao <=59:
    print("Nota E")
else:
    print("Pontuação inválida")