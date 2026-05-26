aluno = {}
aluno["nome"] = input("Digite o nome do aluno: ")
aluno["idade"] = int(input("Digite a idade do aluno: "))
aluno["nota"] = float(input("Digite a nota do aluno: "))
print("\nInformações do aluno:")
for chave, valor in aluno.items():
    print(f"{chave}: {valor}")
