import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class Background1(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("绘制背景颜色")

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setBrush(Qt.yellow)
        painter.drawRect(self.rect())


if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = Background1()
    form.show()
    sys.exit(app.exec_())


