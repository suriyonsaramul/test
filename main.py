from PyQt5.QtWidgets import *
from PyQt5 import uic

class Calculator(QMainWindow):
  def __init__(self):
    super(Calculator, self).__init__()
    uic.loadUi('calculator.ui', self)
    self.show()

    self.btnCalculate.clicked.connect(self.calculate)

  def calculate(self):
    if self.le_a.text() == '' or self.le_b.text() == '':
      pass
    else:
      a = int(self.le_a.text())
      b = int(self.le_b.text())
      c = a+b
      self.lbl_result.setText(f'{a} + {b} = {c}')
      self.le_a.setText('')
      self.le_b.setText('')

def main():
  app = QApplication([])
  window = Calculator()
  app.exec_()

if __name__ == '__main__':
  main()