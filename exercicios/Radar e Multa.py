vel = int(input('Digite sua velocidade: '))
if vel <= 80:
    print('Você passou dentro do limete permitido')
else:
    print('Você foi multado e pagará R${:.2f}'.format((vel - 80) * 7))
