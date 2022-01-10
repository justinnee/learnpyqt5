import sys
import MainWindowVerticalLayout
import qdarkstyle
from PyQt5.QtWidgets import QApplication,QMainWindow

if __name__ == '__main__':
    # create QApplication subject
    app = QApplication(sys.argv)
    # dark mode
    app.setStyleSheet(qdarkstyle.load_stylesheet())

    # main window
    mainWindow = QMainWindow()
    ui = MainWindowVerticalLayout.Ui_MainWindow()
    # add widgets on main window
    ui.setupUi(mainWindow)
    mainWindow.show()

    # into the main loop of the program,using exit to ensure a safe loop end
    sys.exit(app.exec_())