'''

自定义信号
pyqtSignal()

'''
import sys,qdarkstyle
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
class MyTypeSiganl(QObject):
    # 定义一个信号
    sendmsdg = pyqtSignal(object)

    def run(self):
        self.sendmsdg.emit('Hello PyQt5')

class MySlot(QObject):
    def get(self,msg):
        print('信息:'+msg)


if __name__ == '__main__':
    send = MyTypeSiganl()
    slot = MySlot()

    send.sendmsdg.connect(slot.get)

    send.run()

