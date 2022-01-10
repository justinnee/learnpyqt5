# _*_coding: UTF-8_*_
# 开发人员 : Justin Nee
# 开发时间 : 2022/1/5  16:05
# 文件名称 : IconForm.py
# 开发工具 : PyCharm
import sys
from PyQt5.QtWidgets import  QMainWindow,QApplication
from PyQt5.QtGui import QIcon
import qdarkstyle

class IconForm(QMainWindow):
    def __init__(self,parent = None):
        super(IconForm,self).__init__(parent)
        self.initUI()

    def initUI(self):

        self.setGeometry(300,300,250,250)
        # set title of main window
        self.setWindowTitle('Set Icon')
        # set window icon
        self.setWindowIcon(QIcon('./images/Siri.png'))

if __name__ == '__main__':
    # create QApplication subject
    app = QApplication(sys.argv)
    # dark mode
    app.setStyleSheet(qdarkstyle.load_stylesheet())

    main = IconForm()
    main.show()

    # into the main loop of the program,using exit to ensure a safe loop end
    sys.exit(app.exec_())