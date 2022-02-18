import sys

from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

app = QApplication(sys.argv)
win = QMainWindow()
win.setWindowTitle("背景图片")
win.resize(350, 250)
win.setObjectName("MainWindow")

# 通过QPalette设置背景图片和背景颜色
# palette调色板
palette = QPalette()
# 设置画刷
palette.setBrush(QPalette.Background, QBrush(QPixmap("C:/Users/SYL/Pictures/20191204071629b17a9deb213c3991b077a796159b74dd.jpg.h700.jpg")))
palette.setColor(QPalette.Background,Qt.red)
win.setPalette(palette)

win.show()
sys.exit(app.exec())
