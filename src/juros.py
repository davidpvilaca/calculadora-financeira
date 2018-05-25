import os
import time
import interface

# Função a ser chamada quando a opção
# de juros simples for selecionada no
# menu de juros.
def simples():

  # Função para realizar o cálculo da fórmula de juros simples
  # retornando a variável passada como None.
  # Ex: Se j for None retornará c * i * t
  def calcular(j, c, i, t):
    if j is None:
      return c * (i if i < 0 else i/100) * t


  #####################################
  # INTERFACE VISUAL DE JUROS SIMPLES #
  #####################################
  jurosSimplesMenu = interface.Interface()
  # Opções de menu
  jurosSimplesMenu.setOptions([
    ('1 - j - Juros', 'j', 1),
    ('2 - i - Taxa', 'i', 2),
    ('3 - t - Tempo', 't', 3),
    ('4 - C - Capital inicial', 'c', 3),
    ('0 - Voltar', 'voltar', 0)
  ])
  # Título
  jurosSimplesMenu.setTitle('JUROS SIMPLES\n\n\tO que se deseja obter?')

  # Obter valores do usuário
  while 1:
    selected = jurosSimplesMenu.getInputOption()

    # Voltar
    if (selected == 0):
      break

    # Usuário deseja obter J
    elif (selected == 1):
      c = jurosSimplesMenu.getInputNumber('(Capital inicial R$) C')
      i = jurosSimplesMenu.getInputNumber('(Taxa %) i')
      t = jurosSimplesMenu.getInputNumber('(Tempo) t')
      print('\n\tC={0:.{1}f}'.format(c, 0 if int(c) == float(c) else 2))
      print('\ti={0:.{1}f}%'.format(i if i >= 1 else i*100, 0 if int(i) == float(i) else 2))
      print('\tt={0:.{1}f}\n'.format(t, 0 if int(t) == float(t) else 2))
      result = calcular(None, c, i, t)
      print('\tJ = R${0:.{1}f}'.format(result, 2))
      print('\tM = R${0:.{1}f}\n'.format(result+c, 2))
      os.system('pause')

    # Usuário deseja obter i
    elif (selected == 2):
      os.system('pause')

    # Usuário deseja obter t
    elif (selected == 3):
      os.system('pause')

# fim da função simples



# Função a ser chamada quando a opção
# de juros composto for selecionada no
# menu de juros.
def composto():
  os.system('cls')
  print('FAZER LOGICA JUROS COMPOSTO')
  time.sleep(2)
  return 0
# fim da função composto


# Função a ser chamada quando a opção
# de juros for selecionada no menu principal.
def juros():

  #############################
  # INTERFACE VISUAL DE JUROS #
  #############################
  jurosMenu = interface.Interface()
  # Opções de menu
  jurosMenu.setOptions([
    ('1 - Simples - Calcular juros simples', 'simples', 1),
    ('2 - Composto - Calcular juros composto', 'composto', 2),
    ('0 - Voltar', 'voltar', 0)
  ])
  # Título
  jurosMenu.setTitle('JUROS')

  # Loop infinito para escolha de opções
  # até que a opção de voltar seja escolhida
  while 1:
    selected = jurosMenu.getInputOption()
    # Voltar para main menu
    if (selected == 0):
      break
    elif (selected == 1):
      simples()
    elif (selected == 2):
      composto()
