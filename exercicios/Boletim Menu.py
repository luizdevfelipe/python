boletim = []
while True:
    nome = str(input('Nome: ')).strip()
    not1 = float(input('1ª Nota: '))
    not2 = float(input('2ª Nota: '))
    med = (not1 + not2) / 2
    boletim.append([nome, [not1, not2], med])
    quer = str(input('Quer Continuar? [S/N] ')).strip()
    if quer in 'Nn':
        break
print('='*30)
print(f'{"BOLETIM":^30}')
print('='*30)
print(f'{"No.":<8}', f'{"Nome":^8}', f'{"Média":>8}')
print('-'*30)
for pos, alu in enumerate(boletim):
    print(f'{pos:<8}{alu[0]:^8}{alu[2]:>8}')
while True:
    print('-='*15)
    opc = int(input('Mostrar as notas do aluno: [999 STOP] '))
    if opc == 999:
        print('FINALIZANDO...')
        break
    if opc <= len(boletim) - 1:
        print(f'Notas de {boletim[opc][0]} são {boletim[opc][1]}')
print('<<<< Volte Sempre >>>>')
