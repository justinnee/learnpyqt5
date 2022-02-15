'''
按列排序

1.按哪一列排序
2.排序类型：升序或降序

sortItems(columnIndex, orderType)

'''

import sys,qdarkstyle
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

class ColumnSort(QWidget):
    def __init__(self):
        super(ColumnSort,self).__init__()
        self.initUI()
    def initUI(self):
        self.setWindowTitle("按列排序")
        self.resize(430,230)
        layout = QVBoxLayout()
        self.tableWidget = QTableWidget()
        self.tableWidget.setRowCount(4)
        self.tableWidget.setColumnCount(3)
        layout.addWidget(self.tableWidget)

        self.tableWidget.setHorizontalHeaderLabels(['Name','Sex','Weight'])

        self.tableWidget.setItem(0, 0,QTableWidgetItem('Jason'))
        self.tableWidget.setItem(0, 1, QTableWidgetItem('B'))
        self.tableWidget.setItem(0, 2, QTableWidgetItem('70'))

        self.tableWidget.setItem(1, 0, QTableWidgetItem('Justin'))
        self.tableWidget.setItem(1, 1, QTableWidgetItem('B'))
        self.tableWidget.setItem(1, 2, QTableWidgetItem('65'))

        self.tableWidget.setItem(2, 0, QTableWidgetItem('Sally'))
        self.tableWidget.setItem(2, 1, QTableWidgetItem('G'))
        self.tableWidget.setItem(2, 2, QTableWidgetItem('55'))

        self.button = QPushButton('排序')
        self.button.clicked.connect(self.order)
        layout.addWidget(self.button)

        self.orderType = Qt.DescendingOrder

        self.setLayout(layout)

    def order(self):
        if self.orderType == Qt.DescendingOrder:
            self.orderType = Qt.AscendingOrder
        else:
            self.orderType = Qt.DescendingOrder

        self.tableWidget.sortItems(2,self.orderType)

if __name__ == '__main__':
    # create QApplication subject
    app = QApplication(sys.argv)
    # dark mode
    app.setStyleSheet(qdarkstyle.load_stylesheet())

    main = ColumnSort()
    main.show()
    # into the main loop of the program,using exit to ensure a safe loop end
    sys.exit(app.exec_())
