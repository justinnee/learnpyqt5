'''

改变单元格中图片的尺寸

'''
import sys,qdarkstyle
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class CellImageSize(QWidget):
    def __init__(self):
        super(CellImageSize, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("改变单元格中图片的尺寸")
        self.resize(1000,900)

        layout = QHBoxLayout()

        tableWidget = QTableWidget()
        tableWidget.setRowCount(5)
        tableWidget.setColumnCount(4)
        tableWidget.setIconSize(QSize(300,200))
        layout.addWidget(tableWidget)

        tableWidget.setHorizontalHeaderLabels(['Name', 'Sex', 'Weight', 'Picture'])

        # 让列的宽度与图片的宽度相同
        for i in range(4):
            tableWidget.setColumnWidth(i,300)

        # 让行的高度与图片的高度相同
        for i in range(5):
            tableWidget.setRowHeight(i, 200)

        newItem = QTableWidgetItem('Jason')
        tableWidget.setItem(0, 0, newItem)
        newItem = QTableWidgetItem('男')
        tableWidget.setItem(0, 1, newItem)
        newItem = QTableWidgetItem('136')
        tableWidget.setItem(0, 2, newItem)

        newItem = QTableWidgetItem(QIcon(r'G:\learnpyqt5\src\drapclip\images\c8.jpg'), 'c8')
        tableWidget.setItem(0, 3, newItem)

        self.setLayout(layout)


if __name__ == '__main__':
    # create QApplication subject
    app = QApplication(sys.argv)
    # dark mode
    app.setStyleSheet(qdarkstyle.load_stylesheet())

    main = CellImageSize()
    main.show()
    # into the main loop of the program,using exit to ensure a safe loop end
    sys.exit(app.exec_())