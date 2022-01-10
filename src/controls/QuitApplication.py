# _*_coding: UTF-8_*_
# 开发人员 : Justin Nee
# 开发时间 : 2022/1/5  15:10
# 文件名称 : QuitApplication.py
# 开发工具 : PyCharm
import sys
import qdarkstyle
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QHBoxLayout,QMainWindow,QApplication,QPushButton,QWidget

class QuitApplication(QMainWindow):
    def __init__(self):
        super(QuitApplication,self).__init__()
        self.resize(300,120)
        self.setWindowTitle('退出应用程序')

        # add button

        self.button1 = QPushButton('退出应用程序')
        # connect signal & slot
        self.button1.clicked.connect(self.onClick_Button)

        # Horizontal layout
        layout = QHBoxLayout()
        layout.addWidget(self.button1)

        mainFrame = QWidget()
        mainFrame.setLayout(layout)

        self.setCentralWidget(mainFrame)

    # method of clicking on the button (customized slot)
    def onClick_Button(self):
        sender = self.sender()
        print(sender.text()+'按钮被按下')
        app = QApplication.instance()

        # # dark mode
        # app.setStyleSheet(qdarkstyle.load_stylesheet())

        # quit app
        app.quit()

if __name__ == '__main__':
    # create QApplication subject
    app = QApplication(sys.argv)
    # dark mode
    app.setStyleSheet(qdarkstyle.load_stylesheet())

    app.setWindowIcon(QIcon('./images/Siri.png'))
    main = QuitApplication()
    main.show()

    # into the main loop of the program,using exit to ensure a safe loop end
    sys.exit(app.exec_())
