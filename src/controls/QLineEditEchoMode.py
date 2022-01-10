# _*_coding: UTF-8_*_
# 开发人员 : Justin Nee
# 开发时间 : 2022/1/7  13:25
# 文件名称 : QLineEditEchoMode.py
# 开发工具 : PyCharm
"""
QLineEdit EchoMode

1. input single line text

EchoMode(4 types):

1. Normal            # 显示输入的文本
2. NoEcho            # 什么都不显示   Linux password
3. Password          # 仅显示已输入密码的位数
4. PasswordEchoEdit  # 输密码显示文本

"""
from PyQt5.QtWidgets import *
import sys
import qdarkstyle

class QLineEditEchoMode(QWidget):
    def __init__(self):
        super(QLineEditEchoMode, self).__init__()
        self.initUI()
    def initUI(self):
        self.setWindowTitle('EchoMode')

        formlayout = QFormLayout()

        normalLineEdit = QLineEdit()
        noEchoLineEdit = QLineEdit()
        passwordLineEdit = QLineEdit()
        passwordEchoOnLineEdit = QLineEdit()

        formlayout.addRow("Normal",normalLineEdit)
        formlayout.addRow("NoEcho",noEchoLineEdit)
        formlayout.addRow("Password",passwordLineEdit)
        formlayout.addRow("PasswordEchoOnEdit",passwordEchoOnLineEdit)

        # place holder text : tip information
        normalLineEdit.setPlaceholderText("Normal")
        noEchoLineEdit.setPlaceholderText("NoEcho")
        passwordLineEdit.setPlaceholderText("Password")
        passwordEchoOnLineEdit.setPlaceholderText("PasswordEchoOnEdit")

        normalLineEdit.setEchoMode(QLineEdit.Normal)
        noEchoLineEdit.setEchoMode(QLineEdit.NoEcho)
        passwordLineEdit.setEchoMode(QLineEdit.Password)
        passwordEchoOnLineEdit.setEchoMode(QLineEdit.PasswordEchoOnEdit)

        self.setLayout(formlayout)

if __name__ == '__main__':
    # create QApplication subject
    app = QApplication(sys.argv)
    # dark mode
    app.setStyleSheet(qdarkstyle.load_stylesheet())

    main = QLineEditEchoMode()
    main.show()

    # into the main loop of the program,using exit to ensure a safe loop end
    sys.exit(app.exec_())

