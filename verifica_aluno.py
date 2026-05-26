alunos = {}
while True:
    nome = input(
        "Digite o nome do aluno (ou 'sair' para encerrar): ").strip().title()
    if nome.lower() == 'sair':
        break
    nota = float(input(f"Digite a nota de {nome}: "))
    alunos[nome] = nota
print("\n--- Lista de alunos e notas ---")
for nome, nota in alunos.items():
    print(f"{nome}: {nota:.1f}")
print("\n--- Situação dos alunos ---")
for nome, nota in alunos.items():
    if nota >= 7:
        print(f"{nome} está APROVADO(A).")
    elif nota >= 5:
        print(f"{nome} está em RECUPERAÇÃO.")
    else:
        print(f"{nome} está REPROVADO(A).")
