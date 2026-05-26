import tkinter as tk
from tkinter import messagebox
# Dicionário para armazenar os dados
dados = {}


# Função para adicionar pessoa
def adicionar():
    nome = entry_nome.get()
    idade = entry_idade.get()
    if nome == "" or idade == "":
        messagebox.showwarning("Aviso", "Preencha todos os campos!")
        return
    dados[nome] = idade
    atualizar_lista()
    entry_nome.delete(0, tk.END)
    entry_idade.delete(0, tk.END)


# Função para atualizar lista na tela
def atualizar_lista():
    lista.delete(0, tk.END)
    for nome, idade in dados.items():
        lista.insert(tk.END, f"{nome} - {idade} anos")


# Função para remover pessoa
def remover():
    selecionado = lista.curselection()
    if not selecionado:
        messagebox.showwarning("Aviso", "Selecione alguém para remover!")
        return
    texto = lista.get(selecionado)
    nome = texto.split(" - ")[0]
    del dados[nome]
    atualizar_lista()


# Criando janela principal
janela = tk.Tk()
janela.title("Cadastro com Dicionário")
# Labels e entradas
tk.Label(janela, text="Nome:").pack()
entry_nome = tk.Entry(janela)
entry_nome.pack()
tk.Label(janela, text="Idade:").pack()
entry_idade = tk.Entry(janela)
entry_idade.pack()
# Botões
tk.Button(janela, text="Adicionar",
          command=adicionar).pack(pady=5)
tk.Button(janela, text="Remover",
          command=remover).pack(pady=5)
# Lista
lista = tk.Listbox(janela, width=40)
lista.pack(pady=10)
# Rodando aplicação
janela.mainloop()
