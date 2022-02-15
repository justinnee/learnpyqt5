'''
Lesson 65
显示列表数据(QListView控件)
'''
import qdarkstyle
from PyQt5.QtWidgets import QApplication,QWidget,QVBoxLayout,QListView,QMessageBox
from PyQt5.QtGui import *
from PyQt5.QtCore import QStringListModel
import sys
import os

class ListViewDemo(QWidget):
    def __init__(self,parent = None):
        super(ListViewDemo,self).__init__(parent)
        self.setWindowTitle('QListView 例子')
        self.resize(300,270)

        layout = QVBoxLayout()

        listview = QListView()
        listModel = QStringListModel()

        self.list = os.listdir('H:/YOLOX-main/datasets/VOCdevkit/JPEGImages')

        listModel.setStringList(self.list)

        listview.setModel(listModel)
        listview.clicked.connect(self.clicked)
        layout.addWidget(listview)

        self.setLayout(layout)

    def clicked(self,item):
        QMessageBox.information(self,'QlistView','您选择了'+self.list[item.row()])



if __name__ == "__main__":
    # create QApplication subject
    app = QApplication(sys.argv)
    # dark mode
    app.setStyleSheet(qdarkstyle.load_stylesheet())

    main = ListViewDemo()
    main.show()

    # into the main loop of the program,using exit to ensure a safe loop end
    sys.exit(app.exec_())
