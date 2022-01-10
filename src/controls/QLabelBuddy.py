# _*_coding: UTF-8_*_
# 开发人员 : Justin Nee
# 开发时间 : 2022/1/7  13:02
# 文件名称 : QLabelBuddy.py
# 开发工具 : PyCharm
"""
QLabelBuddy

mainLayout.addWidget(obj,rowIndex,columnIndex,row,column)
"""
from PyQt5.QtWidgets import *
import sys
import qdarkstyle

class QLabelBuddy(QDialog):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('QLabel & Buddy Controls')

        nameLabel = QLabel('&Name',self)
        namelineEdit =QLineEdit(self)
        # set buddy
        nameLabel.setBuddy(namelineEdit)

        pwdLabel = QLabel('&Password', self)
        pwdlineEdit = QLineEdit(self)
        # set buddy
        pwdLabel.setBuddy(pwdlineEdit)

        btnOK = QPushButton('&OK')
        btnCancel = QPushButton('&Cancel')

        mainLayout = QGridLayout(self)
        mainLayout.addWidget(nameLabel,0,0)
        mainLayout.addWidget(namelineEdit,0,1,1,2)

        mainLayout.addWidget(pwdLabel,1,0)
        mainLayout.addWidget(pwdlineEdit,1,1,1,2)

        mainLayout.addWidget(btnOK,2,1)
        mainLayout.addWidget(btnCancel,2,2)

if __name__ == '__main__':
    # create QApplication subject
    app = QApplication(sys.argv)
    # dark mode
    app.setStyleSheet(qdarkstyle.load_stylesheet())

    main = QLabelBuddy()
    main.show()

    # into the main loop of the program,using exit to ensure a safe loop end
    sys.exit(app.exec_())