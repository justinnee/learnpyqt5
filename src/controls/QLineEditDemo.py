# _*_coding: UTF-8_*_
# 开发人员 : Justin Nee
# 开发时间 : 2022/1/7  14:50
# 文件名称 : QLineEditDemo.py
# 开发工具 : PyCharm
"""
QLineEdit综合案例
"""
from PyQt5.QtWidgets import *
import qdarkstyle
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt
import sys

class QLineEditDemo(QWidget):
    def __init__(self):
        super(QLineEditDemo, self).__init__()
        self.initUI()
    def initUI(self):
        edit1 = QLineEdit()
        # 使用int校验器
        edit1.setValidator(QIntValidator())
        edit1.setMaxLength(4)
        edit1.setAlignment(Qt.AlignRight)
        edit1.setFont(QFont('Arial',20))

        edit2 = QLineEdit()
        edit2.setValidator(QDoubleValidator(0.99,99.99,2))

        edit3 = QLineEdit()
        edit3.setInputMask('99_9999_999999;#')

        edit4 = QLineEdit()
        edit4.textChanged.connect(self.textChanged)

        edit5 = QLineEdit()
        edit5.setEchoMode(QLineEdit.Password)
        edit5.editingFinished.connect(self.enterPress)

        edit6 = QLineEdit('Hello PyQt5')
        edit6.setReadOnly(True)

        formLayout = QFormLayout()
        formLayout.addRow('整数校验',edit1)
        formLayout.addRow('浮点数校验', edit2)
        formLayout.addRow('Input Mask',edit3)
        formLayout.addRow('文本变化', edit4)
        formLayout.addRow('密码', edit5)
        formLayout.addRow('只读', edit6)


        self.setLayout(formLayout)
        self.setWindowTitle('QLineEdit综合实例')
    def textChanged(self,text):
        print('输入的内容:'+text)
    def enterPress(self):
        print('已输入值')

if __name__ == '__main__':
    # create QApplication subject
    app = QApplication(sys.argv)
    # dark mode
    app.setStyleSheet(qdarkstyle.load_stylesheet())

    main = QLineEditDemo()
    main.show()

    # into the main loop of the program,using exit to ensure a safe loop end
    sys.exit(app.exec_())