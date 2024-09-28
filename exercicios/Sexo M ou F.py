sexo = str(input('Informe seu sexo: [M/F] ')).strip().upper()[0]
while sexo not in 'MF':
    sexo = str(input('Dado inválido informe novamente seu sexo: ')).strip().upper()[0]
print('Sexo {} registrado.'.format(sexo))
