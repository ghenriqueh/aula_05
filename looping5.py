aluno=1
while aluno <=10:
    print(f"--- Aluno {aluno} ---")
    nome = input("Nome do aluno: ")
    nota1 = float(input("Insira a nota 1: "))
    nota2 = float(input("Insira a nota 2: "))
    nota3 = float(input("Insira a nota 3: "))
    media= (nota1+nota2+nota3)/3
    if media>=7:
        situacao = print("Aprovado")
    elif media>=5:
        situacao = print("Recuperação")
    else:
        situacao = print("Reprovado")
    print("\n")
    print ("Resultados")
    print (f"Aluno: {nome} ")
    print (f"Nota 1: {nota1} ")
    print (f"Nota 2: {nota2} ")
    print (f"Nota 3: {nota3} ")
    print (f"Média: {media} ")
    print (f"Situação: {situacao} ")