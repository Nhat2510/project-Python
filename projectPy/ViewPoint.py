import typing
from PyQt6 import QtGui
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QStackedWidget, QMessageBox,QTableWidgetItem
from PyQt6.uic import loadUi
import sys
import pyodbc as mdb


class ViewPoint(QMainWindow):
    connection_string = 'DRIVER={ODBC Driver 17 for SQL Server};SERVER=LAPTOP-RVCC8HD0;DATABASE=QLSVPY;UID=tuannhat;PWD=123123'
    db = mdb.connect(connection_string)
    MaMon = ''
    def __init__(self,widget):
        super(ViewPoint, self).__init__()
        loadUi('viewPoint.ui',self)
       
        self.widget = widget
        
        self.sort_ASC.clicked.connect(self.sortASC)
        self.sort_DESC.clicked.connect(self.sortDesc)
        self.btn_search.clicked.connect(self.find)
        self.clear.clicked.connect(self.clear_x)
        self.btn_close.clicked.connect(self.close)
    def showEvent(self, event):
        self.MaMon = self.subjectID()
        self.start()
    def close(self):
        self.widget.setCurrentIndex(7)
        self.clear_x()
    def clear_x(self):
        self.sort_name.setChecked(True)
        self.search_text.setText("")
        self.start()
    def start(self):
        query = self.db.cursor()
        query.execute("SELECT SV.MaSV,TEN,DIEM FROM DIEM D INNER JOIN SINHVIEN SV ON D.MaSV =SV.MaSV WHERE MaMon =? ",(self.MaMon))
        result = query.fetchall()
        self.loadData(result)
    def sortASC(self):
        query = self.db.cursor()
        query.execute("SELECT SV.MaSV,TEN,DIEM FROM DIEM D INNER JOIN SINHVIEN SV ON D.MaSV =SV.MaSV WHERE MaMon =? ORDER BY DIEM ASC",(self.MaMon))
        result = query.fetchall()
        self.loadData(result)
    def sortDesc(self):
        query = self.db.cursor()
        query.execute("SELECT SV.MaSV,TEN,DIEM FROM DIEM D INNER JOIN SINHVIEN SV ON D.MaSV =SV.MaSV WHERE MaMon =? ORDER BY DIEM DESC",(self.MaMon))
        result = query.fetchall()
        self.loadData(result)
    def find(self):
        isName = self.sort_name.isChecked()
        isMSV = self.sort_msv.isChecked()
        isPoint = self.sort_grade.isChecked()
        text = (self.search_text.text())
        query = self.db.cursor()
        if(isName):
            query.execute("SELECT SV.MaSV,TEN,DIEM FROM DIEM D INNER JOIN SINHVIEN SV ON D.MaSV =SV.MaSV WHERE MaMon =? AND LOWER(TEN)  like LOWER(?)",(self.MaMon,'%' + text.lower() + '%'))
        if(isMSV):
            query.execute("SELECT SV.MaSV,TEN,DIEM FROM DIEM D INNER JOIN SINHVIEN SV ON D.MaSV =SV.MaSV WHERE MaMon =? AND LOWER(SV.MaSV) like LOWER(?)",(self.MaMon,'%' + text.lower() + '%'))
        if(isPoint):
            query.execute("SELECT SV.MaSV,TEN,DIEM FROM DIEM D INNER JOIN SINHVIEN SV ON D.MaSV =SV.MaSV WHERE MaMon =? AND DIEM = ?",(self.MaMon,  float(text)))
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