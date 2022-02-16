'''

绝对布局

指定数值，从左上角窗口开始

'''
import sys,qdarkstyle
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class AbsoluteLayout(QWidget):
    def __init__(self):
        super(AbsoluteLayout,self).__init__()
        self.setWindowTitle('绝对布局')

        self.label1 = QLabel('欢迎',self)
        self.label1.move(15,20)

        self.label2 = QLabel('学习', self)
        self.label2.move(35, 40)

        self.label3 = QLabel('PyQt5', self)
        self.label3.move(55, 70)

if __name__ == '__main__':
    # create QApplication subject
    app = QApplication(sys.argv)
    # dark mode
    app.setStyleSheet(qdarkstyle.load_stylesheet())

    main = AbsoluteLayout()
    main.show()
    # into the main loop of the program,using exit to ensure a safe loop end
    sys.exit(app.exec_())
