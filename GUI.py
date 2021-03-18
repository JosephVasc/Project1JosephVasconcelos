from PyQt5 import QtCore, QtGui, QtWidgets, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from PyQt5 import QtWebEngineWidgets, QtSql
import json
import plotly.express as px
import plotly.io as pio
from pandas import DataFrame

pio.renderers.default = 'firefox'
import sqlite3
import pandas as pd
import numpy as py
import folium
import io
import math
import Demo

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
        self.clearButton = QtWidgets.QPushButton(self.centralwidget)
        self.clearButton.setGeometry(QtCore.QRect(680, 110, 91, 41))
        self.clearButton.setObjectName("pushButton")
        self.clearButton.clicked.connect(self.clearData)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(680, 160, 91, 41))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.ExcelData)
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(25, 21, 631, 421))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(6)
        self.tableWidget.setRowCount(4329)
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(270, 470, 101, 51))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.clicked.connect(self.exit)
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(680, 260, 75, 81))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_4.clicked.connect(self.MAP)
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(680, 200, 91, 41))
        self.pushButton_5.setObjectName("pushButton")
        self.pushButton_5.clicked.connect(self.dataComparison)
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
        MainWindow.setWindowTitle(_translate("MainWindow", "JosephVasconcelos"))
        self.pushButton.setText(_translate("MainWindow", "SQLite DATA"))
        self.clearButton.setText(_translate("MainWindow", "Clear"))
        self.pushButton_2.setText(_translate("MainWindow", "Excel Data"))
        self.pushButton_3.setText(_translate("MainWindow", "Exit"))
        self.pushButton_4.setText(_translate("MainWindow", "map"))
        self.pushButton_5.setText(_translate("MainWindow", "Data Comparison"))

    def clearData(self):
        msg = QMessageBox()
        msg.setWindowTitle("Table Cleared")
        msg.setText("Click Ok to clear data.")
        x = msg.exec_()
        self.tableWidget.setRowCount(0)

    def exit(self):
        sys.exit()

    def SQLiteData(self):
        conn = sqlite3.connect("university_data_new.sqlite")
        sqlquery = "SELECT * FROM university_data_new"
        result = conn.execute(sqlquery)
        self.tableWidget.setRowCount(0)
        for row_number, row_data in enumerate(result):
            self.tableWidget.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableWidget.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))
        conn.close()
    def SQLliteDataSortByState(self):
        conn = sqlite3.connect("university_data_new.sqlite")
        sqlquery = "SELECT * FROM university_data_new order by school_state"
        result = conn.execute(sqlquery)
        self.tableWidget.setRowCount(0)
        for row_number, row_data in enumerate(result):
            self.tableWidget.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableWidget.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))
        conn.close()

    def ExcelData(self):
        conn = sqlite3.connect("university_data_new.sqlite")
        sqlquery = "SELECT * FROM employee_data_sheet"
        result = conn.execute(sqlquery)
        self.tableWidget.setRowCount(0)
        for row_number, row_data in enumerate(result):
            self.tableWidget.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableWidget.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))
        conn.close()

    def dataComparison(self):
        conn = sqlite3.connect("university_data_new.sqlite")
        print("Data comp")
        sqlquery1 = "SELECT columns1 FROM university_data EXCEPT SELECT columns2 FROM employee_data_sheet;"

        result = conn.execute(sqlquery1)

        self.tableWidget.setRowCount(0)
        for row_number, row_data in enumerate(result):
            self.tableWidget.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableWidget.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))

        conn.close()

    def MAP(self):
        united_states = json.load(open("united_states.geojson", 'r'))
        print(united_states['features'][0])
        state_id_map = {}
        for feature in united_states["features"]:
            feature["id"] = feature["properties"]["STATEFP"]
            state_id_map[feature["properties"]["abbr"]] = feature["id"]

        conn = sqlite3.connect("university_data_new.sqlite")
        cursor = conn.cursor()
        query = '''SELECT school_state, sum(TwentySeventeen_earnings) as earnings
                                     FROM university_data_new
                                     WHERE TwentySeventeen_earnings is not NULL and school_state not in ('FM','MH')
                                     GROUP by school_state'''
        result = cursor.execute(query)
        rows = result.fetchall()
        data = []
        for row in rows:
            data.append(row)
        df = pd.DataFrame(data, columns=['school_state', 'earnings'])
        print(df)
        print("State ID Map")
        print(state_id_map)
        print("here crash")
        try:
            df['id'] = df['school_state'].apply(lambda x: state_id_map[x])
            print("hello")
            conn.close()
            fig = px.choropleth(df,
                                locations="id",
                                geojson=united_states,
                                color="earnings",
                                scope='usa',
                                hover_name="school_state",
                                hover_data=['school_state', 'earnings'],
                                title="Mapping of School information"
                                )
            print("hello")
            fig.write_html('tmp.html', auto_open=True)
        except Exception as e:
            print(e)





if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
