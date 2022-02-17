'''
Lesson 111

多线程更新UI数据(在两个线程中传递数据)

'''
import time,sys,qdarkstyle
from PyQt5.QtCore import *
from PyQt5.QtWidgets import  *
class BackendThread(QThread):
    update_date = pyqtSignal(str)

    def run(self):
        while True:
            data = QDateTime.currentDateTime()
            currentTime = data.toString("yyyy-MM-dd hh:mm:ss")
            self.update_date.emit(str(currentTime))
            time.sleep(1)
class ThreadUpdateUI(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        self.setWindowTitle('多线程更新UI数据')
        self.resize(400,100)
        self.input = QLineEdit(self)
        self.input.resize(400,100)

        self.initUI()

    def initUI(self):
        self.backend = BackendThread()
        self.backend.update_date.connect(self.handleDisplay)

        self.backend.start()

    def handleDisplay(self,data):
        self.input.setText(data)

if __name__ == '__main__':
    # create QApplication subject
    app = QApplication(sys.argv)
    # dark mode
    app.setStyleSheet(qdarkstyle.load_stylesheet())

    main = ThreadUpdateUI()
    main.show()
    # into the main loop of the program,using exit to ensure a safe loop end
    sys.exit(app.exec_())


