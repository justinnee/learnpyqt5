# _*_coding: UTF-8_*_
# 开发人员 : Justin Nee
# 开发时间 : 2022/1/7  10:32
# 文件名称 : Tooltip.py
# 开发工具 : PyCharm
# 显示控件提示信息
import sys
from PyQt5.QtWidgets import QHBoxLayout,QMainWindow,QApplication,QToolTip,QPushButton,QWidget
from PyQt5.QtGui import QFont,QIcon
import qdarkstyle

class TooltipForm(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        QToolTip.setFont(QFont('SansSerif',12))
        self.setToolTip('Today is<b>Friday</b>')
        self.setGeometry(300,300,200,300)
        self.setWindowTitle('Set Tooltip Message')

        # add button
        self.button1 = QPushButton('My Button')
        self.button1.setToolTip('This is a button')

        # Horizontal layout
        layout = QHBoxLayout()
        layout.addWidget(self.button1)

        mainFrame = QWidget()
        mainFrame.setLayout(layout)
        self.setCentralWidget(mainFrame)
if __name__ == '__main__':
    # create QApplication subject
    app = QApplication(sys.argv)
    # dark mode
    app.setStyleSheet(qdarkstyle.load_stylesheet())

    app.setWindowIcon(QIcon('./images/Siri.png'))
    main = TooltipForm()
    main.show()

    # into the main loop of the program,using exit to ensure a safe loop end
    sys.exit(app.exec_())