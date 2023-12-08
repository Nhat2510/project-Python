from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QStackedWidget, QMessageBox,QTableWidgetItem
from PyQt6.uic import loadUi
import sys
import pyodbc as mdb

class MenuGV(QMainWindow):
    def __init__(self,widget):
        super(MenuGV, self).__init__()
        loadUi('menuGV.ui',self)
        self.widget = widget
        self.btn_view.clicked.connect(self.viewPoint)
        self.btn_update.clicked.connect(self.updatePoint)
        self.btn_change_password.clicked.connect(self.changePassword)
        self.logout.clicked.connect(self.out)
    def changePassword(self):
        self.widget.setCurrentIndex(9)
    def updatePoint(self):
        self.widget.setCurrentIndex(8)
    def viewPoint(self):
        self.widget.setCurrentIndex(5)
    def out(self):
        f = open('personDN.txt','w')
        f.write('')
        f.close()
        self.widget.setCurrentIndex(0)
    