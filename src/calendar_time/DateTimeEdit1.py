'''
输入各种风格的日期和时间

QDateTimeEdit

'''
import qdarkstyle
import sys,math
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class DateTimeEdit1(QWidget):
    def __init__(self):
        super(DateTimeEdit1, self).__init__()
        self.initUI()

    def initUI(self):
        vlayout = QVBoxLayout()
        dateTimeEdit1 = QDateTimeEdit()
        dateTimeEdit2 = QDateTimeEdit(QDateTime.currentDateTime())
        dateTimeEdit1.setMinimumDate(QDate.currentDate().addDays(-365))
        dateTimeEdit1.setMaximumDate(QDate.currentDate().addDays(365))
        self.dateTimeEdit = dateTimeEdit1
        dateTimeEdit2.setCalendarPopup(True)

        dateEdit = QDateTimeEdit(QDate.currentDate())
        timeEdit = QDateTimeEdit(QTime.currentTime())

        dateTimeEdit1.setDisplayFormat("yyyy-MM-dd HH:mm:ss")
        dateTimeEdit2.setDisplayFormat("yyyy/MM/dd HH-mm-ss")

        dateEdit.setDisplayFormat("yyyy.MM.dd")
        timeEdit.setDisplayFormat("HH:mm:ss")


        dateTimeEdit1.dateChanged.connect(self.onDateChanged)
        dateTimeEdit1.timeChanged.connect(self.onTimeChanged)
        dateTimeEdit1.dateTimeChanged.connect(self.onDateTimeChanged)

        vlayout.addWidget(dateTimeEdit1)
        vlayout.addWidget(dateTimeEdit2)
        vlayout.addWidget(dateEdit)
        vlayout.addWidget(timeEdit)


        self.btn = QPushButton('获取日期和时间')

        vlayout.addWidget(self.btn)
        self.btn.clicked.connect(self.onButtonClick)
        self.setLayout(vlayout)

        self.resize(400,90)
        self.setWindowTitle('设置不同风格的日期和时间')

    def onDateChanged(self,date):
        print(date)

    def onTimeChanged(self,time):
        print(time)

    def onDateTimeChanged(self,datetime):
        print(datetime)

    def onButtonClick(self):
        dateTime = self.dateTimeEdit.dateTime()
        print(dateTime)

        #最大日期
        print(self.dateTimeEdit.maximumDate())

        #最大日期时间
        print(self.dateTimeEdit.maximumDateTime())

        #最小日期
        print(self.dateTimeEdit.minimumDate())

        #最小日期时间
        print(self.dateTimeEdit.minimumDateTime())

if __name__ == '__main__':
    # create QApplication subject
    app = QApplication(sys.argv)
    # dark mode
    app.setStyleSheet(qdarkstyle.load_stylesheet())

    main = DateTimeEdit1()
    main.show()

    # into the main loop of the program,using exit to ensure a safe loop end
    sys.exit(app.exec_())
