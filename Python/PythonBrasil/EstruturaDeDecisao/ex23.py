# 23 - Faça um Programa que peça um número e informe se o número é inteiro ou decimal. 
# Dica: utilize uma função de arredondamento.

num = float(input('Digite um número:'))
if round(num) == num:
    print(f'{num} é inteiro!')
else:
    print(f'{num} é decimal!')