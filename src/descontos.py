import interface

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