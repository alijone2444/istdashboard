import networkx as nx
import matplotlib.pyplot as plt
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys


class ISBN(QMainWindow):
    value = []
    def __init__(self):
        super().__init__()
        self.resize(1000,640)
        self.setWindowTitle("password encryption")

        self.widget = QWidget(self)
        self.setCentralWidget(self.widget)
        self.gridlayout =QGridLayout(self.widget)

        self.label = QLabel("None",self)
        self.label.setStyleSheet("background-color:black;")
        self.label.setMaximumSize(1500,800)
        self.label.setAlignment(Qt.AlignCenter)


        self.movie = QMovie("loader.gif")
        self.label.setMovie(self.movie)
        self.label.setScaledContents(True)
        self.movie.setSpeed(200)
        self.movie.start()

        self.gridlayout.addWidget(self.label)
app = QApplication(sys.argv)
isbn = ISBN()
isbn.showMaximized()
app.exec()