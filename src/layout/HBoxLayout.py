'''
Lesson 96
水平盒布局(QHBoxLayout)

指定数值，从左上角窗口开始

'''
import sys,qdarkstyle
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class HBoxLayout(QWidget):
    def __init__(self):
        super(HBoxLayout,self).__init__()
        self.setWindowTitle('水平盒布局')

        hlayout = QHBoxLayout()
        hlayout.addWidget(QPushButton('Button1'))
        hlayout.addWidget(QPushButton('Button2'))
        hlayout.addWidget(QPushButton('Button3'))
        hlayout.addWidget(QPushButton('Button4'))
        hlayout.addWidget(QPushButton('Button5'))
        hlayout.addWidget(QPushButton('Button6'))

        # 不指定间隔很小 挤
        hlayout.setSpacing(40)

        self.setLayout(hlayout)


if __name__ == '__main__':
    # create QApplication subject
    app = QApplication(sys.argv)
    # dark mode
    app.setStyleSheet(qdarkstyle.load_stylesheet())

    main = HBoxLayout()
    main.show()
    # into the main loop of the program,using exit to ensure a safe loop end
    sys.exit(app.exec_())
