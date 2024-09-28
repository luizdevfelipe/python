import random
n1 = input('Primeiro Aluno: ')
n2 = input('Segundo Aluno: ')
n3 = input('Terceiro Aluno: ')
n4 = input('Quarto Aluno: ')
aluno = [n1, n2, n3, n4]
sorteado = random.choice(aluno)
print('O aluno escolhido foi {}!'.format(sorteado))

