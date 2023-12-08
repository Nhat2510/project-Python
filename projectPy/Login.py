from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QStackedWidget, QMessageBox
from PyQt6 import QtCore
from PyQt6.uic import loadUi
import pyodbc as mdb
from PyQt6.QtCore import *
import os


class Login_w(QMainWindow):
    def __init__(self, widget):
        super(Login_w, self).__init__()
        loadUi('Login.ui', self)
        self.btn_log.clicked.connect(self.login)
        self.widget = widget
    
    def login(self):
        un = self.txt_user.text()
        psw = self.txt_pass.text()
        connection_string = 'DRIVER={ODBC Driver 17 for SQL Server};SERVER=LAPTOP-2A8I63E5\SQLEXPRESS;DATABASE=QLSVPY;UID=thanhan123;PWD=123456'
        db = mdb.connect(connection_string)
        query = db.cursor()
        query.execute("SELECT * FROM ACCOUNT WHERE username=? AND pass=?", (un, psw))
        result = query.fetchone()
        if result:
            query.execute("SELECT MaAC,roles FROM ACCOUNT WHERE username=?", (un,))
            MaAC = query.fetchone()
            if MaAC and MaAC[0]:
                MaAC_names = MaAC[0].split(',')
                with open('personDN.txt','w+') as file:
                    file.write(MaAC_names[0])
                    file.flush()
                    os.fsync(file.fileno())
                    file.close()
                QMessageBox.information(self, "Login output", "Login success")
                if(MaAC[1] == 'admin'):
                    self.widget.setCurrentIndex(2)
                else:
                    self.widget.setCurrentIndex(7)
            else:
                QMessageBox.information(self, "Login output", "User has no roles assigned.")
        else:
            QMessageBox.information(self, "Login output", "Login fail")
            