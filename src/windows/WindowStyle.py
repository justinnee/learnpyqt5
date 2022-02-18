'''
Lesson118 设置窗口风格

窗口、绘图与特效：设置窗口风格
设置窗口中控件的风格

QApplication.setStyle(...)

'''
import sys,qdarkstyle
from PyQt5.QtWidgets import *
from functools import partial
from PyQt5.QtGui import *
from PyQt5 import QtCore

class WindowStyle(QWidget):
    def __init__(self):
        super(WindowStyle, self).__init__()
        self.setWindowTitle('设置窗口风格')
        hlayout = QHBoxLayout()
        self.styleLabel = QLabel('设置窗口风格:')
        self.styleComboBox = QComboBox()
        self.styleComboBox.addItems(QStyleFactory.keys())

        # 获取当前窗口的风格
        print(QApplication.style().objectName())
        index = self.styleComboBox.findText(QApplication.style().objectName(),QtCore.Qt.MatchFixedString)

        self.styleComboBox.setCurrentIndex(index)

        self.styleComboBox.activated[str].connect(self.handleStyleChanged)
        hlayout.addWidget(self.styleLabel)
        hlayout.addWidget(self.styleComboBox)

        self.setLayout(hlayout)
    def handleStyleChanged(self,style):
        QApplication.setStyle(style)
if __name__ == '__main__':
    # create QApplication subject
    app = QApplication(sys.argv)
    # dark mode
    # app.setStyleSheet(qdarkstyle.load_stylesheet())

    main = WindowStyle()
    main.show()
    # into the main loop of the program,using exit to ensure a safe loop end
    sys.exit(app.exec_())
