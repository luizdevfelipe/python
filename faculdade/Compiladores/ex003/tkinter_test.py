import tkinter as tk

# Criar janela principal
janela = tk.Tk()
janela.title("Desenhos com Tkinter")
janela.geometry("800x600")

# Criar a área de desenho
canvas = tk.Canvas(janela, width=800, height=600, bg="#e0cece")
canvas.pack()

# Desenha um Quadrado azul (x1, y1, x2, y2)
canvas.create_rectangle(50, 50, 150, 150, fill="blue", outline="black", width=2)
janela.mainloop()