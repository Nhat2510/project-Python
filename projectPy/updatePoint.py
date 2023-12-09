from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QStackedWidget, QMessageBox,QTableWidgetItem
from PyQt6.uic import loadUi
from PyQt6.QtCore import *
import pyodbc as mdb
import datetime

class UpdatePoint(QMainWindow):
    connection_string = 'DRIVER={ODBC Driver 17 for SQL Server};SERVER=LAPTOP-RVCC8HD0;DATABASE=QLSVPY;UID=tuannhat;PWD=123123'
    db = mdb.connect(connection_string)
    Masv = ''
    def __init__(self,widget):
        super(UpdatePoint, self).__init__()
        self.widget = widget
        loadUi('updatePoint.ui',self)
        self.btn_search.clicked.connect(self.find)
        self.btn_update.clicked.connect(self.update)
        self.btn_back.clicked.connect(self.back)
    def back(self):
        self.text_name.clear()
        self.text_birthday.setDate(QDate.currentDate())
        self.text_grade.clear()
        self.text_msv.clear()
        self.group_up.setEnabled(False)
        self.widget.setCurrentIndex(7)
    def showEvent(self, event):
        self.Mamon = self.subjectID()
    def find(self):
        masv = self.text_msv.text()
        query = self.db.cursor()
        query.execute("""
            SELECT SV.MaSV,TEN, NgaySinh, Diem FROM SINHVIEN SV INNER JOIN DIEM D ON D.MaSV = SV.MaSV WHERE SV.MaSV = ?  and MaMon =?        
        """,(masv,self.Mamon))
        result = query.fetchone()  
        print(result[2])
        if(result != None):
            self.Masv = result[0]
            self.text_name.setText(result[1])
            self.text_birthday.setDate(QDate(result[2].date()))
            self.text_grade.setText(str(result[3]))
            self.group_up.setEnabled(True)
        else:
            self.text_name.setText('')
            self.text_birthday.setDate(QDate.currentDate())
            self.text_grade.setText('')
            QMessageBox.information(self,"Lỗi Ma SV","Không tìm thấy")
            self.group_up.setEnabled(False)
    def update(self):
        grade = self.text_grade.text()
        if(str(grade).isdigit()):
            if int(grade)>10 or int(grade)<0:
                QMessageBox.information(self,"Lỗi điểm","Mời nhập lại điểm")
                return
            else:
                query = self.db.cursor()
                query.execute("""
                Update DIEM SET Diem = ? where MaSV = ? AND MaMon =?           
                """,(int(grade),self.Masv,self.Mamon))
                query.commit()
                QMessageBox.information(self,"Cập nhật điểm","Thành công")
        else:
             QMessageBox.information(self,"Lỗi điểm","Mời nhập lại điểm")
    def subjectID(self):
        f  = open('personDN.txt', 'r')
        MaGV = f.read()
        query = self.db.cursor()
        query.execute("SELECT MaMon FROM GIANGVIEN GV INNER JOIN MON M ON GV.MaGV = M.MaGV WHERE MaAC = ? ",(MaGV))
        result = query.fetchone()
        if(result != None):
            return result[0]
        else:
            return None 
