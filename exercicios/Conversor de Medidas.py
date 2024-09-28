print('<<<< Conversor de Medidas v1.0 >>>>')
nu = float(input('Escreva um valor em Metros '))
km = nu / 1000
hm = nu / 100
dam = nu / 10
dm = nu * 10
cm = nu * 100
mm = nu * 1000
print('Os Valores são  Km {} Hm {} Dam {} Dm {:.0f} Cm {:.0f} MM {:.0f} '.format(km, hm, dam, dm, cm, mm))
