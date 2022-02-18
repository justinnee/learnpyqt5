'''
Lesson 124

QSS子控件选择器

QComboBox
'''
import sys,qdarkstyle
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt,QPoint
class QSSSubControl(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('QSS子控件选择器')
        combo = QComboBox(self)
        combo.setObjectName("myComboBox")
        combo.addItem("Windows")
        combo.addItem("Linux")
        combo.addItem("Mac OS X")

        combo.move(50,50)

        self.setGeometry(250,200,320,150)

if __name__ == '__main__':
    # create QApplication subject
    app = QApplication(sys.argv)
    # dark mode
    # app.setStyleSheet(qdarkstyle.load_stylesheet())

    main = QSSSubControl()
    qssStyle ='''
        QComboBox#myComboBox::drop-down{
            image:url(C:/Users/SYL/Pictures/20191204071629b17a9deb213c3991b077a796159b74dd.jpg.h700.jpg)
        }
        
    '''
    main.setStyleSheet(qssStyle)
    main.show()
    # into the main loop of the program,using exit to ensure a safe loop end
    sys.exit(app.exec_())