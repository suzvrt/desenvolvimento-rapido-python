import tkinter as tk


def adicionar_valor(valor):
    texto_atual = visor.get()
    visor.set(texto_atual + str(valor))


def limpar_visor():
    visor.set("")


def calcular_resultado():
    try:
        conta = visor.get()
        resultado = eval(conta)
        visor.set(str(resultado))
    except:
        visor.set("erro")


# janela principal
janela = tk.Tk()
janela.title("calculadora")
janela.geometry("300x400")
# variável do visor
visor = tk.StringVar()
# campo de exibição
campo = tk.Entry(
    janela,
    textvariable=visor,
    font=("arial", 20),
    bd=10,
    justify="right"
)
campo.grid(row=0, column=0, columnspan=4, sticky="we")
# lista de botões
lista_botoes = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),
]
# criação dos botões
for texto, linha, coluna in lista_botoes:
    if texto == "=":
        botao = tk.Button(janela, text=texto, padx=20,
                          pady=20, command=calcular_resultado)
    else:
        botao = tk.Button(janela, text=texto, padx=20, pady=20,
                          command=lambda t=texto: adicionar_valor(t))
    botao.grid(row=linha, column=coluna)
# botão limpar
botao_limpar = tk.Button(janela, text="c", padx=20,
                         pady=20, command=limpar_visor)
botao_limpar.grid(row=5, column=0, columnspan=4, sticky="we")
# loop da aplicação
janela.mainloop()
