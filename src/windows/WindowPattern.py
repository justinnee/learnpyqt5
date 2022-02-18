'''
设置窗口样式

主要是窗口边框、标题栏及窗口本身的样式

'''
import sys,qdarkstyle
from PyQt5.QtWidgets import *
from functools import partial
from PyQt5.QtGui import *
from PyQt5.QtCore import *
class WindowPattern(QMainWindow):

    def __init__(self):
        super().__init__()
        self.resize(500,260)
        self.setWindowTitle('设置窗口的样式')

        # 设置窗口属性
        self.setWindowFlags(Qt.WindowMaximizeButtonHint | Qt.WindowStaysOnTopHint| Qt.FramelessWindowHint)
        self.setObjectName("MainWindow")
        # self.setStyleSheet("")

if __name__ == '__main__':
    # create QApplication subject
    app = QApplication(sys.argv)
    # dark mode
    app.setStyleSheet(qdarkstyle.load_stylesheet())

    main = WindowPattern()
    main.show()
    # into the main loop of the program,using exit to ensure a safe loop end
    sys.exit(app.exec_())


