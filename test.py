from PyQt5 import QtWidgets
from gui_login import Ui_MainWindow
from gui_select import Ui_select

class LoginWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.login.clicked.connect(self.showSelect)

    def showSelect(self):
        user_id = self.lineEdit_user_id.text()
        password = self.lineEdit_password.text()
        x = users.get(user_id)
        if x == int(password):
            self.close()
            self.selectWindow = SelectWindow()
            self.selectWindow.show()
        else:
            # this is *wrong*, see below
            self.login.setText("Wrong Password, Please Retry")
            time.sleep(1)
            self.login.setText("Login")


class SelectWindow(QtWidgets.QMainWindow, Ui_select):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.back_button.clicked.connect(self.showLogin)

    def showLogin(self):
        self.close()
        self.loginWindow = LoginWindow()
        self.loginWindow.show()


if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    loginWindow = LoginWindow()
    loginWindow.show()
    sys.exit(app.exec_())