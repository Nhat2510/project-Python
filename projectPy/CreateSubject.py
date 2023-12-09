import re
from PyQt6 import QtCore
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QStackedWidget, QMessageBox
from PyQt6.uic import loadUi
import sys
from PyQt6.QtCore import *
import pyodbc as mdb

class Create_Subject(QMainWindow):
    
    def __init__(self, widget):
        super(Create_Subject, self).__init__()
        loadUi('CreateSubject.ui', self)
        self.widget = widget
        self.save.clicked.connect(self.get_data)
        self.btnback.clicked.connect(self.back)
        self.reset.clicked.connect(self.reset_f)
        self.date.setDate(QtCore.QDate.currentDate())
        
    def reset_f(self):
        self.username.clear()
        self.password.clear()
        self.name.clear()
        self.gioi_tinh.setCurrentIndex(0)
        self.date.setDate(QtCore.QDate.currentDate())
        self.numphone.clear()
        self.mail.clear()
        self.maGV.clear()
        self.ma_mon.clear()
        self.ten_mon.clear()
        self.maAcc.clear()
        self.role.setCurrentIndex(0)
        
    def back(self):    
       self.widget.setCurrentIndex(2)
        
    def get_data(self):
        ten_dang_nhap = self.username.text().strip()
        mat_khau = self.password.text().strip()
        ho_va_ten = self.name.text().strip()
        gioi_tinh = self.gioi_tinh.currentText()
        ngay_sinh = self.date.date().toString(QtCore.Qt.DateFormat.ISODate)
        sdt = self.numphone.text().strip()
        email = self.mail.text().strip()
        ma_gv = self.maGV.text().strip()

        ma_mon_hoc = self.ma_mon.text().strip()
        ten_mon_hoc = self.ten_mon.text().strip()
        ma_tk=self.maAcc.text().strip()
        role= self.role.currentText()
        
        if len(mat_khau) < 4:
            QMessageBox.warning(self, 'Lỗi', 'Yêu cầu mật khẩu có độ dài 8 kí tự trở lên')
            return
        if not (9 <= len(sdt) <= 15 and sdt.isdigit()):
            QMessageBox.warning(self, "Error", "Số điện thoại không hợp lệ. Vui lòng nhập lại.")
            return
        if not re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', email):
            QMessageBox.warning(self, 'Lỗi', 'Nhập sai Email')
            return
        
        connection_string = 'DRIVER={ODBC Driver 17 for SQL Server};SERVER=LAPTOP-RVCC8HD0;DATABASE=QLSVPY;UID=tuannhat;PWD=123123'

        try:
            db = mdb.connect(connection_string)
            cursor = db.cursor()
            cursor.execute(f"SELECT * FROM ACCOUNT WHERE username = '{ten_dang_nhap}'")
            if cursor.fetchone():
                QMessageBox.warning(self, "Error", "Tên đăng nhập đã tồn tại. Vui lòng nhập lại.")
                db.close()
                return
            db.close()
        except Exception as e:
            QMessageBox.warning(self, "Error", f"Lỗi khi kiểm tra tên đăng nhập: {str(e)}")
            return

        try:
            db = mdb.connect(connection_string)
            cursor = db.cursor()
            cursor.execute(f"SELECT * FROM GIANGVIEN WHERE MaGV = '{ma_gv}'")
            if cursor.fetchone():
                QMessageBox.warning(self, "Error", "Mã giảng viên đã tồn tại. Vui lòng nhập lại.")
                db.close()
                return
            db.close()
        except Exception as e:
            QMessageBox.warning(self, "Error", f"Lỗi khi kiểm tra mã giảng viên: {str(e)}")
            return
        
        try:
            db = mdb.connect(connection_string)
            cursor = db.cursor()
            cursor.execute(f"SELECT * FROM ACCOUNT WHERE MaAC = '{ma_tk}'")
            if cursor.fetchone():
                QMessageBox.warning(self, "Error", "Mã tài khoản đã tồn tại. Vui lòng nhập lại.")
                db.close()
                return
            db.close()
        except Exception as e:
            QMessageBox.warning(self, "Error", f"Lỗi khi kiểm tra mã tài khoản: {str(e)}")
            return
        
        try:
            db = mdb.connect(connection_string)
            cursor = db.cursor()
            cursor.execute(f"SELECT * FROM MON WHERE MaMon = '{ma_mon_hoc}'")
            if cursor.fetchone():
                QMessageBox.warning(self, "Error", "Mã môn đã tồn tại. Vui lòng nhập lại.")
                db.close()
                return
            db.close()
        except Exception as e:
            QMessageBox.warning(self, "Error", f"Lỗi khi kiểm tra mã môn: {str(e)}")
            return
        
        try:
            db = mdb.connect(connection_string)
            cursor = db.cursor()
            cursor.execute(f"SELECT * FROM MON WHERE TenMon = '{ten_mon_hoc}'")
            if cursor.fetchone() is None:
                QMessageBox.warning(self, "Error", "Tên môn không tồn tại. Vui lòng nhập lại.")
                db.close()
                return
            db.close()
        except Exception as e:
            QMessageBox.warning(self, "Error", f"Lỗi khi kiểm tra tên môn: {str(e)}")
            return

        try:
            db = mdb.connect(connection_string)
            cursor = db.cursor()
            sql_query = f"INSERT INTO ACCOUNT (MaAC, username, pass, roles, check_account) " \
                        f"VALUES ('{ma_tk}', '{ten_dang_nhap}', '{mat_khau}', '{role}','activity')"
            sql_query1 = f"INSERT INTO GIANGVIEN (MaGV, TenGV, Gioitinh, Sdt, Email, MaAC, NgaySinh) " \
                        f"VALUES ('{ma_gv}', '{ho_va_ten}', '{gioi_tinh}', '{sdt}', '{email}', '{ma_tk}', '{ngay_sinh}')"
            sql_query2 = f"INSERT INTO MON (MaMon, TenMon, MaGV) " \
                        f"VALUES ('{ma_mon_hoc}', '{ten_mon_hoc}', '{ma_gv}')"
            cursor.execute(sql_query)   
            cursor.execute(sql_query1)
            cursor.execute(sql_query2)
            db.commit()
            db.close()

            QMessageBox.information(self, "Success", "Tạo tài khoản thành công")

        except Exception as e:
            QMessageBox.warning(self, "Error",f"Lỗi khi Tạo tài khoản: {str(e)}")
            return
    
    