'''
Lesson 68

在单元格中放置控件

'''
import sys
import qdarkstyle
import os
from PyQt5.QtWidgets import *

class PlaceControlInCell(QWidget):
    def __init__(self):
        super(PlaceControlInCell,self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('在单元格中放置控件')
        self.resize(430,300)
        layout = QHBoxLayout()
        tableWidget = QTableWidget()
        tableWidget.setRowCount(4)
        tableWidget.setColumnCount(3)

        layout.addWidget(tableWidget)

        tableWidget.setHorizontalHeaderLabels(['NAME','SEX','WEIGHT(kg)'])
        textItem = QTableWidgetItem('Jason')
        tableWidget.setItem(0,0,textItem)

        combox = QComboBox()
        combox.addItem('MAN')
        combox.addItem('WOMAN')

        #QSS
        combox.setStyleSheet('QComboBox{margin:3px};')
        tableWidget.setCellWidget(0,1,combox)

        modifyButton = QPushButton('修改')
        modifyButton.setDown(True)
        modifyButton.setStyleSheet('QPushButton{margin:3px};')
        tableWidget.setCellWidget(0,2,modifyButton)

        self.setLayout(layout)




if __name__ == '__main__':
    # create QApplication subject
    app = QApplication(sys.argv)
    # dark mode
    app.setStyleSheet(qdarkstyle.load_stylesheet())

    main = PlaceControlInCell()
    main.show()
    # into the main loop of the program,using exit to ensure a safe loop end
    sys.exit(app.exec_())
