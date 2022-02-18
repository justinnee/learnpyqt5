'''
使用多种方式设置窗口背景色和背景图片
1.  QSS
2.  QPalette
3.  直接绘制
'''

import sys
from PyQt5.QtWidgets import *

app = QApplication(sys.argv)
win = QMainWindow()
win.setWindowTitle("背景图片")
win.resize(350, 250)
win.setObjectName("MainWindow")

# 通过QSS动态修改窗口的背景颜色和背景图片
win.setStyleSheet("#MainWindow{border-image:url(C:/Users/SYL/Pictures/20191204071629b17a9deb213c3991b077a796159b74dd.jpg.h700.jpg);}")
# win.setStyleSheet("#MainWindow{background-color:yellow}")

win.show()
sys.exit(app.exec())
