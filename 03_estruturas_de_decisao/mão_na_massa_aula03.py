# TODO: Implemente o menu utilizando match-case ou elif
opcao = int(input("Digite a opção desejada (1, 2 ou 3): "))

# Desenvolva a estrutura de seleção aqui
if opcao==1 :
    print("consultar livros")
elif opcao==2 :
    print("realizar emprestimo")
elif opcao==3:
    print("devolver livro")
else:
    print("opção não encontrada")