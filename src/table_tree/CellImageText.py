'''
Lesson 75
在单元格中实现图文混排的效果

'''
import sys,qdarkstyle
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

class CellImageText(QWidget):
    def __init__(self):
        super(CellImageText, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("在单元格中实现图文混排的效果")
        self.resize(500,300)

        layout = QHBoxLayout()

        tableWidget = QTableWidget()
        tableWidget.setRowCount(5)
        tableWidget.setColumnCount(4)
        layout.addWidget(tableWidget)

        tableWidget.setHorizontalHeaderLabels(['Name', 'Sex', 'Weight','Picture'])

        newItem = QTableWidgetItem('Jason')
        tableWidget.setItem(0, 0, newItem)
        newItem = QTableWidgetItem('男')
        tableWidget.setItem(0, 1, newItem)
        newItem = QTableWidgetItem('136')
        tableWidget.setItem(0, 2, newItem)

        newItem = QTableWidgetItem(QIcon(r'G:\learnpyqt5\src\drapclip\images\c8.jpg'),'c8')
        tableWidget.setItem(0,3,newItem)

        self.setLayout(layout)


if __name__ == '__main__':
    # create QApplication subject
    app = QApplication(sys.argv)
    # dark mode
    app.setStyleSheet(qdarkstyle.load_stylesheet())

    main = CellImageText()
    main.show()
    # into the main loop of the program,using exit to ensure a safe loop end
    sys.exit(app.exec_())