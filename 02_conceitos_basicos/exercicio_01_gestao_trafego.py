"""
EXERCÍCIO 01: Gestão de Tráfego Casas Paulino
Disciplina: Lógica de Programação com Python

ENUNCIADO:
A loja Casas Paulino está veiculando anúncios no Meta Ads em Tianguá.
Escreva um programa que leia:
1. O valor total investido na campanha (em R$).
2. O número total de cliques obtidos.

Calcule e mostre na tela o Custo Por Clique (CPC) médio da campanha formatado em reais.
"""

# TODO: Desenvolva o algoritmo abaixo:
#1. valor investido
valor_investido_str=input("quanto foi investido na campanha ? ")
valor_investido=float(valor_investido_str)
#2. valor de cliques
valor_cliques_str=input("quantos cliques foram obtidos ? ")
valor_clique=int(valor_cliques_str)
#3. qual custo por cliques
cpc=(valor_investido/valor_clique)
print(f"foi pago {cpc} reais por cada clique.")
