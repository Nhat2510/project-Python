from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QStackedWidget, QMessageBox,QTableWidgetItem
from PyQt6.uic import loadUi
import sys
import pyodbc as mdb

class ChangePasswordGV(QMainWindow):
    connection_string = 'DRIVER={ODBC Driver 17 for SQL Server};SERVER=LAPTOP-RVCC8HD0;DATABASE=QLSVPY;UID=tuannhat;PWD=123123'
    db = mdb.connect(connection_string)
    def __init__(self,widget):
        super(ChangePasswordGV, self).__init__()
        loadUi('changePasswordGV.ui',self) 
        self.widget = widget
        self.confirm.clicked.connect(self.change)
        self.back.clicked.connect(self.back_f)

    def change(self):
        password = self.old.text()
        newPassword = self.new_2.text()
        reNewPassword = self.renew.text()
        query = self.db.cursor()
        f = open('personDN.txt','r')
        MaAC = f.read()
        query.execute("select  * from ACCOUNT where MaAC =? and pass =?",(MaAC,password))
        result = query.fetchone()
        if result is None:
            QMessageBox.information(self,"Mật khẩu","không chính xác")
            return
        if newPassword != reNewPassword:
            QMessageBox.information(self,"Mật khẩu","Không trùng khóp")
            return
        query.execute("Update ACCOUNT set pass = ? where MaAC =?",(reNewPassword,MaAC))
        query.commit()
        QMessageBox.information(self,"Mật khẩu","Đổi thành công")
    def back_f(self):
        self.widget.setCurrentIndex(7)
        self.old.setText("")
        self.new_2.setText("")
        self.renew.setText("")