import allure
import pytest
from selenium import webdriver
import datetime
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager
import os

driver = None


# add param to pytest commend
def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )


@pytest.fixture(scope="function")
def setup(request):
    """Fixture for all Test"""
    global driver
    browser_name = request.config.getoption("browser_name")
    if browser_name == "chrome":
        driver = webdriver.Chrome(
            service=ChromeService(ChromeDriverManager().install())
        )
    elif browser_name == "firefox":
        driver = webdriver.Firefox(
            service=FirefoxService(GeckoDriverManager().install())
        )
    elif browser_name == "edge":
        driver = webdriver.Edge(
            service=EdgeService(EdgeChromiumDriverManager().install())
        )
    else :
        raise Exception("Invalid browser specified!")
    request.cls.driver = driver
    yield
    driver.close()


@pytest.fixture(scope="session")
def setupOtherConnection(request):
    """Fixture for all Test"""
    pass


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    """
        Extends the PyTest Plugin to take and embed screenshot in html report, whenever test fails.
        :param item:
    """
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    result = outcome.get_result()
    extra = getattr(result, 'extra', [])

    if (result.when == 'call' or result.when == "setup") and driver is not None:
        timestamp = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
        xfail = hasattr(result, 'wasxfail')
        if (result.skipped and xfail) or (result.failed and not xfail):
            # Attach screenshot to html-report
            if item.config.option.htmlpath is not None:
                folder_dir = os.path.dirname(item.config.option.htmlpath)
                file_name = item.nodeid.split("::")[-1] + timestamp + ".png"
                os.makedirs(folder_dir, exist_ok=True)
                _capture_screenshot(folder_dir + "/" + file_name)
                if file_name:
                    html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
                           'onclick="window.open(this.src)" align="right"/></div>' % file_name
                    extra.append(pytest_html.extras.html(html))
                result.extra = extra

            # Attach screenshot to Allure report
            allure.attach(
                driver.get_screenshot_as_png(),
                name=result.nodeid.replace("::", "_").replace("/", "_") + str(timestamp),
                attachment_type=allure.attachment_type.PNG)

def _capture_screenshot(name):
    driver.get_screenshot_as_file(name)
