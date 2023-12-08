from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QStackedWidget, QMessageBox,QTableWidgetItem
from PyQt6.uic import loadUi
import sys
import pyodbc as mdb

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
        self.text_name.setText('')
        self.text_birthday.setText('')
        self.text_grade.setText('')
        self.text_msv.setText('')
        self.groupBox.setEnabled(False)
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
        if(result != None):
            self.Masv = result[0]
            self.text_name.setText(result[1])
            self.text_birthday.setText(str(result[2]).split(' ')[0])
            self.text_grade.setText(str(result[3]))
            self.groupBox.setEnabled(True)
        else:
            self.text_name.setText('')
            self.text_birthday.setText('')
            self.text_grade.setText('')
            QMessageBox.information(self,"Lỗi Ma SV","Không tìm thấy")
            self.groupBox.setEnabled(False)
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
