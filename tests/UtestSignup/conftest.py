import pytest
from utilities.dataUtils import DataUtilities
import os

# Get the current script file's directory
current_directory = os.path.dirname(os.path.abspath(__file__))
DATA_FILE_NAME = "UtestSignup"
data_file_path = "{}/TestData/{}.xlsx".format(current_directory, DATA_FILE_NAME)


@pytest.fixture(params=DataUtilities.getAllTestData(data_file_path))
def getData(request):
    """Fixture for each Feature Test - Getdata"""
    return request.param
