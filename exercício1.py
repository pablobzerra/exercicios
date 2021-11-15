'''Faça um Programa que peça um número e então mostre a mensagem O número informado foi [número].
'''

n =input("Digite um numero: ")
try:
	t=type(int(n))
	print("O numero informado foi ["+n+"]")
except:
	print("Isto n é um numero")