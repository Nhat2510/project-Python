from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QStackedWidget, QMessageBox
from PyQt6.uic import loadUi
from PyQt6.QtCore import *

class ListFuture(QMainWindow):
    def __init__(self,widget):
        super(ListFuture, self).__init__()
        loadUi('login_success.ui', self)
        self.widget=widget
        self.btn_thsv.clicked.connect(self.addsv)
        self.btn_cnttsv.clicked.connect(self.updatesv)
        self.btn_view_all_sv.clicked.connect(self.viewAllStudent)
    def addsv(self):
        self.widget.setCurrentIndex(3)
    def updatesv(self):
        self.widget.setCurrentIndex(4)
    def viewAllStudent(self):
        self.widget.setCurrentIndex(6)
        