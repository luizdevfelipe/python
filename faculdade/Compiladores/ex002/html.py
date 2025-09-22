import re

pagina = """
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Document</title>
    </head>
    <body>
        <h1 id="titulo" style="color: #ff0000; font-size: 24px;">Olá, Mundo!</h1>
        <p>Este é um parágrafo de exemplo.</p>
        <img src="imagem.jpg" alt="Imagem de exemplo">
        <a href='https://www.example.com'>Link para Example.com</a>
    </body>
</html>
"""

tokens = re.split('\n', pagina)
nivel = -1
tipo = 'abertura'
autocontidas = ['meta', 'img', 'br', 'hr', 'input', 'link']

# Nível | Tag | Atributos (lista) | Styles (lista) | innerHTML (resumo).
for i, token in enumerate(tokens):

    tag = re.findall(r'<\/?([a-z1-6]+)', token)

    if tipo == 'abertura' and len(tag) == 1 and tag[0] not in autocontidas:
        nivel = nivel + 1
        tipo = 'abertura'
    elif tipo == 'abertura' and len(tag) == 1 and tag[0] in autocontidas:
        nivel = nivel + 1
        tipo = 'fechamento'
    elif tipo == 'fechamento' and len(tag) == 1 and tag[0] not in autocontidas:
        nivel = nivel - 1
        tipo = 'abertura'
    

    atributos = re.findall(r'([a-z]+)=["\']([\w #-=;]+)["\']', token)
    styles = re.findall(r'([\w-]+: ?[#\w]+;)', token)
        
    innerHTML = re.findall(r'>(.+)<\/[a-z1-6]+>', token)
    if len(innerHTML) == 0 and i < len(tokens)-1:
        innerHTML = re.findall(r'([^\s]+)', tokens[i+1])[:3]
    
    if len(tag) > 0:
        print("Nível:", nivel)
        print("Tag:", tag)
        print("Atributos:", atributos)
        print("Styles:", styles)
        print("innerHTML:",  ' '.join(innerHTML))        
        print("=-="*30)