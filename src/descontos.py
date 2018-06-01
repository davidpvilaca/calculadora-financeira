import interface
import os

def racional():

  # Função para exibir na tela as variáveis depois
  # dos cálculos
  def printVariables(d, n, i, t):
    print('\n\tDr = R${0:.{1}f}'.format(d, 2))
    print('\tn = R${0:.{1}f}'.format(n, 2))
    print('\ti = {0:.{1}f}%'.format(i, 0 if int(i) == i else 2))
    print('\tt = {0:.{1}f}\n'.format(t, 0 if int(t) == t else 2))
    os.system('pause')
  
  # Função para obter as variáveis da fórmula
  # através de uma entrada do usuário
  def getVariables(d, n, i, t):
    _d, _n, _i, _t = None, None, None, None
    if (d):
      _d = descontoRacionalMenu.getInputNumber('(Desconto racional) Dr')
    if (n):
      _n = descontoRacionalMenu.getInputNumber('(Valor nominal ou título) N')
    if (i):
      _i = descontoRacionalMenu.getInputNumber('(Taxa do desconto %) i')
    if (t):
      _t = descontoRacionalMenu.getInputNumber('(Período de tempo) t')
    return _d, _n, _i, _t
  
  # Função para realizar o cálculo da fórmula de juros simples
  # retornando a variável passada como None.
  # Ex: Se d for None retornará (n * i * t) / (100 + (i * t) )
  def calcular(d, n, i, t):
    if (d is None):
      return (n * i * t) / (100 + (i * t) )
    if (n is None):
      return (d * (100+i*t)) / (i * t)

  #########################################
  # INTERFACE VISUAL DE DOSCONTO RACIONAL #
  #########################################
  descontoRacionalMenu = interface.Interface()
  # Opções de menu
  descontoRacionalMenu.setOptions([
    ('1 - D - Desconto', 'd', 1),
    ('2 - N - Valor nominal', 'N', 2),
    ('0 - Voltar', 'voltar', 0)
  ])
  # Título
  descontoRacionalMenu.setTitle('DESCONTO RACIONAL (OU POR DENTRO)\n\n\tO que se deseja obter?')

  # Obter valores do usuário
  while 1:
    selected = descontoRacionalMenu.getInputOption()

    # Voltar
    if (selected == 0):
      break
    # Usuário deseja obter D
    elif (selected == 1):
      d, n, i, t = getVariables(False, True, True, True)
      d = calcular(d, n, i, t)
      printVariables(d, n, i, t)
    # Usuário deseja obter N
    elif (selected == 2):
      d, n, i, t = getVariables(True, False, True, True)
      n = calcular(d, n, i, t)
      printVariables(d, n, i, t)

def comercial():

  # Função para exibir na tela as variáveis depois
  # dos cálculos
  def printVariables(d, n, i, t, l):
    print('\n\tDc = R${0:.{1}f}'.format(d, 2))
    print('\tn = R${0:.{1}f}'.format(n, 2))
    print('\ti = {0:.{1}f}%'.format(i, 0 if int(i) == i else 2))
    print('\tt = {0:.{1}f}'.format(t, 0 if int(t) == t else 2))
    if (l is not None):
      print('\tL = R${0:.{1}f}'.format(l, 2))
    print()
    os.system('pause')
  
  # Função para obter as variáveis da fórmula
  # através de uma entrada do usuário
  def getVariables(d, n, i, t, l):
    _d, _n, _i, _t, _l = None, None, None, None, None
    if (d):
      _d = descontoComercialMenu.getInputNumber('(Desconto comercial) Dc')
    if (n):
      _n = descontoComercialMenu.getInputNumber('(Valor nominal ou título) N')
    if (i):
      _i = descontoComercialMenu.getInputNumber('(Taxa do desconto %) i')
    if (t):
      _t = descontoComercialMenu.getInputNumber('(Período de tempo) t')
    if (l):
      _l = descontoComercialMenu.getInputNumber('(Valor atual líquido) L')
    return _d, _n, _i, _t, _l
  
  def calcularLiquido(n, d):
    return n - d
  
  def calcular(d, n, i, t):
    if (d is None):
      return (n * i * t) / 100
    if (n is None):
      return (d / (i * t)) * 100
    if (i is None):
      return (d / (n * t)) * 100
    if (t is None):
      return (d / (n * i)) * 100
  
  #########################################
  # INTERFACE VISUAL DE DOSCONTO RACIONAL #
  #########################################
  descontoComercialMenu = interface.Interface()
  # Opções de menu
  descontoComercialMenu.setOptions([
    ('1 - D - Desconto', 'd', 1),
    ('2 - N - Valor nominal', 'N', 2),
    ('3 - i - Taxa de desconto', 'i', 3),
    ('4 - t - Período de tempo', 't', 4),
    ('5 - L - Valor líquido atual', 'L', 5),
    ('0 - Voltar', 'voltar', 0)
  ])
  # Título
  descontoComercialMenu.setTitle('DESCONTO COMERCIAL (OU POR FORA)\n\n\tO que se deseja obter?')

  # Obter valores do usuário
  while 1:
    selected = descontoComercialMenu.getInputOption()

    # Voltar
    if (selected == 0):
      break
    # Usuário deseja obter D
    if (selected == 1):
      d, n, i, t, l = getVariables(False, True, True, True, False)
      d = calcular(d, n, i, t)
      l = calcularLiquido(n, d)
      printVariables(d, n, i, t, l)
    # Usuário deseja obter N
    if (selected == 2):
      d, n, i, t, l = getVariables(True, False, True, True, False)
      n = calcular(d, n, i, t)
      l = calcularLiquido(n, d)
      printVariables(d, n, i, t, l)
    # Usuário deseja obter i
    if (selected == 3):
      d, n, i, t, l = getVariables(True, True, False, True, False)
      i = calcular(d, n, i, t)
      l = calcularLiquido(n, d)
      printVariables(d, n, i, t, l)
    # Usuário deseja obter t
    if (selected == 4):
      d, n, i, t, l = getVariables(True, True, True, False, False)
      t = calcular(d, n, i, t)
      l = calcularLiquido(n, d)
      printVariables(d, n, i, t, l)
    # Usuário deseja obter L
    if (selected == 5):
      d, n, i, t, l = getVariables(True, True, False, False, False)
      l = calcularLiquido(n, d)
      print('\n\tL = R${0:.{1}f}\n'.format(l, 2))
      os.system('pause')
      

def descontos():
  descontosMenu = interface.Interface()
  descontosMenu.setOptions([
    ('1 - Racional', 'Calcular descontos racionais', 1),
    ('2 - Comercial', 'Calcular desconto comerciais', 2),
    ('0 - Voltar', 'voltar', 0)
  ])
  descontosMenu.setTitle('DESCONTOS')

  while 1:
    selected = descontosMenu.getInputOption()
    # Voltar para main menu
    if (selected == 0):
      break
    elif (selected == 1):
      racional()
    elif (selected == 2):
      comercial()

if __name__ == '__main__':
  comercial()