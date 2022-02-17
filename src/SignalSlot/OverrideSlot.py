'''
Lesson 115

Override覆盖槽函数
'''

import sys,qdarkstyle
from PyQt5.QtWidgets import *
from functools import partial
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class OverrideSlot(QWidget):
    def __init__(self):
        super(OverrideSlot, self).__init__()
        self.setWindowTitle("Override覆盖槽函数")
    def keyPressEvent(self, e):
        if e.key() == Qt.Key_Escape:
            self.close()
        elif e.key() == Qt.Key_Alt:
            self.setWindowTitle("按下了Alt键")

if __name__ == '__main__':
    # create QApplication subject
    app = QApplication(sys.argv)
    # dark mode
    app.setStyleSheet(qdarkstyle.load_stylesheet())

    main = OverrideSlot()
    main.show()
    # into the main loop of the program,using exit to ensure a safe loop end
    sys.exit(app.exec_())