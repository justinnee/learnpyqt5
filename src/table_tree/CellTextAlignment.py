'''
设置单元格对齐方式

setTextAlignment

Qt.AlignRight    Qt.AlignBottom
'''

import sys,qdarkstyle
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt

class CellTextAlignment(QWidget):
    def __init__(self):
        super(CellTextAlignment,self).__init__()
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

        # 内容、字体、对齐方式都以每个QTableWidgetItem为对象
        newItem = QTableWidgetItem('Jason')
        newItem.setTextAlignment(Qt.AlignRight | Qt.AlignBottom)
        tableWidget.setItem(0,0,newItem)

        newItem = QTableWidgetItem('BOY')
        newItem.setTextAlignment(Qt.AlignRight | Qt.AlignBottom)
        tableWidget.setItem(0, 1, newItem)

        newItem = QTableWidgetItem('80')
        newItem.setTextAlignment(Qt.AlignCenter)
        tableWidget.setItem(0, 2, newItem)

        self.setLayout(layout)

if __name__ == '__main__':
    # create QApplication subject
    app = QApplication(sys.argv)
    # dark mode
    app.setStyleSheet(qdarkstyle.load_stylesheet())

    main = CellTextAlignment()
    main.show()
    # into the main loop of the program,using exit to ensure a safe loop end
    sys.exit(app.exec_())



