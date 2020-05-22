from PyQt5.QtWidgets import QMainWindow,QApplication
import sys

class hi(QMainWindow):
    def __init__(self):
        super().__init__()

        self.top=100
        self.left=100
        self.width=200
        self.height=50
        self.ne()

    def ne(self):
        self.setWindowTitle("simple window")
        self.setGeometry(self.top,self.left,self.width,self.height)
        self.show()

                                                            

        
         
a=QApplication(sys.argv)
h=hi()
sys.exit(a.exec())
