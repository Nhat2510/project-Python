from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QStackedWidget, QMessageBox
from PyQt6.uic import loadUi
from PyQt6.QtCore import *
from Login import Login_w

class ListFuture(QMainWindow):
    def __init__(self,widget):
        super(ListFuture, self).__init__()
        loadUi('login_success.ui', self)
        self.widget=widget
        self.btn_thsv.clicked.connect(self.addsv)
        self.btn_cnttsv.clicked.connect(self.updatesv)
        self.bth_khoatk.clicked.connect(self.blockAC)
        self.btn_logout.clicked.connect(self.logout)
    def addsv(self):
        self.widget.setCurrentIndex(3)

    def updatesv(self):
        self.widget.setCurrentIndex(4)
        
    def blockAC(self):
        self.widget.setCurrentIndex(5)
        
    def logout(self):
        self.widget.setCurrentIndex(1)
        
        