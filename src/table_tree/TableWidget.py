'''

扩展的表格控件(QTableWidget)

QTableView

每一个单元格cell都是一个QTableWidgetItem

'''

import sys
import qdarkstyle
import os
from PyQt5.QtWidgets import QWidget,QTableWidget,QHBoxLayout,QApplication,QTableWidgetItem,QAbstractItemView

class TableWidgetDemo(QWidget):
    def __init__(self):
        super(TableWidgetDemo,self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('QTableWidget演示')
        self.resize(670,230)
        self.piclist = os.listdir('H:/YOLOX-main/datasets/VOCdevkit/JPEGImages')
        layout = QHBoxLayout()
        tablewidget = QTableWidget()
        tablewidget.setRowCount(len(self.piclist))
        tablewidget.setColumnCount(5)

        layout.addWidget(tablewidget)

        tablewidget.setHorizontalHeaderLabels(['图片','缺陷名称','缺陷编码','缺陷置信度','坐标位置'])
        # nameItem = QTableWidgetItem('2021040215')
        # tablewidget.setItem(0,0,nameItem)

        for i in self.piclist:
            nameItem = QTableWidgetItem(i)
            tablewidget.setItem(self.piclist.index(str(i)),0,nameItem)

        # 禁止编辑
        tablewidget.setEditTriggers(QAbstractItemView.NoEditTriggers)

        # 整行选择
        tablewidget.setSelectionBehavior(QAbstractItemView.SelectRows)

        # 调整列和行
        tablewidget.resizeColumnsToContents()
        tablewidget.resizeRowsToContents()

        # tablewidget.horizontalHeader().setVisible(False)
        tablewidget.verticalHeader().setVisible(False)

        # 隐藏表格线
        tablewidget.setShowGrid(False)

        self.setLayout(layout)



if __name__ == '__main__':
    # create QApplication subject
    app = QApplication(sys.argv)
    # dark mode
    app.setStyleSheet(qdarkstyle.load_stylesheet())

    main = TableWidgetDemo()
    main.show()
    # into the main loop of the program,using exit to ensure a safe loop end
    sys.exit(app.exec_())
