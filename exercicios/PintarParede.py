print('<<<< Calculadora de Tinta v1.0 >>>>')
lar = float(input('Digite a largura da parede em metros '))
alt = float(input('Digite a altura da parede em metros '))
area = lar*alt
print('Sua parede tem a dimensão de {}x{} e sua área é de {}m².'.format(lar, alt, area))
print('Para pintar essa parede, você precida de {}l de tinta.'.format(area/2))
