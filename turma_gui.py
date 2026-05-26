import sqlite3
import tkinter as tk
from tkinter import messagebox, ttk

def conectar_db():
    """Cria a conexão com o banco de dados e a tabela se não existir."""
    conexao = sqlite3.connect("sistema_escolar.db")
    cursor = conexao.cursor()
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS alunos (
            matricula TEXT PRIMARY KEY,
            nome TEXT NOT NULL,
            nota1 REAL NOT NULL,
            nota2 REAL NOT NULL,
            media REAL NOT NULL,
            situacao TEXT NOT NULL
        )
    """
    )
    conexao.commit()
    return conexao, cursor



def validar_entradas():
    """Valida os campos da interface e retorna os dados convertidos se válidos."""
    matricula = entry_matricula.get().strip()
    nome = entry_nome.get().strip()
    str_nota1 = entry_nota1.get().strip()
    str_nota2 = entry_nota2.get().strip()

    # Validação de campos vazios
    if not matricula or not nome or not str_nota1 or not str_nota2:
        messagebox.showerror("Erro de Validação", "Todos os campos são obrigatórios!")
        return None

    # Validação de letras no lugar de números
    try:
        nota1 = float(str_nota1.replace(",", "."))
        nota2 = float(str_nota2.replace(",", "."))
    except ValueError:
        messagebox.showerror(
            "Erro de Tipo", "As notas devem ser valores numéricos válidos."
        )
        return None

    # Validação de notas fora do intervalo [0, 10]
    if not (0 <= nota1 <= 10) or not (0 <= nota2 <= 10):
        messagebox.showerror(
            "Erro de Intervalo", "As notas devem estar entre 0.0 e 10.0."
        )
        return None

    return matricula, nome, nota1, nota2


def obter_situacao(media):
    """Define a situação com base nas regras de média escoladas."""
    if media >= 6.0:
        return "Aprovado"
    elif 4.0 <= media < 6.0:
        return "Recuperação"
    else:
        return "Reprovado"



def calcular_media():
    """Calcula a média, define a situação e atualiza os rótulos da tela."""
    dados = validar_entradas()
    if dados is None:
        return None  # Interrompe se a validação falhar

    _, _, nota1, nota2 = dados
    media = (nota1 + nota2) / 2

    situacao = obter_situacao(media)

    # Atualiza os componentes visuais de resultado
    lbl_resultado_media.config(text=f"{media:.2f}")
    lbl_resultado_situacao.config(text=situacao)

    # Muda a cor do texto da situação para melhor feedback visual
    if situacao == "Aprovado":
        lbl_resultado_situacao.config(foreground="green")
    elif situacao == "Recuperação":
        lbl_resultado_situacao.config(foreground="orange")
    else:
        lbl_resultado_situacao.config(foreground="red")

    return media, situacao


def salvar_dados():
    """Calcula os dados e salva/atualiza o registro no banco de dados."""
    dados = validar_entradas()
    if dados is None:
        return

    matricula, nome, nota1, nota2 = dados

    # Força o cálculo da média antes de salvar para garantir consistência
    res = calcular_media()
    if res is None:
        return
    media, situacao = res

    try:
        conn, cursor = conectar_db()
        # INSERT OR REPLACE atualiza o registro caso a matrícula já exista
        cursor.execute(
            """
            INSERT OR REPLACE INTO alunos (matricula, nome, nota1, nota2, media, situacao)
            VALUES (?, ?, ?, ?, ?, ?)
        """,
            (matricula, nome, nota1, nota2, media, situacao),
        )
        conn.commit()
        conn.close()
        messagebox.showinfo(
            "Sucesso", f"Dados do(a) aluno(a) {nome} salvos com sucesso!"
        )
    except sqlite3.Error as e:
        messagebox.showerror("Erro de Banco de Dados", f"Falha ao salvar dados: {e}")


def consultar_alunos():
    """Abre uma nova janela listando todos os alunos cadastrados em uma tabela."""
    janela_consulta = tk.Toplevel(janela_principal)
    janela_consulta.title("Alunos Cadastrados")
    janela_consulta.geometry("700x400")

    lbl_titulo = tk.Label(
        janela_consulta,
        text="Relatório de Alunos Cadastrados",
        font=("Arial", 14, "bold"),
    )
    lbl_titulo.pack(pady=10)

    # Criando a tabela (Treeview)
    colunas = ("matricula", "nome", "nota1", "nota2", "media", "situacao")
    tabela = ttk.Treeview(janela_consulta, columns=colunas, show="headings")

    # Definindo cabeçalhos
    tabela.heading("matricula", text="Matrícula")
    tabela.heading("nome", text="Nome")
    tabela.heading("nota1", text="Nota 1")
    tabela.heading("nota2", text="Nota 2")
    tabela.heading("media", text="Média Final")
    tabela.heading("situacao", text="Situação")

    # Ajustando larguras das colunas
    tabela.column("matricula", width=100, anchor="center")
    tabela.column("nome", width=200, anchor="w")
    tabela.column("nota1", width=70, anchor="center")
    tabela.column("nota2", width=70, anchor="center")
    tabela.column("media", width=80, anchor="center")
    tabela.column("situacao", width=120, anchor="center")

    # Buscando dados do banco
    try:
        conn, cursor = conectar_db()
        cursor.execute(
            "SELECT matricula, nome, nota1, nota2, media, situacao FROM alunos"
        )
        linhas = cursor.fetchall()
        conn.close()

        for linha in linhas:
            tabela.insert("", tk.END, values=linha)

    except sqlite3.Error as e:
        messagebox.showerror("Erro", f"Erro ao ler banco de dados: {e}")

    tabela.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)


def limpar_campos():
    """Limpa todos os campos de texto e redefine os rótulos de resultado."""
    entry_matricula.delete(0, tk.END)
    entry_nome.delete(0, tk.END)
    entry_nota1.delete(0, tk.END)
    entry_nota2.delete(0, tk.END)
    lbl_resultado_media.config(text="-")
    lbl_resultado_situacao.config(text="-", foreground="black")


def encerrar_sistema():
    """Solicita confirmação e encerra o programa."""
    if messagebox.askyesno("Sair", "Deseja realmente encerrar o sistema?"):
        janela_principal.destroy()


# Inicializa o BD ao abrir o app
conectar_db()

janela_principal = tk.Tk()
janela_principal.title("Calculadora de Média Escolar Acadêmica")
janela_principal.geometry("480x420")
janela_principal.resizable(False, False)

# Container principal para espaçamento (Padding)
frame_corpo = ttk.Frame(janela_principal, padding="20")
frame_corpo.pack(fill=tk.BOTH, expand=True)

# --- Seção de Formulário (Entradas) ---
lbl_titulo_app = tk.Label(
    frame_corpo, text="Cadastro e Cálculo de Notas", font=("Arial", 14, "bold")
)
lbl_titulo_app.pack(pady=(0, 15))

frame_form = ttk.LabelFrame(frame_corpo, text=" Dados do Aluno ", padding="10")
frame_form.pack(fill=tk.X, pady=5)

# Matrícula
lbl_matricula = ttk.Label(frame_form, text="Matrícula:")
lbl_matricula.pack(anchor="w")
entry_matricula = ttk.Entry(frame_form)
entry_matricula.pack(fill=tk.X, pady=(0, 10))

# Nome
lbl_nome = ttk.Label(frame_form, text="Nome do Aluno:")
lbl_nome.pack(anchor="w")
entry_nome = ttk.Entry(frame_form)
entry_nome.pack(fill=tk.X, pady=(0, 10))

# Bloco lado a lado para as notas
frame_notas = ttk.Frame(frame_form)
frame_notas.pack(fill=tk.X)

frame_n1 = ttk.Frame(frame_notas)
frame_n1.pack(side=tk.LEFT, expand=True, fill=tk.X, prx=5)
lbl_nota1 = ttk.Label(frame_n1, text="Nota Prova 1:")
lbl_nota1.pack(anchor="w")
entry_nota1 = ttk.Entry(frame_n1)
entry_nota1.pack(fill=tk.X)

frame_n2 = ttk.Frame(frame_notas)
frame_n2.pack(side=tk.RIGHT, expand=True, fill=tk.X, padx=5)
lbl_nota2 = ttk.Label(frame_n2, text="Nota Prova 2:")
lbl_nota2.pack(anchor="w")
entry_nota2 = ttk.Entry(frame_n2)
entry_nota2.pack(fill=tk.X)

# --- Seção de Resultados ---
frame_resultados = ttk.LabelFrame(frame_corpo, text=" Desempenho ", padding="10")
frame_resultados.pack(fill=tk.X, pady=15)

lbl_txt_media = ttk.Label(
    frame_resultados, text="Média Final:", font=("Arial", 11, "bold")
)
lbl_txt_media.pack(side=tk.LEFT, padx=(10, 5))

lbl_resultado_media = ttk.Label(
    frame_resultados, text="-", font=("Arial", 11, "bold")
)
lbl_resultado_media.pack(side=tk.LEFT, padx=(0, 30))

lbl_txt_situacao = ttk.Label(
    frame_resultados, text="Situação:", font=("Arial", 11, "bold")
)
lbl_txt_situacao.pack(side=tk.LEFT, padx=(10, 5))

lbl_resultado_situacao = ttk.Label(
    frame_resultados, text="-", font=("Arial", 11, "bold")
)
lbl_resultado_situacao.pack(side=tk.LEFT)

# --- Seção de Botões ---
frame_botoes = ttk.Frame(frame_corpo)
frame_botoes.pack(fill=tk.X, side=tk.BOTTOM)

# Linha superior de botões
btn_calcular = ttk.Button(
    frame_botoes, text="Calcular Média", command=calcular_media
)
btn_calcular.pack(side=tk.LEFT, expand=True, fill=tk.X, padx=2)

btn_salvar = ttk.Button(frame_botoes, text="Salvar Dados", command=salvar_dados)
btn_salvar.pack(side=tk.LEFT, expand=True, fill=tk.X, padx=2)

btn_consultar = ttk.Button(
    frame_botoes, text="Consultar", command=consultar_alunos
)
btn_consultar.pack(side=tk.LEFT, expand=True, fill=tk.X, padx=2)

# Linha inferior de botões (Limpar e Encerrar)
frame_botoes_sub = ttk.Frame(frame_corpo)
frame_botoes_sub.pack(fill=tk.X, side=tk.BOTTOM, pady=(0, 5))

btn_limpar = ttk.Button(frame_botoes_sub, text="Limpar Campos", command=limpar_campos)
btn_limpar.pack(side=tk.LEFT, expand=True, fill=tk.X, padx=2)

btn_encerrar = ttk.Button(
    frame_botoes_sub, text="Encerrar Sistema", command=encerrar_sistema
)
btn_encerrar.pack(side=tk.LEFT, expand=True, fill=tk.X, padx=2)

# Executa o loop principal da interface
janela_principal.mainloop()