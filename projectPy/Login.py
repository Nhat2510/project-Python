from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QStackedWidget, QMessageBox
from PyQt6 import QtCore
from PyQt6.uic import loadUi
import pyodbc as mdb
from PyQt6.QtCore import *


class Login_w(QMainWindow):
    def __init__(self, widget):
        super(Login_w, self).__init__()
        loadUi('Login.ui', self)
        self.btn_log.clicked.connect(self.login)
        self.widget = widget
    
    def login(self):
        un = self.txt_user.text()
        psw = self.txt_pass.text()
        connection_string = 'DRIVER={ODBC Driver 17 for SQL Server};SERVER=LAPTOP-RVCC8HD0;DATABASE=QLSVPY;UID=tuannhat;PWD=123123'
        db = mdb.connect(connection_string)
        query = db.cursor()
        query.execute("SELECT * FROM ACCOUNT WHERE username=? AND pass=?", (un, psw))
        result = query.fetchone()
        if result:
            query.execute("SELECT MaAC FROM ACCOUNT WHERE username=?", (un,))
            MaAC = query.fetchone()
            if MaAC and MaAC[0]:
                MaAC_names = MaAC[0].split(',')
                file=open('personDN.txt','w')
                file.write(MaAC_names[0])
                QMessageBox.information(self, "Login output", "Login success")
                self.widget.setCurrentIndex(2)
            else:
                QMessageBox.information(self, "Login output", "User has no roles assigned.")
        else:
            QMessageBox.information(self, "Login output", "Login fail")
            