This is template for an Automation project:
- written by Python, Selenium 
- using Page Object Model
- support Log
- support Pytest
- support Report file
- support Parallel testing (By pytest-xdist)
- support Github Action
    + support upload allure report to Github Page (Web server)
    + Slack 

Install Package:
pip install -r requirement.txt

Run Test:
pytest -k <file_test> --html=reports/report.html

Run Test with Pytest Html Report
pytest -k <file_test> --html=reports/report.html

Run Test with Allure Report
pytest -k <file_test> --alluredir=allure-reports ./tests

View Allure report by:
+ allure serve reports
OR
+ allure generate reports  -o reports_allure

Run Parallel Test:
pytest -n auto --dist loadfile  --html=reports/basic-report.html  --alluredir=allure-reports ./tests -v -s
