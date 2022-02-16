'''
让程序定时关闭

QTimer.singleShot
'''

import sys,qdarkstyle
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

if __name__ == '__main__':
    # create QApplication subject
    app = QApplication(sys.argv)

    # dark mode
    # app.setStyleSheet(qdarkstyle.load_stylesheet())

    label = QLabel('<font color=red size=140><b>Hello World,窗口在3秒后自动关闭！</b></font>')
    label.setWindowFlags(Qt.SplashScreen | Qt.FramelessWindowHint)
    label.show()
    QTimer.singleShot(3000, app.quit)

    # into the main loop of the program,using exit to ensure a safe loop end
    sys.exit(app.exec_())