'''

使用Partial对象为槽函数传递参数

'''

import sys,qdarkstyle
from PyQt5.QtWidgets import *
from functools import partial
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class PartialSlotArg(QMainWindow):
    def __init__(self):
        super(PartialSlotArg, self).__init__()
        self.setWindowTitle("使用Partial对象为槽函数传递参数")

        button1 = QPushButton('按钮1')
        button2 = QPushButton('按钮2')

        x = 5
        y = 3
        button1.clicked.connect(partial(self.onButtonClick,x,y))
        button2.clicked.connect(partial(self.onButtonClick,x, -y))

        layout = QHBoxLayout()
        layout.addWidget(button1)
        layout.addWidget(button2)

        mainFrame = QWidget()
        mainFrame.setLayout(layout)
        self.setCentralWidget(mainFrame)

    def onButtonClick(self,m,n):
        print("m+n=",m+n)
        QMessageBox.information(self,"结果",str(m+n))

if __name__ == '__main__':
    # create QApplication subject
    app = QApplication(sys.argv)
    # dark mode
    app.setStyleSheet(qdarkstyle.load_stylesheet())

    main = PartialSlotArg()
    main.show()
    # into the main loop of the program,using exit to ensure a safe loop end
    sys.exit(app.exec_())
#

# def funcos(eps,x):
#     sum = 0
#     for i in range(100):
#         factor = 1
#         for j in range(1,2*i+1):
#             factor *= j
#         item = ((-1)**i)*(x**(2*i))/factor
#         if abs(item) >= eps:
#             sum += item
#         else:
#             return sum
