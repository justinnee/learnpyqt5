'''
Lesson 99
设置伸缩量(addStretch)
'''
import sys,qdarkstyle
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class Stretch(QWidget):
    def __init__(self):
        super(Stretch,self).__init__()
        self.setWindowTitle('设置伸缩量')
        self.resize(800,100)

        btn1 = QPushButton(self)
        btn2 = QPushButton(self)
        btn3 = QPushButton(self)
        btn4 = QPushButton(self)
        btn1.setText('btn1')
        btn2.setText('btn2')
        btn3.setText('btn3')
        btn4.setText('btn4')

        layout = QHBoxLayout()
        layout.addStretch(0)
        layout.addWidget(btn1)
        layout.addWidget(btn2)
        layout.addWidget(btn3)
        layout.addWidget(btn4)

        btnOk = QPushButton(self)
        btnOk.setText('OK')

        layout.addStretch(1)
        layout.addWidget(btnOk)

        self.setLayout(layout)

if __name__ == '__main__':
    # create QApplication subject
    app = QApplication(sys.argv)
    # dark mode
    app.setStyleSheet(qdarkstyle.load_stylesheet())

    main = Stretch()
    main.show()
    # into the main loop of the program,using exit to ensure a safe loop end
    sys.exit(app.exec_())





