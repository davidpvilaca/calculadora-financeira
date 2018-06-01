import os
import interface
import math

# Função a ser chamada quando a opção
# de juros simples for selecionada no
# menu de juros.
def simples():

  # Função para realizar o cálculo da fórmula de juros simples
  # retornando a variável passada como None.
  # Ex: Se j for None retornará c * i * t
  def calcular(j, c, i, t):
    if j is None:
      return c * i * t
    elif c is None:
      return j / (i * t)
    elif i is None:
      return  j / ( c * t )
    elif t is None:
      return j / ( c * i )
  
  # Função para obter as variáveis da fórmula
  # através de uma entrada do usuário
  def getVariables(j, c, i, t):
    _j, _c, _i , _t = None, None, None, None
    if (j):
      _j = jurosSimplesMenu.getInputNumber('(Juros) j')
    if (c):
      _c = jurosSimplesMenu.getInputNumber('(Capital inicial R$) C')
    if (i):
      _i = jurosSimplesMenu.getInputNumber('(Taxa %) i')
      _i = _i/100
    if (t):
      _t = jurosSimplesMenu.getInputNumber('(Tempo) t')
    return _j, _c, _i , _t
  
  # Função para exibir na tela as variáveis depois
  # dos cálculos
  def printVariables(j, c, i, t):
    print('\n\tC = R${0:.{1}f}'.format(c, 2))
    print('\ti = {0:.{1}f}%'.format(i*100, 0 if int(i*100) == i*100 else 2))
    print('\tt = {0:.{1}f}'.format(t, 0 if int(t) == float(t) else 2))
    print('\tJ = R${0:.{1}f}'.format(j, 2))
    print('\tM = R${0:.{1}f}\n'.format(j+c, 2))
    os.system('pause')


  #####################################
  # INTERFACE VISUAL DE JUROS SIMPLES #
  #####################################
  jurosSimplesMenu = interface.Interface()
  # Opções de menu
  jurosSimplesMenu.setOptions([
    ('1 - j - Juros', 'j', 1),
    ('2 - i - Taxa', 'i', 2),
    ('3 - t - Tempo', 't', 3),
    ('4 - C - Capital inicial', 'c', 4),
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
      j, c, i, t = getVariables(False, True, True, True)
      j = calcular(j, c, i, t)
      printVariables(j, c, i, t)

    # Usuário deseja obter i
    elif (selected == 2):
      j, c, i, t = getVariables(True, True, False, True)
      i = calcular(j, c, i, t)
      printVariables(j, c, i, t)

    # Usuário deseja obter t
    elif (selected == 3):
      j, c, i, t = getVariables(True, True, True, False)
      t = calcular(j, c, i, t)
      printVariables(j, c, i, t)

    # Usuário deseja obter C
    elif (selected == 4):
      j, c, i, t = getVariables(True, False, True, True)
      c = calcular(j, c, i, t)
      printVariables(j, c, i, t)

# fim da função simples



# Função a ser chamada quando a opção
# de juros composto for selecionada no
# menu de juros.
def composto():

  # Função para exibir na tela as variáveis depois
  # dos cálculos
  def printVariables(m, c, i, t, j):
    print('\n\tM = R${0:.{1}f}'.format(m, 2))
    print('\tC = R${0:.{1}f}'.format(c, 2))
    print('\ti = {0:.{1}f}%'.format(i*100, 0 if int(i*100) == i*100 else 2))
    print('\tt = {0:.{1}f}'.format(t, 0 if int(t) == t else 2))
    print('\tJ = R${0:.{1}f}\n'.format(j, 2))
    os.system('pause')
  
  # Função para obter as variáveis da fórmula
  # através de uma entrada do usuário
  def getVariables(m, c, i, t, j):
    _m, _c, _i , _t, _j = None, None, None, None, None
    if (m):
      _m = jurosCompostosMenu.getInputNumber('(Montante R$) M')
    if (c):
      _c = jurosCompostosMenu.getInputNumber('(Capital inicial R$) C')
    if (i):
      _i = jurosCompostosMenu.getInputNumber('(Taxa %) i')
      _i = _i/100
    if (t):
      _t = jurosCompostosMenu.getInputNumber('(Tempo) t')
    if (j):
      _j = jurosCompostosMenu.getInputNumber('(Juros) J')
    return _m, _c, _i, _t, _j
  
  # Função para realizar o cálculo da fórmula de juros simples
  # retornando a variável passada como None.
  # Ex: Se m for None retornará c * (1+i)**t
  def calcular(m, c, i, t, j):
    if (m is None):
      return c * ( (1+i)**t )
    if (c is None):
      return m / ( (1+i)**t )
    if (i is None):
      return ( (m/c)**(1/t) ) - 1
    if (t is None):
      return math.log10(m/c) / math.log10(1+i)
    if (j is None):
      return m - c

  #######################################
  # INTERFACE VISUAL DE JUROS COMPOSTOS #
  #######################################
  jurosCompostosMenu = interface.Interface()
  # Opções de menu
  jurosCompostosMenu.setOptions([
    ('1 - M - Montante', 'm', 1),
    ('2 - C - Capital inicial', 'c', 2),
    ('3 - i - Taxa fixa', 'i', 3),
    ('4 - t - Período de tempo', 'i', 4),
    ('5 - J - Juros', 'j', 5),
    ('0 - Voltar', 'voltar', 0)
  ])
  # Título
  jurosCompostosMenu.setTitle('JUROS COMPOSTOS\n\n\tO que se deseja obter?')

  # Obter valores do usuário
  while 1:
    selected = jurosCompostosMenu.getInputOption()

    # Voltar
    if (selected == 0):
      break
    # Usuário deseja obter M
    elif (selected == 1):
      m, c, i, t, j = getVariables(False, True, True, True, False)
      m = calcular(m, c, i, t, j)
      j = m-c
      printVariables(m, c, i, t, j)
    # Usuário deseja obter C
    elif (selected == 2):
      m, c, i, t, j = getVariables(True, False, True, True, False)
      c = calcular(m, c, i, t, j)
      j = m-c
      printVariables(m, c, i, t, j)
    # Usuário deseja obter i
    elif (selected == 3):
      m, c, i, t, j = getVariables(True, True, False, True, False)
      i = calcular(m, c, i, t, j)
      j = m-c
      printVariables(m, c, i, t, j)
    # Usuário deseja obter t
    elif (selected == 4):
      m, c, i, t, j = getVariables(True, True, True, False, False)
      t = calcular(m, c, i, t, j)
      j = m-c
      printVariables(m, c, i, t, j)
    # Usuário deseja obter J
    elif (selected == 5):
      m, c, i, t, j = getVariables(True, True, True, True, False)
      j = calcular(m, c, i, t, j)
      printVariables(m, c, i, t, j)
    

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
