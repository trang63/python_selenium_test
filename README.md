### This is template for an Automation project: ###
* Written by Python, Selenium
* Apply Page Object Model
* Support Log
* Support Pytest
* Support Report file (Pytest-html or Allure)
* Support Parallel testing (By pytest-xdist)
* Support Github Action
  * Upload Report file as Attachment
  * Upload Allure report to Github Page (Web server)
  * Slack message

### Project Structure
```
.
├── README.md
├── .github
│   └── workflows
│       └── test_workflow.yml
├── pageObjects
│   ├── Common
│   │   ├── CommonPage.py
│   │   ├── __init__.py
│   ├── PagesOnTest
│   │   ├── Page1.py
│   │   ├── Page2.py
│   │   └── __init__.py
│   └── __init__.py
├── tests
│   ├── __init__.py
│   ├── conftest.py
│   ├── baseTest.py
│   ├── Test1_WithData
│   │   ├── TestData
│   │   ├── __init__.py
│   │   ├── conftest.py
│   │   └── test_1.py
│   └── Test2
│       ├── __init__.py
│       └── test_2.py
├── utilities
│    ├── DataUtils.py
│    └──__init__.py
├── config
│   ├── __init__.py
│   ├── customFormat.py
│   └── logging.ini
│── pytest.ini
└── requirements.txt
```

### Run Test in Local machine ###
**_Install Package:_** <br>
`pip install -r requirement.txt
`

**_Run Test:_** <br>
`pytest -k <test_name_pattern> --html=reports/report.html
`

**_Run Test with Pytest Html Report:_** <br>
`pytest -k <test_name_pattern> --html=reports/report.html
`

**_Run Test with Allure Report:_** <br>
`pytest -k <test_name_pattern> --alluredir=allure-reports ./tests
`

**_View Allure report by:_** <br>
`allure serve reports` <br>
OR <br>
`allure generate reports  -o reports_allure`

**_Run Parallel Test:_** <br>
Generate Pytest-html report: `pytest -n auto --dist loadfile  --html=reports/basic-report.html -v -s ` <br>
OR <br>
Generate Allure report: `pytest -n auto --dist loadfile --alluredir=allure-reports ./tests -v -s
`
