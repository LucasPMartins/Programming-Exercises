# 1 - Faça um programa para imprimir:
#     1
#     2   2
#     3   3   3
#     .....
#     n   n   n   n   n   n  ... n
# para um n informado pelo usuário. Use uma função que receba um valor n inteiro e
# imprima até a n-ésima linha.

def imprime_n(n):
    for i in range(n):
        print(f'{i}   '*i)

n = int(input('Digite um número:'))
imprime_n(n)