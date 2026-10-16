import tkinter as tk
from tkinter import ttk

# ---------- Janela ----------
janela = tk.Tk()
janela.title("Sistema de Biblioteca")
janela.geometry("600x300")
janela.configure(bg="#0d0d0d")  # fundo escuro

# ---------- Estilo ----------
style = ttk.Style()
style.theme_use("clam")  # 'clam' permite customizar cores

COR_FUNDO   = "#0d0d0d"
COR_CARD    = "#111111"
COR_TEXTO   = "#ffffff"
COR_CINZA   = "#cfcfcf"
COR_LARANJA = "#e07b39"
COR_LINHA   = "#1e1e1e"

style.configure(
    "Custom.Treeview",
    background=COR_CARD,
    foreground=COR_CINZA,
    fieldbackground=COR_CARD,
    rowheight=32,
    borderwidth=0,
    font=("Segoe UI", 11)
)
style.configure(
    "Custom.Treeview.Heading",
    background=COR_CARD,
    foreground=COR_TEXTO,
    font=("Segoe UI", 11, "bold"),
    relief="flat"
)
style.map(
    "Custom.Treeview",
    background=[("selected", COR_LARANJA)],
    foreground=[("selected", "#ffffff")]
)
style.map(
    "Custom.Treeview.Heading",
    background=[("active", COR_CARD)]
)

# ---------- Cabeçalho (ícone + título) ----------
header = tk.Frame(janela, bg=COR_FUNDO)
header.pack(fill="x", padx=20, pady=(20, 5))

icone = tk.Label(header, text="📖", bg=COR_FUNDO, fg=COR_TEXTO,
                 font=("Segoe UI Emoji", 14))
icone.pack(side="left", padx=(0, 8))

titulo = tk.Label(header, text="Sistema de Biblioteca",
                  bg=COR_FUNDO, fg=COR_TEXTO,
                  font=("Segoe UI", 14, "bold"))
titulo.pack(side="left")

# ---------- Tabela ----------
colunas = ("titulo", "autor", "quantidade")
tabela = ttk.Treeview(
    janela,
    columns=colunas,
    show="headings",
    style="Custom.Treeview"
)

tabela.heading("titulo",     text="Título",     anchor="w")
tabela.heading("autor",      text="Autor",      anchor="w")
tabela.heading("quantidade", text="Quantidade", anchor="e")

tabela.column("titulo",     anchor="w", width=220)
tabela.column("autor",      anchor="w", width=220)
tabela.column("quantidade", anchor="e", width=100)

# Dados de exemplo
dados = [
    ("Dom Casmurro", "Machado de Assis", 4),
    ("O Cortiço",    "Aluísio Azevedo",  2),
    ("Iracema",      "José de Alencar",  5),
]

for linha in dados:
    tabela.insert("", tk.END, values=linha)

tabela.pack(fill="both", expand=True, padx=20, pady=(5, 20))

janela.mainloop()