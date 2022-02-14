'''
绘制各种图形

多边形
'''
import sys,math
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import qdarkstyle
class DrawAll(QWidget):
    def __init__(self):
        super(DrawAll, self).__init__()
        self.resize(300,600)
        self.setWindowTitle('绘制各种图形')

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)

        qp.setPen(Qt.white)

        #绘制弧
        rect = QRect(0,10,100,100)
        # alen:一个alen 1/16°
        qp.drawArc(rect,0,200*16)
        # 通过弧绘制圆
        qp.setPen(Qt.red)
        qp.drawArc(120,10,100,100,0,360*16)
        # 绘制带弦的弧
        qp.drawChord(10,120,100,100,12,130*16)
        #绘制扇形
        qp.drawPie(10,240,100,100,12,130*16)
        #绘制椭圆
        qp.drawEllipse(120,120,150,50)

        #绘制5边形

        p1 = QPoint(140, 380)
        p2 = QPoint(270, 420)
        p3 = QPoint(290, 512)
        p4 = QPoint(290, 588)
        p5 = QPoint(200, 533)

        polygon = QPolygon([p1,p2,p3,p4,p5])
        qp.drawPolygon(polygon)


        #绘制图像
        image = QImage('./images/c8.jpg')
        rect = QRect(100,400,image.width()/8,image.height()/8)
        qp.drawImage(rect,image)

        qp.end()
if __name__ == '__main__':
    # create QApplication subject
    app = QApplication(sys.argv)
    # dark mode
    app.setStyleSheet(qdarkstyle.load_stylesheet())

    main = DrawAll()
    main.show()

    # into the main loop of the program,using exit to ensure a safe loop end
    sys.exit(app.exec_())