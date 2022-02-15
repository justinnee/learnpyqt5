'''
Lesson 66
扩展的列表控件(QListWidget)

QListView
'''

import qdarkstyle
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import QStringListModel
import sys
import os

class ListWidgetDemo(QMainWindow):
    def __init__(self,parent = None):
        super(ListWidgetDemo,self).__init__(parent)
        self.setWindowTitle('QListWidget 例子')
        self.resize(300,270)


        self.listwidget = QListWidget()
        self.listwidget.resize(300,120)
        self.listwidget.addItem('item1')
        self.listwidget.addItem('item2')
        self.listwidget.addItem('item3')
        self.listwidget.addItem('item4')
        self.listwidget.addItem('item5')
        self.listwidget.addItem('item6')

        self.listwidget.itemClicked.connect(self.clicked)
        self.setCentralWidget(self.listwidget)

    def clicked(self,Index):
        QMessageBox.information(self,'QListWidget','您选择了'+self.listwidget.item(self.listwidget.row(Index)).text())





if __name__ == "__main__":
    # create QApplication subject
    app = QApplication(sys.argv)
    # dark mode
    app.setStyleSheet(qdarkstyle.load_stylesheet())

    main = ListWidgetDemo()
    main.show()
    # into the main loop of the program,using exit to ensure a safe loop end
    sys.exit(app.exec_())
