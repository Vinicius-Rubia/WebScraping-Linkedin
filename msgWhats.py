import time
import pandas as pd
import pyautogui
import clipboard
import os

def sendMessageWhatsApp(): 
  description = pd.read_excel('DESCRICAO.xlsx')
  title = pd.read_excel('TITULO.xlsx')
  link = pd.read_excel('LINKS.xlsx')

  list_description = []
  list_links = []

  for lin in link[0]:
    list_links.append(lin)

  for desc in description[0]:
    list_description.append(desc)

  pyautogui.press('winleft')
  time.sleep(1)
  pyautogui.write('Chrome')
  time.sleep(1)
  pyautogui.press('enter')
  time.sleep(2)
  pyautogui.write('https://web.whatsapp.com/')
  time.sleep(1)
  pyautogui.press('enter')
  time.sleep(10)
  pyautogui.hotkey('ctrl', 'alt', 'n')
  time.sleep(1)
  pyautogui.write('TESTES')
  time.sleep(1)
  pyautogui.press('enter')
  time.sleep(1)

  for titulo in title[0]:
    pyautogui.write(titulo)
    time.sleep(1)
    pyautogui.hotkey('ctrl', 'enter')
    pyautogui.hotkey('ctrl', 'enter')
    clipboard.copy(f'LINK DA VAGA: {list_links[0]}')
    pyautogui.hotkey('ctrl', 'v')
    time.sleep(1)
    pyautogui.hotkey('ctrl', 'enter')
    pyautogui.hotkey('ctrl', 'enter')
    clipboard.copy(list_description[0])
    time.sleep(1)
    pyautogui.hotkey('ctrl', 'v')
    time.sleep(2)
    pyautogui.press('enter')
    time.sleep(3)
    del list_description[0]
    del list_links[0]
  
  os.remove('DESCRICAO.xlsx')
  os.remove('TITULO.xlsx')
  os.remove('LINKS.xlsx')
  pyautogui.hotkey('ctrl', 'w')