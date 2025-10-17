import tkinter as tk
from PIL import Image, ImageTk  # Necessário para carregar a imagem
import os # Necessário para manipulação de caminhos para carregar a imagem

# Criar janela principal
janela = tk.Tk()
janela.title("Desenhos com Tkinter")
janela.geometry("800x600")

# Criar a área de desenho
canvas = tk.Canvas(janela, width=800, height=600, bg="#e0cece")
canvas.pack()

# Desenha formas geométricas
canvas.create_rectangle(50, 50, 150, 150, fill="blue", outline="black", width=2)
canvas.create_rectangle(200, 50, 350, 130, fill="green", outline="red", width=2)
canvas.create_oval(150, 250, 200, 300, fill="yellow", outline="orange", width=2)

# Texto roxo em fonte grande
canvas.create_text(
    50, 350,
    text="Texto em roxo",
    fill="purple",
    font=("Helvetica", 24),  # Fonte grande
    anchor="nw"  # âncora canto superior esquerdo
)

# Obter o diretório do script atual
script_dir = os.path.dirname(os.path.abspath(__file__))
caminho_imagem = os.path.join(script_dir, "exemple.jpg")

# Carregar imagem externa
imagem_original = Image.open(caminho_imagem)
imagem_tk = ImageTk.PhotoImage(imagem_original)

# Exibir a imagem
canvas.create_image(400, 200, image=imagem_tk, anchor="nw")

# Manter referência da imagem para não ser coletada pelo GC
canvas.imagem_tk = imagem_tk

janela.mainloop()
