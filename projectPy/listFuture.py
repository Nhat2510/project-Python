from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QStackedWidget, QMessageBox
from PyQt6.uic import loadUi
from PyQt6.QtCore import *
from Login import Login_w

class ListFuture(QMainWindow):
    def __init__(self,widget):
        super(ListFuture, self).__init__()
        loadUi('ListFuture.ui', self)
        self.widget=widget
        self.btnCreatetk.clicked.connect(self.taoTK)
        self.btn_thsv.clicked.connect(self.addsv)
        self.btn_cnttsv.clicked.connect(self.updatesv)
        self.bth_khoatk.clicked.connect(self.khoatk)
        self.btn_view_all_sv.clicked.connect(self.viewAllPoints)
        self.btn_logout.clicked.connect(self.logout)
    def logout(self):
        self.widget.setCurrentIndex(1)
    def addsv(self):
        self.widget.setCurrentIndex(3)
    def updatesv(self):
        self.widget.setCurrentIndex(4)
    def taoTK(self):
        self.widget.setCurrentIndex(11)
    def khoatk(self):
        self.widget.setCurrentIndex(12)    
    def viewAllPoints(self):
        self.widget.setCurrentIndex(6)
    
        
    
        