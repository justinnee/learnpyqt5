# _*_coding: UTF-8_*_
# 开发人员 : Justin Nee
# 开发时间 : 2022/1/8  11:10
# 文件名称 : QSliderDemo.py
# 开发工具 : PyCharm
"""
滑块控件
"""
import sys
import qdarkstyle
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class QSliderDemo(QWidget):
    def __init__(self):
        super(QSliderDemo, self).__init__()
        self.initUI()
    def initUI(self):
        self.setWindowTitle('滑块控件演示')
        self.resize(300,100)

        layout = QVBoxLayout()
        self.label = QLabel('Hello PyQt5')
        self.label.setAlignment(Qt.AlignCenter)

        layout.addWidget(self.label)

        self.slider = QSlider(Qt.Vertical)

        # set minimum & maximum
        self.slider.setMinimum(12)
        self.slider.setMaximum(48)
        # set step
        self.slider.setSingleStep(1)

        # set current value
        self.slider.setValue(18)

        # 设置刻度位置 & 间隔
        self.slider.setTickPosition(QSlider.TicksBelow)
        self.slider.setTickInterval(3)

        layout.addWidget(self.slider)
        self.slider.valueChanged.connect(self.valueChange)

        self.slider1 = QSlider()
        layout.addWidget(self.slider1)

        self.setLayout(layout)

    def valueChange(self):
        print('Current: %s' % self.slider.value())
        size = self.slider.value()
        self.label.setFont(QFont('Arial',size))

if __name__ == '__main__':
    # create QApplication subject
    app = QApplication(sys.argv)
    # dark mode
    app.setStyleSheet(qdarkstyle.load_stylesheet())

    main = QSliderDemo()
    main.show()

    # into the main loop of the program,using exit to ensure a safe loop end
    sys.exit(app.exec_())
