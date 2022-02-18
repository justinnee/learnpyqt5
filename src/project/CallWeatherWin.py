import sys,qdarkstyle

import requests
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtSql import *
from WeatherWin import Ui_Form

class MainWindow(QMainWindow):
    def __init__(self,parent = None):
        super(MainWindow,self).__init__(parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)

    def queryWeather(self):
        cityName = self.ui.comboBox.currentIndex()
        cityCode = self.trans(cityName)

        rep = requests.get('http://www.weather.com.cn/data/sk/'+cityCode+'.html')
        rep.encoding = 'utf-8'
        print(rep.json())

        msg1 = '城市：%s' % rep.json()['weatherinfo']['city'] + '\n'
        msg2 = '风向：%s' % rep.json()['weatherinfo']['WD'] + '\n'

        result = msg1 + msg2
        self.ui.textBrowser.setText(result)

    def trans(self,cityName):
        cityCode = ''
        if cityName == '北京':
            cityCode = '101010100'
        elif cityName == '天津':
            cityCode = '101030100'
        elif cityName == '上海':
            cityCode = '101020100'

        return cityCode

    def clearResult(self):
        print('* clearResult   ')
        self.ui.textBrowser.clear()

if __name__ == '__main__':
    # create QApplication subject
    app = QApplication(sys.argv)
    # dark mode
    app.setStyleSheet(qdarkstyle.load_stylesheet())
    win = MainWindow()
    win.show()
    # into the main loop of the program,using exit to ensure a safe loop end
    sys.exit(app.exec_())