#!/usr/bin/python3

import os
import interface
import juros
import descontos

def main():

  mainMenu = interface.Interface()
  mainMenu.setOptions([
    ('1 - Juros - Calculadora de juros', 'juros', 1),
    ('2 - Descontos - Calculadora de descontos', 'descontos', 2),
    ('0 - Sair', 'sair', 0)
  ])
  mainMenu.setTitle('MENU PRINCIPAL')

  while 1:
    selected = mainMenu.getInputOption()
    # Sair
    if (selected == 0):
      break
    # Juros
    if (selected == 1):
      juros.juros()
    # Descontos
    if (selected == 2):
      descontos.descontos()

  os.system('pause')
  return 0

if __name__ == '__main__':
  main()