# Como saber a posição do ponteiro do mouse na tela.
import pyautogui

pyautogui.alert("[Atenção] Posicione o mouse aonde deseja saber a posição dele na tela, em seguida pressione o "
                "'Enter''!")

x, y = pyautogui.position()
print("Posição atual do mouse:")
print("x = "+str(x)+" y = "+str(y))
