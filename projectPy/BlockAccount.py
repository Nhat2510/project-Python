from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QStackedWidget, QMessageBox
from PyQt6.uic import loadUi
import sys
import pyodbc as mdb

class Block_Account(QMainWindow):
    def __init__(self, widget):
        super(Block_Account, self).__init__()
        loadUi('BlockAccount.ui', self)
        self.widget = widget
        self.bt_block.clicked.connect(self.blockAC)
        self.bt_openblock.clicked.connect(self.openblockAC)
        self.btn_back.clicked.connect(self.back)
        self.btn_reset.clicked.connect(self.reset)
        
    def blockAC(self):
        MaAC=self.text_ac.text().strip()
        confirm_msg = "Bạn có chắc chắn khóa tài khoản này không?"
        button_reply = QMessageBox.question(self, 'Xác nhận', confirm_msg, QMessageBox.StandardButton.Yes, QMessageBox.StandardButton.No)
        
        if button_reply == QMessageBox.StandardButton.No:
            return
        
        connection_string = 'DRIVER={ODBC Driver 17 for SQL Server};SERVER=LAPTOP-RVCC8HD0;DATABASE=QLSVPY;UID=tuannhat;PWD=123123'
        
        try:
            db = mdb.connect(connection_string)
            cursor = db.cursor()
            cursor.execute(f"SELECT * FROM ACCOUNT WHERE MaAC = '{MaAC}'")
            if cursor.fetchone():
                try:
                    db= mdb.connect(connection_string)
                    cursor = db.cursor()
                    cursor.execute(f"UPDATE ACCOUNT SET check_account='block' WHERE MaAC='{MaAC}'")
                    db.commit()
                    db.close()
                    QMessageBox.information(self, "Success", "khóa thành công")
                    self.text_ac.clear()
                except Exception as e:
                    QMessageBox.warning(self, "Error", f"Có lỗi khi khóa tài khoản: {str(e)}")
            else :
                QMessageBox.warning(self, "Error", f"Mã ACCOUNT không tồn tại")
                self.text_ac.clear()
        except Exception as e:
            QMessageBox.warning(self, "Error", f"Lỗi khi kiểm tra mã sinh viên: {str(e)}")
        
    def openblockAC(self):
        MaAC=self.text_ac.text().strip()
        confirm_msg = "Bạn có chắc chắn mở khóa tài khoản này không?"
        button_reply = QMessageBox.question(self, 'Xác nhận', confirm_msg, QMessageBox.StandardButton.Yes, QMessageBox.StandardButton.No)
        
        if button_reply == QMessageBox.StandardButton.No:
            return
        
        connection_string = 'DRIVER={ODBC Driver 17 for SQL Server};SERVER=LAPTOP-RVCC8HD0;DATABASE=QLSVPY;UID=tuannhat;PWD=123123'
        
        try:
            db = mdb.connect(connection_string)
            cursor = db.cursor()
            cursor.execute(f"SELECT * FROM ACCOUNT WHERE MaAC = '{MaAC}'")
            if cursor.fetchone():
                cursor_check = db.cursor()
                cursor_check.execute(f"SELECT check_account FROM ACCOUNT WHERE MaAC = '{MaAC}'")
                check_account=cursor_check.fetchone()
                if str(check_account[0])=='activity':
                    QMessageBox.information(self,"Success",f"Tài khoản hiện đang hoạt động")
                    self.text_ac.clear()
                    return
                else: 
                    connection_string = 'DRIVER={ODBC Driver 17 for SQL Server};SERVER=LAPTOP-RVCC8HD0;DATABASE=QLSVPY;UID=tuannhat;PWD=123123'
                    db= mdb.connect(connection_string)
                    cursor = db.cursor()
                    cursor.execute(f"UPDATE ACCOUNT SET check_account='activity' WHERE MaAC='{MaAC}'")
                    db.commit()
                    db.close()
                    QMessageBox.information(self, "Success", "mở khóa thành công")
                    self.text_ac.clear()    
            else : 
                QMessageBox.warning(self, "Error", f"Mã ACCOUNT không tồn tại")
                self.text_ac.clear()
        except Exception as e:
            QMessageBox.warning(self, "Error", f"Lỗi khi kiểm tra mã sinh viên: {str(e)}")
    
    def back(self):
        self.widget.setCurrentIndex(2)
    
    def reset(self):
        self.text_ac.clear()

