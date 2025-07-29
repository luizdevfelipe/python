import pyautogui
import time

def enviar_string_vezes(texto: str, vezes: int, delay: float = 0.5):
    """
    Digita uma string e aperta Enter, repetindo isso 'vezes' vezes.
    
    :param texto: Texto a ser digitado.
    :param vezes: Quantas vezes digitar e enviar.
    :param delay: Tempo entre cada envio (em segundos).
    """
    print("Você tem 5 segundos para focar no campo de entrada...")
    time.sleep(5)

    for _ in range(vezes):
        pyautogui.write(texto)
        pyautogui.press('enter')
        time.sleep(delay)
