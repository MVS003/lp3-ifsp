#Função
#Modularizar o programa
#Reuso
#Manutenabilidade (correção de erros e novas funcionalidades)

#Declaração
def ola_mundo():
    print("Olá, Mundo!")

#Chamada da função
ola_mundo()

#Função sem retorno
#Side effect - efeito colateral
def imprimir_mensagem(nome):
    print(f"bom dia, {nome}")

imprimir_mensagem("Lucas")

#Função com retorno
#Função pura
def mensagem(nome):
    return f"Bom dia, {nome}"

print(mensagem("Maria"))
#enviar_email(mensagem("Maria"))

#Parâmetro e Argumentos
def somar(numero1, numero2):
    return numero1 + numero2

somar(1, 3)

#Escopo de variáveis
def media(nota1, nota2, nota3):
    total= nota1+nota2+nota3
    return total/3

#Parâmetros com valor padrão
def mensagem(nome, mensagem):
    return f"{mensagem}, {nome}."

#Argumentos nomeados
print("Olá", "123", "Teste", sep="@", end="\n\n")
print("Teste")

mensagem(nome="Lucas", mensagem="Boa tarde")

#docstring
#comentário de documentação

def somar (n1,n2):
    '''
    Função que soma dois números

    param n1: primeiro número
    param n2: segundo número
    return: soma dos números
    '''
    return n1 + n2

#Funções built-in
#print, type, len, sum, max, min, input

def media(*notas):
    return sum(notas)/len(notas)

print(media(7,8,9))