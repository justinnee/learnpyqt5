'''
多窗口交互(2): 使用信号与槽
'''
import sys,qdarkstyle
from PyQt5.QtWidgets import *
from functools import partial
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from NewDateDialog import NewDateDialog

class MultiWindow2(QWidget):
    def __init__(self,parent = None):
        super(MultiWindow2,self).__init__(parent)
        self.resize(400,90)
        self.setWindowTitle('多窗口交互(2): 使用信号与槽')

        self.open_btn = QPushButton('获取时间')
        self.lineEdit_inner = QLineEdit(self)
        self.lineEdit_inner.setText('接收子窗口内置信号的时间')
        self.lineEdit_emit = QLineEdit(self)
        self.lineEdit_emit.setText('接收子窗口自定义信号的时间')
        self.open_btn.clicked.connect(self.openDialog)

        grid = QGridLayout()
        grid.addWidget(self.lineEdit_inner)
        grid.addWidget(self.lineEdit_emit)
        grid.addWidget(self.open_btn)
        self.setLayout(grid)

    def openDialog(self):
        dialog = NewDateDialog(self)
        #连接子窗口的内置信号和主窗口的槽函数
        dialog.datetime_inner.dateTimeChanged.connect(self.deal_inner_slot)
        # 连接子窗口的自定义信号和主窗口的槽函数
        dialog.Signal_OneParameter.connect(self.deal_emit_slot)
        dialog.show()

    def deal_inner_slot(self,date):
        self.lineEdit_inner.setText(date.toString())

    def deal_emit_slot(self,dateStr):
        self.lineEdit_emit.setText(dateStr)

if __name__ == '__main__':
    # create QApplication subject
    app = QApplication(sys.argv)
    # dark mode
    app.setStyleSheet(qdarkstyle.load_stylesheet())

    main = MultiWindow2()
    main.show()
    # into the main loop of the program,using exit to ensure a safe loop end
    sys.exit(app.exec_())




