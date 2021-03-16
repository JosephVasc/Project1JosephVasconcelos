from PyQt5 import QtCore, QtGui, QtWidgets, QtWidgets
import sqlite3
import Demo
from PyQt5 import QtSql
import sys


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(680, 70, 91, 41))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.SQLiteData)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(680, 160, 91, 41))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.APIData)
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(25, 21, 631, 421))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(6)
        self.tableWidget.setRowCount(1050)
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(270, 470, 101, 51))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.clicked.connect(self.exit)
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(680, 260, 75, 81))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_4.clicked.connect(self.MAP)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "SQLite DATA"))
        self.pushButton_2.setText(_translate("MainWindow", "API DATA"))
        self.pushButton_3.setText(_translate("MainWindow", "Exit"))
        self.pushButton_4.setText(_translate("MainWindow", "map"))

    def exit(self):
        sys.exit()
    def SQLiteData(self):
        print("sqlite data here")
        conn = sqlite3.connect("university_data.sqlite")
        cursor = conn.cursor()
        sqlquery = "SELECT * FROM university_data"

        self.tableWidget.setRowCount(6)
        tableindex = 0
        for row in cursor.execute(sqlquery):
            print(row)
            self.tableWidget.setItem(tableindex, 0, QtWidgets.QtableWIdgetItem(row[0]))
            self.tableWidget.setItem(tableindex, 1, QtWidgets.QtableWIdgetItem(row[1]))
            self.tableWidget.setItem(tableindex, 2, QtWidgets.QtableWIdgetItem(row[2]))
            self.tableWidget.setItem(tableindex, 3, QtWidgets.QtableWIdgetItem(row[3]))
            self.tableWidget.setItem(tableindex, 4, QtWidgets.QtableWIdgetItem(row[4]))
            self.tableWidget.setItem(tableindex, 5, QtWidgets.QtableWIdgetItem(row[5]))
            tableindex+=1







    def APIData(self):
        print("API data here")
    def MAP(selfs):
        print("map here")






if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())








