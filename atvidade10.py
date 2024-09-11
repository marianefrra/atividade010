# Crie um programa que receba um número inteiro e informe se ele é par ou ímpar.

numero = int(input("digite o número"))


div = numero % 2 
if (div == 0):
    print(f"{numero} é um número par.")
else: print(f"{numero} é um número impar")

