from random import shuffle
n1 = str(input('Primeiro Aluno: '))
n2 = str(input('Segundo Aluno '))
n3 = str(input('Terciero Aluno: '))
n4 = str(input('Quarto Aluno: '))
alunos = [n1, n2, n3, n4]
shuffle(alunos)
print('A ordem de apresentação será')
print('{}'.format(alunos))
