import sqlite3
from typing import Tuple
import random

def open_db(filename: str) -> Tuple[sqlite3.Connection, sqlite3.Cursor]:
    db_connection = sqlite3.connect(filename)#connect to existing DB or create new one
    cursor = db_connection.cursor()#read/write data
    return db_connection, cursor


def close_db(connection: sqlite3.Connection):
    connection.commit()#make sure any changes get saved
    connection.close()


def setup_db(cursor: sqlite3.Cursor):
    cursor.execute('''CREATE TABLE IF NOT EXISTS uni_data(
    school_name,
    school_city,
    TwentyEighteen_student_size,
    TwentySeventeen_student_size,
    TwentySeventeen_earnings ,
    TwentySixteen_repayment 
    );''')

def api_data(cursor: sqlite3.Cursor):
    all_data = get_data()
    for i in range(len(all_data)):
        data1 = all_data[i]['school.name']
        data2 = all_data[i]['school.city']
        data3 = all_data[i]['2018.student.size']
        data4 = all_data[i]['2017.student.size']
        data5 = all_data[i]['2017.earnings.3_yrs_after_completion.overall_count_over_poverty_line']
        data6 = all_data[i]['2016.repayment.3_yr_repayment.overall']
        cursor.execute('INSERT INTO uni_data VALUES(?, ?, ?, ?, ?, ?)',
                            (data1, data2, data3, data4, data5, data6))


def main():
    conn, cursor = open_db("uni_data.sqlite")
    setup_db(cursor)
    api_data(cursor)
    print(type(conn))
    close_db(conn)