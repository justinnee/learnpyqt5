'''
Lesson 98
垂直盒布局(QVBoxLayout)

指定数值，从左上角窗口开始

'''
import sys,qdarkstyle
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class VBoxLayout(QWidget):
    def __init__(self):
        super(VBoxLayout,self).__init__()
        self.setWindowTitle('水平盒布局')

        vlayout = QVBoxLayout()
        vlayout.addWidget(QPushButton('Button1'))
        vlayout.addWidget(QPushButton('Button2'))
        vlayout.addWidget(QPushButton('Button3'))

        # 不指定间隔很小 挤
        vlayout.setSpacing(40)

        self.setLayout(vlayout)


if __name__ == '__main__':
    # create QApplication subject
    app = QApplication(sys.argv)
    # dark mode
    app.setStyleSheet(qdarkstyle.load_stylesheet())

    main = VBoxLayout()
    main.show()
    # into the main loop of the program,using exit to ensure a safe loop end
    sys.exit(app.exec_())
