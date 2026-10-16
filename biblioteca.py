
import tkinter as tk
from tkinter import ttk, messagebox


# Classe que representa um livro
class Livro:
    def __init__(self, titulo, autor, quantidade):
        self.titulo = titulo
        self.autor = autor
        self._quantidade = 0
        self.quantidade = quantidade

    @property
    def quantidade(self):
        return self._quantidade

    @quantidade.setter
    def quantidade(self, valor):
        if not isinstance(valor, int) or valor < 0:
            raise ValueError("A quantidade deve ser um inteiro não negativo.")
        self._quantidade = valor


# Classe que representa a interface gráfica
class AppBiblioteca:
    def __init__(self, janela):
        self.janela = janela
        self.janela.title("Sistema de Biblioteca")
        self.janela.geometry("700x450")

        # Lista que armazenará os objetos Livro
        self.livros = []

        # Título
        tk.Label(
            janela,
            text="Cadastro de Livros",
            font=("Arial", 18, "bold")
        ).pack(pady=10)

        # Formulário
        formulario = tk.Frame(janela)
        formulario.pack(pady=10)

        tk.Label(formulario, text="Título:").grid(
            row=0, column=0, padx=5, pady=5
        )
        self.campo_titulo = tk.Entry(formulario, width=35)
        self.campo_titulo.grid(row=0, column=1, padx=5)

        tk.Label(formulario, text="Autor:").grid(
            row=1, column=0, padx=5, pady=5
        )
        self.campo_autor = tk.Entry(formulario, width=35)
        self.campo_autor.grid(row=1, column=1, padx=5)

        tk.Label(formulario, text="Quantidade:").grid(
            row=2, column=0, padx=5, pady=5
        )
        self.campo_quantidade = tk.Entry(formulario, width=35)
        self.campo_quantidade.grid(row=2, column=1, padx=5)

        # Botão cadastrar
        tk.Button(
            janela,
            text="Cadastrar Livro",
            command=self.cadastrar,
            bg="#2563EB",
            fg="white"
        ).pack(pady=10)

        # Criando a tabela Treeview
        self.tabela = ttk.Treeview(
            janela,
            columns=("titulo", "autor", "quantidade"),
            show="headings"
        )

        # Cabeçalhos
        self.tabela.heading("titulo", text="Título")
        self.tabela.heading("autor", text="Autor")
        self.tabela.heading("quantidade", text="Quantidade")

        # Largura das colunas
        self.tabela.column("titulo", width=230)
        self.tabela.column("autor", width=230)
        self.tabela.column("quantidade", width=100, anchor="center")

        self.tabela.pack(pady=10, padx=15, fill="both", expand=True)

    # Método para cadastrar livros
    def cadastrar(self):
        titulo = self.campo_titulo.get().strip()
        autor = self.campo_autor.get().strip()
        quantidade_texto = self.campo_quantidade.get().strip()

        # Validação
        if not titulo or not autor or not quantidade_texto:
            messagebox.showerror(
                "Erro",
                "Preencha todos os campos!"
            )
            return

        try:
            quantidade = int(quantidade_texto)
            livro = Livro(titulo, autor, quantidade)
        except ValueError:
            messagebox.showerror(
                "Erro",
                "Informe uma quantidade inteira maior ou igual a zero!"
            )
            return

        # Armazenando o objeto na lista
        self.livros.append(livro)

        # Inserindo os dados na Treeview
        self.tabela.insert(
            "",
            tk.END,
            values=(
                livro.titulo,
                livro.autor,
                livro.quantidade
            )
        )

        # Limpando os campos
        self.campo_titulo.delete(0, tk.END)
        self.campo_autor.delete(0, tk.END)
        self.campo_quantidade.delete(0, tk.END)

        messagebox.showinfo(
            "Sucesso",
            "Livro cadastrado com sucesso!"
        )


# Executando o aplicativo
if __name__ == "__main__":
    janela = tk.Tk()
    app = AppBiblioteca(janela)
    janela.mainloop()
