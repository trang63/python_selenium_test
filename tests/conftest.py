import allure
import pytest
from selenium import webdriver
import time
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
    """Fixtest for all Test"""
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
    elif browser_name == "Edge":
        driver = webdriver.Edge(
            service=EdgeService(EdgeChromiumDriverManager().install())
        )

    request.cls.driver = driver
    yield
    driver.close()


@pytest.fixture(scope="session")
def setupOtherConnection(request):
    """Fixtest for all Test"""
    pass


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    """
        Extends the PyTest Plugin to take and embed screenshot in html report, whenever test fails.
        :param item:
        """
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])

    if report.when == 'call' or report.when == "setup":
        timestamp = int(time.time() * 1000)
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            if item.config.option.htmlpath is not None:
                folder_dir = os.path.dirname(item.config.option.htmlpath)
                file_name = report.nodeid.replace("::", "_").replace("/", "_") + str(timestamp) + ".png"
                _capture_screenshot(folder_dir + "/" + file_name)
                if file_name:
                    html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
                           'onclick="window.open(this.src)" align="right"/></div>' % file_name
                    extra.append(pytest_html.extras.html(html))

            allure.attach(
                driver.get_screenshot_as_png(),
                name=report.nodeid.replace("::", "_").replace("/", "_") + str(timestamp),
                attachment_type=allure.attachment_type.PNG)

        report.extra = extra


def _capture_screenshot(name):
    driver.get_screenshot_as_file(name)
