'''
像素点绘制正弦曲线
-2pi 2pi
drawPoint(x,y)
'''

import sys,math
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt
import qdarkstyle
class DrawPoints(QWidget):
    def __init__(self):
        super(DrawPoints, self).__init__()
        self.resize(300,300)
        self.setWindowTitle('在窗口上用像素点绘制2个周期的正弦曲线')

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.begin(self)

        painter.setPen(Qt.blue)
        size = self.size()

        for i in range(1000):
            x = 100 * (-1+2.0*i/1000)+size.width()/2.0
            y = -50 * math.sin((x-size.width()/2.0)*math.pi/50)+size.height()/2.0
            painter.drawPoint(x,y)

        painter.end()

if __name__ == '__main__':
    # create QApplication subject
    app = QApplication(sys.argv)
    # dark mode
    app.setStyleSheet(qdarkstyle.load_stylesheet())

    main = DrawPoints()
    main.show()

    # into the main loop of the program,using exit to ensure a safe loop end
    sys.exit(app.exec_())