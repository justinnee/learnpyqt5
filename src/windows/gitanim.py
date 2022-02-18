'''
Lesson 130
装载gif动画
QMovie

'''
import sys,qdarkstyle
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
class LoadingGif(QWidget):
    def __init__(self):
        super().__init__()
        self.label =QLabel("",self)
        self.setFixedSize(360,240)
        self.setWindowFlags(Qt.Dialog | Qt.CustomizeWindowHint)
        self.movie= QMovie(r"C:\Users\SYL\Pictures\1645162806775.gif")
        self.label.setMovie(self.movie)
        self.movie.start()

if __name__ == '__main__':
    # create QApplication subject
    app = QApplication(sys.argv)
    # dark mode
    app.setStyleSheet(qdarkstyle.load_stylesheet())

    main = LoadingGif()
    main.show()
    # into the main loop of the program,using exit to ensure a safe loop end
    sys.exit(app.exec_())

