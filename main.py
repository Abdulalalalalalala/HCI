import os
import sys

from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPixmap

from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QMainWindow, QFileDialog, QListWidget, QLabel, QVBoxLayout
from PyQt6 import QtCore, QtGui, QtWidgets



# class LoginWindow(QMainWindow):
#
#     # Initialising the GUI
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         uic.loadUi("layout.ui", self)
#         self.login.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.ViewSchedule))
#         self.viewSched.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.ViewSchedule))
#         self.manSched.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.ManageSchedule))
#         self.records.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.Records))
#         self.logout.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.Logout))


class LoginWindow(QtWidgets.QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        uic.loadUi("login.ui", self)
        appWindow = None
        self.login.clicked.connect(self.handleButton)
        self._appWindow = appWindow
        # self.setGeometry(500, 100, 100, 50)
        # self.button = QtWidgets.QPushButton('Go To Window 2', self)
        # self.button.clicked.connect(self.handleButton)
        # self.setCentralWidget(self.button)
        # self._appWindow = appWindow

    def handleButton(self):
        self.hide()
        if self._appWindow is None:
            self._appWindow = AppWindow(self)
        self._appWindow.show()

class AppWindow(QtWidgets.QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        uic.loadUi("appLayout.ui", self)
        loginWindow = None
        self.logout.clicked.connect(self.handleButton)
        self.viewSched.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.ViewSchedule))
        self.manSched.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.ManageSchedule))
        self.records.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.Records))
        # self.button = QtWidgets.QPushButton('Go To Window 1', self)
        # self.button.clicked.connect(self.handleButton)
        # self.setCentralWidget(self.button)
        self._loginWindow = loginWindow

    def handleButton(self):
        self.hide()
        if self._loginWindow is None:
            self._loginWindow = LoginWindow(self)
        self._loginWindow.show()



if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyleSheet(open('stylesheet.css').read())
    window = LoginWindow()
    window.show()
    app.exec()

