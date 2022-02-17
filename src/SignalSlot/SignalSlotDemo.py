'''
Lesson 105
Signal & Slot
'''
import sys,qdarkstyle
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
class SignalSlotDemo(QWidget):
    def __init__(self):
        super(SignalSlotDemo,self).__init__()
        self.initUI()
        self.btn = QPushButton('我的按钮',self)
        self.btn.clicked.connect(self.onClick)

    def onClick(self):
        self.btn.setText('信号已经发出')
        self.btn.setStyleSheet("QPushButton{max-width:200px;min-width:200px}")

    def initUI(self):
        self.setGeometry(300,300,500,400)
        self.setWindowTitle('Signal & Slot')

if __name__ == '__main__':
    # create QApplication subject
    app = QApplication(sys.argv)
    # dark mode
    app.setStyleSheet(qdarkstyle.load_stylesheet())

    main = SignalSlotDemo()
    main.show()
    # into the main loop of the program,using exit to ensure a safe loop end
    sys.exit(app.exec_())

