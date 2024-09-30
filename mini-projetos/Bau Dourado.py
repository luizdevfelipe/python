from keyboard import press
from pyautogui import click, hotkey, doubleClick
from time import sleep

"""
Programa para abrir baús no jogo Mr.Mine
"""

def clicar(x=0, y=0):
    click(x, y)
    sleep(0.5)


while True:
    tipo = int(input('\nQual baú quer abrir? Normal[0] Dourado[1] Mapa[2] '))
    baus = int(input('Quantos baús quer abrir? '))

    hotkey('alt', 'tab')

    if tipo == 0:
        for c in range(0, baus):
            clicar(392, 806)
            clicar(882, 564)
            doubleClick(1291, 564)

    elif tipo == 1:
        for c in range(0, baus):
            clicar(1493, 636)
            clicar(1010, 139)
            clicar(1533, 602)
            clicar(1530, 602)
            click()

    elif tipo == 2:
        for c in range(0, baus):
            press('space')
            clicar(1174, 597)
            click()
            click()
            click()
    continuar = str(input('Quer abrir outro tipo de baú? [S/N] '))
    if continuar.lower() == 'n':
        break
