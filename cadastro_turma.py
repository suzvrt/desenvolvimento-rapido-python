turma = {}
total_alunos = int(input("Quantos alunos há na turma? "))
for i in range(total_alunos):
    print(f"\n--- Cadastro do aluno {i+1} ---")
    nome = input("Nome: ")
    idade = int(input("Idade: "))
    nota = float(input("Nota: "))
    turma[nome] = {"idade": idade, "nota": nota}

print("\n=== Lista de alunos cadastrados ===")
for nome, dados in turma.items():
    print(f"Aluno: {nome} | Idade: {dados['idade']} | Nota: {dados['nota']}")
