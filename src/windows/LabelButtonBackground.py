'''
Lesson 131
使用QSS为标签和按钮添加背景图
'''
import sys,qdarkstyle
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class LabelButtonBackground(QWidget):
    def __init__(self):
        super(LabelButtonBackground, self).__init__()
        label1 =QLabel(self)
        label1.setToolTip('这是一个文本标签')
        label1.setStyleSheet('QLabel{border-image:url(C:/Users/SYL/Pictures/image.png");}')

        btn1 = QPushButton(self)
        btn1.setObjectName('btn1')
        btn1.setMaximumSize(48,48)
        btn1.setMinimumSize(48,48)

        style = '''
            # btn1{
                border-radius:4px;
                background-image:url("C:/Users/SYL/Pictures/image.png");
            }
        
        '''
        btn1.setStyleSheet(style)

        vbox = QVBoxLayout()
        vbox.addWidget(label1)
        vbox.addStretch()
        vbox.addWidget(btn1)

        self.setLayout(vbox)
        self.setWindowTitle('使用QSS为标签和按钮添加背景图')

if __name__ == '__main__':
    # create QApplication subject
    app = QApplication(sys.argv)
    # dark mode
    app.setStyleSheet(qdarkstyle.load_stylesheet())

    main = LabelButtonBackground()
    main.show()
    # into the main loop of the program,using exit to ensure a safe loop end
    sys.exit(app.exec_())
