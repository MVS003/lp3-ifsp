#operadores
#aritimeticos
#+, -, /, *, %
nota1 = 10
nota2 = 3
media = (nota1 + nota2)/2

#potencia
numero = 2 ** 3 #elevado ao cubo
numero = 10 ** 2 #elevado ao quadrado

#logicos
#and, or, not
# acesso liberado = não bloqueado, idade > 18, horário comercial

bloqueado = False
idade = 21
hora_atual = 10

if not bloqueado and idade >= 18 and hora_atual >=8 and hora_atual <=18:
    print("Liberado")
else:
    print("Não liberado")

#operadores de comparação
# >, <, >=, <=, ==, =!
numeros = [1, 2, 3]
numeros2 = [1, 2, 3]

print(numeros == numeros2) #True

#operador is
print(numeros is numeros2) #False

numeros3 = [1, 2]
numeros4 = numeros3

print (numeros3 is numeros4) #True
print (numeros3 is not numeros4) #False

#in (bool)
print("a" in "python") #False

prontuarios = ["sp001", "sp002", "sp003"]
prontuario = "SP002"
print(prontuario in prontuarios) #true

#sim, não, talvez
opcao = " "

if opcao == "sim" or opcao == "não" or opcao == "talvez":
    print("opção válida")
else:
    print("opção inválida")


#if opcao in 