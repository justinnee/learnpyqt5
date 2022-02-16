'''
Lesson 80
增加修改删除树中节点
'''
import sys,qdarkstyle
from PyQt5.QtWidgets import *

class ModifyTree(QWidget):
    def __init__(self,parent = None):
        super(ModifyTree,self).__init__(parent)
        self.setWindowTitle('TreeWidget 修改例子')

        operatorLayout = QHBoxLayout()
        addBtn = QPushButton('添加节点')
        updateBtn = QPushButton('修改节点')
        deleteBtn = QPushButton('删除节点')

        operatorLayout.addWidget(addBtn)
        operatorLayout.addWidget(updateBtn)
        operatorLayout.addWidget(deleteBtn)

        addBtn.clicked.connect(self.addNode)
        updateBtn.clicked.connect(self.updateNode)
        deleteBtn.clicked.connect(self.deleteNode)

        self.tree = QTreeWidget()
        # 为树控件指定列数
        self.tree.setColumnCount(2)
        self.tree.setHeaderLabels(['key', 'value'])

        root = QTreeWidgetItem(self.tree)
        root.setText(0, 'root')
        root.setText(1, '0')

        child1 = QTreeWidgetItem(root)
        child1.setText(0, 'child1')
        child1.setText(1, '1')

        child2 = QTreeWidgetItem(root)
        child2.setText(0, 'child2')
        child2.setText(1, '2')

        child3 = QTreeWidgetItem(child2)
        child3.setText(0, 'child3')
        child3.setText(1, '3')

        self.tree.clicked.connect(self.onTreeClicked)

        mainLayout = QVBoxLayout(self)
        mainLayout.addLayout(operatorLayout)
        mainLayout.addWidget(self.tree)

        self.setLayout(mainLayout)

    def onTreeClicked(self,index):
        item = self.tree.currentItem()
        # print(index.row())
        print('key=%s,value=%s' % (item.text(0),item.text(1)))

    def addNode(self):
        print('添加节点')
        item = self.tree.currentItem()
        print(item)
        node = QTreeWidgetItem(item)
        node.setText(0,'新节点')
        node.setText(1, '新值')

    def updateNode(self):
        print('修改节点')
        item = self.tree.currentItem()
        item.setText(0, '修改节点')
        item.setText(1, '值已经被修改')

    def deleteNode(self):
        item = self.tree.currentItem()
        root = self.tree.invisibleRootItem()
        for item in self.tree.selectedItems():
            if item.parent() != None:
                print('删除节点')
                (item.parent() or root).removeChild(item)

if __name__ == '__main__':
    # create QApplication subject
    app = QApplication(sys.argv)
    # dark mode
    app.setStyleSheet(qdarkstyle.load_stylesheet())

    main = ModifyTree()
    main.show()
    # into the main loop of the program,using exit to ensure a safe loop end
    sys.exit(app.exec_())


