'''
Lesson 81

QTreeView 控件与系统定制模式

QTreeWidget

Model

QDirModel

'''
import sys,qdarkstyle
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

if __name__ == '__main__':
    # create QApplication subject
    app = QApplication(sys.argv)
    # dark mode
    app.setStyleSheet(qdarkstyle.load_stylesheet())

    model = QDirModel()
    tree = QTreeView()
    tree.setModel(model)

    tree.setWindowTitle('QTreeView')
    tree.resize(600,400)
    tree.show()

    # into the main loop of the program,using exit to ensure a safe loop end
    sys.exit(app.exec_())