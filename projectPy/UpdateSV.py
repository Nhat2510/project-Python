from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QStackedWidget, QMessageBox
from PyQt6 import QtCore
from PyQt6.uic import loadUi
import pyodbc as mdb
from PyQt6.QtCore import *

class Update_SV(QMainWindow):
    def __init__(self, widget):
        super(Update_SV, self).__init__()
        loadUi('UpdateSV.ui', self)
        self.btnsearch.clicked.connect(self.search)
        self.btnUpdate.clicked.connect(self.update)
        self.btn_back.clicked.connect(self.back)
        self.reset.clicked.connect(self.reset_f)
        self.Ngay_sinh.setDate(QtCore.QDate.currentDate())
        self.widget = widget

        connection_string = 'DRIVER={ODBC Driver 17 for SQL Server};SERVER=LAPTOP-RVCC8HD0;DATABASE=QLSVPY;UID=tuannhat;PWD=123123'
        self.connection = mdb.connect(connection_string)
    
    def reset_f(self):
        self.clear_textboxes()
        
    
    def back(self):
        self.clear_textboxes()
        self.widget.setCurrentIndex(2)
        
    def database_query(self, mssv):
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM SINHVIEN WHERE MaSV=?", (mssv,))
        result = cursor.fetchone()

        if result:
            ngaysinh_date = result.Ngaysinh.date() if result.Ngaysinh else None

            student_data = {
                'name': result.TEN, 
                'gioitinh': result.Gioitinh,
                'ngaysinh': ngaysinh_date,
                'email': result.Email,
                'sdt': result.Sdt,
            }
            return student_data
        else:
            return None
        
    def search(self):
        mssv = self.Masv.text().strip()
        student_data = self.database_query(mssv)
        
        if not mssv:
            QMessageBox.warning(self, 'Warning', 'Vui lòng nhập mã số sinh viên.')
            self.clear_textboxes()
            self.groupBox.setEnabled(False)
            return
        
        if student_data:
            self.name.setText(student_data['name'])
            self.Gioi_tinh.setCurrentText(student_data['gioitinh'])
            birth_date = student_data['ngaysinh']
            if birth_date:
                self.Ngay_sinh.setDate(QtCore.QDate(birth_date))
                self.Email.setText(student_data['email'])
                self.SDT.setText(student_data['sdt'])
                self.groupBox.setEnabled(True)
        else:
            QMessageBox.warning(self, 'Warning', 'Mã sinh viên không hợp lệ. Vui lòng nhập lại')
            self.groupBox.setEnabled(False)
            self.clear_textboxes()

    def update(self):
        mssv = self.Masv.text().strip()
        
        if not mssv:
            QMessageBox.warning(self, 'Warning', 'Vui lòng nhập mã số sinh viên.')
            return
        
        name = self.name.text().strip()
        gioitinh = self.Gioi_tinh.currentText()
        ngaysinh = self.Ngay_sinh.date().toString(QtCore.Qt.DateFormat.ISODate)
        email = self.Email.text().strip()
        sdt = self.SDT.text().strip()
        
        confirm_msg = "Bạn có chắc chắn muốn cập nhật dữ liệu không?"
        button_reply = QMessageBox.question(self, 'Xác nhận', confirm_msg, QMessageBox.StandardButton.Yes, QMessageBox.StandardButton.No)
        
        if button_reply == QMessageBox.StandardButton.No:
            return

        cursor = self.connection.cursor()
        
        update_query = "UPDATE SINHVIEN SET TEN=?, Gioitinh=?, Ngaysinh=?, Email=?, Sdt=? WHERE MaSV=?"
        
        cursor.execute(update_query, (name, gioitinh, ngaysinh, email, sdt, mssv))
        self.connection.commit()

        QMessageBox.information(self, 'Information', 'Student information updated successfully!')
    def clear_textboxes(self):
        self.Masv.clear()
        self.name.clear()
        self.Gioi_tinh.setCurrentIndex(0)
        self.Ngay_sinh.setDate(QtCore.QDate.currentDate())
        self.Email.clear()
        self.SDT.clear()
