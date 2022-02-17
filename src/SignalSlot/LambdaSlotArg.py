'''

使用Lambda表达式为槽函数传递参数

Lambda表达式：匿名函数，没有名字的函数

fun = lambda :print("hello world")
fun()

fun1 = lambda x,y:print(x,y)
fun1("a","b")

'''

import sys,qdarkstyle
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class LambdaSlotArg(QMainWindow):
    def __init__(self):
        super(LambdaSlotArg, self).__init__()
        self.setWindowTitle("使用Lambda表达式为槽函数传递参数")

        button1 = QPushButton('按钮1')
        button2 = QPushButton('按钮2')

        ok = 100

        button1.clicked.connect(lambda :self.onButtonClick(10,20))
        button2.clicked.connect(lambda: self.onButtonClick(ok,-20))

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

    main = LambdaSlotArg()
    main.show()
    # into the main loop of the program,using exit to ensure a safe loop end
    sys.exit(app.exec_())


