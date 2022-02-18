'''
Lesson 134
装载QSS文件
'''

import sys,qdarkstyle
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from CommonHelper import CommonHelper

class MainWindow(QMainWindow):
    def __init__(self,parent=None):
        super(MainWindow, self).__init__(parent)
        self.resize(1300,900)
        self.setWindowTitle('加载QSS文件')

        btn = QPushButton()
        btn.setText('装载QSS文件')
        btn.setToolTip('提示文本')

        vbox = QVBoxLayout()
        vbox.addWidget(btn)
        btn.clicked.connect(self.onClick)
        self.setLayout(vbox)

        widget = QWidget(self)
        self.setCentralWidget(widget)
        widget.setLayout(vbox)

    def onClick(self):
        styleFile = './style.qss'
        qssStyle = CommonHelper.readQSS(styleFile)
        win.setStyleSheet(qssStyle)



if __name__ == '__main__':
    # create QApplication subject
    app = QApplication(sys.argv)
    # dark mode
    app.setStyleSheet(qdarkstyle.load_stylesheet())
    win = MainWindow()
    win.show()
    # into the main loop of the program,using exit to ensure a safe loop end
    sys.exit(app.exec_())