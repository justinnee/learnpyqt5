'''

信号与槽自动连接

on_objectname_signalname

on_okButton_clicked
'''
import sys,qdarkstyle
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class AutoSignalSlot(QWidget):
    def __init__(self):
        super(AutoSignalSlot, self).__init__()
        self.okButton = QPushButton("ok",self)
        self.okButton.setObjectName("okButton")

        layout = QHBoxLayout()
        layout.addWidget(self.okButton)
        self.setLayout(layout)
        QMetaObject.connectSlotsByName(self)
        # self.okButton.clicked.connect(self.on_okButton_clicked)

    @pyqtSlot()
    def on_okButton_clicked(self):
        print('点击了ok按钮')

if __name__ == '__main__':
    # create QApplication subject
    app = QApplication(sys.argv)
    # dark mode
    app.setStyleSheet(qdarkstyle.load_stylesheet())

    main = AutoSignalSlot()
    main.show()
    # into the main loop of the program,using exit to ensure a safe loop end
    sys.exit(app.exec_())

