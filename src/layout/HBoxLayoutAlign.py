'''
Lesson 97

设置控件的对齐方式

'''
import sys,qdarkstyle
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class HBoxLayoutAlign(QWidget):
    def __init__(self):
        super(HBoxLayoutAlign,self).__init__()
        self.setWindowTitle('水平盒布局2')

        hlayout = QHBoxLayout()
        hlayout.addWidget(QPushButton('Button1'),1,Qt.AlignLeft | Qt.AlignTop)
        hlayout.addWidget(QPushButton('Button2'),1,Qt.AlignLeft | Qt.AlignTop)
        hlayout.addWidget(QPushButton('Button3'))
        hlayout.addWidget(QPushButton('Button4'),1,Qt.AlignLeft | Qt.AlignBottom)
        hlayout.addWidget(QPushButton('Button5'))
        hlayout.addWidget(QPushButton('Button6'))

        # 不指定间隔很小 挤
        hlayout.setSpacing(40)

        self.setLayout(hlayout)


if __name__ == '__main__':
    # create QApplication subject
    app = QApplication(sys.argv)
    # dark mode
    app.setStyleSheet(qdarkstyle.load_stylesheet())

    main = HBoxLayoutAlign()
    main.show()
    # into the main loop of the program,using exit to ensure a safe loop end
    sys.exit(app.exec_())
