import os


def criar_arquivo():
    nome = input("Digite o nome do arquivo (ex: teste.txt): ")
    conteudo = input("Digite o conteúdo inicial: ")
    with open(nome, "w", encoding="utf-8") as f:
        f.write(conteudo)
    print("Arquivo criado com sucesso em:", os.path.abspath(nome))


def ler_arquivo():
    nome = input("Digite o nome do arquivo: ")
    if os.path.exists(nome):
        with open(nome, "r", encoding="utf-8") as f:
            print("\nConteúdo do arquivo:\n")
            print(f.read())
    else:
        print("Arquivo não encontrado!")


def adicionar_conteudo():
    nome = input("Digite o nome do arquivo: ")
    if os.path.exists(nome):
        novo = input("Digite o conteúdo a adicionar: ")
        with open(nome, "a", encoding="utf-8") as f:
            f.write("\n" + novo)
        print("Conteúdo adicionado!")
    else:
        print("Arquivo não encontrado!")


def excluir_arquivo():
    nome = input("Digite o nome do arquivo: ")
    if os.path.exists(nome):
        os.remove(nome)
        print("Arquivo excluído com sucesso!")
    else:
        print("Arquivo não encontrado!")


def menu():
    while True:
        print("\n=== GERENCIADOR DE ARQUIVOS ===")
        print("1 - Criar arquivo")
        print("2 - Ler arquivo")
        print("3 - Adicionar conteúdo")
        print("4 - Excluir arquivo")
        print("0 - Sair")
        opcao = input("Escolha uma opção: ")
        if opcao == "1":
            criar_arquivo()
        elif opcao == "2":
            ler_arquivo()
        elif opcao == "3":
            adicionar_conteudo()
        elif opcao == "4":
            excluir_arquivo()
        elif opcao == "0":
            print("Encerrando...")
            break
        else:
            print("Opção inválida!")


menu()
