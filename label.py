from PyQt5.QtWidgets import *
import sys
from PyQt5 import QtGui
from PyQt5.QtCore import QRect
from PyQt5 import QtCore


class hi(QDialog):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Label")
        self.setGeometry(100,100,1000,100)
        self.setWindowIcon(QtGui.QIcon("home.jpg"))
        self.ji()

    def ji(self):
        vb=QVBoxLayout()
        l=QLabel("this is my label")  #label
        vb.addWidget(l)

        l1=QLabel("hi how are you!")
        l1.setFont(QtGui.QFont("Chiller",20)) #customize label
        vb.addWidget(l1)
        
        b=QPushButton("click me",self) #button
        vb.addWidget(b)

        
        self.setLayout(vb)
        self.show()


a=QApplication(sys.argv)
h=hi()
sys.exit(h.exec())



    
