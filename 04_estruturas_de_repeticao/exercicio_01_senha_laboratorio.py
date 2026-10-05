"""
EXERCÍCIO 01: Senha Fixa do Laboratório
Disciplina: Lógica de Programação com Python

ENUNCIADO:
Repita a leitura da senha até que o usuário digite a senha correta (2002).
Para cada tentativa incorreta, imprima "Senha Invalida".
Ao acertar, imprima "Acesso Permitido" e finalize o programa.
"""

# TODO: Desenvolva o algoritmo abaixo:
senha=2002
numero= float(input("digite a senha: ")) 
while numero!= 2002:
    print("senha invalida")
    numero=float(input("digite outra senha: "))
    
    if numero==2002:
        print("acesso permitido")
    