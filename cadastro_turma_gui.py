import tkinter as tk
from tkinter import messagebox
# Dicionário principal
alunos = {}


# Função para calcular média
def calcular_media(n1, n2, n3):
    return (n1 + n2 + n3) / 3


# Função para cadastrar aluno
def cadastrar():
    nome = entry_nome.get()
    try:
        n1 = float(entry_nota1.get())
        n2 = float(entry_nota2.get())
        n3 = float(entry_nota3.get())
    except:
        messagebox.showerror("Erro", "Digite notas válidas!")
        return
    if nome == "":
        messagebox.showwarning("Aviso", "Digite o nome do aluno!")
        return
    media = calcular_media(n1, n2, n3)
    situacao = "Aprovado" if media >= 6 else "Reprovado"
    alunos[nome] = {
        "nota1": n1,
        "nota2": n2,
        "nota3": n3,
        "media": media,
        "situacao": situacao
    }
    atualizar_lista()
    limpar_campos()


# Atualiza lista na tela
def atualizar_lista():
    lista.delete(0, tk.END)
    for nome, dados in alunos.items():
        lista.insert(
            tk.END, f"{nome} | Média: {dados['media']:.1f} | {dados['situacao']}")


# Limpa campos
def limpar_campos():
    entry_nome.delete(0, tk.END)
    entry_nota1.delete(0, tk.END)
    entry_nota2.delete(0, tk.END)
    entry_nota3.delete(0, tk.END)


# Remove aluno
def remover():
    selecionado = lista.curselection()
    if not selecionado:
        messagebox.showwarning("Aviso", "Selecione um aluno!")
        return
    texto = lista.get(selecionado)
    nome = texto.split(" | ")[0]
    del alunos[nome]
    atualizar_lista()


# Buscar aluno
def buscar():
    nome = entry_nome.get()
    if nome in alunos:
        dados = alunos[nome]
        messagebox.showinfo(
            "Aluno encontrado", f"Nome: {nome}\n" f"Notas: {dados['nota1']}, {dados['nota2']}, {dados['nota3']}\n"f"Média: {dados['media']:.1f}\n" f"Situação: {dados['situacao']}"
        )
    else:
        messagebox.showwarning("Aviso", "Aluno não encontrado!")


# Criando janela
janela = tk.Tk()
janela.title("Sistema de Alunos")
janela.geometry("400x400")
# Campos
tk.Label(janela, text="Nome do aluno").pack()
entry_nome = tk.Entry(janela)
entry_nome.pack()
tk.Label(janela, text="Nota 1").pack()
entry_nota1 = tk.Entry(janela)
entry_nota1.pack()
tk.Label(janela, text="Nota 2").pack()
entry_nota2 = tk.Entry(janela)
entry_nota2.pack()
tk.Label(janela, text="Nota 3").pack()
entry_nota3 = tk.Entry(janela)
entry_nota3.pack()
# Botões
tk.Button(janela, text="Cadastrar",
          command=cadastrar).pack(pady=5)
tk.Button(janela, text="Buscar",
          command=buscar).pack(pady=5)
tk.Button(janela, text="Remover",
          command=remover).pack(pady=5)
# Lista
lista = tk.Listbox(janela, width=50)
lista.pack(pady=10)
# Executar
janela.mainloop()
