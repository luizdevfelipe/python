import re
import os 
import webbrowser
import tkinter as tk
import tkinter.font as tkFont
from PIL import Image, ImageTk

def abrirLink(link):
    webbrowser.open(link)

def getMarginTopAndBottom(styles):
    margin_top = 0 if styles.get('margin-top') == None else styles.get('margin-top').replace('px', '')
    margin_bottom = 0 if styles.get('margin-bottom') == None else styles.get('margin-bottom').replace('px', '')
    return margin_top, margin_bottom


def getDefaultsMargins(default_styles, tagName):
    bottom = top = left = right = 0
    if 'margin-top' in default_styles[tagName]:
        top = default_styles[tagName]['margin-top'].replace('px', '')
    if 'margin-bottom' in default_styles[tagName]:
        bottom = default_styles[tagName]['margin-bottom'].replace('px', '')

    if 'margin' in default_styles[tagName]:
        top = default_styles[tagName]['margin'].replace('px', '')
        bottom = default_styles[tagName]['margin'].replace('px', '')
        left = default_styles[tagName]['margin'].replace('px', '')
        right = default_styles[tagName]['margin'].replace('px', '')
    return top, bottom, left, right


def handleAndReturnMargins(tagName, styles, default_styles, prev_margin_bottom):
    margin_top = margin_bottom = margin_left = margin_right = 0

    if default_styles != None:
        margin_top, margin_bottom, margin_left, margin_right = getDefaultsMargins(default_styles, tagName)

    mt, mb = getMarginTopAndBottom(styles)

    margin_top = margin_top if mt == 0 else mt
    margin_bottom = margin_bottom if mb == 0 else mb

    margin_top = 0 if margin_top == None else int(margin_top)
    margin_bottom = 0 if margin_bottom == None else int(margin_bottom)
    margin_left = 0 if margin_left == None else int(margin_left)
    margin_right = 0 if margin_right == None else int(margin_right)

    if prev_margin_bottom != 0 and margin_top != 0:
        margin_top = abs(margin_top - prev_margin_bottom)

    return margin_top, margin_bottom, margin_left, margin_right

script_dir = os.path.dirname(os.path.abspath(__file__))

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
        <div style="background-color: #bebebe; width: 200px; height: 60px; color: red;"> Texto em DIV! </div>
    </body>
</html>
"""

linhas = re.split('\n', pagina)
nivel = 0
after_inline_tag_content = None

useless = ['html', 'head', 'meta', 'title']
autocontidas = ['meta', 'img', 'br', 'hr', 'input', 'link']
draw_text = ['h1', 'p']

default_styles = {
    "body": {"margin": "8px"},
    "h1": {"color": "black", "font-size": "24px", "font-weight": "bold", "margin-top": "16px", "margin-bottom": "16px", "font-weight": "bold"},
    "p": {"color": "black", "font-size": "12px", "margin-top": "16px", "margin-bottom": "16px"},
}

# Criar janela principal
janela = tk.Tk()
title = re.findall(r'<title>([\w ]+)<\/title>', pagina)
janela.title(title[0])
janela.geometry("1280x720")

# Criar a área de desenho SE TIVER UM BACKGROUND-COLOR NO BODY DEVE SER APLICADO AQUI
canvas = tk.Canvas(janela, width=1280, height=720, bg="#ffffff")
canvas.pack()

# CASO BODY TENHA PADDING OU MARGIN DEVE SER SOMADO AQUI JÁ
x = 0
y = 0
prev_margin_bottom = 0

for i, linha in enumerate(linhas):
    # Encontra todas as tags na linha
    tags = re.findall(r'(<\/?[a-z1-6]+)', linha)
    # Somente processa se encontrar tags
    if len(tags) > 0:
        # Para cada tag encontrada
        for tag in tags:
            tipo = "undefined"
            # Formata a tag para ter somente o nome
            tagName = tag.replace('<', '').replace('/', '')

            if tagName in useless:
                continue
            # Verifica se é de fechamento
            elif re.match(r'<\/[a-z1-6]+', tag):
                nivel -= 1
                estado = 'fechamento'
                if tagName == 'a':
                    tipo = 'close_link'
            # Verifica se é autocontida
            elif tagName in autocontidas:
                estado = 'autocontida'
                if tagName == 'img':
                    tipo = "img"
            # Verifica se é de abertura
            elif re.match(r'<[a-z1-6]+', tag):
                estado = 'abertura'
                if tagName in draw_text:
                    tipo = "text"
                elif tagName == "body":
                    tipo = "body"
                elif tagName == "a":
                    tipo = "open_link"

            # Extrai atributos e styles misturados
            conteudoTag = re.findall(rf'{tag}([^>]*)>', linha)
            # Se possuir conteúdo, irá extraí-los
            if len(conteudoTag) > 0:
                conteudoTag = conteudoTag[0]
                atributos_regex = re.findall(r'([a-z]+)=["\']([^"\']+)["\']', conteudoTag)
                styles_regex = re.findall(r'([\w-]+:\s*[^;]+;)', conteudoTag)
                # Para cada estilo encontrado, separa por chave e valor atribuindo a um dicionário
                styles = {}
                for item in styles_regex:
                    key, value = item.split(':')
                    key = key.strip()
                    value = value.strip().strip(';')
                    styles[key] = value
                atributos = {}
                for item in atributos_regex:
                    atributos[item[0]] = item[1]
            else:
                atributos = []
                styles = {}

            
            innerHTML = ""
            if estado == 'abertura':
                # Tenta pegar conteúdo na mesma linha
                conteudo = re.findall(rf'<{tagName}[^>]*>(.*?)<\/{tagName}>', linha, flags=re.S)
                if conteudo:
                    innerHTML = re.sub(r'\s+', ' ', conteudo[0].strip())
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

                if tipo == "text" and re.search(r'<a', innerHTML):
                    match = re.match(r'(.*?)<a .*?</a>(.*)', innerHTML)
                    print(match)
                    innerHTML = match.group(1)
                    after_inline_tag_content = match.group(2)

            if tipo == "text":                
                color = styles.get('color', 'black')
                font = styles.get('font-family', 'Times New Roman')
                size = styles.get('font-size')
                font_weight = styles.get('font-weight')

                margin_top, margin_bottom, m_le, m_ri = handleAndReturnMargins(tagName, styles, default_styles, prev_margin_bottom)
                prev_margin_bottom = margin_bottom

                # Incrementa o margin em Y
                if margin_top > 0:
                    y = y + margin_top

                # Faz a validação do font-size, inclusive definindo um padrão quando nulo
                if size == None and 'size' in default_styles[tagName]:
                    size = default_styles[tagName]['font-size']
                elif size == None:
                    size = "12px"
                size = size.replace('px', '')
                size = int(size)

                if color == None and 'color' in default_styles[tagName]:
                    color = default_styles[tagName]['color']

                if font_weight == None and 'font-weight' in default_styles[tagName]:
                    font_weight = default_styles[tagName]['font-weight']
                if font_weight == None:
                    font_weight = "normal"

                canvas.create_text(
                    x, y,
                    text=innerHTML,
                    fill=color,
                    font=(font, size, font_weight),
                    anchor="nw"
                )
                
                # Caso tenha uma inline tag, incrementa o x para continuar na mesma linha
                if after_inline_tag_content != None:
                    fonte = tkFont.Font(family=font, size=size, weight=font_weight)
                    largura = fonte.measure(innerHTML)
                    x = x + largura
                else:
                    y = y + size + margin_bottom

            elif tipo == "img":
                margin_top, margin_bottom, mb_le, mb_ri = handleAndReturnMargins(tagName, styles, None, prev_margin_bottom)
                prev_margin_bottom = margin_bottom

                if margin_top > 0:
                    y = y + margin_top

                caminho_imagem = os.path.join(script_dir, atributos["src"])
                imagem_original = Image.open(caminho_imagem)
                largura, altura = imagem_original.size
                imagem_tk = ImageTk.PhotoImage(imagem_original)
                canvas.create_image(x, y, image=imagem_tk, anchor="nw")
                canvas.imagem_tk = imagem_tk
                y = y + altura + margin_bottom

            elif tipo == 'open_link':
                color = styles.get('color', 'blue')
                font = styles.get('font-family', 'Times New Roman')
                size = styles.get('font-size', 12)
                font_weight = styles.get('font-weight', 'underline')
                link = atributos['href']

                texto_id = canvas.create_text(
                    x, y,
                    text=innerHTML,
                    fill=color,
                    font=(font, size, font_weight),
                    anchor="nw"
                )
                canvas.tag_bind(texto_id, "<Button-1>", lambda event: abrirLink(link))
                fonte = tkFont.Font(family=font, size=size, weight='normal')
                largura = fonte.measure(innerHTML)
                x = x + largura

            elif tipo == "close_link":
                color = styles.get('color', 'black')
                font = styles.get('font-family', 'Times New Roman')
                size = styles.get('font-size', 12)
                font_weight = styles.get('font-weight', 'normal')

                canvas.create_text(
                    x, y,
                    text=after_inline_tag_content,
                    fill=color,
                    font=(font, size, font_weight),
                    anchor="nw"
                )
                fonte = tkFont.Font(family=font, size=size, weight='normal')
                largura = fonte.measure(innerHTML)
                x = x + largura
                after_inline_tag_content = None

            elif tipo == "body":
                margin_top, margin_bottom, margin_left, margin_right = handleAndReturnMargins(tagName, styles, default_styles, prev_margin_bottom)
                prev_margin_bottom = margin_bottom
                if margin_top > 0:
                    y = y + margin_top
                x = x + margin_left

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