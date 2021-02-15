import Secrets
import requests
import json
import sqlite3
from typing import Tuple
import random


def get_data():
    all_data = []
    page = 0
    for page in range(5):

        response = requests.get(f"https://api.data.gov/ed/collegescorecard/v1/schools.json?school.degrees_awarded.predominant=2,3&fields=school.name,school.state,2018.student.size,2017.student.size,2017.earnings.3_yrs_after_completion.overall_count_over_poverty_line,2016.repayment.3_yr_repayment.overall&api_key={Secrets.api_key}&page={page}")
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
    cursor.execute('''CREATE TABLE IF NOT EXISTS uni_data(
    school_name,
    school_state,
    TwentyEighteen_student_size,
    TwentySeventeen_student_size,
    TwentySeventeen_earnings,
    TwentySixteen_repayment 
    );''')

def api_data(cursor: sqlite3.Cursor):
    all_data = get_data()
    for i in range(len(all_data)):
        data1 = all_data[i]['school.name']
        data2 = all_data[i]['school.state']
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






def saveToFile(all_data): #saving all data to a json file.
    with open('file.json', "w") as my_data_file:
        json.dump(all_data, my_data_file)



#def main():
    #demo_data = get_data()

if __name__ == '__main__':
    main()
