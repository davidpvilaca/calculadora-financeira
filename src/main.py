#!/usr/bin/python3

import interface
import juros
import descontos

def main():

  ############################
  # INTERFACE VISUAL DO MAIN #
  ############################
  mainMenu = interface.Interface()
  # Opções de menu
  mainMenu.setOptions([
    ('1 - Juros - Calculadora de juros', 'juros', 1),
    ('2 - Descontos - Calculadora de descontos', 'descontos', 2),
    ('0 - Sair', 'sair', 0)
  ])
  # Título
  mainMenu.setTitle('MENU PRINCIPAL')

  # Loop infinito para escolha de opções
  # até que a opção de sair seja escolhida
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

  return 0

if __name__ == '__main__':
  main()