'''
Lesson 106-107
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

    # 发送3个参数的信号
    sendmsg1 = pyqtSignal(str,int,int)

    def run(self):
        self.sendmsdg.emit('Hello PyQt5')

    def run1(self):
        self.sendmsg1.emit('Hello',3,4)


class MySlot(QObject):
    def get(self,msg):
        print('信息:'+msg)
    def get1(self,msg,a,b):
        print(msg)
        print(a+b)


if __name__ == '__main__':
    send = MyTypeSiganl()
    slot = MySlot()

    send.sendmsdg.connect(slot.get)
    send.sendmsg1.connect(slot.get1)
    send.run()
    send.run1()

    send.sendmsdg.disconnect(slot.get)
    send.run()

