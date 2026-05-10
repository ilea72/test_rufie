from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
        QApplication, QWidget, 
        QHBoxLayout, QVBoxLayout, QGridLayout, 
        QGroupBox, QRadioButton,
        QPushButton, QLabel, QListWidget, QLineEdit)
        
from instr import *

class FinalWin(QWidget):
    def __init__(self,exp):
        ''' окно, в котором проводится опрос '''
        super().__init__()
        self.exp=exp
        # создаём и настраиваем графические элелементы:
        self.initUI()

        #устанавливает, как будет выглядеть окно (надпись, размер, место)
        self.set_appear()
        
        
        # старт:
        self.show()

    def initUI(self):
        ''' создает графические элементы '''
        self.workh_text = QLabel(txt_workheart)
        self.index_text = QLabel(self.result())

        self.layout_line = QVBoxLayout()
        self.layout_line.addWidget(self.index_text, alignment = Qt.AlignCenter)
        self.layout_line.addWidget(self.workh_text, alignment = Qt.AlignCenter)         
        self.setLayout(self.layout_line)

    ''' устанавливает, как будет выглядеть окно (надпись, размер, место) '''
    def set_appear(self):
        self.setWindowTitle(txt_finalwin)
        self.resize(win_width, win_height)
        self.move(win_x, win_y)

    def result(self):
        self.index= ((self.exp.t1+self.exp.t2+self.exp.t3) * 4 - 200)/10
        return str(self.index)