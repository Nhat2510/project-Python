from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QStackedWidget, QMessageBox,QTableWidgetItem
from PyQt6.uic import loadUi
import sys
import pyodbc as mdb
from PyQt6.QtCore import *

class ViewInfoSV(QMainWindow):
    connection_string = 'DRIVER={ODBC Driver 17 for SQL Server};SERVER=LAPTOP-2A8I63E5\SQLEXPRESS;DATABASE=QLSVPY;UID=thanhan123;PWD=123456'
    db = mdb.connect(connection_string)
    def __init__(self,widget):
        super(ViewInfoSV, self).__init__()
        loadUi('viewInfoSV.ui',self) 
        self.widget = widget
        self.search.clicked.connect(self.find)
        self.back.clicked.connect(self.back_f)
        self.reset.clicked.connect(self.reset_f)
    
    def reset_f(self):
        self.clear()
        self.msv.clear()
        
    def back_f(self):
        self.clear()
        self.msv.setText('')
        self.widget.setCurrentIndex(0)
    def find(self):
        msv = self.msv.text()
        query = self.db.cursor()
        query.execute("""
            select sv.MaSV,TEN,Ngaysinh,Gioitinh,Sdt,Email, max(case when MaMon ='M001' then Diem else null end)as'toan',
            max(case when MaMon ='M002' then Diem else null end) as 'tieng anh', max(case when MaMon ='M003' then Diem else null end) as 'cntt',
            AVG(DIEM) AS 'Điểm Trung Bình'
            from SINHVIEN sv inner join DIEM on sv.MaSV = DIEM.MaSV
            where sv.MaSV = ?
            group by sv.MaSV,TEN,Ngaysinh,Gioitinh,Sdt,Email
        """,(msv))
        result = query.fetchone()
        if result is None:
            QMessageBox.information(self,"Thông báo","Không tìm thấy mã sinh viên")
            self.clear()
            self.groupBox.setEnabled(False)
            return
        self.name.setText(result[1])
        self.day.setDate(QDate(result[2].date()))
        self.sex.setText(result[3])
        self.phone.setText(result[4])
        self.email.setText(result[5])
        self.toan.setText(str(result[6]))
        self.anh.setText(str(result[7]))
        self.cntt.setText(str(result[8]))
        self.groupBox.setEnabled(True)
    def clear(self):
        self.name.setText('')
        self.day.setDate(QDate.currentDate())
        self.sex.setText('')
        self.phone.setText('')
        self.email.setText('')
        self.toan.setText('')
        self.anh.setText('')
        self.cntt.setText('')
        self.groupBox.setEnabled(False)
