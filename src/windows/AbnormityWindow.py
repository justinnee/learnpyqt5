'''
Lesson 127
实现不规则窗口
（通过mask实现异形窗口）
需要一张透明的png图，透明部分被扣出，形成一个非矩形区域

'''
import sys,qdarkstyle
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt,QPoint
class AbnormityWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('实现不规则窗口')
        self.pix = QBitmap(r"C:\Users\SYL\Pictures\image.png")
        self.setMask(self.pix)

    def paintEvent(self, QPaintEvent):
        painter = QPainter(self)
        painter.drawPixmap(0,0,self.pix.width(),self.pix.height(),QPixmap(r"C:\Users\SYL\Pictures\image.png"))

if __name__ == '__main__':
    # create QApplication subject
    app = QApplication(sys.argv)
    # dark mode
    app.setStyleSheet(qdarkstyle.load_stylesheet())

    main = AbnormityWindow()
    main.show()
    # into the main loop of the program,using exit to ensure a safe loop end
    sys.exit(app.exec_())