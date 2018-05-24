import os
import time
import interface

def simples():
  os.system('cls')
  print('FAZER LOGICA JUROS SIMPLES')
  time.sleep(2)
  return 0

def composto():
  os.system('cls')
  print('FAZER LOGICA JUROS COMPOSTO')
  time.sleep(2)
  return 0

def juros():
  jurosMenu = interface.Interface()
  jurosMenu.setOptions([
    ('1 - Simples', 'Calcular juros simples', 1),
    ('2 - Composto', 'Calcular juros composto', 2),
    ('0 - Voltar', 'voltar', 0)
  ])
  jurosMenu.setTitle('JUROS')

  while 1:
    selected = jurosMenu.getInputOption()
    # Voltar para main menu
    if (selected == 0):
      break
    elif (selected == 1):
      simples()
    elif (selected == 2):
      composto()
