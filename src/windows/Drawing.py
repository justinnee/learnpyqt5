'''
Lesson 121

项目实战 实现绘图应用
1.如何绘图
    paintEvent方法中绘图，调用update方法触发paintEvent的调用
2.哪里绘图
    白色背景的QPixmap对象中绘图
3.如何通过移动鼠标进行绘图
    （1）鼠标按下
    （2）鼠标移动
    （3）鼠标释放
'''
import sys,qdarkstyle
from PyQt5.QtWidgets import QApplication,QWidget
from PyQt5.QtGui import QPainter,QPixmap
from PyQt5.QtCore import Qt,QPoint
class Drawing(QWidget):
    def __init__(self,parent = None):
        super(Drawing,self).__init__(parent)
        self.setWindowTitle('绘图应用')
        self.pix = QPixmap()
        self.lastPoint = QPoint()
        self.endPoint = QPoint()
        self.initUI()

    def initUI(self):

        self.resize(600,600)
        # 画布大小为400*400 白色背景
        self.pix = QPixmap(600,600)
        self.pix.fill(Qt.white)

    def paintEvent(self,event):
        pp = QPainter(self.pix)
        pp.drawLine(self.lastPoint,self.endPoint)
        self.lastPoint = self.endPoint
        painter = QPainter(self)
        painter.drawPixmap(0,0,self.pix)

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.lastPoint = event.pos()

    def mouseMoveEvent(self, event):
        if event.buttons() and Qt.LeftButton:
            self.endPoint = event.pos()
            self.update()

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.endPoint = event.pos()
            self.update()

if __name__ == '__main__':
    # create QApplication subject
    app = QApplication(sys.argv)
    # dark mode
    app.setStyleSheet(qdarkstyle.load_stylesheet())

    main = Drawing()
    main.show()
    # into the main loop of the program,using exit to ensure a safe loop end
    sys.exit(app.exec_())



