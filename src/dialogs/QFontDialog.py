# _*_coding: UTF-8_*_
# 开发人员 : Justin Nee
# 开发时间 : 2022/2/13  15:34
# 文件名称 : QFontDialog.py
# 开发工具 : PyCharm
'''
字体对话框： QFontDialog
'''
import sys
import qdarkstyle
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
class QFontDialogDemo(QWidget):
    def __init__(self):
        super(QFontDialogDemo, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Font Dialog例子')
        layout = QVBoxLayout()
        self.fontButton = QPushButton('选择字体')
        self.fontButton.clicked.connect(self.getFont)
        layout.addWidget(self.fontButton)

        self.fontLabel = QLabel('Hello,测试字体例子')
        layout.addWidget(self.fontLabel)

        self.setLayout(layout)

    def getFont(self):
        font,ok = QFontDialog.getFont()
        if ok :
            self.fontLabel.setFont(font)



if __name__ == '__main__':
    # create QApplication subject
    app = QApplication(sys.argv)
    # dark mode
    app.setStyleSheet(qdarkstyle.load_stylesheet())

    main = QFontDialogDemo()
    main.show()

    # into the main loop of the program,using exit to ensure a safe loop end
    sys.exit(app.exec_())