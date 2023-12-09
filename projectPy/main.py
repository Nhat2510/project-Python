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
from changePassswordAD import changePassswordAD
from BlockAccount import Block_Account
from ViewPointAll import ViewPointAll
from menuGV import MenuGV
from updatePoint import UpdatePoint
from changePasswordGV import ChangePasswordGV
from viewInfoSV import ViewInfoSV


app = QApplication(sys.argv)
widget = QStackedWidget()
Home_f=Home_w(widget)
Login_f = Login_w(widget)
ListFuture_f = ListFuture(widget)
changePassswordAD_f = changePassswordAD(widget)
them_SV_f=them_SV(widget)
Update_SV_f=Update_SV(widget)
Block_Account_f=Block_Account(widget)
View_Point_f=ViewPoint(widget)
View_Point_All_f = ViewPointAll(widget)
MenuGV_f = MenuGV(widget)
UpdatePoint_f = UpdatePoint(widget)
ChangePasswordGV_f = ChangePasswordGV(widget)
ViewInfoSV_f = ViewInfoSV(widget)

widget.addWidget(Home_f) 
widget.addWidget(Login_f)
widget.addWidget(ListFuture_f)
widget.addWidget(them_SV_f)
widget.addWidget(Update_SV_f)
widget.addWidget(View_Point_f)
widget.addWidget(View_Point_All_f)
widget.addWidget(MenuGV_f)
#8
widget.addWidget(UpdatePoint_f)
#9
widget.addWidget(ChangePasswordGV_f)
#10
widget.addWidget(ViewInfoSV_f)
#11
widget.addWidget(changePassswordAD_f)
#12
widget.addWidget(Block_Account_f)



widget.setCurrentIndex(2)
widget.resize(1000,650)
widget.show()
sys.exit(app.exec())
