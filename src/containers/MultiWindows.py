'''

容纳多文档的窗口

QMdiArea

QMdiSubWindow

'''

import sys,qdarkstyle,os
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class MultiWindows(QMainWindow):
    count = 0
    def __init__(self,parent=None):
        super(MultiWindows,self).__init__(parent)

        self.setWindowTitle('容纳多文档的窗口')

        self.mdi = QMdiArea()
        self.setCentralWidget(self.mdi)
        bar = self.menuBar()
        file = bar.addMenu('File')
        file.addAction('New')
        file.addAction('cascade')
        file.addAction('Tiled')

        file.triggered.connect(self.windowaction)

    def windowaction(self,q):
        print(q.text())
        if q.text() == "New":
            MultiWindows.count = MultiWindows.count + 1
            sub = QMdiSubWindow()
            sub.setWidget(QTextEdit())
            sub.setWindowTitle('子窗口'+str(MultiWindows.count))
            self.mdi.addSubWindow(sub)
            sub.show()
        elif q.text() == "cascade":
            self.mdi.cascadeSubWindows()
        elif q.text() == 'Tiled':
            self.mdi.tileSubWindows()




if __name__ == '__main__':
    # create QApplication subject
    app = QApplication(sys.argv)
    # dark mode
    app.setStyleSheet(qdarkstyle.load_stylesheet())

    main = MultiWindows()
    main.show()
    # into the main loop of the program,using exit to ensure a safe loop end
    sys.exit(app.exec_())
