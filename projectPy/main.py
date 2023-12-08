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
them_SV_f=them_SV(widget)
Update_SV_f=Update_SV(widget)
View_Point_f=ViewPoint(widget)
View_Point_All_f = ViewPointAll(widget)
MenuGV_f = MenuGV(widget)
UpdatePoint_f = UpdatePoint(widget)
ChangePasswordGV_f = ChangePasswordGV(widget)
ViewInfoSV_f = ViewInfoSV(widget)

# 0
widget.addWidget(Home_f) 
# 1
widget.addWidget(Login_f)
# 2
widget.addWidget(ListFuture_f)
# 3
widget.addWidget(them_SV_f)
# 4
widget.addWidget(Update_SV_f)
# 5
widget.addWidget(View_Point_f)
# 6
widget.addWidget(View_Point_All_f)
# 7
widget.addWidget(MenuGV_f)
#8
widget.addWidget(UpdatePoint_f)
#9
widget.addWidget(ChangePasswordGV_f)
#10
widget.addWidget(ViewInfoSV_f)

widget.setCurrentIndex(0)
widget.resize(1000,800)
widget.show()
sys.exit(app.exec())
