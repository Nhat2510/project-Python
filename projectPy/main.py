from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QStackedWidget, QMessageBox
from PyQt6.uic import loadUi
import sys
import pyodbc as mdb

# Cửa sổ login
class Login_w(QMainWindow):
    def __init__(self, widget):
        super(Login_w, self).__init__()
        loadUi('Login.ui', self)
        self.btn_log.clicked.connect(self.login)
        self.widget = widget
        
    def login(self):
        un = self.txt_user.text()
        psw = self.txt_pass.text()
        connection_string = 'DRIVER={ODBC Driver 17 for SQL Server};SERVER=LAPTOP-RVCC8HD0;DATABASE=QLSV;UID=tuannhat;PWD=123123'
        db = mdb.connect(connection_string)
        query = db.cursor()
        # query.execute(f"SELECT * FROM ACCOUNT WHERE username='{un}' AND password='{psw}'")
        query.execute("SELECT * FROM ACCOUNT WHERE username=? AND pass=?", (un, psw))
        result = query.fetchone()
        if result:
            QMessageBox.information(self, "Login output", "Login success")
            self.widget.setCurrentIndex(2)  # Assuming the index for the Main_w is 1
        else:
            QMessageBox.information(self, "Login output", "Login fail")

class Main_w(QMainWindow):
    def __init__(self):
        super(Main_w, self).__init__()
        loadUi('login_success.ui', self)
class Home_w(QMainWindow):
    def __init__(self,widget):
        super(Home_w, self).__init__()
        loadUi('Home.ui', self)
        self.b2.clicked.connect(self.admin)
        self.widget = widget
    def admin(self):
        self.widget.setCurrentIndex(1)


app = QApplication(sys.argv)
widget = QStackedWidget()
Home_f=Home_w(widget)
Login_f = Login_w(widget)
Main_f = Main_w()
widget.addWidget(Home_f)
widget.addWidget(Login_f)
widget.addWidget(Main_f)
widget.setCurrentIndex(0)
widget.setFixedHeight(800)
widget.setFixedWidth(800)
widget.show()
sys.exit(app.exec())
