from datetime import date


def verificar_idade():
    idade = int(input("Digite sua idade: "))
    if idade < 18:
        print("Você é menor de idade.")
    elif idade < 60:
        print("Você é adulto.")
    else:
        print("Você é idoso.")


def contar_ate_n():
    ano_nascimento = int(input("Digite seu ano de nascimento (4 dígitos): "))
    ano_atual = date.today().year
    idade = ano_atual - ano_nascimento
    print(f"Você tem {idade} anos de idade.")


def menu():
    while True:
        print("\n=== MENU ===")
        print("1. Verificar idade")
        print("2. Contar até N")
        print("3. Sair")
        opcao = input("Escolha uma opção: ")
        if opcao == "1":
            verificar_idade()
        elif opcao == "2":
            contar_ate_n()
        elif opcao == "3":
            print("Encerrando o programa...")
            break
        else:
            print("Opção inválida.")


menu()
