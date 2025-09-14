import re

pagina = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <h1>Olá, Mundo!</h1>
    <p>Este é um parágrafo de exemplo.</p>
</body>
</html>"""

# (<[a-z1-6]+>)(.+)(<\/[a-z1-6]+>)
tokens = re.split('\n', pagina)

# Nível | Tag | Atributos (lista) | Styles (lista) | innerHTML (resumo).
for token in tokens:
    print(token)
