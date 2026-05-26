turma = {
    "Ana": [8.0, 9.0, 7.5],
    "Bruno": [6.5, 7.0, 8.0],
    "Carlos": [9.0, 9.5, 8.5]
}
# Calculando a média de cada aluno
for nome, notas in turma.items():
    media = sum(notas) / len(notas)
    print(f"{nome} - Média: {media:.2f}")
# Exemplo de uso condicional
for nome, notas in turma.items():
    media = sum(notas) / len(notas)
    situacao = "Aprovado" if media >= 7 else "Reprovado"
    print(f"{nome}: {situacao}")
