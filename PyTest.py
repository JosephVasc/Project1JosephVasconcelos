import pytest
import Demo
import PyQt5
import GUI
import openpyxl


@pytest.fixture
def get_api_data():
    import Demo
    return Demo.api_data()

def setup_db():
    assert Demo.setup_db() == True
def test_records_dict():
    # first required test
    assert len(Demo.get_data()) >=1000
    assert type(Demo.get_data[1]) is dict

def test_save_data():
    # second required test
    demo_data = {'id': 1234, 'type': "Testable"}
    list_data = []
    list_data.append(demo_data)
    file_name = Demo.saveToFile(list_data)

    testfile = open(file_name, 'r')
    collected_data = testfile.readlines()
    #the save puts a newline at the end
    assert f"{str(demo_data)}\n" in collected_data
def test_excel_data():
    file = 'state_M2019_dl.xlsx'
    isTrue = False
    isTrue = Demo.excel_data(file)
    assert isTrue== True
def widgetTest():
    widget = GUI.QtWidgets() #ran out of time...........




