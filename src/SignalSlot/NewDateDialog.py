'''
多窗口交互（2）：使用信号与槽
如果一个窗口A与另一个窗口B交互，那么A尽量不要直接访问B的窗口中的控件
应该访问B中的信号，并指定与信号绑定的槽函数

例：如果A直接访问B窗口的控件，一旦B窗口控件发生改变，那么A和B的代码都需要发生变化
如果A访问B中信号，B中的控件发生了改变，只需要修改B中代码即可.

'''
import sys,qdarkstyle
from PyQt5.QtWidgets import *
from functools import partial
from PyQt5.QtGui import *
from PyQt5.QtCore import *
class NewDateDialog(QDialog):
    Signal_OneParameter = pyqtSignal(str)

    def __init__(self,parent=None):
        super(NewDateDialog, self).__init__(parent)
        self.setWindowTitle('SubWin:用来发射信号')

        layout = QVBoxLayout(self)

        self.label = QLabel(self)
        self.label.setText('前者发射内置信号\n后者发射自定义信号')
        layout.addWidget(self.label)

        self.datetime_inner = QDateTimeEdit(self)
        self.datetime_inner.setCalendarPopup(True)
        self.datetime_inner.setDateTime(QDateTime.currentDateTime())

        self.datetime_emit = QDateTimeEdit(self)
        self.datetime_emit.setCalendarPopup(True)
        self.datetime_emit.setDateTime(QDateTime.currentDateTime())

        layout.addWidget(self.datetime_inner)
        layout.addWidget(self.datetime_emit)
        #使用两个button分别连接accept和reject槽函数
        buttons = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel,Qt.Horizontal,self)
        buttons.accepted.connect(self.accept)
        buttons.rejected.connect(self.reject)

        layout.addWidget(buttons)

        self.datetime_emit.dateTimeChanged.connect(self.emit_signal)

    def emit_signal(self):
        date_str = self.datetime_emit.dateTime().toString()
        self.Signal_OneParameter.emit(date_str)





