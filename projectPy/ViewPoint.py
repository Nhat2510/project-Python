from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QStackedWidget, QMessageBox,QTableWidgetItem
from PyQt6.uic import loadUi
import sys
import pyodbc as mdb

class ViewPoint(QMainWindow):
    connection_string = 'DRIVER={ODBC Driver 17 for SQL Server};SERVER=LAPTOP-2A8I63E5\SQLEXPRESS;DATABASE=QLSVPY;UID=thanhan123;PWD=123456'
    db = mdb.connect(connection_string)
    def __init__(self,widget):
        super(ViewPoint, self).__init__()
        loadUi('viewPoint.ui',self)
        self.widget = widget
        self.start()
        self.sort_ASC.clicked.connect(self.sortASC)
        self.sort_DESC.clicked.connect(self.sortDesc)
        self.btn_search.clicked.connect(self.find)
        self.clear.clicked.connect(self.clear_x)
        self.btn_close.clicked.connect(self.close)
    def clear_x(self):
        self.sort_name.setChecked(True)
        self.start()
    def close(self):
        self.widget.setCurrentIndex(0)
    def start(self):
        query = self.db.cursor()
        query.execute("SELECT SV.MaSV,TEN,DIEM FROM DIEM D INNER JOIN SINHVIEN SV ON D.MaSV =SV.MaSV WHERE MaMon =? ",("M001"))
        result = query.fetchall()
        self.loadData(result)
    def sortASC(self):
        query = self.db.cursor()
        query.execute("SELECT SV.MaSV,TEN,DIEM FROM DIEM D INNER JOIN SINHVIEN SV ON D.MaSV =SV.MaSV WHERE MaMon =? ORDER BY DIEM ASC",("M001"))
        result = query.fetchall()
        self.loadData(result)
    def sortDesc(self):
        query = self.db.cursor()
        query.execute("SELECT SV.MaSV,TEN,DIEM FROM DIEM D INNER JOIN SINHVIEN SV ON D.MaSV =SV.MaSV WHERE MaMon =? ORDER BY DIEM DESC",("M001"))
        result = query.fetchall()
        self.loadData(result)
    def find(self):
        isName = self.sort_name.isChecked()
        isMSV = self.sort_msv.isChecked()
        isPoint = self.sort_grade.isChecked()
        text = (self.search_text.text())
        query = self.db.cursor()
        if(isName):
            query.execute("SELECT SV.MaSV,TEN,DIEM FROM DIEM D INNER JOIN SINHVIEN SV ON D.MaSV =SV.MaSV WHERE MaMon =? AND LOWER(TEN)  like LOWER(?)",("M001",'%' + text.lower() + '%'))
        if(isMSV):
            query.execute("SELECT SV.MaSV,TEN,DIEM FROM DIEM D INNER JOIN SINHVIEN SV ON D.MaSV =SV.MaSV WHERE MaMon =? AND LOWER(SV.MaSV) like LOWER(?)",("M001",'%' + text.lower() + '%'))
        if(isPoint):
            query.execute("SELECT SV.MaSV,TEN,DIEM FROM DIEM D INNER JOIN SINHVIEN SV ON D.MaSV =SV.MaSV WHERE MaMon =? AND DIEM = ?",("M001",  float(text)))
        result = query.fetchall()
        self.loadData(result)
        
    def loadData(self, result):
        rowNumber = 0
        self.table.setColumnWidth(0,140)
        self.table.setColumnWidth(1,393)
        self.table.setColumnWidth(2,95)
        self.table.setRowCount(len(result))
        for row in result:
            self.table.setItem(rowNumber, 0, QTableWidgetItem(row[0]))
            self.table.setItem(rowNumber, 1, QTableWidgetItem(row[1]))
            self.table.setItem(rowNumber, 2, QTableWidgetItem(str(row[2])))
            rowNumber+=1