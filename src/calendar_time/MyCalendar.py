'''
Lesson 56

日历控件
QCalendarWidget

'''
import qdarkstyle
import sys,math
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class MyCalendar(QWidget):
    def __init__(self):
        super(MyCalendar, self).__init__()
        self.initUI()

    def initUI(self):
        self.cal = QCalendarWidget(self)
        self.cal.setMinimumDate(QDate(1988,1,1))
        self.cal.setMaximumDate(QDate(2088,1,1))

        # self.cal.setGridVisible(True)
        self.cal.move(20,20)
        self.cal.clicked.connect(self.showDate)

        self.resize(400, 350)
        self.setWindowTitle('日历演示')

        self.label = QLabel(self)
        date = self.cal.selectedDate()
        self.label.setText(date.toString('yyyy-MM-dd dddd'))
        self.label.move(20,300)


    def showDate(self,date):
        self.label.setText((date.toString('yyyy-MM-dd dddd')))

if __name__ == '__main__':
    # create QApplication subject
    app = QApplication(sys.argv)
    # dark mode
    app.setStyleSheet(qdarkstyle.load_stylesheet())

    main = MyCalendar()
    main.show()

    # into the main loop of the program,using exit to ensure a safe loop end
    sys.exit(app.exec_())
