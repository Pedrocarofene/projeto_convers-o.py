import tkinter as tk
from tkinter import filedialog, messagebox
from docx2pdf import convert

def escolher_arquivo():
    arquivo = filedialog.askopenfilename(
        title="Selecione um arquivo DOCX",
        filetypes=[("Documentos Word", "*.docx")]
    )
    if arquivo:
        try:
            convert(arquivo)  # converte para PDF
            messagebox.showinfo("Sucesso", "✅ Arquivo convertido para PDF com sucesso!")
        except Exception as e:
            messagebox.showerror("Erro", f"Ocorreu um erro: {e}")

# Criando a janela principal
janela = tk.Tk()
janela.title("Conversor DOCX → PDF")
janela.geometry("700x300")

# Texto
label = tk.Label(janela, text="Selecione um arquivo DOCX para converter:", pady=10)
label.pack()

# Botão para escolher arquivo
botao = tk.Button(janela, text="Escolher arquivo", command=escolher_arquivo)
botao.pack(pady=10)

# Rodando a interface
janela.mainloop()
