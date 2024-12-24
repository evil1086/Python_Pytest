import pytest
from selenium import webdriver
import time
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.firefox.options import Options


driver = None

def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="firefox"
    )


@pytest.fixture(scope="class")
def setup(request):
    global driver
    browser_name=request.config.getoption("browser_name")
    ffoptions = Options()
    options = webdriver.ChromeOptions()
    options.accept_insecure_certs = True
    foptions = webdriver.FirefoxOptions()
    options.add_argument("--incognito")
    options.add_argument("disable-gpu")
    # options.add_argument("--headless")
    options.add_argument("no-default-browser-check")
    options.add_argument("no-first-run")
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument("start-maximized")
    options.add_argument('--window-size=3840,2160')
    if browser_name == "chrome":
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    elif browser_name == "firefox":
        driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
    elif browser_name == "IE":
        print("IE driver")
    # driver.get("https://rahulshettyacademy.com/angularpractice/")
    driver.get("https://www.saucedemo.com/")
    driver.maximize_window()

    request.cls.driver = driver
    yield
    driver.close()


@pytest.mark.hookwrapper
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
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            file_name = report.nodeid.replace("::", "_") + ".png"
            _capture_screenshot(file_name)
            if file_name:
                html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>' % file_name
                # extra.append(pytest_html.extras.html(html))
        report.extra = extra


def _capture_screenshot(name):
        # driver.get_screenshot_as_file(name)
        pass

