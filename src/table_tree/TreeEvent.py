'''

Lesson 79

为树节点添加响应事件

'''

import sys,qdarkstyle
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
class TreeEvent(QMainWindow):
    def __init__(self,parent = None):
        super(TreeEvent,self).__init__(parent)
        self.setWindowTitle('树控件QTreeWidget的基本用法')

        self.tree = QTreeWidget()
        # 为树控件指定列数
        self.tree.setColumnCount(2)
        self.tree.setHeaderLabels(['key','value'])

        root = QTreeWidgetItem(self.tree)
        root.setText(0,'root')
        root.setText(1,'0')

        child1 = QTreeWidgetItem(root)
        child1.setText(0,'child1')
        child1.setText(1,'1')

        child2 = QTreeWidgetItem(root)
        child2.setText(0, 'child2')
        child2.setText(1, '2')

        child3 = QTreeWidgetItem(child2)
        child3.setText(0, 'child3')
        child3.setText(1, '3')

        self.tree.clicked.connect(self.onTreeClicked)
        self.setCentralWidget(self.tree)

    def onTreeClicked(self,index):
        item = self.tree.currentItem()
        print(index.row())
        print('key=%s,value=%s' % (item.text(0),item.text(1)))


if __name__ == '__main__':
    # create QApplication subject
    app = QApplication(sys.argv)
    # dark mode
    app.setStyleSheet(qdarkstyle.load_stylesheet())

    main = TreeEvent()
    main.show()
    # into the main loop of the program,using exit to ensure a safe loop end
    sys.exit(app.exec_())