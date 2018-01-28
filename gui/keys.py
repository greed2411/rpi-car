from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget
from PyQt5.uic import loadUiType
from PyQt5.QtWidgets import QApplication
import sys

Ui_MainWindow, QMainWindow = loadUiType('gui.ui')

"""class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self, parent=parent)
        self.setupUi(self)

    def keyPressEvent(self, e):
        if e.key() == Qt.Key_F5:
            self.close()




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    w = MainWindow()
    w.show()
    sys.exit(app.exec_())"""


class Main(QMainWindow, Ui_MainWindow):
    def __init__(self,):
        super(Main,self).__init__()
        self.setupUi(self)
    def keyPressEvent(self, e):
        #print(e)
        if e.key() == Qt.Key_W:
            print("Key_UP")
        if e.key() == Qt.Key_S:
            print("Key_DOWN")
        if e.key() == Qt.Key_D:
            print("Key_RIGHT")
        if e.key() == Qt.Key_A:
            print("Key_LEFT")
        if e.key() == Qt.Key_Space:
            print("Key_Break")

if __name__ == '__main__' :
    app=QApplication(sys.argv)
    main = Main()
    main.show()
    sys.exit(app.exec_())
