import re

pagina = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <h1 style="color: #ff0000; font-size: 24px;">Olá, Mundo!</h1>
    <p>Este é um parágrafo de exemplo.<br></p>
    <img src="imagem.jpg" alt="Imagem de exemplo">
    <a href='https://www.example.com'>Link para Example.com sdkhjdfhkjfdshjsdfhjksdfhjksfdjkhsfkdhjdfkhjsdfkhjshjdfhjfdshdf</a>
</body>
</html>"""

tokens = re.split('\n', pagina)

# Nível | Tag | Atributos (lista) | Styles (lista) | innerHTML (resumo).
for token in tokens:
    nivel = len(re.findall(r'   ', token))
    tag = re.findall(r'<([a-z1-6]+)|</([a-z1-6]+)>', token)
    atributos = re.findall(r'(\w+)="([^"]+)"', token)
    styles = re.findall(r'style="([^"]+)"', token)
    innerHTML = re.findall(r'>(.+)<\/[a-z1-6]+>', token)[0][0:20] + '...' if re.findall(r'>(.+)<\/[a-z1-6]+>', token) else None
    
    print(
        "Nível:", nivel, " | ",
        "Tag:", tag, " | ",
        "Atributos:", atributos, " | ",
        "Styles:", styles, " | ",
        "innerHTML:", innerHTML
    )