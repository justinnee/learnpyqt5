# QDesktopWidget
import sys
from PyQt5.QtWidgets import  QDesktopWidget,QMainWindow,QApplication
from PyQt5.QtGui import QIcon
import qdarkstyle

class CenterForm(QMainWindow):
    def __init__(self,parent = None):
        super(CenterForm,self).__init__(parent)

        # set title of main window
        self.setWindowTitle('让窗口居中')

        # set window size
        self.resize(400,300)
        self.center()

    def center(self):
        # get screen coordinate system
        screen = QDesktopWidget().screenGeometry()
        # get window coordinate system
        size = self.geometry()
        newLeft = int((screen.width()-size.width()) / 2)
        newTop = int((screen.height()-size.height()) / 2)
        self.move(newLeft,newTop)


if __name__ == '__main__':
    # create QApplication subject
    app = QApplication(sys.argv)
    # dark mode
    app.setStyleSheet(qdarkstyle.load_stylesheet())

    app.setWindowIcon(QIcon('./images/Siri.png'))
    main = CenterForm()
    main.show()

    # into the main loop of the program,using exit to ensure a safe loop end
    sys.exit(app.exec_())