'''
设置单元格字体和颜色

'''

import sys,qdarkstyle,os
from PyQt5.QtWidgets import *
from PyQt5 import QtCore
from PyQt5.QtGui import QColor,QBrush,QFont

class CellFontAndColor(QWidget):
    def __init__(self):
        super(CellFontAndColor,self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("设置单元格字体和颜色")
        self.resize(430,230)

        layout = QHBoxLayout()

        self.piclist = os.listdir('H:/YOLOX-main/datasets/VOCdevkit/JPEGImages')
        layout = QHBoxLayout()
        tableWidget = QTableWidget()
        tableWidget.setRowCount(len(self.piclist))
        tableWidget.setColumnCount(5)

        layout.addWidget(tableWidget)

        tableWidget.setHorizontalHeaderLabels(['图片', '缺陷名称', '缺陷编码', '缺陷置信度', '坐标位置'])

        newItem = QTableWidgetItem('A.jpg')
        newItem.setFont(QFont('Times',14,QFont.Black))
        newItem.setForeground(QBrush(QColor(255,0,0)))
        tableWidget.setItem(0,0,newItem)

        newItem = QTableWidgetItem('B.jpg')
        newItem.setFont(QFont('Times', 20, QFont.Black))
        newItem.setForeground(QBrush(QColor(255, 255, 0)))
        newItem.setBackground(QBrush(QColor(0,0,255)))
        tableWidget.setItem(0, 1, newItem)

        self.setLayout(layout)
if __name__ == '__main__':
    # create QApplication subject
    app = QApplication(sys.argv)
    # dark mode
    app.setStyleSheet(qdarkstyle.load_stylesheet())

    main = CellFontAndColor()
    main.show()
    # into the main loop of the program,using exit to ensure a safe loop end
    sys.exit(app.exec_())