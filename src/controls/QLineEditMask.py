# _*_coding: UTF-8_*_
# 开发人员 : Justin Nee
# 开发时间 : 2022/1/7  14:23
# 文件名称 : QLineEditMask.py
# 开发工具 : PyCharm
"""
掩码限制QLineEdit控件的输入
A 必须输入ASCII字母字符A-Z或a-z
a 允许输入ASCII字母字符
N 必须输入ASCII字母字符A-Z或a-z或0-9
n 允许输入ASCII字母和数字字符
X 任何字符必须输入
x 允许输入任何字符
9 必须输入ASCII数字字符0-9     # D
0 允许输入ASCII数字字符        # d
# 允许输入ASCII数字字符和加减号
H 十六进制字符必须输入
h 十六进制字符允许输入
B 二进制必须输入0-1
b 二进制允许输入
> 所有字母字符大写
< 所有字母字符小写
！ 关闭大小写转换
\ 使用转义

"""
import qdarkstyle
from PyQt5.QtWidgets import *
import sys

class QLineEditMask(QWidget):
    def __init__(self):
        super(QLineEditMask, self).__init__()
        self.initUI()
    def initUI(self):
        self.setWindowTitle('用掩码限制QLineEdit控件的输入')
        formLayout = QFormLayout()

        ipLineEdit = QLineEdit()
        macLineEdit = QLineEdit()
        dateLineEdit = QLineEdit()
        licenseLineEdit = QLineEdit()

        # 192.168.21.45
        ipLineEdit.setInputMask('000.000.000.000;_')
        macLineEdit.setInputMask('HH:HH:HH:HH:HH:HH;_')
        dateLineEdit.setInputMask('0000-00-00')
        licenseLineEdit.setInputMask('>AAAAA-AAAAA-AAAAA-AAAAA-AAAAA;#')

        formLayout.addRow('数字掩码',ipLineEdit)
        formLayout.addRow('MAC掩码', macLineEdit)
        formLayout.addRow('日期掩码', dateLineEdit)
        formLayout.addRow('许可证掩码', licenseLineEdit)

        self.setLayout(formLayout)

if __name__ == '__main__':
    # create QApplication subject
    app = QApplication(sys.argv)
    # dark mode
    app.setStyleSheet(qdarkstyle.load_stylesheet())

    main = QLineEditMask()
    main.show()

    # into the main loop of the program,using exit to ensure a safe loop end
    sys.exit(app.exec_())
