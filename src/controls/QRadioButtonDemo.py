# _*_coding: UTF-8_*_
# 开发人员 : Justin Nee
# 开发时间 : 2022/1/7  16:30
# 文件名称 : QRadioButtonDemo.py
# 开发工具 : PyCharm
"""

QRadioButton
单选按钮控件

"""
import qdarkstyle
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys

class QRadioButtonDemo(QDialog):
    def __init__(self):
        super(QRadioButtonDemo, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('QRadioButton')
        layout = QHBoxLayout()

        self.button1 = QRadioButton('单选按钮1')
        self.button1.setChecked(True)
        self.button1.toggled.connect(self.buttonState)
        layout.addWidget(self.button1)

        self.button2 = QRadioButton('单选按钮2')
        self.button2.toggled.connect(self.buttonState)
        layout.addWidget(self.button2)

        self.setLayout(layout)

    def buttonState(self):
        radioButton = self.sender()
        if radioButton.text() == "单选按钮1":
            if radioButton.isChecked() == True:
                print('<'+radioButton.text()+'>被选中')
            else:
                print('<'+radioButton.text()+'>被取消选中状态')
        if radioButton.text() == "单选按钮2":
            if radioButton.isChecked() == True:
                print('<'+radioButton.text()+'>被选中')
            else:
                print('<'+radioButton.text()+'>被取消选中状态')

if __name__ == '__main__':
    # create QApplication subject
    app = QApplication(sys.argv)
    # dark mode
    app.setStyleSheet(qdarkstyle.load_stylesheet())

    main = QRadioButtonDemo()
    main.show()

    # into the main loop of the program,using exit to ensure a safe loop end
    sys.exit(app.exec_())
