from PyQt5.QtWidgets import QMainWindow,QApplication,QPushButton
import sys
from PyQt5 import QtGui
from PyQt5.QtCore import QRect
from PyQt5 import QtCore


class hi(QMainWindow):
    def __init__(self):
        super().__init__()

        self.top=100
        self.left=100
        self.width=200
        self.height=50
        iconName="home.jpg" #choose your images 

        self.setWindowTitle("Button")   #title
        self.setWindowIcon(QtGui.QIcon(iconName))#window icon
                                
        self.setGeometry(self.top,self.left,self.width,self.height)
        self.button()
        self.show()

    def button(self):
        b=QPushButton("click me",self)  #button
        b.setGeometry(QRect(2,10,60,30))#geometry
        b.setIcon(QtGui.QIcon("home.jpg"))  #icon for button
        b.setIconSize(QtCore.QSize(40,40))   #iconsize

                                                            

        
         
a=QApplication(sys.argv)
h=hi()
sys.exit(a.exec())
