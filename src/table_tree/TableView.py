'''
Lesson 64
显示二维表数据(QTableView控件)

数据源

Model

需要创建QTableView实例和一个数据源(Model)，然后将两者关联

MVC： Model Viewer Controller

MVC的目的是将后端的数据和前端的页面的耦合度降低

'''
import qdarkstyle
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import sys

class TableView(QWidget):
    def __init__(self,arg = None):
        super(TableView,self).__init__(arg)
        self.setWindowTitle("QTableView表格视图控件演示")
        self.resize(500,300)

        self.model = QStandardItemModel(4,3)
        self.model.setHorizontalHeaderLabels(['id','name','age'])

        self.tableview = QTableView()
        # 关联QTableView控件和Model
        self.tableview.setModel(self.model)

        # 添加数据
        item11 = QStandardItem('10')
        item12 = QStandardItem('Mask')
        item13 = QStandardItem('28')
        self.model.setItem(0, 0, item11)
        self.model.setItem(0, 1, item12)
        self.model.setItem(0, 2, item13)

        layout = QVBoxLayout()
        layout.addWidget(self.tableview)
        self.setLayout(layout)


if __name__ == '__main__':
    # create QApplication subject
    app = QApplication(sys.argv)
    # dark mode
    app.setStyleSheet(qdarkstyle.load_stylesheet())

    main = TableView()
    main.show()

    # into the main loop of the program,using exit to ensure a safe loop end
    sys.exit(app.exec_())

