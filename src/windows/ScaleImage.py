'''
缩放图片
QImage.scaled

'''
import sys,qdarkstyle
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class ScaleImage(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('缩放图片')
        filename = "C:/Users/SYL/Pictures/f0Q5-89ufXbZ2yT3cSzk-n6.jpg"
        img = QImage(filename)
        label1 = QLabel(self)
        label1.setFixedWidth(200)
        label1.setFixedHeight(200)

        result = img.scaled(label1.width(),label1.height(),Qt.IgnoreAspectRatio,Qt.SmoothTransformation)
        # result = img.scaled(label1.width(), label1.height())
        label1.setPixmap(QPixmap.fromImage(result))

        vbox = QVBoxLayout()
        vbox.addWidget(label1)

        self.setLayout(vbox)

if __name__ == '__main__':
    # create QApplication subject
    app = QApplication(sys.argv)
    # dark mode
    app.setStyleSheet(qdarkstyle.load_stylesheet())

    main = ScaleImage()
    main.show()
    # into the main loop of the program,using exit to ensure a safe loop end
    sys.exit(app.exec_())


