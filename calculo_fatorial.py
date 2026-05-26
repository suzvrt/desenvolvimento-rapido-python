def calcular_fatorial(n):
    if n < 0:
        return None  # não existe fatorial de número negativo
    resultado = 1
    for i in range(1, n + 1):
        resultado *= i
    return resultado


while True:
    try:
        numero = int(
            input("Digite um número inteiro positivo (ou -1 para sair): "))
        if numero == -1:
            print("Encerrando o programa. Até logo!")
            break  # sai do loop
        elif numero < 0:
            print("Erro: o número deve ser positivo!")
            continue  # volta ao início do loop
        else:
            fatorial = calcular_fatorial(numero)
        print(f"O fatorial de {numero} é {fatorial}")
    except ValueError:
        print("Entrada inválida! Por favor, digite um número inteiro.")
