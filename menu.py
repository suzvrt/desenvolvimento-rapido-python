def verificar_idade():
    idade = int(input("Digite sua idade: "))
    if idade < 18:
        print("Você é menor de idade.")
    elif idade < 60:
        print("Você é adulto.")
    else:
        print("Você é idoso.")


def contar_ate_n():
    n = int(input("Digite um número: "))
    for i in range(1, n + 1):
        print(i, end=" ")
    print()


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
