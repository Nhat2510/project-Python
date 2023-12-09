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
        self.back.clicked.connect(self.back_f)
        self.widget = widget
    
    def back_f(self):
        self.txt_user.clear()
        self.txt_pass.clear()
        self.widget.setCurrentIndex(0)
    
    def login(self):
        un = self.txt_user.text()
        psw = self.txt_pass.text()
        connection_string = 'DRIVER={ODBC Driver 17 for SQL Server};SERVER=LAPTOP-RVCC8HD0;DATABASE=QLSVPY;UID=tuannhat;PWD=123123'
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
                QMessageBox.information(self, "Thông báo", "Đăng nhập thành công")
                self.txt_user.clear()
                self.txt_pass.clear()
                if MaAC[1] =='admin':
                    self.widget.setCurrentIndex(2)
                else:
                    self.widget.setCurrentIndex(7)
                    
            else:
                QMessageBox.information(self, "Thông báo", "Người dùng không có vai trò nào được chỉ định.")
        else:
            QMessageBox.information(self, "Thông báo", "Đăng nhập thất bại")
            self.txt_user.clear()
            self.txt_pass.clear()
            