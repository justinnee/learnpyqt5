'''
Lesson 100
按钮永远在窗口右下角

'''

import sys,qdarkstyle
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class RightButtomButton(QWidget):
    def __init__(self):
        super(RightButtomButton,self).__init__()
        self.setWindowTitle('按钮永远在窗口右下角')
        self.resize(400,300)

        okButton = QPushButton('确定')
        cancelButton = QPushButton('取消')

        hbox = QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(okButton)
        hbox.addWidget(cancelButton)

        vbox = QVBoxLayout()
        btn1 = QPushButton('按钮1')
        btn2 = QPushButton('按钮2')
        btn3 = QPushButton('按钮3')

        vbox.addStretch(1)
        vbox.addWidget(btn1)
        vbox.addWidget(btn2)
        vbox.addWidget(btn3)

        vbox.addLayout(hbox)

        self.setLayout(vbox)

if __name__ == '__main__':
    # create QApplication subject
    app = QApplication(sys.argv)
    # dark mode
    app.setStyleSheet(qdarkstyle.load_stylesheet())

    main = RightButtomButton()
    main.show()
    # into the main loop of the program,using exit to ensure a safe loop end
    sys.exit(app.exec_())




