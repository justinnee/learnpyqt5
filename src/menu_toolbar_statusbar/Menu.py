'''

创建和使用菜单

'''
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class Menu(QMainWindow):
    def __init__(self):
        super(Menu,self).__init__()
        bar = self.menuBar()  #获取菜单栏

        file = bar.addMenu('文件')
        file.addAction('新建')

        save = QAction('保存',self)
        save.setShortcut("Ctrl+S")
        file.addAction(save)

        save.triggered.connect(self.process)

        edit = bar.addMenu('Edit')
        edit.addAction("copy")
        edit.addAction("paste")
        quit = QAction("退出",self)
        file.addAction(quit)

    def process(self,a):
        #print(a.text())
        print(self.sender().text())


if __name__ == '__main__':
    # create QApplication subject
    app = QApplication(sys.argv)
    # dark mode
    # app.setStyleSheet(qdarkstyle.load_stylesheet())

    main = Menu()
    main.show()

    # into the main loop of the program,using exit to ensure a safe loop end
    sys.exit(app.exec_())