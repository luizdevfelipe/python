import re

codigo_fonte = """
var x = 3;
var y = 5;
var z = x + y;
document.write(z);
"""

linhas = codigo_fonte.split()

positions = []
for i, linha in enumerate(linhas):
    if re.search(r";$", linha):
        linhas[i] = re.sub(r";$", "", linha)
        positions.append(i+1)

for pos in reversed(positions):
    linhas.insert(pos, ";")

for linha in linhas:
    print(linha, end=" ")
    if re.search(r"^(var|let|const|document\.write\(.+\));*$", linha):
        print(" <-- Palavra Reservada")
    elif re.search(r"^[a-zA-Z_]+\w*$", linha):
        print(" <-- Identificador")
    elif re.search(r"^\d+;*$", linha):
        print(" <-- Literal Numerico")
    elif re.search(r"^[=+\-*/]$", linha):
        print(" <-- Operador")
    elif re.search(r"^;$", linha):
        print(" <-- Simbolo Separador")
    else:
        print(" <-- Desconhecido")