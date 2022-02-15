'''
Lesson 62
使用打印机  -> pdf
'''
from PyQt5 import QtGui,QtWidgets,QtPrintSupport
from PyQt5.QtWidgets import *
import sys
import qdarkstyle

class PrintSupport(QMainWindow):
    def __init__(self):
        super(PrintSupport,self).__init__()
        self.setGeometry(500,200,300,300)
        self.button = QPushButton('打印QTextEdit控件中的内容',self)
        self.button.setGeometry(20,20,260,30)
        self.editor = QTextEdit('默认文本',self)
        self.editor.setGeometry(20,60,260,200)

        self.button.clicked.connect(self.print)

    def print(self):
        printer = QtPrintSupport.QPrinter()
        painter = QtGui.QPainter()

        painter.begin(printer)
        screen = self.editor.grab()
        painter.drawPixmap(10,10,screen)
        painter.end()
if __name__ == '__main__':
    # create QApplication subject
    app = QApplication(sys.argv)
    # dark mode
    app.setStyleSheet(qdarkstyle.load_stylesheet())

    gui = PrintSupport()
    gui.show()

    # into the main loop of the program,using exit to ensure a safe loop end
    sys.exit(app.exec_())