from PyQt6.QtWidgets import *
from PyQt6 import QtCore
from PyQt6.uic import loadUi
import sys
import pyodbc as mdb
from PyQt6.QtCore import *
import re
from ThemSV import them_SV
from UpdateSV import Update_SV
from Login import Login_w
from listFuture import ListFuture
from home import Home_w
from ViewPoint import ViewPoint


app = QApplication(sys.argv)
widget = QStackedWidget()
Home_f=Home_w(widget)
Login_f = Login_w(widget)
ListFuture_f = ListFuture(widget)
them_SV_f=them_SV(widget)
Update_SV_f=Update_SV(widget)
View_Point_f=ViewPoint(widget)
widget.addWidget(Home_f)
widget.addWidget(Login_f)
widget.addWidget(ListFuture_f)
widget.addWidget(them_SV_f)
widget.addWidget(Update_SV_f)
widget.addWidget(View_Point_f)
widget.setCurrentIndex(5)
widget.resize(1000,800)
widget.show()
sys.exit(app.exec())
