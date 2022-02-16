'''
Lesson 84 停靠控件

QDockWidget

'''
import sys,qdarkstyle,os
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class DockDemo(QMainWindow):
    def __init__(self,parent=None):
        super(DockDemo,self).__init__(parent)

        self.setWindowTitle('停靠控件 (QDockWidget)')

        layout = QHBoxLayout()
        self.items = QDockWidget('Dockable',self)
        self.listWidget = QListWidget()
        self.filelist = os.listdir('H:/YOLOX-main/datasets/VOCdevkit/JPEGImages')
        for file in self.filelist:
            self.listWidget.addItem(str(file))
        # List 加入Dock
        self.items.setWidget(self.listWidget)
        self.setCentralWidget(QLineEdit())

        # self.items.setFloating(True)
        self.addDockWidget(Qt.RightDockWidgetArea,self.items)


if __name__ == '__main__':
    # create QApplication subject
    app = QApplication(sys.argv)
    # dark mode
    app.setStyleSheet(qdarkstyle.load_stylesheet())

    main = DockDemo()
    main.show()
    # into the main loop of the program,using exit to ensure a safe loop end
    sys.exit(app.exec_())