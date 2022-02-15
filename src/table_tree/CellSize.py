'''

默认可以调整大小

'''
from PyQt5.QtCore import *
import sys,qdarkstyle,os
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QColor,QBrush,QFont

class CellSize(QWidget):
    def __init__(self):
        super(CellSize,self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('设置单元格的文本对齐方式')
        self.resize(430,230)
        layout = QHBoxLayout()

        tableWidget = QTableWidget()
        tableWidget.setRowCount(4)
        tableWidget.setColumnCount(3)
        layout.addWidget(tableWidget)

        tableWidget.setHorizontalHeaderLabels(['Name', 'Sex', 'Weight'])
        # 列宽行高
        tableWidget.setRowHeight(0,40)
        tableWidget.setColumnWidth(1,20)
        tableWidget.setRowHeight(2,100)

        newItem = QTableWidgetItem('Sally')
        newItem.setFont(QFont('Times', 14, QFont.Black))
        newItem.setForeground(QBrush(QColor(255, 0, 0)))
        tableWidget.setItem(0, 0, newItem)

        newItem = QTableWidgetItem('G')
        newItem.setForeground(QBrush(QColor(255, 255, 0)))
        newItem.setBackground(QBrush(QColor(0, 0, 255)))
        tableWidget.setItem(0, 1, newItem)

        newItem = QTableWidgetItem('58')
        newItem.setFont(QFont('Times', 50, QFont.Black))
        newItem.setForeground(QBrush(QColor(0, 125, 255)))
        tableWidget.setItem(0, 2, newItem)

        self.setLayout(layout)

if __name__ == '__main__':
    # create QApplication subject
    app = QApplication(sys.argv)
    # dark mode
    app.setStyleSheet(qdarkstyle.load_stylesheet())

    main = CellSize()
    main.show()
    # into the main loop of the program,using exit to ensure a safe loop end
    sys.exit(app.exec_())