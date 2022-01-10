# _*_coding: UTF-8_*_
# 开发人员 : Justin Nee
# 开发时间 : 2022/1/7  10:48
# 文件名称 : QLabelDemo.py
# 开发工具 : PyCharm
"""
QLabel
setAlignment(): 设置文本的对齐方式
setIndent(): 设置文本缩进
text(): 获取文本内容
setBuddy():设置伙伴关系
setText(): 设置文本内容
selectedText(): 返回所选择的字符
setWordWrap(): 设置是否允许换行

signal:
1.  鼠标滑过：linkHovered
2.  鼠标单击：linkActivated

"""
import sys
from PyQt5.QtWidgets import QVBoxLayout,QMainWindow,QApplication,QLabel,QWidget
from PyQt5.QtGui import QFont,QIcon,QPalette,QPixmap
from PyQt5.QtCore import Qt
import qdarkstyle

class QLabelDemo(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        label1 = QLabel(self)
        label2 = QLabel(self)
        label3 = QLabel(self)
        label4 = QLabel(self)

        label1.setText("<font color=yellow>这是一个文本标签.</font>")
        label1.setAutoFillBackground(True)
        palette =QPalette()
        palette.setColor(QPalette.Window,Qt.blue)
        label1.setPalette(palette)
        label1.setAlignment(Qt.AlignCenter)

        label2.setText("<a href='#'>欢迎GUI</a>")

        label3.setAlignment(Qt.AlignCenter)
        label3.setToolTip('This is a picture label.')
        label3.setPixmap(QPixmap('./images/Siri.png'))

        label4.setText("<a href='https://item.jd.com/12417265.html'>感谢关注</a>")
        label4.setAlignment(Qt.AlignRight)
        label4.setToolTip('This is a website.')

        vbox = QVBoxLayout()
        vbox.addWidget(label1)
        vbox.addWidget(label2)
        vbox.addWidget(label3)
        vbox.addWidget(label4)

        label2.linkHovered.connect(self.linkHovered)

        label4.linkActivated.connect(self.linkClicked)

        self.setLayout(vbox)
        self.setWindowTitle('Qlabel Demo')

    def linkHovered(self):
        print('鼠标滑过label2')

    def linkClicked(self):
        print('鼠标按下label4')

if __name__ == '__main__':
    # create QApplication subject
    app = QApplication(sys.argv)
    # dark mode
    app.setStyleSheet(qdarkstyle.load_stylesheet())

    app.setWindowIcon(QIcon('./images/Siri.png'))
    main = QLabelDemo()
    main.show()

    # into the main loop of the program,using exit to ensure a safe loop end
    sys.exit(app.exec_())