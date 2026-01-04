#===========================PyQt5 introduction=====================
import sys
from PyQt5.QtWidgets import QApplication,QMainWindow,QLabel
from PyQt5.QtGui import QIcon,QFont
from PyQt5.QtCore import Qt


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        #self.setWindowTitle("My cool first window")
        self.setGeometry(700,500,500,600)
        #self.setWindowIcon(QIcon("ok.jpeg"))
        label = QLabel("hi, This is Milan",self)
        label.setFont(QFont("Arial",40))
        label.setGeometry(0,0,500,600)
        label.setStyleSheet("color: purple; background-color: blue;" \
        " font-weight:bold; ; font-style:italic; text-decoration:underline")
        #label.setAlignment(Qt.AlignTop) #Vertically Top 
        #label.setAlignment(Qt.AlignBottom) #Vertically Bottom
        #label.setAlignment(Qt.AlignVCenter)  #Vertically center
        #label.setAlignment(Qt.AlignRight) #Horizontally center
        #label.setAlignment(Qt.AlignHCenter) 
        #label.setAlignment(Qt.AlignHCenter | Qt.AlignBottom) #Center and Bottom
        #label.setAlignment(Qt.AlignVCenter | Qt.AlignTop) # Center and Top
        label.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)




def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

if __name__=="__main__":
    main()