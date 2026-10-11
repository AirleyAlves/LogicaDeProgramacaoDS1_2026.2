"""
DESAFIO 04: REFATORAÇÃO INVESTIGATIVA
Disciplina: Lógica de Programação com Python

RELATÓRIO DA INVESTIGAÇÃO:
O código monolítico repete cálculos de desconto e impostos várias vezes.

SUA MISSÃO:
1. Crie uma função calcular_preco_final(preco_base, taxa_desc, taxa_imp) com return.
2. Crie um procedimento exibir_relatorio_item(numero_item, preco_final) com print.
3. Teste suas funções refatoradas.
"""

# TODO: Desenvolva as funções modulares abaixo:
def calcular_preco_final(preco_base,taxa_desc,taxa_imp):
    preco_final=preco_base-(preco_base*taxa_desc)+(preco_base*taxa_imp)
    return preco_final

def exibir_relatorio(numero_item,preco_final):
    print(f"o item {numero_item} ficou no valor de {preco_final}")

taxa_desc=0.07
taxa_imp=0.10
numero_item=int(input("digite o numero do produto escolhido: "))
preco_base=float(input("digite o valor do preço base desse produto: "))
preco_final=calcular_preco_final(preco_base, taxa_desc,taxa_imp)
relatorio=exibir_relatorio(numero_item,preco_final)

