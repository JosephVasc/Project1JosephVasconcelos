import Secrets
import requests
import json
import sqlite3
from typing import Tuple
import openpyxl
import random


def get_data():
    all_data = []
    page = 0
    for page in range(160):

        response = requests.get(f"https://api.data.gov/ed/collegescorecard/v1/schools.json?school.degrees_awarded.predominant=2,3&fields=school.name,school.state,2018.student.size,2017.student.size,2017.earnings.3_yrs_after_completion.overall_count_over_poverty_line,2016.repayment.repayment_cohort.3_year_declining_balance&api_key={Secrets.api_key}&page={page}")
        if response.status_code != 200:
            print ("error getting data")
            exit(-1)

        page_of_data = response.json()
        page_of_school_data = page_of_data['results']
        all_data.extend(page_of_school_data)
    saveToFile(all_data)


    return all_data


def open_db(filename: str) -> Tuple[sqlite3.Connection, sqlite3.Cursor]:
    db_connection = sqlite3.connect(filename)# connect to existing DB or create new one
    cursor = db_connection.cursor()#get ready to read/write data
    return db_connection, cursor




def close_db(connection: sqlite3.Connection):
    connection.commit()#make sure any changes get saved
    connection.close()


def setup_db(cursor: sqlite3.Cursor):
    cursor.execute('''CREATE TABLE IF NOT EXISTS university_data(
    school_name,
    school_state,
    TwentyEighteen_student_size,
    TwentySeventeen_student_size,
    TwentySeventeen_earnings,
    TwentySixteen_repayment 
    );''')
    cursor.execute("DROP TABLE IF EXISTS employee_data_sheet")
    cursor.execute('''CREATE TABLE IF NOT EXISTS employee_data_sheet(
    occ_code,
    state,
    oc_total,
    tot_emp,
    h_pct,
    a_pct 
    );''')
    return True



def api_data(cursor: sqlite3.Cursor):
    all_data = get_data()
    for i in range(len(all_data)):
        d1 = all_data[i]['school.name']
        d2 = all_data[i]['school.state']
        d3 = all_data[i]['2018.student.size']
        d4 = all_data[i]['2017.student.size']
        d5 = all_data[i]['2017.earnings.3_yrs_after_completion.overall_count_over_poverty_line']
        d6 = all_data[i]['2016.repayment.repayment_cohort.3_year_declining_balance']
        cursor.execute('INSERT INTO university_data VALUES(?, ?, ?, ?, ?, ?)',
                            (d1, d2, d3, d4, d5, d6))
def excel_data(file):
    wb = openpyxl.load_workbook(file)
    ws = wb.active
    return ws
def excel_data_sheet(cursor: sqlite3.Cursor):
    xcl_info = excel_data('state_M2019_dl.xlsx')
    for row in xcl_info.iter_rows(values_only=True):
        if 'major' in row[9]:
            cursor.execute('INSERT OR REPLACE INTO employee_data_sheet VALUES(?, ?, ?, ?, ?, ?)',
                       (row[7], row[1], row[8], row[10], row[19], row[24]))

def main():
    conn, cursor = open_db("university_data.sqlite")
    setup_db(cursor)
    api_data(cursor)
    excel_data_sheet(cursor)
    print(type(conn))
    close_db(conn)



def saveToFile(all_data): #saving all data to a json file.
    with open('file.json', "w") as my_data_file:
        json.dump(all_data, my_data_file)
    file = 'file.json'
    return file


#def main():
    #demo_data = get_data()

if __name__ == '__main__':
    main()
