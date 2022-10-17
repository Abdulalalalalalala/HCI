import os
import sys

import pandas as pd
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPixmap

from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QMainWindow, QFileDialog, QWidget, QLabel, QVBoxLayout, QTableWidgetItem
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
        viewScheduleWindow = None
        self.login.clicked.connect(self.loginButton)
        self._viewScheduleWindow = viewScheduleWindow
    # self.setGeometry(500, 100, 100, 50)
        # self.button = QtWidgets.QPushButton('Go To Window 2', self)
        # self.button.clicked.connect(self.handleButton)
        # self.setCentralWidget(self.button)
        # self._appWindow = appWindow

    def loginButton(self):
        self.hide()
        if self._viewScheduleWindow is None:
            self._viewScheduleWindow = ViewScheduleWindow(self)
        self._viewScheduleWindow.show()


class ViewScheduleWindow(QtWidgets.QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        uic.loadUi("viewSchedule.ui", self)
        viewScheduleWindow = None
        self._viewScheduleWindow = viewScheduleWindow

        manageScheduleWindow = None
        self._manageScheduleWindow = manageScheduleWindow

        recordsWindow = None
        self._recordsWindow = recordsWindow

        logoutWindow = None
        self._logoutWindow = logoutWindow

        self.viewSched.clicked.connect(self.viewButton)
        self.manSched.clicked.connect(self.manButton)
        self.records.clicked.connect(self.recButton)
        self.logout.clicked.connect(self.logoutButton)
        # self.setGeometry(500, 100, 100, 50)
        # self.button = QtWidgets.QPushButton('Go To Window 2', self)
        # self.button.clicked.connect(self.handleButton)
        # self.setCentralWidget(self.button)
        # self._appWindow = appWindow

    def viewButton(self):
        self.hide()
        if self._viewScheduleWindow is None:
            self._viewScheduleWindow = ViewScheduleWindow(self)
        self._viewScheduleWindow.show()

    def manButton(self):
        self.hide()
        if self._manageScheduleWindow is None:
            self._manageScheduleWindow = ManageScheduleWindow(self)
        self._manageScheduleWindow.show()

    def recButton(self):
        self.hide()
        if self._recordsWindow is None:
            self._recordsWindow = RecordsWindow(self)
        self._recordsWindow.show()

    def logoutButton(self):
        self.hide()
        if self._logoutWindow is None:
            self._logoutWindow = LogoutWindow(self)
        self._logoutWindow.show()


class ManageScheduleWindow(QtWidgets.QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        uic.loadUi("manageSchedule.ui", self)
        viewScheduleWindow = None
        self._viewScheduleWindow = viewScheduleWindow

        manageScheduleWindow = None
        self._manageScheduleWindow = manageScheduleWindow

        recordsWindow = None
        self._recordsWindow = recordsWindow

        logoutWindow = None
        self._logoutWindow = logoutWindow



        self.viewSched.clicked.connect(self.viewButton)
        self.manSched.clicked.connect(self.manButton)
        self.records.clicked.connect(self.recButton)
        self.logout.clicked.connect(self.logoutButton)
        # self.setGeometry(500, 100, 100, 50)
        # self.button = QtWidgets.QPushButton('Go To Window 2', self)
        # self.button.clicked.connect(self.handleButton)
        # self.setCentralWidget(self.button)
        # self._appWindow = appWindow

    def viewButton(self):
        self.hide()
        if self._viewScheduleWindow is None:
            self._viewScheduleWindow = ViewScheduleWindow(self)
        self._viewScheduleWindow.show()

    def manButton(self):
        self.hide()
        if self._manageScheduleWindow is None:
            self._manageScheduleWindow = ManageScheduleWindow(self)
        self._manageScheduleWindow.show()

    def recButton(self):
        self.hide()
        if self._recordsWindow is None:
            self._recordsWindow = RecordsWindow(self)
        self._recordsWindow.show()

    def logoutButton(self):
        self.hide()
        if self._logoutWindow is None:
            self._logoutWindow = LogoutWindow(self)
        self._logoutWindow.show()





class RecordsWindow(QtWidgets.QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        uic.loadUi("records.ui", self)
        viewScheduleWindow = None
        self.scope_file_path = 'scopes.xlsx'
        self.worksheet_name = 'scope'
        self._viewScheduleWindow = viewScheduleWindow

        manageScheduleWindow = None
        self._manageScheduleWindow = manageScheduleWindow

        recordsWindow = None
        self._recordsWindow = recordsWindow

        logoutWindow = None
        self._logoutWindow = logoutWindow

        self.viewSched.clicked.connect(self.viewButton)
        self.manSched.clicked.connect(self.manButton)
        self.records.clicked.connect(self.recButton)
        self.logout.clicked.connect(self.logoutButton)
        self.scope.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.Scope))
        # self.scope.clicked.connect(lambda _, xl_path=self.scope_file_path, sheet_name=self.worksheet_name: self.loadExcelData(xl_path, sheet_name))
        self.washer.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.Washer))
        self.mainBackButton.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.MainPage))
        self.mainBackButton_2.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.MainPage))

    def viewButton(self):
        self.hide()
        if self._viewScheduleWindow is None:
            self._viewScheduleWindow = ViewScheduleWindow(self)
        self._viewScheduleWindow.show()

    def manButton(self):
        self.hide()
        if self._manageScheduleWindow is None:
            self._manageScheduleWindow = ManageScheduleWindow(self)
        self._manageScheduleWindow.show()

    def recButton(self):
        self.hide()
        if self._recordsWindow is None:
            self._recordsWindow = RecordsWindow(self)
        self._recordsWindow.show()

    def logoutButton(self):
        self.hide()
        if self._logoutWindow is None:
            self._logoutWindow = LogoutWindow(self)
        self._logoutWindow.show()

    # def loadExcelData(self, excel_file_dir, worksheet_name):
    #
    #     df = pd.read_excel(excel_file_dir, worksheet_name)
    #     if df.size == 0:
    #         return
    #
    #     df.fillna('', inplace=True)
    #     self.scopeTable.setRowCount(df.shape[0])
    #     self.scopeTable.setColumnCount(df.shape[1])
    #     self.scopeTable.setHorizontalHeaderLabels(df.columns)
    #
    #     # returns pandas array object
    #     for row in df.iterrows():
    #         values = row[1]
    #         for col_index, value in enumerate(values):
    #             if isinstance(value, (float, int)):
    #                 value = '{0:0,.0f}'.format(value)
    #             scopeTableItem = QTableWidgetItem(str(value))
    #             self.scopeTable.setItem(row[0], col_index, scopeTableItem)
    #
    #     self.scopeTable.setColumnWidth(2, 300)


class LogoutWindow(QtWidgets.QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        uic.loadUi("logout.ui", self)
        viewScheduleWindow = None
        self._viewScheduleWindow = viewScheduleWindow

        manageScheduleWindow = None
        self._manageScheduleWindow = manageScheduleWindow

        recordsWindow = None
        self._recordsWindow = recordsWindow

        logoutWindow = None
        self._logoutWindow = logoutWindow

        loginWindow = None
        self._loginWindow = loginWindow

        self.viewSched.clicked.connect(self.viewButton)
        self.manSched.clicked.connect(self.manButton)
        self.records.clicked.connect(self.recButton)
        self.logout.clicked.connect(self.logoutButton)
        self.yesButton.clicked.connect(self.confirmButton)
        self.noButton.clicked.connect(self.viewButton)

    def viewButton(self):
        self.hide()
        if self._viewScheduleWindow is None:
            self._viewScheduleWindow = ViewScheduleWindow(self)
        self._viewScheduleWindow.show()

    def manButton(self):
        self.hide()
        if self._manageScheduleWindow is None:
            self._manageScheduleWindow = ManageScheduleWindow(self)
        self._manageScheduleWindow.show()

    def recButton(self):
        self.hide()
        if self._recordsWindow is None:
            self._recordsWindow = RecordsWindow(self)
        self._recordsWindow.show()

    def logoutButton(self):
        self.hide()
        if self._logoutWindow is None:
            self._logoutWindow = LogoutWindow(self)
        self._logoutWindow.show()

    def confirmButton(self):
        self.hide()
        if self._loginWindow is None:
            self._loginWindow = LoginWindow(self)
        self._loginWindow.show()





# class AppWindow(QtWidgets.QMainWindow):
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         uic.loadUi("appLayout.ui", self)
#         loginWindow = None
#         self.current = None
#         self.previous = None
#         # self.logout.clicked.connect(self.handleButton)
#         self.viewSched.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.ViewSchedule))
#         
#         self.manSched.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.ManageSchedule))
#         self.records.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.Records))
#         self.logout.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.Logout))
#         self.yesButton.clicked.connect(self.handleButton)
#         self.noButton.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.ViewSchedule))
#         self.scope.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.Scope))
#         self.washer.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.Washer))
#         Logout(self.Logout)
#         # self.button = QtWidgets.QPushButton('Go To Window 1', self)
#         # self.button.clicked.connect(self.handleButton)
#         # self.setCentralWidget(self.button)
#         self._loginWindow = loginWindow
#
#     def handleButton(self):
#         self.hide()
#         if self._loginWindow is None:
#             self._loginWindow = LoginWindow(self)
#         self._loginWindow.show()
#
#     def pathChange(self):
#         self.previous = self.current
#         self.current = self.ViewSchedule
#         print("view")

        # if newpath == "viewSched":
        #     self.stackedWidget.setCurrentWidget(self.ViewSchedule)
        #     self.current = self.ViewSchedule
        #     print("viewSched")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyleSheet(open('stylesheet.css').read())
    window = LoginWindow()
    window.show()
    app.exec()
