# _*_coding: UTF-8_*_
# 开发人员 : Justin Nee
# 开发时间 : 2022/1/5  15:29
# 文件名称 : ScreenGeometry.py
# 开发工具 : PyCharm
import sys
import qdarkstyle
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QHBoxLayout,QMainWindow,QApplication,QPushButton,QWidget

app = QApplication(sys.argv)
# dark mode
app.setStyleSheet(qdarkstyle.load_stylesheet())

def onClick_Button():
    # x,y calculate started from the title bar
    print('1')
    print('widget.x() = %d' % widget.x())           # 250 窗口横坐标
    print('widget.y() = %d' % widget.y())           # 200 窗口纵坐标
    print('widget.width() = %d' % widget.width())   # 300 工作区宽度
    print('widget.height() = %d' % widget.height()) # 240 工作区高度

    # x,y calculate started from the true content
    print('2')
    print('widget.geometry().x() = %d' % widget.geometry().x())             # 251 工作区横坐标
    print('widget.geometry().y() = %d' % widget.geometry().y())             # 252 工作区纵坐标
    print('widget.geometry().width() = %d' % widget.geometry().width())     # 300 工作区宽度
    print('widget.geometry().height() = %d' % widget.geometry().height())   # 240 工作区宽度

    # x,y calculate started from the title bar
    # width,height contains the title bar
    print('3')
    print('widget.frameGeometry().x() = %d' % widget.frameGeometry().x())           # 250 窗口横坐标
    print('widget.frameGeometry().y() = %d' % widget.frameGeometry().y())           # 200 窗口纵坐标
    print('widget.frameGeometry().width() = %d' % widget.frameGeometry().width())   # 302 窗口宽度
    print('widget.frameGeometry().height() = %d' % widget.frameGeometry().height()) # 293 窗口高度

widget = QWidget()
btn = QPushButton(widget)
btn.setText('Button')
btn.clicked.connect(onClick_Button)
btn.move(24,52)

widget.resize(300,240)

widget.move(250,200)

widget.setWindowTitle('Screen Geometry')

widget.show()

sys.exit(app.exec_())

