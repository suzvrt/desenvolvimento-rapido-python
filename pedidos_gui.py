import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3
#======BANCO DE DADOS =================
conexao = sqlite3.connect("pedidos.db")
cursor = conexao.cursor()
cursor.execute("""
create table if not exists pedidos(
id integer primary key autoincrement,
cliente text,
data text
               )
               """)
cursor.execute("""
create table if not exists itens_pedido(
id integer primary key autoincrement,
pedido_id integer,
produto text,
quantidade integer,
valor real,
foreign key(pedido_id)
references pedidos(id)
               )""")
conexao.commit()
# ============ FUNCOES ================:
def formatar_data(event=None):
    texto = entrada_data.get()
    texto = texto.replace("/","")
    novo=""
    for i in range(len(texto)):
        if i== 2 or i== 4:
            novo +="/"
        novo += texto[i]
    entrada_data.delete(0, tk.END)
    entrada_data.insert(0, novo[:10])
def cadastrar_pedido():
    cliente = entrada_cliente.get()
    data = entrada_data.get()
    if cliente =="" or data =="":
        messagebox.showerror("Erro","Preencha os campos")
        return
    cursor.execute("""
    insert into pedidos(cliente, data)
    values(?,?)
    """,(cliente, data))
    conexao.commit()
    messagebox.showinfo("Sucesso","Pedido cadastrado")
    entrada_cliente.delete(0, tk.END)
    entrada_data.delete(0, tk.END)
    listar_pedidos()
def listar_pedidos():
    for item in tabela_pedidos.get_children():
        tabela_pedidos.delete(item)
    cursor.execute("""
    select* from pedidos
    order by id desc
    """)
    pedidos = cursor.fetchall()
    for pedido in pedidos:
        tabela_pedidos.insert("", tk.END, values=pedido)
def selecionar_pedido(event=None):
    selecionado =tabela_pedidos.focus()
    if selecionado =="":
        return
    dados = tabela_pedidos.item(selecionado)
    id_pedido = dados["values"][0]
    entrada_pedido_id.delete(0, tk.END)
    entrada_pedido_id.insert(0, id_pedido)
def adicionar_item():
    pedido_id = entrada_pedido_id.get()
    produto = entrada_produto.get()
    quantidade = entrada_quantidade.get()
    valor = entrada_valor.get()
    if ( pedido_id =="" or produto =="" or quantidade =="" or valor ==""):
        messagebox.showerror("Erro","Preencha todos os campos")
        return
    try:
        quantidade = int(quantidade)
        valor = float(valor)
    except:
        messagebox.showerror("Erro","Quantidade e valor inválidos")
        return
    cursor.execute("""
    insert into itens_pedido(
        pedido_id,
        produto,
        quantidade,
        valor
    )
    values(?,?,?,?)
                   """,(
        pedido_id,
        produto,
        quantidade,
        valor
    ))
    conexao.commit()
    messagebox.showinfo("Sucesso","Item adicionado")
    entrada_produto.delete(0, tk.END)
    entrada_quantidade.delete(0, tk.END)
    entrada_valor.delete(0, tk.END)
def excluir_pedido():
    selecionado= tabela_pedidos.focus()
    if selecionado =="":
        messagebox.showwarning("Atenção","Selecione um pedido")
        return
    dados = tabela_pedidos.item(selecionado)
    id_pedido = dados["values"][0]
    resposta = messagebox.askyesno("Confirmação","Deseja excluir o pedido?")
    if resposta:
        cursor.execute("""
        delete from itens_pedido
        where pedido_id= ?
        """,(id_pedido,))
        cursor.execute("""
        delete from pedidos
        where id = ?
        """,(id_pedido,))
        conexao.commit()
        messagebox.showinfo("Sucesso","Pedido excluido")
        listar_pedidos()
def listar_itens():
    selecionado = tabela_pedidos.focus()
    if selecionado =="":
        messagebox.showwarning("Atenção","Selecione um pedido")
        return
    dados= tabela_pedidos.item(selecionado)
    id_pedido = dados["values"][0]
    janela_itens = tk.Toplevel()
    janela_itens.title( f"Itens do pedido {id_pedido}")
    janela_itens.geometry("700x400")
    tabela = ttk.Treeview(
        janela_itens,
        columns=(
        "produto",
        "quantidade",
        "valor",
        "subtotal"
        ),
        show="headings"
    )
    tabela.heading("produto", text="Produto")
    tabela.heading("quantidade", text="Quantidade")
    tabela.heading("valor", text="Valor")
    tabela.heading("subtotal", text="Subtotal")
    tabela.column("produto", width=250)
    tabela.column("quantidade", width=100)
    tabela.column("valor", width=100)
    tabela.column("subtotal", width=120)
    tabela.pack(
    fill="both",
    expand=True,
    padx=10,
    pady=10
    )
    cursor.execute("""
    select produto, quantidade, valor
    from itens_pedido
    where pedido_id =?
    """,(id_pedido,))
    itens = cursor.fetchall()
    total = 0.0
    for item in itens:
        produto = item[0]
        quantidade = int(item[1])
        valor = float(item[2])
        subtotal= quantidade * valor
        total += subtotal
        tabela.insert(
        "",
        tk.END,
        values=(
        produto,
        quantidade,
        f"R$ {valor:.2f}",
        f"R$ {subtotal:.2f}"
        )
        )
    label_total= tk.Label(
        janela_itens,
        text=f"Total do pedido: R$ {total:.2f}",
        font=("arial",14,"bold")
    )
    label_total.pack(pady=10)
#=================JANELA =================
janela= tk.Tk()
janela.title("Controle de Pedidos")
janela.geometry("950x550")
janela.configure(bg="#f2f2f2")
#============ TITULO =================
titulo = tk.Label(
    janela,
    text="Sistema de Controle de Pedidos",
    font=("arial", 20,"bold"),
    bg="#f2f2f2",
    fg="#1f3b73"
)
titulo.pack(pady=15)
# ================= FRAME PEDIDO ================:
frame_pedido = tk.LabelFrame(
    janela,
    text="Cadastro de pedido",
    font=("arial", 11,"bold"),
    bg="#f2f2f2",
    padx=10,
    pady=10
)
frame_pedido.pack(
    fill="x",
    padx=20,
    pady=10
)
tk.Label(
    frame_pedido,
    text="Cliente",
    bg="#f2f2f2"
).grid(row=0,column=0)
entrada_cliente = tk.Entry(
    frame_pedido,
    width=30
)
entrada_cliente.grid(
    row=0,
    column=1,
    padx=5
)
tk.Label(
    frame_pedido,
    text="Data",
    bg="#f2f2f2"
).grid(row=0, column=2)
entrada_data = tk.Entry(
    frame_pedido,
    width=15
)
entrada_data.grid(
    row=0,
    column=3,
    padx=5
)
entrada_data.bind(
    "<KeyRelease>",
    formatar_data
)
botao_cadastrar = tk.Button(
    frame_pedido,
    text="Cadastrar pedido",
    bg="#1f6aa5",
    fg="white",
    width=18,
    command=cadastrar_pedido
)
botao_cadastrar.grid(
row=0,
column=4,
padx=10
)
botao_excluir = tk.Button(
    frame_pedido,
    text="Excluir pedido",
    bg="#c0392b",
    fg="white",
    width=18,
    command=excluir_pedido
)
botao_excluir.grid(
row=0,
column=5
)
#================= TABELA PEDIDOS ================:
tabela_pedidos = ttk.Treeview(
    janela,
    columns=("id","cliente","data"),
    show="headings",
    height=10
)
tabela_pedidos.heading("id",text="ID")
tabela_pedidos.heading("cliente", text="Cliente")
tabela_pedidos.heading("data", text="Data")
tabela_pedidos.column("id", width=80)
tabela_pedidos.column("cliente", width=350)
tabela_pedidos.column("data", width=120)
tabela_pedidos.pack(
    fill="x",
    padx=20,
    pady=10
)
tabela_pedidos.bind(
    "<ButtonRelease-1>",
    selecionar_pedido
)
# ================= FRAME ITENS ================:
frame_itens = tk. LabelFrame( janela, text="Adicionar item ao pedido", font=("arial", 11,"bold"), bg="#f2f2f2",
padx=10, pady=10)
frame_itens.pack( fill="x", padx=20, pady=10)
tk.Label(frame_itens, text="Pedido ID",bg="#f2f2f2").grid(row=0, column=0)
entrada_pedido_id = tk.Entry( frame_itens, width=10)
entrada_pedido_id.grid( row=0, column=1, padx=5)
tk.Label(frame_itens, text="Produto", bg="#f2f2f2").grid(row=0, column=2)
entrada_produto = tk.Entry(frame_itens, width=25)
entrada_produto.grid( row=0, column=3, padx=5)
tk.Label(frame_itens, text="Quantidade",bg="#f2f2f2").grid(row=0,column=4)
entrada_quantidade = tk.Entry( frame_itens, width=10)
entrada_quantidade.grid( row=0, column=5, padx=5)
tk.Label(frame_itens, text="Valor", bg="#f2f2f2").grid(row=0, column=6)
entrada_valor= tk.Entry(frame_itens, width=10)
entrada_valor.grid(row=0, column=7, padx=5)
botao_item = tk.Button( frame_itens, text="Adicionar item", bg="#27ae60", fg="white", width=18, command=adicionar_item)
botao_item.grid( row=0, column=8, padx=10)
#================= BOTAO LISTAR ===============
botao_listar= tk.Button(janela, text="Listar itens do pedido", bg="#34495e", fg="white", font=("arial", 11,
"bold"), width=25, command=listar_itens)
botao_listar.pack(pady=15)
# =================INICIO =================
listar_pedidos()
janela.mainloop()
