import re
import tkinter as tk

pagina = """
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Minha Página</title>
    </head>
    <body>
        <h1 id="titulo" style="color: black; font-size: 24px;">Olá, Mundo!</h1>
        <p id="paragrafo">
            Este é um parágrafo de exemplo.  
        </p>
        <img src="exemple.jpg" alt="Imagem de exemplo">
        <p>Outro parágrafo com <a href="https://www.google.com">um link</a> embutido.</p>
    </body>
</html>
"""

linhas = re.split('\n', pagina)
nivel = 0

useless = ['html', 'head', 'meta', 'title', 'body']
autocontidas = ['meta', 'img', 'br', 'hr', 'input', 'link']

draw_text = ['h1', 'p']
tipo = "undefined"

# Criar janela principal
janela = tk.Tk()
title = re.findall(r'<title>([\w ]+)<\/title>', pagina)
janela.title(title[0])
janela.geometry("1280x720")

# Criar a área de desenho SE TIVER UM BACKGROUND-COLOR NO BODY DEVE SER APLICADO AQUI
canvas = tk.Canvas(janela, width=1280, height=720, bg="#e0cece")
canvas.pack()

# CASO BODY TENHA PADDING OU MARGIN DEVE SER SOMADO AQUI JÁ
x = 0
y = 0

for i, linha in enumerate(linhas):
    # Encontra todas as tags na linha
    tags = re.findall(r'(<\/?[a-z1-6]+)', linha)

    # Somente processa se encontrar tags
    if len(tags) > 0:
        # Para cada tag encontrada
        for tag in tags:
            # Formata a tag para ter somente o nome
            tagName = tag.replace('<', '').replace('/', '')

            if tagName in useless:
                continue
            # Verifica se é de fechamento
            elif re.match(r'<\/[a-z1-6]+', tag):
                nivel -= 1
                estado = 'fechamento'
            # Verifica se é autocontida
            elif tagName in autocontidas:
                estado = 'autocontida'
            # Verifica se é de abertura
            elif re.match(r'<[a-z1-6]+', tag):
                estado = 'abertura'
                if tagName in draw_text:
                    tipo = "text"

            # Extrai atributos e styles misturados
            conteudoTag = re.findall(rf'{tag}([^>]*)>', linha)
            # Se possuir conteúdo, irá extraí-los
            if len(conteudoTag) > 0:
                conteudoTag = conteudoTag[0]
                atributos = re.findall(r'([a-z]+)=["\']([^"\']+)["\']', conteudoTag)
                styles_regex = re.findall(r'([\w-]+:\s*[^;]+;)', conteudoTag)
                # Para cada estilo encontrado, separa por chave e valor atribuindo a um dicionário
                styles = {}
                for item in styles_regex:
                    key, value = item.split(':')
                    key = key.strip()
                    value = value.strip().strip(';')
                    styles[key] = value
            else:
                atributos = []
                styles = {}

            innerHTML = ""
            if estado == 'abertura':
                # Tenta pegar conteúdo na mesma linha
                conteudo = re.findall(rf'<{tagName}[^>]*>(.*?)<\/{tagName}>', linha, flags=re.S)
                if conteudo:
                    texto = re.sub(r'\s+', ' ', conteudo[0].strip())
                else:
                    # Se não encontrar, acumula linhas seguintes até achar fechamento
                    innerHTML_acumulado = linha.split('>', 1)[-1]  # pega o que vem depois da abertura
                    j = i + 1
                    while j < len(linhas):
                        if re.search(rf'<\/{tagName}>', linhas[j]):
                            innerHTML_acumulado += ' ' + re.sub(rf'<\/{tagName}>', '', linhas[j])
                            break
                        innerHTML_acumulado += ' ' + linhas[j]
                        j += 1
                    innerHTML = re.sub(r'\s+', ' ', innerHTML_acumulado.strip())[:60]
            
            if tipo == "text":
                
                color = styles.get('color', 'black')
                font = styles.get('font-family', 'Helvetica')
                size = 24 if styles.get('font-size') == None else styles.get('font-size', 24).replace('px', '')

                canvas.create_text(
                    x, y,
                    text=innerHTML,
                    fill=color,
                    font=(font, size),  # FONTE ESTá COMO H1
                    anchor="nw"  # âncora canto superior esquerdo
                )

                y = y + 24

            # imprime
            print("Nível:", nivel)
            print("Tag:", tag)
            print("Atributos:", atributos)
            print("Styles:", styles)
            print("innerHTML:", innerHTML)
            print("=-="*30)

            # só sobe depois de imprimir a abertura
            if estado == 'abertura':
                nivel += 1

janela.mainloop()