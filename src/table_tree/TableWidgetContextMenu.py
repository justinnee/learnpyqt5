''''
Lesson 77
表格中显示上下文菜单

1. 如何弹出菜单
2. 如何在满足条件的情况下弹出菜单

QMenu.exec_
'''
import sys,qdarkstyle
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
class TableWidgetContextMenu(QWidget):
    def __init__(self):
        super(TableWidgetContextMenu, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("表格中显示上下文菜单")
        self.resize(500,300)

        layout = QHBoxLayout()
        self.tableWidget = QTableWidget()
        self.tableWidget.setRowCount(5)
        self.tableWidget.setColumnCount(3)
        layout.addWidget(self.tableWidget)

        self.tableWidget.setHorizontalHeaderLabels(['性别','年龄','体重'])

        newItem = QTableWidgetItem('张三')
        self.tableWidget.setItem(0,0,newItem)
        newItem = QTableWidgetItem('男')
        self.tableWidget.setItem(0, 1, newItem)
        newItem = QTableWidgetItem('150')
        self.tableWidget.setItem(0, 2, newItem)
        newItem = QTableWidgetItem('李四')
        self.tableWidget.setItem(1, 0, newItem)
        newItem = QTableWidgetItem('男')
        self.tableWidget.setItem(1, 1, newItem)
        newItem = QTableWidgetItem('160')
        self.tableWidget.setItem(1, 2, newItem)
        newItem = QTableWidgetItem('王丽')
        self.tableWidget.setItem(2, 0, newItem)
        newItem = QTableWidgetItem('女')
        self.tableWidget.setItem(2, 1, newItem)
        newItem = QTableWidgetItem('120')
        self.tableWidget.setItem(2, 2, newItem)

        # 右键菜单策略
        self.tableWidget.setContextMenuPolicy(Qt.CustomContextMenu)
        self.tableWidget.customContextMenuRequested.connect(self.generateMenu)

        self.setLayout(layout)

    def generateMenu(self,pos):
        print(pos)
        for i in self.tableWidget.selectionModel().selection().indexes():
            rowNum = i.row()
        # 如果选择的行索引小于2，弹出上下文菜单
        if rowNum < 3 :
            menu = QMenu()
            item1 = menu.addAction('菜单项1')
            item2 = menu.addAction('菜单项2')
            item3 = menu.addAction('菜单项3')
            # 单元格附近创建菜单位置
            screenPos = self.tableWidget.mapToGlobal(pos)
            print(screenPos)
            # 被阻塞
            action = menu.exec(screenPos)
            if action == item1:
                print('选择了第一个菜单项',self.tableWidget.item(rowNum,0).text(),
                      self.tableWidget.item(rowNum,1).text(),
                      self.tableWidget.item(rowNum,2).text())
            elif action == item2:
                print('选择了第二个菜单项',self.tableWidget.item(rowNum,0).text(),
                      self.tableWidget.item(rowNum,1).text(),
                      self.tableWidget.item(rowNum,2).text())
            elif action == item3:
                print('选择了第三个菜单项',self.tableWidget.item(rowNum,0).text(),
                      self.tableWidget.item(rowNum,1).text(),
                      self.tableWidget.item(rowNum,2).text())
            else:
                return


if __name__ == '__main__':
    # create QApplication subject
    app = QApplication(sys.argv)
    # dark mode
    app.setStyleSheet(qdarkstyle.load_stylesheet())

    main = TableWidgetContextMenu()
    main.show()
    # into the main loop of the program,using exit to ensure a safe loop end
    sys.exit(app.exec_())