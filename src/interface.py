import os

class Interface():
  
  def setOptions(self, options):
    self._options = options
  
  def setTitle(self, title):
    self.title = title

  def displayOptions(self, error):
    os.system('cls')
    print('\t#############################')
    print('\t###   SELECIONE A OPÇÃO   ###')
    print('\t#############################\n')
    print('\t%s\n' %(self.title))
    for i in range(len(self._options)):
      print('\t %s' % (self._options[i][0]))
    if (len(error) > 0):
      print('\n\n\t%s\n\n' %(error))
  
  def getInputOption(self):
    error = ''
    while 1:
      self.displayOptions(error)
      selected = self.getSelected(input('>'))
      if (selected == -1):
        error = 'Opção inválida!'
      else:
        break
    return selected
  
  def getSelected(self, selected):
    for i in range(len(self._options)):
      option = self._options[i]
      if (option[1].lower() == str(selected).lower() or str(option[2]) == selected):
        return option[2]
    return -1