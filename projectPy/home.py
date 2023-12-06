from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QStackedWidget, QMessageBox
from PyQt6 import QtCore
from PyQt6.uic import loadUi
import pyodbc as mdb
from PyQt6.QtCore import *

class Home_w(QMainWindow):
    def __init__(self,widget):
        super(Home_w, self).__init__()
        loadUi('Home.ui', self)
        self.b2.clicked.connect(self.admin)
        self.widget = widget
    def admin(self):
        self.widget.setCurrentIndex(1)
