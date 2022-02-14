'''
绘图API：绘制文本
1.文本
2.各种图形 直线、点、椭圆、弧、扇形、多边形等
3.图像

QPainter

painter = QPainter()

painter.begin()

painter.drawText(...)

painter.end()

必须在paintEvent事件方法中绘制各种元素
'''
import sys
from PyQt5.QtWidgets import QApplication,QWidget
from PyQt5.QtGui import QPainter,QColor,QFont
from PyQt5.QtCore import Qt
import qdarkstyle

class DrawText(QWidget):
    def __init__(self):
        super(DrawText,self).__init__()
        self.setWindowTitle('在窗口上绘制文本')
        self.resize(300,200)
        self.text = 'Python'
    def paintEvent(self,event):
        painter = QPainter(self)
        painter.begin(self)

        painter.setPen(QColor(150,43,5))
        painter.setFont(QFont('微软雅黑',25))

        painter.drawText(event.rect(),Qt.AlignCenter,self.text)

        painter.end()

if __name__ == '__main__':
    # create QApplication subject
    app = QApplication(sys.argv)
    # dark mode
    app.setStyleSheet(qdarkstyle.load_stylesheet())

    main = DrawText()
    main.show()

    # into the main loop of the program,using exit to ensure a safe loop end
    sys.exit(app.exec_())