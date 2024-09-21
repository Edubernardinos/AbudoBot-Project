import tkinter as tk
from tkinter import messagebox

def show_popup(message, title="Status"):
    # Cria uma janela principal oculta
    root = tk.Tk()
    root.withdraw()  # Oculta a janela principal
    # Mostra a mensagem pop-up
    messagebox.showinfo(title, message)
    root.destroy()  # Fecha a janela após a mensagem

# Exemplo de uso
if __name__ == "__main__":
    show_popup("Janela do jogo focada com sucesso.", "Sucesso")