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
+ allure serve reports <br>
OR
+ allure generate reports  -o reports_allure

**_Run Parallel Test:_** <br>
`pytest -n auto --dist loadfile  --html=reports/basic-report.html -v -s ` <br>
OR

`pytest -n auto --dist loadfile --alluredir=allure-reports ./tests -v -s
`