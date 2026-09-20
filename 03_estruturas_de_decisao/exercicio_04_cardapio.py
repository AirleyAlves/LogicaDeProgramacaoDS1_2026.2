"""
EXERCÍCIO 04: Cardápio da Lanchonete
Disciplina: Lógica de Programação com Python

TABELA:
1 - Cachorro Quente: R$ 4.00
2 - X-Salada: R$ 4.50
3 - X-Bacon: R$ 5.00
4 - Torrada Simples: R$ 2.00
5 - Refrigerante: R$ 1.50

ENUNCIADO:
Leia o código do item e a quantidade consumida.
Calcule e mostre o total a pagar.
"""

# TODO: Desenvolva o algoritmo abaixo:
codigo=int(input("digite o código do item que você pediu: " ))
quantidade=int(input("digite a quantidade que você pediu: " ))
if codigo==1:
    preco_unit=4.00
elif codigo==2:
    preco_unit=4.50
elif codigo==3:
    preco_unit=5.00
elif codigo==4.00:
    preco_unit=2.00
elif codigo==5:
    preco_unit=1.50
else:
    print("pedido invalido!")

if 0<codigo<6:
    preco_total=preco_unit*quantidade
    print(f"o valor total a ser pago é R${preco_total:.2f}")