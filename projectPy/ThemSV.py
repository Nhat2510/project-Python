from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QStackedWidget, QMessageBox
from PyQt6 import QtCore
from PyQt6.uic import loadUi
import pyodbc as mdb
from PyQt6.QtCore import *
import re
        
class them_SV(QMainWindow):
    def __init__(self, widget):
        super(them_SV, self).__init__()
        loadUi('ThemSV.ui', self)
        self.btnAdd.clicked.connect(self.add)
        self.btn_Back.clicked.connect(self.back)
        self.widget = widget
    
    def back(self):
        self.widget.setCurrentIndex(2)


    def add(self):
        mssv = self.Masv.text().strip()
        name = self.name.text().strip()
        gioitinh = self.Gioi_tinh.currentText()
        ngaysinh = self.Ngay_sinh.date().toString(QtCore.Qt.DateFormat.ISODate)
        email = self.Email.text().strip()
        sdt = self.SDT.text().strip()
        
        if not mssv or not name or not email or not sdt:
            QMessageBox.warning(self, "Error", "Vui lòng nhập đầy đủ thông tin.")
            return
        
        if name.isdigit():
            QMessageBox.warning(self, "Error", "Tên không hợp lệ. Vui lòng nhập lại.")
            return
        
        if not re.match(r"SV\d+", mssv):
            QMessageBox.warning(self, "Error", "Mã sinh viên không hợp lệ. Vui lòng nhập lại theo định dạng SV001.")
            return

        if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            QMessageBox.warning(self, "Error", "Email không hợp lệ. Vui lòng nhập lại.")
            return

        if not (9 <= len(sdt) <= 15 and sdt.isdigit()):
            QMessageBox.warning(self, "Error", "Số điện thoại không hợp lệ. Vui lòng nhập lại.")
            return

        confirm_msg = "Bạn có chắc chắn muốn thêm dữ liệu không?"
        button_reply = QMessageBox.question(self, 'Xác nhận', confirm_msg, QMessageBox.StandardButton.Yes, QMessageBox.StandardButton.No)
        
        if button_reply == QMessageBox.StandardButton.No:
            return

        connection_string = 'DRIVER={ODBC Driver 17 for SQL Server};SERVER=LAPTOP-2A8I63E5\SQLEXPRESS;DATABASE=QLSVPY;UID=thanhan123;PWD=123456'
        try:
            db = mdb.connect(connection_string)
            cursor = db.cursor()
            cursor.execute(f"SELECT * FROM SINHVIEN WHERE MaSV = '{mssv}'")
            if cursor.fetchone():
                QMessageBox.warning(self, "Error", "Mã sinh viên đã tồn tại. Vui lòng nhập lại.")
                db.close()
                return
            db.close()
        except Exception as e:
            QMessageBox.warning(self, "Error", f"Lỗi khi kiểm tra mã sinh viên: {str(e)}")
            return

        try:
            db = mdb.connect(connection_string)
            cursor = db.cursor()
            sql_query = f"INSERT INTO SINHVIEN (MaSV, TEN, Gioitinh, Ngaysinh, Sdt, Email) " \
                        f"VALUES ('{mssv}', '{name}', '{gioitinh}', '{ngaysinh}', '{sdt}', '{email}')"
            cursor.execute(sql_query)
            db.commit()
            db.close()

            QMessageBox.information(self, "Success", "Thêm dữ liệu vào bảng SINHVIEN thành công")

        except Exception as e:
            QMessageBox.warning(self, "Error", f"Có lỗi khi thêm dữ liệu vào bảng SINHVIEN: {str(e)}")

