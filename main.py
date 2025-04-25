import pyodbc
import tkinter as tk
from tkinter import messagebox

# Conexão com o banco de dados
conexao = pyodbc.connect(
    r'DRIVER={ODBC Driver 17 for SQL Server};'
    r'SERVER=localhost\SQLEXPRESS;'
    r'DATABASE=TesteCRUD;'
    r'Trusted_Connection=yes;'
)

cursor = conexao.cursor()

# Funções CRUD

def criar_pessoa():
    nome = entry_nome.get()
    idade = entry_idade.get()

    if nome and idade:
        cursor.execute("INSERT INTO Pessoas (Nome, Idade) VALUES (?, ?)", (nome, int(idade)))
        conexao.commit()
        messagebox.showinfo("Sucesso", "Pessoa adicionada com sucesso.")
    else:
        messagebox.showwarning("Erro", "Por favor, preencha todos os campos.")

def listar_pessoas():
    cursor.execute("SELECT * FROM Pessoas")
    listbox.delete(0, tk.END)  # Limpa a listbox antes de adicionar novos dados
    for row in cursor.fetchall():
        listbox.insert(tk.END, f"ID: {row.Id}, Nome: {row.Nome}, Idade: {row.Idade}")

def atualizar_pessoa():
    id = entry_id.get()
    nome = entry_nome.get()
    idade = entry_idade.get()

    if id and nome and idade:
        cursor.execute("UPDATE Pessoas SET Nome = ?, Idade = ? WHERE Id = ?", (nome, int(idade), int(id)))
        conexao.commit()
        messagebox.showinfo("Sucesso", "Pessoa atualizada com sucesso.")
    else:
        messagebox.showwarning("Erro", "Por favor, preencha todos os campos.")

def deletar_pessoa():
    id = entry_id.get()

    if id:
        cursor.execute("DELETE FROM Pessoas WHERE Id = ?", (int(id),))
        conexao.commit()
        messagebox.showinfo("Sucesso", "Pessoa deletada com sucesso.")
    else:
        messagebox.showwarning("Erro", "Por favor, preencha o ID da pessoa.")

# Criando a interface gráfica

root = tk.Tk()
root.title("Sistema CRUD - Pessoas")

# Labels e Entradas
tk.Label(root, text="ID").grid(row=0, column=0)
entry_id = tk.Entry(root)
entry_id.grid(row=0, column=1)

tk.Label(root, text="Nome").grid(row=1, column=0)
entry_nome = tk.Entry(root)
entry_nome.grid(row=1, column=1)

tk.Label(root, text="Idade").grid(row=2, column=0)
entry_idade = tk.Entry(root)
entry_idade.grid(row=2, column=1)

# Botões
tk.Button(root, text="Adicionar", command=criar_pessoa).grid(row=3, column=0)
tk.Button(root, text="Listar", command=listar_pessoas).grid(row=3, column=1)
tk.Button(root, text="Atualizar", command=atualizar_pessoa).grid(row=4, column=0)
tk.Button(root, text="Deletar", command=deletar_pessoa).grid(row=4, column=1)

# Listbox para exibir as pessoas
listbox = tk.Listbox(root, width=50, height=10)
listbox.grid(row=5, column=0, columnspan=2)

# Rodando a interface
root.mainloop()
