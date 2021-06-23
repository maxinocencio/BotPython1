import pyautogui
import time


print('-='*30)
campeao = input('Insira o nome do campeão: ')
print('-='*30)


pyautogui.press('win')
time.sleep(0.5)
pyautogui.write('opera')
time.sleep(0.5)
pyautogui.press('enter')

time.sleep(4)

pyautogui.write('https://www.leagueofgraphs.com/champions/runes/')
pyautogui.write(campeao)

time.sleep(1) 

pyautogui.press('enter')

print('')
print('^^')