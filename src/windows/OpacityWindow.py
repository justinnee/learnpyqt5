'''
Lesson 133
创建透明窗口
'''

import sys,qdarkstyle
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
if __name__ == '__main__':
    # create QApplication subject
    app = QApplication(sys.argv)
    # dark mode
    app.setStyleSheet(qdarkstyle.load_stylesheet())

    win = QMainWindow()
    win.setWindowTitle('窗口的透明度设置')
    win.setWindowOpacity(0.9)

    button = QPushButton('我的按钮',win)
    win.resize(400,200)
    win.show()
    # into the main loop of the program,using exit to ensure a safe loop end
    sys.exit(app.exec_())