'''Ex02 - Tabuada de Um Número: Solicite ao usuário um número e exiba a tabuada desse número de 1 a 10.
'''
numero = float(input("Digite o número: "))

def tabuada(numero):
   multiplicador = 0

   while multiplicador >0 and multiplicador <11:
        resultado = numero * multiplicador
        print(f"{numero} x {multiplicador} = {resultado}")
        multiplicador +=1
        
   
tabuada()
    
