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
        <p id="paragrafo">
            Este é um parágrafo de exemplo.  
            <img src="imagem.jpg" alt="Imagem de exemplo">
        </p>
        <p>Outro parágrafo com <a href="https://www.google.com" >um link</a> embutido.</p>
        <a href='https://www.example.com'>Link para Example.com</a>
    </body>
</html>
"""

linhas = re.split('\n', pagina)
nivel = 0

autocontidas = ['meta', 'img', 'br', 'hr', 'input', 'link']

for i, linha in enumerate(linhas):
    # Encontra todas as tags na linha
    tags = re.findall(r'(<\/?[a-z1-6]+)', linha)

    # Somente processa se encontrar tags
    if len(tags) > 0:
        # Para cada tag encontrada
        for tag in tags:
            # Formata a tag para ter somente o nome
            testTag = tag.replace('<', '').replace('/', '')

            # Verifica se é de fechamento
            if re.match(r'<\/[a-z1-6]+', tag):
                nivel -= 1
                estado = 'fechamento'
            # Verifica se é autocontida
            elif testTag in autocontidas:
                estado = 'autocontida'
            # Verifica se é de abertura
            elif re.match(r'<[a-z1-6]+', tag):
                estado = 'abertura'

            # Extrai atributos e styles misturados
            conteudoTag = re.findall(rf'{tag}([^>]*)>', linha)
            # Se possuir conteúdo, irá extraí-los
            if len(conteudoTag) > 0:
                conteudoTag = conteudoTag[0]
                atributos = re.findall(r'([a-z]+)=["\']([^"\']+)["\']', conteudoTag)
                styles = re.findall(r'([\w-]+:\s*[^;]+;)', conteudoTag)
                # Para cada estilo encontrado, separa por chave e valor atribuindo a um dicionário
                styles = {k.strip(): v.strip(';') for k, v in (s.split(':') for s in styles)}
            else:
                atributos = []
                styles = {}

            innerHTML = ""
            if estado == 'abertura':
                # Tenta pegar conteúdo na mesma linha
                conteudo = re.findall(rf'<{testTag}[^>]*>(.*?)<\/{testTag}>', linha, flags=re.S)
                if conteudo:
                    texto = re.sub(r'\s+', ' ', conteudo[0].strip())
                    innerHTML = texto[:60]  # resumo até 60 chars
                else:
                    # Se não encontrar, acumula linhas seguintes até achar fechamento
                    innerHTML_acumulado = linha.split('>', 1)[-1]  # pega o que vem depois da abertura
                    j = i + 1
                    while j < len(linhas):
                        if re.search(rf'<\/{testTag}>', linhas[j]):
                            innerHTML_acumulado += ' ' + re.sub(rf'<\/{testTag}>', '', linhas[j])
                            break
                        innerHTML_acumulado += ' ' + linhas[j]
                        j += 1
                    innerHTML = re.sub(r'\s+', ' ', innerHTML_acumulado.strip())[:60]

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
