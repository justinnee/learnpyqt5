import sys
import qdarkstyle
from PyQt5.QtWidgets import QApplication,QWidget

if __name__ == '__main__':
    # create QApplication subject
    app = QApplication(sys.argv)
    # dark mode
    app.setStyleSheet(qdarkstyle.load_stylesheet())

    # create a window
    w =QWidget()
    w.resize(300,150)
    w.move(300,300)

    # set the label of the window
    w.setWindowTitle('first desktop app based on pyqt5')
    # show the window
    w.show()

    # into the main loop of the program,using exit to ensure a safe loop end
    sys.exit(app.exec_())
