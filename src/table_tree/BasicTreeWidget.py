'''

树控件QTreeWidget的基本用法

'''

import sys,qdarkstyle
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon,QBrush,QColor
from PyQt5.QtCore import Qt

class BasicTreeWidget(QMainWindow):
    def __init__(self,parent = None):
        super(BasicTreeWidget,self).__init__(parent)
        self.setWindowTitle('树控件QTreeWidget的基本用法')

        self.tree = QTreeWidget()
        # 为树控件指定列数
        self.tree.setColumnCount(2)

        #指定列标签
        self.tree.setHeaderLabels(['key','value'])

        root = QTreeWidgetItem(self.tree)
        root.setText(0,'根节点')
        root.setIcon(0,QIcon(r"G:\learnpyqt5\src\menu_toolbar_statusbar\images\save.png"))
        self.tree.setColumnWidth(0,120)

        # 添加子节点1
        child1 = QTreeWidgetItem(root)
        child1.setText(0,'子节点1')
        child1.setText(1, '子节点1的数据')
        child1.setIcon(0,QIcon(r"G:\learnpyqt5\src\menu_toolbar_statusbar\images\Siri.png"))
        child1.setCheckState(0,Qt.Checked)

        # 添加子节点2
        child2 = QTreeWidgetItem(root)
        child2.setText(0, '子节点2')
        child2.setIcon(0, QIcon(r"G:\learnpyqt5\src\menu_toolbar_statusbar\images\Siri.png"))

        # 为子节点2添加子节点
        child3 = QTreeWidgetItem(child2)
        child3.setText(0, '子节点2-1')
        child3.setText(1, '子节点2-1的数据')
        child3.setIcon(0, QIcon(r"G:\learnpyqt5\src\menu_toolbar_statusbar\images\Siri.png"))


        self.setCentralWidget(self.tree)


if __name__ == '__main__':
    # create QApplication subject
    app = QApplication(sys.argv)
    # dark mode
    app.setStyleSheet(qdarkstyle.load_stylesheet())

    main = BasicTreeWidget()
    main.show()
    # into the main loop of the program,using exit to ensure a safe loop end
    sys.exit(app.exec_())