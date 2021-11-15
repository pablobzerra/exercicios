'''
Faça um Programa que peça dois números e imprima a soma.
'''
n1 = input("Digite um numero: ")
n2 = input("Digite o segundo numero: ")
try:
	err="Isto n é um numero"
	i = int(n1)
	ii = int(n2)
	err="ocorreu um erro ao soma"
	soma = str(i ++ ii)
	print("\nO resultado é "+soma)
except:
	print(err)