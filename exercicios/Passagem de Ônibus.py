nu = int(input('Digite a quilometragem: '))
if nu <= 200:
    print('Sua viagem é curta, você pagará ao todo R${:.2f}, são R$0,50 por quilômetro.'.format(0.5 * nu))
else:
    print('Sua viagem é longa ao todo você pagará R${:.2f}, são R$0,45 por quilômetro.'.format(nu * 0.45))
print('Tenha uma boa Viagem! :)')
