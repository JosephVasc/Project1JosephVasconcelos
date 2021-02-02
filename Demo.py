import Secrets
import requests

def get_data():
    all_data = []
    page = 0
    for page in range(5):

        response = requests.get(f"https://api.data.gov/ed/collegescorecard/v1/schools.json?school.degrees_awarded.predominant=2,3&fields=school.name,school.state,2018.student.size&api_key={Secrets.api_key}&page={page}")
        if response.status_code != 200:
            print ("error getting data")
            exit(-1)

        page_of_data = response.json()

        page_of_school_data = page_of_data['results']
        all_data.extend(page_of_school_data)
    return all_data


def main():
    demo_data = get_data()

if __name__ == '__main__':
    main()
