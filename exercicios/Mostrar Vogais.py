palavras = ('Processador', 'Memoria', 'Mouse', 'Teclado', 'Fone',
            'Notebook')
for p in palavras:
    print(f'\nNa palavra {p.upper()} temos ', end='')
    for letras in p:
        if letras.lower() in 'aeiou':
            print(f'{letras}', end=' ')
