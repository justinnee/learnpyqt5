'''
Lesson 103
表单布局
'''

import sys,qdarkstyle
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
class FormForm(QWidget):
    def __init__(self):
        super(FormForm,self).__init__()
        self.setWindowTitle('表单布局')
        self.resize(350,300)

        formLayout = QFormLayout()

        titleLabel = QLabel('标题')
        authorLabel = QLabel('作者')
        contentLabel = QLabel('内容')

        titleEdit = QLineEdit()
        authorEdit = QLineEdit()
        contentEdit = QTextEdit()

        formLayout.addRow(titleLabel,titleEdit)
        formLayout.addRow(authorLabel,authorEdit)
        formLayout.addRow(contentLabel,contentEdit)

        self.setLayout(formLayout)

if __name__ == '__main__':
    # create QApplication subject
    app = QApplication(sys.argv)
    # dark mode
    app.setStyleSheet(qdarkstyle.load_stylesheet())

    main = FormForm()
    main.show()
    # into the main loop of the program,using exit to ensure a safe loop end
    sys.exit(app.exec_())
