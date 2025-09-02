import tkinter as tk
from tkinter import filedialog, messagebox
from docx2pdf import convert

def escolher_arquivo():
    arquivo = filedialog.askopenfilename(
        title="Selecione um arquivo DOCX",
        filetypes=[("Documentos word", "*docx")]
    )
    if arquivo:
        try:
            convert(arquivo)
            messagebox.showinfo("Sucesso","✅ Arquivo convertido com sucesso!")
        except Exception as e:
            messagebox.showerror("ERRO!!", f"Ocorreu um erro: {e}!")

janela=tk.Tk()
janela.title("Conversor DOCX para PDF")
janela.geometry("700x400")

#texto
label = tk.Label(janela, text="Selecione um arquivo DOCX para converter:", pady=40)
label.pack()

#botao para escolher o arquivo
botao = tk.Button(janela, text="Escolher arquivo",command=escolher_arquivo)
botao.pack(pady=10)

#interface

janela.mainloop()

