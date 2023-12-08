from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QStackedWidget, QMessageBox,QTableWidgetItem
from PyQt6.uic import loadUi
import sys
import pyodbc as mdb
from math import *

class ViewPointAll(QMainWindow):
    connection_string = 'DRIVER={ODBC Driver 17 for SQL Server};SERVER=LAPTOP-2A8I63E5\SQLEXPRESS;DATABASE=QLSVPY;UID=thanhan123;PWD=123456'
    db = mdb.connect(connection_string)
    def __init__(self,widget):
        super(ViewPointAll, self).__init__()
        loadUi('ViewPointAll.ui',self)
        self.widget = widget
        self.start()
        self.sort_desc.clicked.connect(self.sortDESC)
        self.sort_asc.clicked.connect(self.sortASC)
        self.btn_search.clicked.connect(self.search)
        self.btn_clear.clicked.connect(self.clear)
        self.sort_default.clicked.connect(self.start)
        self.btn_close.clicked.connect(self.close)
    def close(self):
        self.widget.setCurrentIndex(2)
    def clear(self):
        self.ip.setText("")
        self.sort_default.setChecked(True)
        self.start()

    def start(self):
        query = self.db.cursor()
        query.execute(""" 
            select sv.MaSV,TEN,Ngaysinh,Gioitinh,Sdt,Email, max(case when MaMon ='M001' then Diem else null end)as'toan',
            max(case when MaMon ='M002' then Diem else null end) as 'tieng anh', max(case when MaMon ='M003' then Diem else null end) as 'cntt',
            AVG(DIEM) AS 'Điểm Trung Bình'
            from SINHVIEN sv inner join DIEM on sv.MaSV = DIEM.MaSV
            group by sv.MaSV,TEN,Ngaysinh,Gioitinh,Sdt,Email
        """ )
        result = query.fetchall()
        self.loadData(result)
    def sortDESC(self):
        query = self.db.cursor()
        query.execute(""" 
            select sv.MaSV,TEN,Ngaysinh,Gioitinh,Sdt,Email, max(case when MaMon ='M001' then Diem else null end)as'toan',
            max(case when MaMon ='M002' then Diem else null end) as 'tieng anh', max(case when MaMon ='M003' then Diem else null end) as 'cntt',
            AVG(DIEM) AS 'Điểm Trung Bình'
            from SINHVIEN sv inner join DIEM on sv.MaSV = DIEM.MaSV
            group by sv.MaSV,TEN,Ngaysinh,Gioitinh,Sdt,Email
            order by avg(diem) desc
        """ )
        result = query.fetchall()
        self.loadData(result)
    def sortASC(self):
        query = self.db.cursor()
        query.execute(""" 
            select sv.MaSV,TEN,Ngaysinh,Gioitinh,Sdt,Email, max(case when MaMon ='M001' then Diem else null end)as'toan',
            max(case when MaMon ='M002' then Diem else null end) as 'tieng anh', max(case when MaMon ='M003' then Diem else null end) as 'cntt',
            AVG(DIEM) AS 'Điểm Trung Bình'
            from SINHVIEN sv inner join DIEM on sv.MaSV = DIEM.MaSV
            group by sv.MaSV,TEN,Ngaysinh,Gioitinh,Sdt,Email
            order by avg(diem) asc
        """ )
        result = query.fetchall()
        self.loadData(result)
    
    def search(self):
        ip = self.ip.text()
        query = self.db.cursor()
        query.execute(""" 
            select sv.MaSV,TEN,Ngaysinh,Gioitinh,Sdt,Email, max(case when MaMon ='M001' then Diem else null end)as'toan',
            max(case when MaMon ='M002' then Diem else null end) as 'tieng anh', max(case when MaMon ='M003' then Diem else null end) as 'cntt',
            AVG(DIEM) AS 'Điểm Trung Bình'
            from SINHVIEN sv inner join DIEM on sv.MaSV = DIEM.MaSV
            where LOWER(sv.MaSV) like ? or LOWER(TEN) like  ?
            group by sv.MaSV,TEN,Ngaysinh,Gioitinh,Sdt,Email
            order by avg(diem) asc
        """ ,('%' + str(ip).lower()+'%','%' + str(ip).lower()+'%'))
        result = query.fetchall()
        self.loadData(result)
        

    def loadData(self,result):
        rowNumber = 0
        # self.table.setColumnWidth(0,140)
        # self.table.setColumnWidth(1,393)
        # self.table.setColumnWidth(2,95)
        self.table.setRowCount(len(result))
        for row in result:
            self.table.setItem(rowNumber, 0, QTableWidgetItem(row[0]))
            self.table.setItem(rowNumber, 1, QTableWidgetItem(row[1]))
            self.table.setItem(rowNumber, 2, QTableWidgetItem("".join(str(row[2]).split(' ')[0])))
            self.table.setItem(rowNumber, 3, QTableWidgetItem(row[3]))
            self.table.setItem(rowNumber, 4, QTableWidgetItem(row[4]))
            self.table.setItem(rowNumber, 5, QTableWidgetItem(row[5]))
            self.table.setItem(rowNumber, 6, QTableWidgetItem(str(row[6])))
            self.table.setItem(rowNumber, 7, QTableWidgetItem(str(row[7])))
            self.table.setItem(rowNumber, 8, QTableWidgetItem(str(row[8])))
            self.table.setItem(rowNumber, 9, QTableWidgetItem(str(round(row[9],1))))
            rowNumber+=1