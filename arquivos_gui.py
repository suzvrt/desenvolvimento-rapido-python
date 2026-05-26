nome_arquivo = "meu_arquivo.txt"
conteudo = "Olá! Este é um arquivo criado com Python.\nAprendendo a programar!"
with open(nome_arquivo, "w", encoding="utf-8") as arquivo:
    arquivo.write(conteudo)
print("Arquivo criado com sucesso!")