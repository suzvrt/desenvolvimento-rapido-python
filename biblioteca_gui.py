import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3

conexao = sqlite3.connect("biblioteca.db")
cursor = conexao.cursor()
cursor.execute("""
               create table if not exists livros(
               id integer primary key autoincrement,
               nome text)
               """)
cursor.execute("""
               create table if not exists emprestimos(
               id integer primary key autoincrement,
               livro_id integer,
               aluno text,
               foreign key(livro_id) references livros (id))
               """)
conexao.commit()

def cadastrar_livro():
    nome = entrada_livro.get()
    if nome == "":
        messagebox.showerror("Erro", "Digite o nome do livro")
        return
    cursor.execute("""
                   insert into livros(nome)
                   values(?)
                   """, (nome,))
    conexao.commit()
    entrada_livro.delete(0, tk.END)
    listar_livros()

def listar_livros():
    for item in tabela.get_children():
        tabela.delete(item)
    cursor.execute("""
                   select * from livros
                   """)
    dados = cursor.fetchall()
    for livro in dados:
        tabela.insert("", tk.END, values=livro)

def selecionar_livro(event):
    item = tabela.focus()
    if item == "":
        return
    dados = tabela.item(item)
    id_livro = dados["values"][0]
    entrada_id.delete(0, tk.END)
    entrada_id.insert(0, id_livro)

def emprestar():
    livro_id = entrada_id.get()
    aluno = entrada_aluno.get()
    if livro_id == "" or aluno == "":
        messagebox.showerror("Erro", "Preencha os campos")
        return
    cursor.execute("""
                    insert into emprestimos(
                   livro_id,
                   aluno)
                   values(?,?)
                   """, (
                       livro_id,
                       aluno
                   ))
    conexao.commit()
    entrada_aluno.delete(0, tk.END)
    messagebox.showinfo(
        "Sucesso",
        "Empréstimo realizado"
    )

def listar_emprestimos():
    item = tabela.focus()
    if item == "":
        return
    dados = tabela.item(item)
    id_livro = dados["values"][0]
    janela = tk.Toplevel()
    janela.title("Empréstimos")
    janela.geometry("400x300")
    lista = tk.Listbox(
        janela,
        font=("arial", 12)
    )
    lista.pack(
        fill="both",
        expand=True,
        padx=10,
        pady=10
    )
    cursor.execute("""
                   select aluno from emprestimos
                   where livro_id = ?
                   """, (id_livro,))
    emprestimos = cursor.fetchall()
    for emprestimo in emprestimos:
        lista.insert(tk.END, emprestimo[0])

def excluir_livro():
    item = tabela.focus()
    if item == "":
        return
    dados = tabela.item(item)
    id_livro = dados["values"][0]
    cursor.execute("""
                   delete from emprestimos where livro_id = ?
                   """, (id_livro,))
    cursor.execute("""
                   delete from livros where id = ?
                   """, (id_livro,))
    conexao.commit()
    listar_livros()

janela = tk.Tk()
janela.title("Biblioteca")
janela.geometry("700x500")
janela.configure(bg="#ecf0f1")
titulo = tk.Label(
    janela,
    text="Sistema de Biblioteca",
    font=("arial", 20, "bold"),
    bg="#ecf0f1",
    fg="#2c3e50")
titulo.pack(pady=15)
frame1 = tk.Frame(
    janela,
    bg="#ecf0f1"
)
frame1.pack(pady=10)
tk.Label(
    frame1,
    text="Livro",
    bg="#ecf0f1",
).grid(row=0, column=0)
entrada_livro = tk.Entry(frame1, width=30)
entrada_livro.grid(row=0, column=1, padx=5)
botao_cadastrar = tk.Button(frame1, text="Cadastrar", bg="#3498db", fg="white", command=cadastrar_livro)
botao_cadastrar.grid(
    row=0,
    column=2,
    padx=5
)
tabela = ttk.Treeview(
    janela,
    columns=("id","nome"),
    show="headings",
    height=10
)
tabela.heading("id", text="id")
tabela.heading("nome", text="livro")
tabela.column("id", width=80)
tabela.column("nome", width=400)
tabela.pack(padx=20, pady=15)
tabela.bind("<ButtonRelease-1>",selecionar_livro)
frame2 = tk.Frame(janela, bg="#ecf0f1")
frame2.pack(pady=10)

tk.Label(frame2, text="id", bg="#ecf0f1").grid(row=0,column=0)
entrada_id = tk.Entry(
    frame2,
    width=10
)
entrada_id.grid(row=0, column=1, padx=5)

tk.Label(frame2, text="aluno", bg="#ecf0f1").grid(row=0,column=2)
entrada_aluno = tk.Entry(
    frame2,
    width=25
)
entrada_aluno.grid(row=0, column=3, padx=5)

botao_emprestar = tk.Button(frame2, text="Emprestar", bg="#27ae60", fg="white", command=emprestar)
botao_emprestar.grid(row=0, column=4, padx=5)

frame3 = tk.Frame(janela, bg="#ecf0f1")
frame3.pack(pady=20)

botao_listar = tk.Button(frame3, text="Listar empréstimos", bg="#34495e", fg="white", width=20, command=listar_emprestimos)
botao_listar.grid(row=0, column=0, padx=10)

botao_excluir = tk.Button(frame3, text="Excluir livro", bg="#c0392b", fg="white", width=20, command=excluir_livro)
botao_excluir.grid(row=0, column=1, padx=10)

listar_livros()
janela.mainloop()
