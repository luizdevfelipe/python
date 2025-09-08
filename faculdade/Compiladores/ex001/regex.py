import re

codigo_fonte = """
var x = 3;
var y = 5;
var z = x + y;
let nome = "João";
document.write(z);
"""

palavras_reservadas = ["var", "let", "const", "function", "return", "document", "write"]
separadores = [";", "(", ")", "{", "}", ","]

tokens = re.findall(r"[A-Za-z_][\wÁ-ý]*|\d+|\"[\wÁ-ý]*\"|[=+\-*\/;()]|\.", codigo_fonte)

for token in tokens:
    if token in palavras_reservadas:
        print(token, "<-- Palavra Reservada")
    elif re.match(r"^\d+$", token):
        print(token, "<-- Literal Numérico")
    elif re.match(r"^[=+\-*/]$", token):
        print(token, "<-- Operador")
    elif token in separadores:
        print(token, "<-- Separador")
    elif re.match(r"\"[\wÁ-ý]*\"", token):
        print(token, "<-- Literal String")
    elif re.match(r"^[A-Za-z_]\w*$", token):
        print(token, "<-- Identificador")
    elif token == ".":
        print(token, "<-- Operador de Acesso")
    else:
        print(token, "<-- Desconhecido")
