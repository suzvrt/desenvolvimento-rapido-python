import tkinter as tk
from tkinter import messagebox
tarefas = {}


# Adicionar tarefa
def adicionar():
    tarefa = entry_tarefa.get()
    if tarefa == "":
        messagebox.showwarning("Aviso", "Digite uma tarefa!")
        return
    tarefas[tarefa] = "Pendente"
    atualizar_lista()
    entry_tarefa.delete(0, tk.END)


# Atualizar lista
def atualizar_lista():
    lista.delete(0, tk.END)
    for tarefa, status in tarefas.items():
        lista.insert(tk.END, f"{tarefa} - {status}")


# Marcar como concluída
def concluir():
    selecionado = lista.curselection()
    if not selecionado:
        messagebox.showwarning("Aviso", "Selecione uma tarefa!")
        return
    texto = lista.get(selecionado)
    tarefa = texto.split(" - ")[0]
    tarefas[tarefa] = "Concluída"
    atualizar_lista()


# Remover tarefa
def remover():
    selecionado = lista.curselection()
    if not selecionado:
        messagebox.showwarning("Aviso", "Selecione uma tarefa!")
        return
    texto = lista.get(selecionado)
    tarefa = texto.split(" - ")[0]
    del tarefas[tarefa]
    atualizar_lista()


janela = tk.Tk()
janela.title("Lista de Tarefas")
# Campo
tk.Label(janela, text="Nova tarefa:").pack()
entry_tarefa = tk.Entry(janela, width=40)
entry_tarefa.pack()
tk.Button(janela, text="Adicionar",
          command=adicionar).pack(pady=5)
tk.Button(janela, text="Concluir",
          command=concluir).pack(pady=5)
tk.Button(janela, text="Remover",
          command=remover).pack(pady=5)
lista = tk.Listbox(janela, width=50)
lista.pack(pady=10)
janela.mainloop()
