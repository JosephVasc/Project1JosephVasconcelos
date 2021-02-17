import pytest
import Demo



@pytest.fixture
def get_data():
    import Demo
    return Demo.api_data()


def test_records_dict(get_data):
    # first required test
    assert len(get_data) >=1000
    assert type(get_data[1]) is dict

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