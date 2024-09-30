valor = 1000000
f = 1

while(valor >= 1):
    print(valor, 'x ' if valor > 1 else '=-> ', end='')
    f *= valor
    valor -= 1
print('Abra o documento de texto para ver o resultado!')
with open('fatorial.txt', 'w') as arquivo:
    arquivo.write(str(f))
