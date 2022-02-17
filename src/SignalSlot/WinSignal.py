'''
Lesson 110

为窗口类添加信号

'''

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import sys,qdarkstyle

class WinSignal(QWidget):

    button_clicked_signal = pyqtSignal()

    def __init__(self):
        super(WinSignal,self).__init__()
        self.setWindowTitle('为窗口类添加信号')
        self.resize(300,100)

        btn = QPushButton('关闭窗口',self)

        btn.clicked.connect(self.btn_clicked)
        self.button_clicked_signal.connect(self.btn_close)

    def btn_clicked(self):
        self.button_clicked_signal.emit()

    def btn_close(self):
        self.close()

if __name__ == '__main__':

    # create QApplication subject
    app = QApplication(sys.argv)
    # dark mode
    app.setStyleSheet(qdarkstyle.load_stylesheet())

    main = WinSignal()
    main.show()
    # into the main loop of the program,using exit to ensure a safe loop end
    sys.exit(app.exec_())

