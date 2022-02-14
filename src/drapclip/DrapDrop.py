'''
让控件支持拖拽操作
A.setDrapEnabled(True)

B.setAcceptDrops(True)

B需要两个事件
1.dragEnterEvent    将A拖到B触发
2.dropEvent         在B区域放下A触发

'''
import sys,math
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class MyComboxBox(QComboBox):
    def __init__(self):
        super(MyComboxBox, self).__init__()
        self.setAcceptDrops(True)
    def dragEnterEvent(self, e):
        print(e)
        if e.mimeData().hasText():
            e.accept()
        else:
            e.ignore()

    def dropEvent(self, e):
        AllItems = [self.itemText(i) for i in range(self.count())]
        if e.mimeData().text() not in AllItems:
            self.addItem(e.mimeData().text())

class DrapDropDemo(QWidget):
    def __init__(self):
        super(DrapDropDemo, self).__init__()
        formLayout = QFormLayout()
        formLayout.addRow(QLabel('请将左边的文本拖拽到右边的下拉列表中'))
        lineEdit = QLineEdit()
        lineEdit.setDragEnabled(True)   #让QLineEdit控件可拖动

        combo = MyComboxBox()
        formLayout.addRow(lineEdit,combo)
        self.setLayout(formLayout)
        self.setWindowTitle('拖拽案例')

if __name__ == '__main__':
    # create QApplication subject
    app = QApplication(sys.argv)
    # dark mode
    # app.setStyleSheet(qdarkstyle.load_stylesheet())

    main = DrapDropDemo()
    main.show()

    # into the main loop of the program,using exit to ensure a safe loop end
    sys.exit(app.exec_())
