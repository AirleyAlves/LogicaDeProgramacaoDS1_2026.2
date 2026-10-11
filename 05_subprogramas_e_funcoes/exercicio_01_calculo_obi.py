"""
EXERCÍCIO 01: Pontuação OBI (Astro Lume Devs)
Disciplina: Lógica de Programação com Python

ENUNCIADO:
Crie uma função nomeada `calcular_pontuacao_total(fase1, fase2, fase3)` com a diretiva `def`
que receba as 3 notas como parâmetros e retorne a pontuação total da equipe.
"""

# TODO: Desenvolva a função e os testes abaixo:
def calcular_pontuação_total(fase1,fase2,fase3):
    pont_total=fase1+fase2+fase3
    return pont_total

equipe=str(input("digite o nome da equipe: "))
fase1=int(input("digite a pontuação da equipe na primeira fase: "))
fase2=int(input("digite a pontuação da equipe na segunda fase: "))
fase3=int(input("digite a pontuação da equipe na terceira fase: "))
pont_total=calcular_pontuação_total(fase1,fase2,fase3)

print(f"a pontuação da equipe {equipe} foi de {pont_total}")