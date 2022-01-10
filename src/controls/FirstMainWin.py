import sys
from PyQt5.QtWidgets import  QMainWindow,QApplication
from PyQt5.QtGui import QIcon
import qdarkstyle

class FirstMainWin(QMainWindow):
    def __init__(self,parent = None):
        super(FirstMainWin,self).__init__(parent)

        # set title of main window
        self.setWindowTitle('第一个主窗口应用')


        # set window size
        self.resize(400,300)

        self.status = self.statusBar()

        self.status.showMessage('只存在5秒的消息',5000)

if __name__ == '__main__':
    # create QApplication subject
    app = QApplication(sys.argv)
    # dark mode
    app.setStyleSheet(qdarkstyle.load_stylesheet())

    # QApplication.setWindowIcon set the main window & exe icon
    # it uses QMainWindow.setWindowIcon
    app.setWindowIcon(QIcon('./images/Siri.png'))
    main = FirstMainWin()
    main.show()

    # into the main loop of the program,using exit to ensure a safe loop end
    sys.exit(app.exec_())
