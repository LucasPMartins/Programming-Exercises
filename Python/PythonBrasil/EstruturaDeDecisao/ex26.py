# 26 - Um posto está vendendo combustíveis com a seguinte tabela de descontos:
# Álcool:
# até 20 litros, desconto de 3% por litro
# acima de 20 litros, desconto de 5% por litro
# Gasolina:
# até 20 litros, desconto de 4% por litro
# acima de 20 litros, desconto de 6% por litro 
# Escreva um algoritmo que leia o número de litros vendidos, o tipo de combustível 
# (codificado da seguinte forma: A-álcool, G-gasolina), calcule e imprima o valor a 
# ser pago pelo cliente sabendo-se que o preço do litro da gasolina é R$ 2,50 o preço
# do litro do álcool é R$ 1,90.

litros = float(input('Litros vendidos:'))
tipo = input('Tipo de combustível (A-álcool, G-gasolina):').upper()
if tipo == 'G':
    total = litros * 2.5
    if litros < 20:
        total -= litros * 0.04
    else:
        total -= litros * 0.06
elif tipo == 'A':
    total = litros * 1.9
    if litros < 20:
        total -= litros * 0.03
    else:
        total -= litros * 0.05
print(f'Total a pagar R${total:.2f} por {litros} litros de','gasolina' if tipo == 'G' else 'álcool')