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
    ('2 - N - Valor líquido ou valor atual', 'N', 2),
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

if __name__ == '__main__':
  racional()