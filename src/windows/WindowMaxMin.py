'''
Lesson 120
用代码控制窗口的最大化和最小化
'''
import sys,qdarkstyle
from PyQt5.QtWidgets import *
from functools import partial
from PyQt5.QtGui import *
from PyQt5.QtCore import *
class WindowMaxMin(QWidget):
    def __init__(self,parent = None):
        super(WindowMaxMin,self).__init__(parent)
        self.resize(300,400)
        self.setWindowTitle('用代码控制窗口的最大化和最小化')
        layout = QVBoxLayout()
        maxButton1 = QPushButton()
        maxButton1.setText('窗口最大化1')
        maxButton1.clicked.connect(self.maximized1)

        layout.addWidget(maxButton1)

        maxButton2 = QPushButton()
        maxButton2.setText('窗口最大化2')
        maxButton2.clicked.connect(self.showMaximized)

        layout.addWidget(maxButton2)

        minButton = QPushButton()
        minButton.setText('窗口最小化')
        minButton.clicked.connect(self.showMinimized)

        layout.addWidget(minButton)
        self.setLayout(layout)

    def maximized1(self):
        desktop = QApplication.desktop()
        # 获得桌面可用尺寸
        rect = desktop.availableGeometry()
        self.setGeometry(rect)

if __name__ == '__main__':
    # create QApplication subject
    app = QApplication(sys.argv)
    # dark mode
    app.setStyleSheet(qdarkstyle.load_stylesheet())

    main = WindowMaxMin()
    main.show()
    # into the main loop of the program,using exit to ensure a safe loop end
    sys.exit(app.exec_())


