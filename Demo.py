import Secrets
import requests
import json



def get_data():
    all_data = []
    page = 0
    for page in range(160):

        response = requests.get(f"https://api.data.gov/ed/collegescorecard/v1/schools.json?school.degrees_awarded.predominant=2,3&fields=school.name,school.state,2018.student.size,2017.student.size,2017.earnings.3_yrs_after_completion.overall_count_over_poverty_line,2016.repayment.3_yr_repayment.overall&api_key={Secrets.api_key}&page={page}")
        if response.status_code != 200:
            print ("error getting data")
            exit(-1)

        page_of_data = response.json()
        page_of_school_data = page_of_data['results']
        all_data.extend(page_of_school_data)
    saveToFile(all_data)


    return all_data

def saveToFile(all_data): #saving all data to a json file.
    with open('file.json', "w") as my_data_file:
        json.dump(all_data, my_data_file)



def main():
    demo_data = get_data()

if __name__ == '__main__':
    main()
