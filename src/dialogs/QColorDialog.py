# _*_coding: UTF-8_*_
# 开发人员 : Justin Nee
# 开发时间 : 2022/2/13  15:45
# 文件名称 : QColorDialog.py
# 开发工具 : PyCharm
import sys
import qdarkstyle
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
class QColorDialogDemo(QWidget):
    def __init__(self):
        super(QColorDialogDemo, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Color Dialog 例子')
        layout = QVBoxLayout()
        self.colorButton = QPushButton('设置颜色')
        self.colorButton.clicked.connect(self.getColor)
        layout.addWidget(self.colorButton)

        self.colorButton1 = QPushButton('设置北京颜色')
        self.colorButton1.clicked.connect(self.getBGColor)
        layout.addWidget(self.colorButton1)

        self.colorLabel = QLabel('Hello,测试颜色例子')
        layout.addWidget(self.colorLabel)

        self.setLayout(layout)

    def getColor(self):
        color = QColorDialog.getColor()
        p = QPalette()
        p.setColor(QPalette.WindowText,color)
        self.colorLabel.setPalette(p)

    def getBGColor(self):
        color = QColorDialog.getColor()
        p = QPalette()
        p.setColor(QPalette.Window,color)
        self.colorLabel.setAutoFillBackground(True)
        self.colorLabel.setPalette(p)


if __name__ == '__main__':
    # create QApplication subject
    app = QApplication(sys.argv)
    # dark mode
    # app.setStyleSheet(qdarkstyle.load_stylesheet())

    main = QColorDialogDemo()
    main.show()

    # into the main loop of the program,using exit to ensure a safe loop end
    sys.exit(app.exec_())