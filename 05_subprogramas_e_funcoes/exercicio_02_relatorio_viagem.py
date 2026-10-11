"""
EXERCÍCIO 02: Modularizando Relatório de Viagem
Disciplina: Lógica de Programação com Python

ENUNCIADO:
Crie duas funções:
1. `calcular_custo_transporte(distancia_km, consumo_kml, preco_combustivel)`
2. `calcular_custo_alimentacao(qtd_pessoas, dias, diaria_alimentacao)`

No programa principal, leia os dados, execute as funções e mostre o custo total da viagem.
"""

# TODO: Desenvolva as funções e o programa principal abaixo:
def calcular_custo_transporte(distancia_km,consumo_kml,preco_combustivel):
    custo_transporte=(distancia_km*consumo_kml)*preco_combustivel
    return custo_transporte

def calcular_custo_alimentação(qtd_pessoas,dias,diaria_alimentação):
    custo_alimentação=(qtd_pessoas*dias)*diaria_alimentação
    return custo_alimentação

#variaveis do calculo do custo de combustivel
distancia_km=float(input("digite a distancia percorrida na viagem: "))
consumo_kml=float(input("digite o custo de combustivel por quilometro:"))
preco_combustivel=float(input("digite o preço do combustivel: "))
custo_transporte=calcular_custo_transporte(distancia_km,consumo_kml,preco_combustivel)

#variaveis do calculo do custo alimentação
qtd_pessoas=int(input("digite o numero de pessoas que foram na viagem: "))
dias=int(input("digite o numero de dias que vcs passaram lá: "))
diaria_alimentação=float(input("digite o valor do custo da diaria de alimentação"))
custo_alimentação=calcular_custo_alimentação(qtd_pessoas,dias,diaria_alimentação)

custo_total=custo_transporte+custo_alimentação 

print(f"o custo total dessa viajem foi de {custo_total:.2f}")
